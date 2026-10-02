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
