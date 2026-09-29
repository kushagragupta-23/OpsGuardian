# 6-8 Minute Demo Script

1. Show `dataset/source_manifest.csv` and explain the eight evidence types.
2. Run `python ingest.py --reset` once before the demo.
3. Ask: **Why did checkout latency spike after v2.18.0?** Show INC-001, checkout logs and config evidence.
4. Ask: **Was database CPU the main cause of the payment outage?** Explain evidence vs assumption.
5. Ask: **What confirms the worker was OOMKilled?** Show Kubernetes event evidence.
6. Show the notebook's similarity/MMR/hybrid retrieval cells.
7. Show LangGraph `START -> retrieve -> generate -> END`.
8. Ask an unsupported cricket question to demonstrate controlled failure.
9. Finish with `python evaluate.py` and explain retrieval metrics.
