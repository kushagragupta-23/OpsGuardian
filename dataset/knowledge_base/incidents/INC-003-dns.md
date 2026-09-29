# INC-003 - Inventory DNS Failure
Severity: SEV-2
Service: inventory-service
Evidence: checkout logs showed `inventory-service.prod.svc: Name or service not known`. CoreDNS errors increased after a cluster DNS configuration rollout. TCP connection metrics did not increment because resolution failed first.
Action: revert CoreDNS config. Service recovered.
Root cause: invalid upstream resolver configuration.
