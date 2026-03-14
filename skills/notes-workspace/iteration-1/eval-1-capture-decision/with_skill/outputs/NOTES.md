# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Database: PostgreSQL** (decided 2026-03-14) — Chose PostgreSQL over SQLite. The API will need concurrent writes from multiple services, which rules out SQLite (single-writer limitation). **Rejected:** SQLite — insufficient concurrency support for multi-service write workloads.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Framework choice — FastAPI vs Flask?
- Deployment target — undecided

---

## Taxonomy / Conventions

*(None yet)*
