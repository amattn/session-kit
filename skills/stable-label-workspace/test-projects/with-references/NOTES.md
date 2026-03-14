# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support. Satisfies REQ_3 (real database testing).

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support. Supports REQ_1 (Python 3.12+).

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience. Renamed to "Cloud hosting" for clarity.

### DEC_4: CI — GitHub Actions (2026-03-14)
Standard for GitHub-hosted repos.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum
Load-bearing — informs framework choices. See DEC_2.

### REQ_2: Proper HTTP status codes
All endpoints must return appropriate status codes.

### REQ_3: No database mocking in tests
Integration tests hit a real database. See DEC_1 for the database choice this enables.

### REQ_4: snake_case JSON responses
Top-level "data" key for success, "error" key for failures.

## Architecture Notes

The deployment pipeline (DEC_3) runs tests via GitHub Actions (DEC_4) before deploying to Fly.io. This ensures REQ_3 compliance — tests hit a real PostgreSQL instance in CI, not mocks.

API responses follow REQ_4 conventions. All error responses include a machine-readable error code per DEC_3.
