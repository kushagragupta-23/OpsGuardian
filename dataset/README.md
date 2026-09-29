# OpsGuardian RAG Dataset

This is a **bundled synthetic-but-realistic DevOps operations corpus** created for the OpsGuardian portfolio project. It is deliberately multi-source so RAG has to connect evidence across logs, runbooks, incidents, configs, alerts, Kubernetes events and postmortems.

## Corpus size

- 34 source files
- 5 application/service scopes plus platform-wide material
- Evidence types: runbooks, incidents, postmortems, logs, configs, Kubernetes events, SLO/alert docs and architecture/deployment docs

## Key scenarios represented

1. Redis client-pool regression causing checkout latency
2. Database connection leak causing payment failures
3. Cluster DNS failure
4. JWT validation failures caused by clock skew
5. Kubernetes OOMKilled worker
6. Queue backlog caused by downstream rate limiting

`source_manifest.csv` supplies metadata attached to documents before chunking.

The corpus is fictional and contains no real credentials, customer data or production secrets.
