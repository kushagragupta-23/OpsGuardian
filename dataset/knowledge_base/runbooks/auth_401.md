# Runbook: Sudden 401 Increase
Check token validation errors, issuer/audience configuration, key rotation, and clock synchronization. A broad 401 spike immediately after a config deployment often indicates auth configuration mismatch. Do not reset user passwords without evidence.
