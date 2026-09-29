# INC-002 - Payments DB Pool Saturation
Severity: SEV-1
Service: payments-api
Impact: payment authorization error rate reached 24%.
Evidence: `PoolTimeout` logs, active=30 idle=0 waiters=118. Database CPU 42%; max_connections had headroom. Release v4.6.1 introduced a code path that failed to release a connection on gateway timeout.
Action: rollback v4.6.1 and deploy connection cleanup fix.
Root cause: connection leak during exception handling.
