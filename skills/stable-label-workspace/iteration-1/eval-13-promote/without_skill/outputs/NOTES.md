# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum

### REQ_2: Proper HTTP status codes

### REQ_3: No database mocking in tests

### REQ_4: Standardized API error handling
All endpoints must use a consistent error response format with machine-readable error codes. No stack traces or generic 500s in responses. (Promoted from OBS_1)

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
| OBS    | Observations |
