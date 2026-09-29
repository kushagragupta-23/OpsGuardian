# Runbook: Kubernetes CrashLoopBackOff
Collect `kubectl describe pod`, previous container logs, exit code, restart count and recent deployment changes.
Exit code 137 commonly indicates termination after exceeding memory limits, but confirm Kubernetes events before concluding OOMKilled.
For configuration errors, inspect missing Secrets/ConfigMaps and startup validation messages.
