# ADR 0001 — Polyrepo boundaries

- Status: Accepted
- Date: 2026-09-06

## Context

The system contains one frontend, four independently deployable backend services and shared
cross-service infrastructure. Each backend has distinct storage/runtime/testing concerns.

## Decision

Use separate repositories for each deployable service, plus `zolotoy-dev-frontend`,
`zolotoy-dev-infra` and this umbrella documentation repository.

Backend repository names follow their current source specifications: `order-service`, `auth-service`,
`notification-service`, `url-shortener`.

## Consequences

- service contracts/migrations can evolve independently;
- CI and container images map cleanly to deployable units;
- cross-repository changes require explicit coordination;
- duplicated canonical documentation must be avoided;
- this umbrella repo is necessary to keep system-level architecture discoverable.
