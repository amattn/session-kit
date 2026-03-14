# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Caching: in-memory cache, not Redis** (2026-03-14) — Use a simple in-memory cache rather than Redis. User said: "forget Redis — let's just use an in-memory cache for now." Rationale is pragmatic simplicity at this stage. The "for now" qualifier suggests this may be revisited later if the project outgrows in-process caching (e.g., multi-instance deployment, persistence needs). **Rejected:** Redis — too heavy for current needs.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Database choice — PostgreSQL vs SQLite?
- Framework choice — FastAPI vs Flask?
- Deployment target — undecided

---

## Taxonomy / Conventions

*(None yet)*
