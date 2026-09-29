# OpsGuardian

OpsGuardian is a local incident-investigation tool for service and platform teams. It searches incident records, postmortems, runbooks, alerts, configuration, logs and Kubernetes events, then lays out the evidence and suggests the next checks.

The main notebook follows the instructor's Generative AI Labs 1-6 pattern. The rest of the repository applies that pattern to a small, fixed DevOps incident corpus.

## Included data

The repository includes a ready-to-index dataset under `dataset/` with **34 source files** and **24 evaluation questions**. No external download is required for the demo.

Evidence types include runbooks, incident records, postmortems, Kubernetes events, service configs, logs, alerts/SLOs and architecture/deployment docs.

## Retrieval and answer flow

`low-temperature LLM -> load -> split 1000/200 -> OllamaEmbeddings -> Chroma -> similarity/MMR/BM25+Chroma -> ChatPromptTemplate -> Pydantic -> LCEL -> MultiQuery -> LangGraph -> retrieval evaluation`

## Models

- Chat: `qwen3:8b` through Ollama by default
- Embeddings: `nomic-embed-text`
- Optional Groq generation is supported via `.env`

## Run on Windows

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

## Scope and limits

OpsGuardian is decision support. It retrieves evidence and suggests safe diagnostic steps; it does not directly execute production changes.
