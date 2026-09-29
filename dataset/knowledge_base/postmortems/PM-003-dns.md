# Postmortem PM-003: Cluster DNS Change
CoreDNS configuration was changed without a production-like validation step. Add synthetic DNS probes and staged CoreDNS rollout. Credential rotation was unrelated to the incident.
