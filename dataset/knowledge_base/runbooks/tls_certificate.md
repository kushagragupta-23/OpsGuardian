# Runbook: TLS Certificate Expiry
Symptoms: certificate has expired, x509 validation errors, clients fail during TLS handshake.
Check certificate notAfter timestamp and renewal controller. Renew/rotate the certificate and verify the full chain. Do not disable certificate verification as a workaround.
