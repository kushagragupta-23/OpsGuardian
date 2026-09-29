# Runbook: API Latency Spike
Service scope: checkout-api, payments-api, orders-api.

Trigger: p95 latency above 800 ms for 10 minutes.

Triage order:
1. Compare current latency with the last deployment time.
2. Check upstream dependency latency before restarting pods.
3. Inspect Redis, database, and payment-gateway timeout counters.
4. Check Kubernetes CPU throttling and memory pressure.
5. If a new release correlates with the spike and dependency health is normal, perform a controlled rollback.

Do not treat a timeout as proof of CPU saturation. Preserve request IDs and timestamps for correlation.
