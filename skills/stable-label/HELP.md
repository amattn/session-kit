# /stable-label — Quick Reference

**Setup:** Run `/stable-label` in your project. It scans existing artifacts, proposes a prefix table (e.g., `DEC` for decisions, `REQ` for requirements), adds convention rules to CLAUDE.md, and writes the prefix table to NOTES.md under Taxonomy / Conventions.

**Ongoing:** IDs are assigned automatically when you create or commit to something — a new requirement, a design decision, a feature. The agent won't assign IDs to exploratory output (brainstorms, summaries, option lists). Invoke `/stable-label` when you want to:
- Add a new prefix to the table
- Run a consistency pass (Quick for a single ID, Standard for a batch, Sweep for a whole prefix)
- Manage ID lifecycle — splitting, merging, deprecating, or promoting items

**Example:**
```
You: add a new requirement: API responses must be under 200ms
Agent: Added to the requirements spec:
       REQ_7 — API responses must complete within 200ms (p95)

You: let's go with Redis caching to meet that
Agent: (adds to NOTES.md)

       ### Caching strategy: Redis (2026-03-14)
       DEC_12 — Use Redis for response caching to meet REQ_7.
       - Rejected: CDN-only — doesn't help for authenticated endpoints

You: ok now implement the caching middleware
Agent: (writes code with traceability)

       # Cache middleware for API responses
       # Implements DEC_12 (Redis caching) to satisfy REQ_7 (200ms p95)
       class ResponseCache:
           ...

You: (later) grep REQ_7
       spec.md:         REQ_7 — API responses must complete within 200ms
       NOTES.md:        DEC_12 — Redis caching to meet REQ_7
       middleware.py:   # Implements DEC_12 to satisfy REQ_7
```
