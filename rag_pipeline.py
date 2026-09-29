from __future__ import annotations
import os
from pathlib import Path
from uuid import uuid4
from typing import List
from typing_extensions import TypedDict
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph, END
from ops_loader import load_ops_dataset

load_dotenv(override=True)
ROOT = Path(__file__).resolve().parent
DATASET_DIR = ROOT / "dataset"
PERSIST_DIR = ROOT / "chroma_opsguardian_db"


def build_llm():
    provider = os.getenv("MODEL_PROVIDER", "ollama").lower()
    if provider == "groq":
        return init_chat_model(
            os.getenv("GROQ_CHAT_MODEL", "openai/gpt-oss-20b"),
            model_provider="groq", temperature=0.1
        )
    return ChatOllama(model=os.getenv("OLLAMA_CHAT_MODEL", "qwen3:8b"), temperature=0.1)

llm = build_llm()
embeddings_model = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text"))

class OpsGuardianResponse(BaseModel):
    incident_summary: str = Field(description="Short evidence-grounded summary of the operational issue")
    likely_causes: list[str] = Field(description="Likely causes supported by retrieved evidence")
    recommended_steps: list[str] = Field(description="Ordered safe diagnostic or mitigation steps supported by context")
    evidence: list[str] = Field(description="Concrete signals or facts from retrieved context")
    source_documents: list[str] = Field(description="Titles or paths of retrieved sources used")
    escalation_required: bool = Field(description="True when the retrieved evidence indicates escalation")
    information_gap: bool = Field(description="True if context is insufficient for a reliable answer")

SYSTEM = """You are OpsGuardian, a DevOps incident-resolution assistant.
Use ONLY the retrieved context. Do not invent metrics, commands, root causes, incident history or remediation.
Separate observed evidence from possible causes. Prefer reversible diagnostics before risky actions.
Do not recommend destructive actions such as deleting data, disabling TLS verification, or flushing caches unless the retrieved runbook explicitly supports it.
If evidence is insufficient, set information_gap=true and say what evidence is missing.
Selected service scope: {service}

Retrieved context:
{context}
"""
prompt = ChatPromptTemplate([("system", SYSTEM), ("human", "Incident question: {question}")])
structured_llm = llm.with_structured_output(OpsGuardianResponse)

def format_docs(docs: List[Document]) -> str:
    parts=[]
    for d in docs:
        parts.append(
            f"SOURCE: {d.metadata.get('source')}\nTITLE: {d.metadata.get('title')}\n"
            f"CATEGORY: {d.metadata.get('category')}\nSERVICE: {d.metadata.get('service')}\n"
            f"CONTENT:\n{d.page_content}"
        )
    return "\n\n".join(parts)

class OpsGuardianRAG:
    def __init__(self):
        self.docs = load_ops_dataset(DATASET_DIR)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
        self.splits = splitter.split_documents(self.docs)
        self.store = Chroma(collection_name="opsguardian-rag", embedding_function=embeddings_model, persist_directory=str(PERSIST_DIR))

    def index(self, reset=False):
        """Rebuild the local collection from the bundled corpus.

        The corpus is the source of truth. Rebuilding on every index call keeps
        repeated ingestion idempotent and prevents UUID-based duplicate chunks.
        """
        try:
            self.store.delete_collection()
        except Exception:
            pass
        self.store = Chroma(
            collection_name="opsguardian-rag",
            embedding_function=embeddings_model,
            persist_directory=str(PERSIST_DIR),
        )
        ids=[str(uuid4()) for _ in self.splits]
        self.store.add_documents(self.splits, ids=ids)
        return len(self.splits)

    def _selected(self, service: str):
        if not service or service.lower() in {"all", "platform"}:
            return self.splits
        selected=[d for d in self.splits if d.metadata.get("service") in {service, "platform"}]
        return selected or self.splits

    def similarity_retriever(self, service="all", k=4):
        kwargs={"k":k}
        if service and service.lower() not in {"all", "platform"}:
            kwargs["filter"]={"service": service}
        return self.store.as_retriever(search_type="similarity", search_kwargs=kwargs)

    def mmr_retriever(self, service="all", k=4):
        kwargs={"k":k}
        if service and service.lower() not in {"all", "platform"}:
            kwargs["filter"]={"service": service}
        return self.store.as_retriever(search_type="mmr", search_kwargs=kwargs)

    def hybrid_retriever(self, service="all", k=4):
        selected=self._selected(service)
        bm25=BM25Retriever.from_documents(selected); bm25.k=k
        dense=self.similarity_retriever(service, k)
        return EnsembleRetriever(retrievers=[bm25,dense], weights=[0.7,0.3])

    def ask(self, service, question, method="hybrid"):
        if method == "similarity": r=self.similarity_retriever(service)
        elif method == "mmr": r=self.mmr_retriever(service)
        else: r=self.hybrid_retriever(service)
        docs=r.invoke(question)
        answer=(prompt | structured_llm).invoke({"service":service,"question":question,"context":format_docs(docs)})
        return answer, docs

    def multiquery(self, service, question):
        base=self.similarity_retriever(service, k=2)
        mq=MultiQueryRetriever.from_llm(retriever=base, llm=llm, include_original=True)
        return mq.invoke(question)

    def graph(self, service="all"):
        outer=self
        class State(TypedDict):
            service: str
            question: str
            context: List[Document]
            answer: OpsGuardianResponse
        def retrieve(state: State):
            return {"context": outer.hybrid_retriever(state["service"]).invoke(state["question"])}
        def generate(state: State):
            response=(prompt | structured_llm).invoke({
                "service": state["service"], "question": state["question"], "context": format_docs(state["context"])
            })
            return {"answer": response}
        gb=StateGraph(State); gb.add_node("retrieve",retrieve); gb.add_node("generate",generate)
        gb.add_edge(START,"retrieve"); gb.add_edge("retrieve","generate"); gb.add_edge("generate",END)
        return gb.compile()
