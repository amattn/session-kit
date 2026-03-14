# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support. MongoDB rejected (team lacks experience). Satisfies REQ_3 (real database testing) and REQ_6 (concurrent access).

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support and built-in OpenAPI docs. Supports REQ_1 (Python 3.12+) and REQ_7 (auto-generated API docs).

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience. Low operational overhead.

### DEC_4: CI — GitHub Actions (2026-03-14)
Standard for GitHub-hosted repos. Runs full integration test suite per REQ_3.

### DEC_5: Caching — in-memory (2026-03-14)
Redis rejected as overkill for now. Revisit if REQ_6 demands it.

### DEC_6: Auth — JWT tokens (2026-03-14)
Chose over session tokens for statelessness. Supports REQ_8 (API must be stateless).

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum
Load-bearing — informs framework choices, syntax usage, dependency selection.

### REQ_2: Proper HTTP status codes
All endpoints must return appropriate status codes.

### REQ_3: No database mocking in tests
Integration tests hit a real database. See DEC_1 and DEC_4.

### REQ_4: snake_case JSON responses
Top-level "data" key for success, "error" key for failures.

### REQ_5: Mobile app support
API must support the companion mobile app with offline sync capabilities.

### REQ_6: Concurrent access support
Multiple services write to the database simultaneously. See DEC_1.

### REQ_7: Auto-generated API documentation
OpenAPI/Swagger docs generated from code. See DEC_2.

### REQ_8: Stateless API
No server-side session state. See DEC_6.

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
