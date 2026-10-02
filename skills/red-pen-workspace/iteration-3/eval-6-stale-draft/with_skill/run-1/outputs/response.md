Wrote `docs/design.md`. The export flow (background job, CSV, webhook, 24-hour URL) and all three storage options are kept; the Next steps list is gone because it restated the sections. Two claims were stale and I replaced them from NOTES.md:

- "Rate limiting has not yet been decided", with a per-IP in-process counter proposed. NOTES.md decided Redis state (09-10) and per-API-key keying with 429 + `Retry-After` (09-12).
- "The database choice for ledgerd is still open." It is Postgres; that is now an assumption to tick.

Before:

> Export requests should be rate limited. The rate limiting approach for ledgerd has not yet been decided, so this design proposes a simple per-IP counter in process memory as a starting point, which can be revisited later.

After:

> Export requests are rate limited the way the rest of ledgerd is: state in Redis, keyed per API key, 429 with `Retry-After` when limited (NOTES.md, 2026-09-10 and 2026-09-12). This design sets no export-specific limit.

| Symptom | Before | After |
|---|---|---|
| Claims contradicting NOTES.md | 2 | 0 |
| Overview / Background / Next steps headers | 3 | 0 |
| Session narration ("In this document we will cover...") | 2 | 0 |
| Open items with no lean | 1 | 0 |

Two things in the new text are mine, not the original's, so strike them if they are wrong: the storage lean (Postgres, unless exports are too large for the database) and the named reader (the engineers building export).
