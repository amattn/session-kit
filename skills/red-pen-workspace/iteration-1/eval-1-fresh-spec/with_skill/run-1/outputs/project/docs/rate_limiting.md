# Rate Limiting Plan

This plan is for product, who confirm who gets limited and what partners see, and for the engineers building it. Product can stop after Decisions. NOTES.md already settled state in Redis, 429 + Retry-After, and keying per API key.

## Open item

Is v1 partners-only, with one limit for all? Product's call. Lean yes: the noisy-neighbor incident was partner traffic, and the ask was a default, not knobs. Mobile stays unlimited. Revisit if mobile abuse appears or a partner negotiates a higher tier.

## Decisions

- Token bucket over sliding window: partners run batch syncs, and a burst allowance lets a catch-up through while capping the average. Revisit if partners report 429s they cannot predict.
- 100 rps sustained, burst 200, per key: a guess, 20x under the 2k rps incident. Log-only the first week, then enforce; `would_have_429` logs turn the guess into a measurement.
- Fail open when Redis is unreachable: the limiter is for noisy neighbors, not attackers, and a Redis outage already breaks the balance cache.
- One bucket per key across all routes. Fewer knobs.

## Assumptions

- [ ] Every partner request carries an API key.
- [ ] The mobile app authenticates per user, not through one shared key. If shared, 40k users share one bucket.
- [ ] One extra Redis round-trip (~1ms) per request is acceptable.
- [ ] Partners honor Retry-After. Mobile does; partners are unverified.

## Risks

- A partner's legitimate sync gets 429s if its burst exceeds 200 in a second. The log-only week shows this first.
- Redis failover resets buckets; a partner briefly gets a fresh burst. Acceptable.

## Implementation

- FastAPI dependency on partner routes; a Lua script refills and decrements the bucket in one atomic round-trip.
- Key `ratelimit:{api_key}` holds tokens and last-refill time, with a TTL so idle partners cost nothing.
- `docs/design.md` proposes a per-IP in-process counter for export; export uses this limiter and that paragraph is stale.

## Scope out

Per-tenant quotas, admin UI, `X-RateLimit-*` headers, per-endpoint limits, a dashboard. Logs are the dashboard for v1.
