Wrote `docs/design.md`. Kept the Storage, Rate limiting, and Approach sections and the 24-hour URL expiry; cut Overview, Background, and Next steps (two of its four items are now settled, the other two restate the Approach). The doc named no reader, so the preamble names the owner (storage decision) and the implementing engineer; change it if that is wrong.

| Symptom | Before | After |
|---|---|---|
| Claims the record already settles ("database choice still open" — CLAUDE.md fixes Postgres; "rate limiting not yet decided" — NOTES.md has three decisions) | 2 | 0 |
| Proposal contradicting the record (per-IP counter in process memory vs. Redis state, keyed per API key) | 1 | 0 |
| Open decisions presented as a balanced menu with no lean | 1 | 0 (one ask, with lean) |
| Scaffold headers (Overview / Background / Next steps) | 3 | 0 |
| Session narration ("In this document we will cover") | 2 | 0 |
| Hedges on a settled default ("This is a reasonable default", "can be revisited later") | 2 | 0 |
| Words | 263 | 184 |

Before:

> The storage backend for the export files is still an open question. We could use Postgres large objects, S3, or the local filesystem. Each option has trade-offs. Postgres keeps everything in one system. S3 is durable and cheap. The local filesystem is simplest but does not work across replicas. The database choice for ledgerd itself is also still open; this design assumes Postgres but should be revisited if that changes.

After:

> Open: Postgres large objects or S3. The local filesystem is out; it does not work across the three replicas. Lean S3 on this note's own grounds (durable, cheap); Postgres large objects if keeping everything in one system matters more.
