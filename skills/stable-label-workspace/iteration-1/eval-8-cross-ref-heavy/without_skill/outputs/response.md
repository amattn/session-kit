# Cross-Reference Summary: Decisions and Requirements

## How Decisions Relate to Requirements

The six technical decisions (DEC_1 through DEC_6) form an interconnected system that collectively satisfies the eight requirements (REQ_1 through REQ_8). Here is how they map.

### Direct Satisfaction

| Decision | Requirement(s) Satisfied | Relationship |
|----------|--------------------------|--------------|
| DEC_1 (PostgreSQL) | REQ_3 (real DB testing), REQ_6 (concurrent access) | PostgreSQL provides the real database that tests run against (REQ_3) and handles concurrent writes from multiple services (REQ_6). |
| DEC_2 (FastAPI) | REQ_1 (Python 3.12+), REQ_7 (auto-generated docs) | FastAPI requires modern Python (REQ_1) and produces OpenAPI/Swagger docs from code automatically (REQ_7). |
| DEC_4 (GitHub Actions CI) | REQ_3 (real DB testing) | CI runs the full integration test suite against a real database, enforcing the no-mocking rule. |
| DEC_6 (JWT auth) | REQ_8 (stateless API) | JWT tokens carry all auth state in the token itself, eliminating server-side session storage. |

### Decisions Without Direct Requirement Links

| Decision | Status |
|----------|--------|
| DEC_3 (Fly.io deployment) | Chosen for team familiarity and low operational overhead. Not tied to a specific requirement but enables the production environment for the API. |
| DEC_5 (In-memory caching) | A pragmatic starting point. Redis was rejected as overkill. Explicitly noted for revisit if REQ_6 (concurrent access) demands it at scale. |

### Requirements Without Direct Decision Links

| Requirement | Status |
|-------------|--------|
| REQ_2 (proper HTTP status codes) | A code-level convention enforced in endpoint implementations. No dedicated infrastructure decision needed. |
| REQ_4 (snake_case JSON, data/error keys) | A serialization convention. FastAPI (DEC_2) supports this via Pydantic response models, but no standalone decision was made for it. |
| REQ_5 (mobile app with offline sync) | A product-level requirement. No decision yet addresses offline sync specifically. This is a gap worth tracking. |

## Decision-to-Decision Relationships

Several decisions reinforce or depend on each other:

- **DEC_1 (PostgreSQL) + DEC_4 (GitHub Actions):** CI spins up a real Postgres instance for integration tests, jointly satisfying REQ_3.
- **DEC_2 (FastAPI) + DEC_6 (JWT):** FastAPI's dependency injection system is a natural fit for JWT middleware, together delivering a stateless, well-documented API (REQ_7 + REQ_8).
- **DEC_5 (in-memory cache) + DEC_1 (PostgreSQL):** The caching layer sits in front of the database. If concurrent access patterns (REQ_6) cause contention, the cache strategy may need to escalate to Redis, which would become a new decision.
- **DEC_3 (Fly.io) + DEC_1 (PostgreSQL):** Fly.io offers managed Postgres, making deployment of the chosen database straightforward.

## Open Gaps

1. **REQ_5 (mobile/offline sync)** has no corresponding decision yet. Offline sync typically requires conflict resolution strategy, versioning, or a sync protocol — none of which have been decided.
2. **DEC_5 (in-memory caching)** is explicitly provisional. Under heavy concurrent load (REQ_6), it may need to be revisited.
