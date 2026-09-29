# Postmortem PM-002: Payment Connection Leak
INC-002 root cause was a missing connection release in exception handling. Corrective actions: context-managed connections, leak test, pool waiters dashboard, and rollback automation. Increasing pool size was not the permanent fix.
