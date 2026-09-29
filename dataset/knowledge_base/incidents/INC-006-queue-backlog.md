# INC-006 - Order Queue Backlog
Severity: SEV-2
Service: orders-worker
Queue depth increased from 2k to 140k and oldest message age reached 22 minutes. Worker CPU was low. Logs showed repeated HTTP 429 from the fulfillment provider. Scaling workers increased 429s.
Action: reduce consumer rate, add exponential backoff, coordinate provider limit increase.
Root cause: downstream rate limiting.
