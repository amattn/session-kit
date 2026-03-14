# Technical Decision Cross-Reference Summary

This document maps how the six design decisions in inventory-api relate to each other and which requirements each one satisfies. Every reference below is a greppable stable label — grep any ID to find its definition in NOTES.md and every place it is referenced.

---

## Decision-to-Requirement Traceability

| Decision | Satisfies | Rationale |
|----------|-----------|-----------|
| DEC_1 (PostgreSQL) | REQ_3, REQ_6 | PostgreSQL provides the real database that REQ_3 demands for integration testing and the concurrent write support that REQ_6 requires. |
| DEC_2 (FastAPI) | REQ_1, REQ_7 | FastAPI runs on REQ_1's Python 3.12+ baseline and generates the OpenAPI docs that REQ_7 mandates. |
| DEC_3 (Fly.io) | — | Operational choice driven by team experience, not directly tied to a numbered requirement. |
| DEC_4 (GitHub Actions) | REQ_3 | CI runs the full integration test suite against a real database per REQ_3. |
| DEC_5 (In-memory caching) | — | Interim decision. Redis was rejected as premature, but REQ_6 (concurrent access) is the trigger for revisiting. |
| DEC_6 (JWT auth) | REQ_8 | JWTs keep the API stateless, directly satisfying REQ_8. |

## Requirements Not Yet Covered by a Decision

| Requirement | Status |
|-------------|--------|
| REQ_2 (Proper HTTP status codes) | Convention, not a technology choice — enforced by code review and tests rather than a specific DEC. |
| REQ_4 (snake_case JSON / data+error envelope) | Response format convention. No DEC selects a serialization library or envelope strategy yet. |
| REQ_5 (Mobile app with offline sync) | No decision addresses offline sync architecture. This is an open area that will likely generate future DECs around conflict resolution strategy, sync protocol, and data versioning. |

## How Decisions Relate to Each Other

**DEC_1 + DEC_4 — the testing backbone.** DEC_1 chose PostgreSQL partly because REQ_3 forbids database mocking. DEC_4 chose GitHub Actions as the CI platform that executes those real-database integration tests. Together they form a chain: DEC_1 provides the database, DEC_4 runs the tests against it, and REQ_3 is the requirement that makes both necessary.

**DEC_2 + DEC_1 — the application stack.** DEC_2 (FastAPI) is the framework; DEC_1 (PostgreSQL) is the data layer. FastAPI's async support pairs well with PostgreSQL's concurrent write capabilities (REQ_6). Both decisions share REQ_1 as a baseline constraint — Python 3.12+ is load-bearing for framework choice and dependency selection.

**DEC_6 + DEC_5 — statelessness by design.** DEC_6 chose JWTs to satisfy REQ_8 (stateless API). DEC_5 chose in-memory caching over Redis, which is consistent with the stateless philosophy — no external state store beyond the database. If REQ_6 pressure grows, DEC_5 may need revisiting, but the current pairing keeps the architecture simple.

**DEC_3 — operationally independent.** DEC_3 (Fly.io) stands alone. It doesn't directly satisfy a numbered requirement and doesn't constrain other decisions. It could change without affecting DEC_1 through DEC_6 or any REQ.

## Requirement Clusters

Three natural clusters emerge from the cross-references:

1. **Data integrity cluster** — REQ_3 (real DB testing), REQ_6 (concurrent access), served by DEC_1 and DEC_4. This cluster ensures the database layer is trustworthy under real conditions.

2. **API design cluster** — REQ_1 (Python 3.12+), REQ_2 (HTTP status codes), REQ_4 (JSON conventions), REQ_7 (auto-generated docs), REQ_8 (stateless). Served by DEC_2 and DEC_6. This cluster defines how the API presents itself to consumers.

3. **Mobile/client cluster** — REQ_5 (mobile app with offline sync). Currently unserved by any DEC. This is the most significant gap in the decision landscape and the most likely source of future architectural decisions.
