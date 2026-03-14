# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

- **Database: PostgreSQL** — chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience).
- **Framework: FastAPI** — chose over Flask for async support and built-in OpenAPI docs.
- **Deployment: Fly.io** — team already has experience with it.
- **CI: GitHub Actions** — standard for GitHub-hosted repos.
- **Caching: in-memory** — Redis rejected as overkill for now.

## Invariants & Critical Requirements

- Python 3.12 minimum
- All endpoints return proper HTTP status codes
- Never mock the database in tests
- API responses use snake_case JSON with top-level "data"/"error" keys

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
- Auth: JWT vs session tokens?
