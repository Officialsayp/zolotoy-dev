# Roadmap

## Now

- [x] Frontend Foundation + Order/Auth/Notification/Shortener UI modules
- [x] Frontend mock/live boundary
- [x] Umbrella repository bootstrap
- [x] Infrastructure repository bootstrap
- [ ] Create `order-service`

## Backend milestone sequence

- [ ] Order MVP: domain + PostgreSQL + REST + tests
- [ ] Order hardening: idempotency + optimistic concurrency + outbox
- [ ] Auth MVP + threat model + PostgreSQL/Redis
- [ ] URL Shortener MVP + Redis hot path + load tests
- [ ] Notification MVP + Kafka + retries/DLQ semantics
- [ ] Cross-service Order events → Notification

## Infrastructure milestones

- [ ] First published backend image
- [ ] Selectel Container Registry decision/setup
- [ ] First Selectel backend deployment
- [ ] Edge routing + TLS + health smoke checks
- [ ] Shared Prometheus/Grafana
- [ ] Encrypted backups with a tested restore
- [ ] Production frontend real-mode acceptance

## Stretch goals

Kubernetes/Helm, advanced tracing backend, ClickHouse analytics and horizontal scaling are intentionally
not core milestones. Add them only after the single-server system is measurable and reproducible.
