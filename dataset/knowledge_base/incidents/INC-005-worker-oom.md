# INC-005 - Orders Worker OOM
Severity: SEV-2
Service: orders-worker
Kubernetes events showed `Reason: OOMKilled`, exit code 137. Memory rose steadily to the 768Mi limit while processing a large batch. Release v3.2.0 introduced an unbounded in-memory deduplication map.
Action: rollback and cap the map size.
