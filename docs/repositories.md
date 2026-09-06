# Repository boundaries

## Why a polyrepo

The portfolio is intentionally split by deployable boundary. Each service has its own lifecycle,
contract, migrations, tests, container image and operational concerns. The frontend and infrastructure
also evolve independently.

| Repository | Owns | Must not own |
| --- | --- | --- |
| `zolotoy-dev` | System docs, status, cross-repo ADRs | App code, deploy manifests, canonical service OpenAPI |
| `zolotoy-dev-frontend` | Vue SPA, module API facades, mock scenarios, UI tests | Backend domain rules, DB migrations |
| `order-service` | Order domain/API/schema/outbox | Notification delivery state |
| `auth-service` | Identity/session/API/schema/Redis usage | Generic API gateway or other service authorization data |
| `notification-service` | Kafka consumer, jobs/attempts, provider adapters | Order state ownership |
| `url-shortener` | Link/redirect/cache/analytics behavior | Shared platform cache for other services |
| `zolotoy-dev-infra` | Cross-service networks, edge routing, production Compose, shared observability/backups/runbooks | Business logic, service migrations, canonical API DTOs |

## Service-local infrastructure

Each backend specification explicitly expects a `Dockerfile`, local `compose.yaml`, healthchecks and
an environment template in the service repository. Keep that service-local developer experience
there. `zolotoy-dev-infra` should compose **published service images** for integration/production,
not become the only way a developer can run one service locally.

## Naming

The current backend specs define repository/canonical names as:

- `order-service`
- `auth-service`
- `notification-service`
- `url-shortener`

Do not rename them to `zolotoy-dev-*-service` merely for visual grouping unless the specs and all
cross-repository links are updated by an explicit decision. The umbrella and infra repository names
already provide project-level discoverability.
