# Transaction Export Design

This note is for the ledgerd owner, who decides where export files are stored, and for the engineer building the job. Storage is the one open decision and comes first; the rest follows decisions already recorded in NOTES.md.

## Storage

Open: Postgres large objects or S3. The local filesystem is out; it does not work across the three replicas. Lean S3 on this note's own grounds (durable, cheap); Postgres large objects if keeping everything in one system matters more.

## Rate limiting

Exports go through the existing limiter (state in Redis, keyed per API key, 429 with `Retry-After`; NOTES.md 2026-09-10 and 2026-09-12) rather than a separate one; revisit if bulk exports crowd out partners' ordinary traffic.

## Approach

The export runs as a background job that writes a CSV, then notifies the partner by webhook with a download URL that expires after 24 hours.

Assumptions:
- [ ] Paging `/transactions` is the pain: large accounts are slow to page.
- [ ] Webhook delivery is at-least-once and partners dedupe on `event_id` (src/webhook_client.py), so a repeated "export ready" notification is harmless.
