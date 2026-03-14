# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Caching: in-memory, not Redis** — Decided to use a simple in-memory cache rather than Redis. Keeps the stack simpler for now; can revisit if we need distributed caching or persistence later.

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
