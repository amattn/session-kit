# NOTES.md — ledgerd

## Project Context

ledgerd serves balances and transaction history to the mobile app (~40k daily users) and to 6 partner integrations over HTTP. Three replicas, Postgres, Redis.

## Invariants & Critical Requirements

- **Never return a balance older than 30 seconds.** Cache TTL is 30s and is load-bearing for the mobile app's "available funds" screen.

## Important Concepts & Insights

### From the user

- "partners are the noisy neighbors — one of them hammered us at 2k rps last month and the mobile app got slow"
- "I don't want a config knob for everything. pick a default and we'll revisit"

## Key Design Decisions

### Rate limiter state lives in Redis (2026-09-10)

Chose Redis over an in-process counter because there are three replicas and the limit has to be shared. Rejected: sticky sessions — partners don't send cookies.

### Rate-limited responses are 429 with Retry-After (2026-09-12)

Chose 429 + `Retry-After` over 503 because the mobile client already handles 429 by backing off. Rejected: silently queueing requests — hides the problem from partners.

### Rate limit keyed per API key, not per IP (2026-09-12)

Partners share egress IPs; keying by IP would throttle them together.

### Webhook delivery retries on 5xx and transport errors, not 4xx (2026-10-01)

`WebhookClient.send` makes up to 3 attempts with exponential backoff (200ms base, 2s cap, full jitter). Retry is safe because delivery is at-least-once and partners dedupe on event_id. 4xx fails fast, including 429 — a partner throttling us is their signal to slow down, not a reason to hit them again. Policy is fixed constants, not constructor knobs (per "pick a default and we'll revisit"). Rejected: honoring `Retry-After` on 429 — no partner sends it yet.

## Open Questions

- Per-tenant quotas (different limits per partner) — not decided. Default is one limit for all partners.
- Whether the mobile app gets its own, higher limit.
