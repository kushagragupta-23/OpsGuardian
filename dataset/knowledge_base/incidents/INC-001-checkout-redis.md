# INC-001 - Checkout Latency after v2.18.0
Severity: SEV-2
Service: checkout-api
Start: 2026-08-14 10:02 UTC

Impact: checkout p95 rose from 340 ms to 2.8 s; 7% of requests returned 504.
Evidence: `RedisTimeoutError` began within three minutes of deployment v2.18.0. Redis server CPU was 31% and healthy. Client metric `redis_pool_active=20` equaled the new pool limit; waiters rose to 46. Previous release used pool size 80.
Action: rollback to v2.17.4. Latency normalized within six minutes.
Root cause: client connection-pool limit was accidentally reduced from 80 to 20.
