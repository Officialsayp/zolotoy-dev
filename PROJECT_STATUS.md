# Project status

Status snapshot: **2026-09-06**.

This file records what is actually implemented or intentionally planned. Update it when repository
ownership, deploy state or integration state changes; do not use future architecture as present-tense
status.

| Area | Repository | Current state | Next meaningful gate |
| --- | --- | --- | --- |
| Frontend | `Officialsayp/zolotoy-dev-frontend` | Implemented; mock-first Vue SPA; Cloudflare deployment | Stable backend contracts, then real-mode integration |
| Order | `Officialsayp/order-service` | Not created | Domain/application skeleton, PostgreSQL, HTTP API, tests |
| Auth | `Officialsayp/auth-service` | Not created | Threat model, sessions/tokens, PostgreSQL/Redis, tests |
| Notification | `Officialsayp/notification-service` | Not created | Kafka consumer model, durable jobs/retries, tests |
| URL Shortener | `Officialsayp/url-shortener` | Not created | PostgreSQL/Redis redirect path, analytics, tests |
| Cross-service infra | `Officialsayp/zolotoy-dev-infra` | Bootstrap repository | Add runnable integration/deploy config only when first service image exists |
| Selectel backend deployment | `zolotoy-dev-infra` | Not provisioned/claimed here | Provision after a deployable backend service exists |
| Frontend real mode | `zolotoy-dev-frontend` | Not production-enabled for all services | Enable only when required service endpoints/contracts are available |

## Important current integration constraint

The frontend currently exposes a global `VITE_API_MODE=mock|real`. It is therefore not assumed that
production can mix one real backend module with three mock modules without a deliberate frontend
architecture change. Partial backend development should be verified through service/API tests first;
do not invent per-service runtime modes just to accelerate integration.
