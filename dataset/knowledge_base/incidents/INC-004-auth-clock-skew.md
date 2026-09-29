# INC-004 - Auth 401 Spike
Severity: SEV-2
Service: auth-service
Evidence: `token used before issued` and `iat in future` appeared across pods on node pool blue. NTP offset on those nodes was +94 seconds. Signing keys and issuer config were unchanged.
Action: drain affected nodes and restore time synchronization.
Root cause: node clock skew.
