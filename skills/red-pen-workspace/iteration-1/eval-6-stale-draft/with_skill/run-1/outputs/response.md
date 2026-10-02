Edited `docs/design.md` in place (263 words to 194).

```
# Transaction Export Design

This document is for the ledgerd owner deciding where export files are stored; it assumes the decisions in NOTES.md and the deploy in CLAUDE.md (3 replicas, Postgres, Redis). Open decisions come first; everything after them is settled and one line each.

## Open

- Storage for export files: Postgres large objects or S3. Lean Postgres, because it is already in the deploy and S3 would be a new dependency; S3 if exports are large. What settles it: expected CSV size per export. Local filesystem is out: 3 replicas.
- Whether exports count against the partner's `/transactions` budget or get their own. Lean shared, so a partner cannot use exports to bypass the limit; revisit if exports crowd out reads.

## Decisions

- Export runs as a background job that writes one CSV.
- Partner is notified by webhook (`src/webhook_client.py`, at-least-once) with a download URL.
- Download URL expires after 24 hours; revisit if partners report missing the window.
- Export requests use the existing limiter: Redis-backed, keyed per API key, 429 + `Retry-After` (NOTES.md 2026-09-10, 2026-09-12).

## Assumptions

- [ ] Partners want bulk history, not faster paging of `/transactions`.
```

What was wrong, by symptom:

- Stale, 2 claims. "The database choice for ledgerd itself is also still open" (CLAUDE.md: Postgres). "The rate limiting approach has not yet been decided" (NOTES.md has three decisions, 2026-09-10 and 09-12), and the draft's proposal contradicted every one of them: in-process not Redis, per-IP not per-key, no 429. Replaced the proposal with the record; the one real residual question, whether exports share the partner's budget, is now an ask with a lean.
- No stance, 1 section. Storage listed three options with a trade-off each and no lean. Filesystem is already ruled out by the record (3 replicas); between the other two I put a lean and what would settle it. The lean is mine; overrule it.
- Scaffold headers, 3 of 7: Overview (narrated the doc's own table of contents), Background (one useful sentence, now an assumption), Next steps (restated the two open items and the two decisions above it).
- Session narration, 2 ("In this document we will cover", "This document describes"). Opener/hedge, 1 ("This is a reasonable default" on the 24h expiry, replaced with a revisit condition).
- Missing preamble: the draft never said who it was for or what it needed from them. Added one; readers aren't in CLAUDE.md, so I assumed the single reader is you as owner.

Before/after, the rate-limiting section:

> Export requests should be rate limited. The rate limiting approach for ledgerd has not yet been decided, so this design proposes a simple per-IP counter in process memory as a starting point, which can be revisited later.

> Export requests use the existing limiter: Redis-backed, keyed per API key, 429 + `Retry-After` (NOTES.md 2026-09-10, 2026-09-12).

Nothing else in the project was touched.
