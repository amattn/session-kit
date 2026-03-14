# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| ICR    | Invariants & critical requirements |
| OPQ    | Open questions |

## Key Design Decisions

- **DEC_1 Database: PostgreSQL** — chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience).
- **DEC_2 Framework: FastAPI** — chose over Flask for async support and built-in OpenAPI docs.
- **DEC_3 Deployment: Fly.io** — team already has experience with it.
- **DEC_4 CI: GitHub Actions** — standard for GitHub-hosted repos.
- **DEC_5 Caching: in-memory** — Redis rejected as overkill for now.

## Invariants & Critical Requirements

- **ICR_1** Python 3.12 minimum
- **ICR_2** All endpoints return proper HTTP status codes
- **ICR_3** Never mock the database in tests
- **ICR_4** API responses use snake_case JSON with top-level "data"/"error" keys

## Open Questions

- **OPQ_1** ORM: SQLAlchemy vs raw SQL?
- **OPQ_2** Auth: JWT vs session tokens?
