# Commerce Platform Architecture
Internet -> ingress -> checkout-api.
checkout-api calls auth-service, inventory-service, payments-api and Redis session/cache. payments-api calls PostgreSQL and an external payment gateway. orders-worker consumes `orders.created` from the queue.
Observability includes request IDs, OpenTelemetry traces, Prometheus alerts and Kubernetes events.
