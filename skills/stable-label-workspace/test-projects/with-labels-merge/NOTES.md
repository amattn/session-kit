# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience with it. Low operational overhead.

### DEC_4: CI — GitHub Actions (2026-03-14)
Standard for GitHub-hosted repos. Runs integration tests before deploy.

### DEC_5: Caching — in-memory (2026-03-14)
Redis rejected as overkill for now.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum

### REQ_2: Proper HTTP status codes

### REQ_3: No database mocking in tests

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
