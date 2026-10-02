# Transaction Export Design

Status: draft. Storage and the export-specific rate limit are undecided (see Open questions).

## Problem

Partners can only get transaction history by paging through `/transactions`, which is slow for large accounts. They have asked for a bulk export.

## Approach

1. A partner requests an export.
2. A background job writes the transactions to a CSV file.
3. When the file is complete, ledgerd sends the partner a webhook containing a download URL.
4. The URL expires after 24 hours.

The webhook goes through the existing `WebhookClient` (`src/webhook_client.py`). Delivery is at-least-once and partners dedupe on `event_id`, so a partner may receive the "export ready" event more than once.

## Rate limiting

Export requests go through ledgerd's existing rate limiter, as decided in `NOTES.md`:

- State lives in Redis, because the limit has to be shared across the three replicas.
- The limit is keyed per API key, not per IP. Partners share egress IPs.
- A limited request gets a 429 with `Retry-After`.

## Storage

Not decided. The export file has to be readable from whichever replica serves the download, which rules out the local filesystem. That leaves:

- **Postgres large objects.** No new system to run. Export files then share the database with balance and transaction queries.
- **S3.** Durable and cheap. Adds a dependency beyond Postgres and Redis.

## Open questions

- Storage: Postgres large objects or S3.
- Whether exports need their own, lower limit than ordinary requests. An export costs far more than a page of `/transactions`. `NOTES.md` has one limit for all partners, with per-tenant quotas still open.
- How a partner requests an export: the endpoint, its parameters (account, date range), and what it returns.
- How the download URL is authorized: a signed URL, or the partner's API key.
- What happens when the job fails or the webhook cannot be delivered. This design gives a partner no way to ask for an export's status.
- Whether 24 hours is the right expiry. No one has checked it against how partners will use the file.
- What runs the background job.

## Next steps

- Decide on storage.
- Decide whether exports get their own limit.
- Specify the request endpoint and the download authorization.
- Implement the background job.
- Implement the webhook notification.
