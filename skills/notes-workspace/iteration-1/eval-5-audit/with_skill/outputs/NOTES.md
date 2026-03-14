# NOTES.md — api-project

## Project Context

REST API for managing inventory.

---

## Key Design Decisions

### Database: PostgreSQL (2026-03-14)

Chose PostgreSQL over SQLite. Need concurrent writes from multiple services.

### Framework: FastAPI (2026-03-14)

Chose FastAPI over Flask for async support.

### Deployment: Fly.io (2026-03-14)

Chose Fly.io for deployment. Previously undecided — captured during audit pass.

### CI/CD: GitHub Actions (2026-03-14)

Chose GitHub Actions for CI. Previously undecided — captured during audit pass.

---

## Open Questions

(none currently)
