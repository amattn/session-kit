# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience with it.

### DEC_4: CI — GitHub Actions (2026-03-14)
Standard for GitHub-hosted repos.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum

### REQ_2: Proper HTTP status codes

### REQ_3: No database mocking in integration tests
Integration tests must hit a real database. Team got burned by mock/prod divergence.

### REQ_5: No database mocking in unit tests
Unit tests must also hit a real database. Same rationale as REQ_3 — mock/prod divergence burned the team.

### REQ_4: snake_case JSON responses

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
