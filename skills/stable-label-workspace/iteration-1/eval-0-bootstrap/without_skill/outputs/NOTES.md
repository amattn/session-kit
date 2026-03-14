# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Stable Labels

Stable labels are greppable identifiers that provide permanent, location-independent references to key decisions, invariants, and architectural anchors. They survive file moves and refactors. Format: `[LABEL-NAME]` — grep for the label to find all references.

| Label | Meaning |
|-------|---------|
| `[DB-POSTGRES]` | Database is PostgreSQL; do not switch without revisiting concurrency assumptions |
| `[FRAMEWORK-FASTAPI]` | Framework is FastAPI; async-first, OpenAPI built-in |
| `[DEPLOY-FLYIO]` | Deployment target is Fly.io |
| `[CI-GHA]` | CI runs on GitHub Actions |
| `[CACHE-INMEMORY]` | Caching is in-memory only; no Redis |
| `[PY312-MIN]` | Python 3.12 is the minimum supported version |
| `[STATUS-CODES]` | All endpoints must return proper HTTP status codes |
| `[NO-DB-MOCKS]` | Never mock the database in tests; use real DB |
| `[RESPONSE-FORMAT]` | API responses: snake_case JSON, top-level "data"/"error" keys |
| `[OPEN-ORM]` | Unresolved: SQLAlchemy vs raw SQL |
| `[OPEN-AUTH]` | Unresolved: JWT vs session tokens |

## Key Design Decisions

- **Database: PostgreSQL** `[DB-POSTGRES]` — chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience).
- **Framework: FastAPI** `[FRAMEWORK-FASTAPI]` — chose over Flask for async support and built-in OpenAPI docs.
- **Deployment: Fly.io** `[DEPLOY-FLYIO]` — team already has experience with it.
- **CI: GitHub Actions** `[CI-GHA]` — standard for GitHub-hosted repos.
- **Caching: in-memory** `[CACHE-INMEMORY]` — Redis rejected as overkill for now.

## Invariants & Critical Requirements

- Python 3.12 minimum `[PY312-MIN]`
- All endpoints return proper HTTP status codes `[STATUS-CODES]`
- Never mock the database in tests `[NO-DB-MOCKS]`
- API responses use snake_case JSON with top-level "data"/"error" keys `[RESPONSE-FORMAT]`

## Open Questions

- ORM: SQLAlchemy vs raw SQL? `[OPEN-ORM]`
- Auth: JWT vs session tokens? `[OPEN-AUTH]`
