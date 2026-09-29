# Production SLO and Escalation Policy
checkout-api: availability 99.9%, p95 latency target < 500 ms.
payments-api: availability 99.95%, p95 latency target < 650 ms.
SEV-1: broad checkout/payment outage or >20% error rate for 5 minutes. Page incident commander and service owner immediately.
SEV-2: material degradation without broad outage. Page service owner and open incident channel.
