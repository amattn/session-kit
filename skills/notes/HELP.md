# /notes — Quick Reference

**Setup:** Run `/notes` on a project without NOTES.md. It creates NOTES.md with suggested sections (Key Design Decisions, Invariants, Important Concepts, Taxonomy, Open Questions), references it from CLAUDE.md, and adds a Notes Discipline block that enforces note-taking in every future session.

**Ongoing:** Mostly automatic — the discipline block tells the agent to update NOTES.md after every decision before moving on. You don't need to invoke `/notes` for routine note-taking. Invoke it when you want to:
- Reorganize sections that have grown unwieldy
- Set up routing for multiple NOTES.md files (e.g., `guide/NOTES.md` for a subfolder with its own decision history)
- Set up a new project

**Example:**
```
You: let's go with PostgreSQL for the event store
Agent: (updates NOTES.md immediately)

       ### Database choice: PostgreSQL for event store (2026-03-14)
       User: "let's go with PostgreSQL for the event store"
       Chosen for durability guarantees and JSONB support.
       - Rejected: SQLite — insufficient for concurrent writes
       - Rejected: DynamoDB — team has no AWS experience

You: oh and we should never delete events, only soft-delete
Agent: (adds to Invariants & Critical Requirements)

       **Events are append-only — never hard-delete.**
       Soft-delete via a `deleted_at` timestamp. This is load-bearing
       for audit compliance and event replay.

You: I keep saying this but — names should be verbs for actions, nouns for systems
Agent: (adds to Important Concepts & Insights, under "From the user")

       User: "names should be verbs for actions, nouns for systems"
```
