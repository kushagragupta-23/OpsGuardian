# Postmortem PM-001: Checkout Redis Client Regression
INC-001 escaped because the canary check monitored error rate but not dependency pool waiters. Corrective actions: add redis pool saturation alert, test config diffs, and include dependency latency in canary gates. Flushing Redis was explicitly rejected because it would have increased database traffic.
