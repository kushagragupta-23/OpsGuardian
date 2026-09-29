# Viva Questions and Answers

**Why RAG?** Operational answers must be grounded in runbooks, logs and incident history rather than only model memory.

**Why hybrid retrieval?** BM25 helps exact operational terms such as `PoolTimeout`, `OOMKilled` and incident IDs; dense retrieval helps paraphrases such as “checkout got slow after deploy.”

**Why Chroma?** It is the same vector-store style used in the class RAG workflow and is easy to run locally.

**Why Ollama?** Kushagra can run the chat model and embeddings locally on his GPU, improving privacy and avoiding per-call hosted inference for the demo.

**What does MultiQuery do?** It generates alternative phrasings of the question to improve recall when user wording differs from the documents.

**Why LangGraph if the graph is simple?** The simple retrieve/generate state graph mirrors Sir's Lab 6 and provides a clean path for future approval/escalation nodes.

**How do you prevent hallucination?** Context-only prompt, structured output, explicit information-gap field, source display and controlled-failure tests.

**Can OpsGuardian fix production automatically?** No. This implementation is decision support; actions stay human-approved.

**What is the strongest evaluation?** Retrieval should be evaluated independently of generation. The supplied labelled questions measure whether the expected source/category appears and how highly it ranks.
