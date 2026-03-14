# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Database: PostgreSQL** (not SQLite) — Need concurrent writes from multiple services; SQLite's single-writer limitation rules it out.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- ~~Database choice — PostgreSQL vs SQLite?~~ **Decided: PostgreSQL** (see Key Design Decisions)
- Framework choice — FastAPI vs Flask?
- Deployment target — undecided

---

## Taxonomy / Conventions

*(None yet)*
