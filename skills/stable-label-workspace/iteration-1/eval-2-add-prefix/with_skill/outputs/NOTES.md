# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience).

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support and built-in OpenAPI docs.

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience with it.

### DEC_4: CI — GitHub Actions (2026-03-14)
Standard for GitHub-hosted repos.

### DEC_5: Caching — in-memory (2026-03-14)
Redis rejected as overkill for now.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum
Load-bearing — informs framework choices, syntax usage, dependency selection.

### REQ_2: Proper HTTP status codes
All endpoints must return appropriate status codes.

### REQ_3: No database mocking in tests
Integration tests hit a real database. Team got burned by mock/prod divergence.

### REQ_4: snake_case JSON responses
Top-level "data" key for success, "error" key for failures.

### REQ_5: Mobile app support
API must support the companion mobile app with offline sync capabilities.

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
| END    | API endpoints |

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
- Auth: JWT vs session tokens?
