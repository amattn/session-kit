# Rate Limiting Plan

This plan is for product, who confirm the partner-facing rules and own two open items, and for the engineer who builds it. Product can stop after Decisions; assumptions, risks, and scope are for the implementer. Three choices settled in NOTES.md (state in Redis, 429 with `Retry-After`, keyed per API key) are not re-argued.

## Open items

1. The limit. The record's only number: one partner at 2k rps slowed the mobile app. I lean to 2x the busiest partner's normal p99 from the LB logs; measure first. Owner: product and eng.
2. Is the mobile app exempt? One shared app key would throttle ~40k daily users as one client and stale the available-funds screen. I lean exempt; the complaint is partners. Owner: product.
3. Redis unreachable: allow or reject? I lean allow, logged. Redis is also the balance cache, so the app is already degraded, and rejecting turns a slowdown into an outage. Owner: eng.

## Decisions

- Token bucket (a burst allowance that refills at a fixed rate) over sliding-window counter: one atomic Redis Lua call per request, no timestamp log. Revisit if a partner needs smoothed rather than capped throughput.
- FastAPI middleware on every partner route, including export, over per-route decorators: one policy. Supersedes the per-IP in-process counter in docs/design.md.
- One limit for all partners over per-tenant quotas, per "pick a default and we'll revisit". Revisit if a partner contract specifies a rate.
- 401 before the limiter runs, so there is no shared "no key" bucket.

## Assumptions

- [ ] Middleware can read the partner API key before the handler runs.
- [ ] The mobile app uses one shared key (if not, item 2 is moot).
- [ ] All three replicas share one Redis.

## Risks

- Each request gains one Redis round trip; measure p99 latency before ship.

## Scope out

- Per-tenant quotas.
- Per-user limiting of mobile users.
- `X-RateLimit-*` headers on successful responses.
- Admin UI or runtime config for limits.
