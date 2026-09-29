# Runbook: Database Connection Pool Saturation
Symptoms include pool-acquisition timeout, active connections equal pool size, and request latency increasing while database CPU remains normal.

Steps:
1. Check pool size, active, idle, and waiters.
2. Search for a deployment that changed concurrency or connection lifecycle.
3. Inspect long-running transactions.
4. Avoid simply increasing pool size until database max-connections and leak risk are understood.
5. Roll back a confirmed regression and verify waiters return to zero.
