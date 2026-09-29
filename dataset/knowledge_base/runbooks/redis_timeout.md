# Runbook: Redis Timeout / Cache Connectivity
Symptoms: `RedisTimeoutError`, rising cache-miss rate, checkout latency, intermittent 5xx.

Checks:
- Confirm Redis endpoint and DNS resolution.
- Inspect connection-pool utilization and rejected connections.
- Check Redis server CPU and maxclients.
- Compare timeout start time with application deployment/config changes.
- Do not flush the cache as a first response; this can amplify database load.

If the client pool is exhausted after a release, rollback or restore the prior pool settings, then monitor p95 latency and Redis errors.
