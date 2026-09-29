# Runbook: Service DNS Resolution Failure
Symptoms include `Name or service not known`, `NXDOMAIN`, or connection attempts failing before TCP establishment.
Check CoreDNS health, DNS query errors, service name/namespace, and recent Service changes. Do not rotate credentials for a DNS failure unless separate evidence indicates authentication trouble.
