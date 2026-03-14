# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

- **[DEC-001] Database: PostgreSQL** — chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience).
- **[DEC-002] Framework: FastAPI** — chose over Flask for async support and built-in OpenAPI docs.
- **[DEC-003] Deployment: Fly.io** — team already has experience with it.
- **[DEC-004] CI: GitHub Actions** — standard for GitHub-hosted repos.
- **[DEC-005] Caching: in-memory** — Redis rejected as overkill for now.

## Invariants & Critical Requirements

- **[REQ-001]** Python 3.12 minimum
- **[REQ-002]** All endpoints return proper HTTP status codes
- **[REQ-003]** Never mock the database in tests
- **[REQ-004]** API responses use snake_case JSON with top-level "data"/"error" keys

## Open Questions

- **[OPEN-001]** ORM: SQLAlchemy vs raw SQL?
- **[OPEN-002]** Auth: JWT vs session tokens?
