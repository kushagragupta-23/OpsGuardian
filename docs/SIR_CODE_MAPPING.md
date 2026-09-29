# Sir Code Mapping

| Instructor lab | OpsGuardian implementation |
|---|---|
| Lab 1: LLM Generation Parameters | `temperature=0.1` for evidence-grounded answers |
| Lab 2: Introduction to LangChain | chat model, `ChatPromptTemplate`, runnable `prompt | structured_llm` |
| Lab 3: Structured Output | `OpsGuardianResponse` Pydantic schema + `with_structured_output` |
| Lab 4: RAG | `TextLoader`, `RecursiveCharacterTextSplitter(1000,200)`, `OllamaEmbeddings`, Chroma, BM25, EnsembleRetriever |
| Lab 5: Advanced RAG | MMR and `MultiQueryRetriever` experiment |
| Lab 6: RAG With LangGraph | `State` + `START -> retrieve -> generate -> END` |

Project-specific additions are limited to the DevOps dataset/metadata, service filtering, evaluation labels and app/API wrappers.
