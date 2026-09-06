# Contract ownership

## Transitional state

The backend requirements currently live under
`Officialsayp/zolotoy-dev-frontend/docs/backend-specs/` because the frontend was designed before the
backend repositories were created. That is acceptable temporarily but should not become permanent
ownership.

## Migration rule

When creating a backend repository:

1. seed it from the matching backend specification;
2. add its canonical OpenAPI and domain documentation there;
3. treat the backend repository as authoritative for implemented behavior;
4. change the frontend to consume the canonical contract incrementally;
5. replace the old frontend-side spec with a pointer/archive only when doing so will not destroy useful
   project history;
6. update this umbrella repository so only one location is described as canonical.

## Contract categories

- REST schema and error codes: canonical OpenAPI in the service repository once available.
- Kafka events: producer-owned versioned schema; consumers validate compatibility but do not redefine it.
- Database schema: service migrations only; never a cross-service SQL contract.
- Browser runtime integration: frontend config/API facade; it must not invent backend fields to satisfy a UI.

Unknown shapes remain `TBD / requires API contract decision` rather than being guessed.
