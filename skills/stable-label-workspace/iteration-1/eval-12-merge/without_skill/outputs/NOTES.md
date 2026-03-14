# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

### DEC_3: Deployment Infrastructure — Fly.io + GitHub Actions (2026-03-14)
Deploy to Fly.io (team already has experience, low operational overhead). CI via GitHub Actions (standard for GitHub-hosted repos, runs integration tests before deploy). Merged from former DEC_3 and DEC_4 — both are deployment infrastructure concerns.

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
