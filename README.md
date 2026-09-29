# OpsGuardian - DevOps Incident Resolution RAG

A complete local-first RAG portfolio project for Kushagra. **The main notebook follows Sir's Generative AI Labs 1-6 pattern** while the domain-specific code adds a realistic DevOps incident corpus and application interfaces.

## Included dataset

The ZIP includes a ready-to-index dataset under `dataset/` with **34 source files** and **24 evaluation questions**. No external dataset download is required for the demo.

Evidence types include runbooks, incident records, postmortems, Kubernetes events, service configs, logs, alerts/SLOs and architecture/deployment docs.

## Main class-style flow

`low-temperature LLM -> load -> split 1000/200 -> OllamaEmbeddings -> Chroma -> similarity/MMR/BM25+Chroma -> ChatPromptTemplate -> Pydantic -> LCEL -> MultiQuery -> LangGraph -> retrieval evaluation`

## Local models

- Chat: `qwen3:8b` through Ollama by default
- Embeddings: `nomic-embed-text`
- Optional Groq generation is supported via `.env`

## Windows setup

```powershell
ollama pull qwen3:8b
ollama pull nomic-embed-text
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python ingest.py --reset
streamlit run app.py
```

## Example questions

- Why did checkout latency spike after v2.18.0?
- What evidence proves the orders worker was OOMKilled?
- Why did scaling workers worsen the queue backlog?
- Was database CPU the root cause of the payment incident?
- What should we check during a broad 401 spike?

## API

```powershell
uvicorn api:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Evaluation

```powershell
python evaluate.py
```
Compares similarity, MMR and hybrid retrieval using source hit, category hit and reciprocal rank.

## Important safety/design point

OpsGuardian is decision support. It retrieves evidence and suggests safe diagnostic steps; it does not directly execute production changes.
