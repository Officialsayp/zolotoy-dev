# Integration plan

This plan orders risk. It is not a commitment to implement every component at once.

## Phase 0 — repository foundations (now)

- keep `zolotoy-dev-frontend` deployed in mock mode;
- create `zolotoy-dev` and `zolotoy-dev-infra` as documentation/ownership scaffolds;
- do not provision production infrastructure solely because the repositories exist.

Exit gate: repository boundaries and source ownership are clear.

## Phase 1 — Order Service

Build `order-service` locally first:

1. domain model/invariants and application layer;
2. PostgreSQL repository + migrations;
3. REST/OpenAPI boundary;
4. idempotency and concurrency behavior;
5. unit/integration/e2e coverage;
6. Dockerfile + service-local Compose;
7. metrics/logging baseline;
8. transactional outbox, then Kafka publisher.

Exit gate: a reproducible container image and stable API contract exist.

## Phase 2 — Auth and URL Shortener

Implement independently, each with service-owned PostgreSQL/Redis semantics. Avoid sharing tables,
Redis keys or migrations.

Exit gate: stable API contracts and reproducible images exist.

## Phase 3 — Notification and event integration

Implement Kafka consumer/deduplication/durable delivery jobs, then connect it to versioned Order events.
Test duplicates, provider failures, retries and restart behavior before calling the flow reliable.

Exit gate: Order outbox → Kafka → Notification is reproducible under failure scenarios.

## Phase 4 — cross-service Selectel environment

Only now does `zolotoy-dev-infra` gain active integration/production manifests:

- Caddy edge/TLS;
- Docker Compose for published images;
- internal-only PostgreSQL/Redis/Kafka endpoints;
- Prometheus/Grafana and optional OTel Collector when instrumentation is ready;
- backup/restore and rollback procedures;
- Selectel Container Registry integration if selected.

Deploy one service at a time and smoke-test it before publishing DNS for the next.

## Phase 5 — frontend real mode

The current frontend runtime mode is global (`mock` or `real`). Do not switch production to `real`
until the endpoints needed by the production demo are actually available and contract-compatible.
Then build the frontend with the real service base URLs and execute cross-service browser acceptance.

## Phase 6 — optional frontend move to Selectel

Moving the static SPA from Cloudflare to the VPS is independent of backend correctness. Do it only if
there is an operational reason (single origin, routing/resilience requirements, learning objective,
etc.). Keep a rollback path during cutover.
