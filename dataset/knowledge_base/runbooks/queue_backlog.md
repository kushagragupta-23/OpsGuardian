# Runbook: Queue Backlog
Symptoms: queue depth rising, message age rising, workers healthy but throughput lower than ingress.
Check worker error rate, consumer lag, poison messages, downstream rate limits, and autoscaling. Scale consumers only if the downstream system can safely accept more traffic.
