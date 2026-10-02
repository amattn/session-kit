# Transaction Export Design

This document is for the engineers building partner bulk export; it assumes familiarity with ledgerd. Settled decisions come first, and the one undecided item is under Open.

Partners export transaction history today by paging through `/transactions`, which is slow for large accounts. Export gives them one bulk download.

## Decisions

- The export runs as a background job that writes a CSV.
- When the CSV is complete, the partner is notified by webhook. The payload contains a download URL.
- The URL expires after 24 hours.
- Export requests are rate limited the way the rest of ledgerd is: state in Redis, keyed per API key, 429 with `Retry-After` when limited (NOTES.md, 2026-09-10 and 2026-09-12). This design sets no export-specific limit.

## Assumptions

- [ ] Postgres stays ledgerd's database.
- [ ] ledgerd keeps running as more than one replica, which is what rules out local-filesystem storage below.

## Open

- **Where export files are stored: Postgres large objects or S3.** Postgres keeps everything in one system; S3 is durable and cheap. The local filesystem is out because it does not work across replicas. Lean: Postgres, since a file lives 24 hours and it adds no new system; S3 if exports are too large to hold in the database. The largest expected export size would settle it.
