# Rate Limiting Plan

Status: proposal. Owner: eng. Reviewers: product, eng.

## Why

Last month one partner sent ~2k requests/sec and the mobile app got slow. ledgerd has no rate limiting today, so any one of the 6 partners can degrade the service for the ~40k daily mobile users. This plan adds a shared limit so one noisy partner can't take down everyone else.

## What is already decided

These were settled in `NOTES.md` and this plan builds on them rather than reopening them:

| Decision | Why |
|---|---|
| Limiter state lives in Redis | Three replicas; the limit must be shared across them. |
| Over-limit requests get `429` with a `Retry-After` header | The mobile client already backs off on 429. 503 and silent queueing were rejected. |
| Limits are keyed per API key, not per IP | Partners share egress IPs; keying by IP would throttle them together. |

## Proposal

### Who gets limited

- **Partner API keys**: limited. Every partner gets the same limit in v1.
- **Mobile app**: not limited in v1. Mobile is the thing we're protecting, not the thing we're protecting against. If we later see abuse from the mobile side, add a per-user limit then.

This answers the two open questions in `NOTES.md` with a default: no per-partner quotas yet, and mobile is exempt rather than given its own higher limit. Both are easy to change later because the limit is looked up by key.

### The limit

**Default: 100 requests/sec sustained per partner key, with a burst allowance of 200.**

Reasoning: 6 partners at 100 rps each is 600 rps of partner traffic worst case, well under the 2k rps that caused the incident. The burst allowance absorbs short spikes (a partner's batch job starting up) without rejecting them. We do not know the partners' normal traffic shape yet; the shadow-mode rollout below tells us before we enforce anything.

Per the project's stated preference, this is one hardcoded default, not a per-partner config system. We revisit once we have data.

### Algorithm: token bucket

Each partner key has a bucket holding up to 200 tokens, refilled at 100 tokens/sec. Each request takes one token; an empty bucket means 429.

Why token bucket over the alternatives:

- **Fixed window** is simplest but lets a client send 2x the limit across a window boundary. Not good enough for the "one partner hammers us" case.
- **Sliding window counter** is a reasonable alternative and would be the pick if we wanted to disallow bursts entirely. Partner traffic is bursty by nature (batch jobs), so allowing a bounded burst is a feature here.
- **Sliding window log** is precise but stores a timestamp per request; too much Redis memory at these rates.

### Implementation

- A FastAPI middleware runs on every request, before the route handler.
- Bucket check-and-decrement is a single Redis Lua script so it is atomic across the three replicas. One round trip per request.
- Redis keys: `ratelimit:{api_key}` holding `tokens` and `last_refill`. Keys expire after 10s of inactivity so idle partners cost nothing.
- Responses include `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and on 429, `Retry-After` (seconds until at least one token is available, rounded up, minimum 1).
- **If Redis is unreachable, fail open** (allow the request, log it, bump a metric). A Redis outage should not take down balance serving. The limiter is a protection layer, not a correctness layer.
- Requests without an API key (mobile traffic) skip the limiter entirely.

Note: `CLAUDE.md` says route handlers live in `src/api/`, but that directory is not in the tree I can see. The middleware will go wherever the FastAPI app is constructed; exact file paths to be confirmed when implementing.

### Interaction with the 30-second balance invariant

Rate limiting does not touch the cache or its TTL. A rate-limited partner gets a 429, not a stale balance. Mobile traffic is exempt, so the "available funds" screen is unaffected.

### Rollout

1. **Shadow mode (1-2 weeks).** The middleware runs and records what it *would* have done, but never returns 429. We get per-partner traffic rates and a count of would-be rejections. If the default would reject a well-behaved partner's normal traffic, we adjust before anyone notices.
2. **Partner notice.** Product tells the 6 partners the limit, the 429 behavior, and the enforcement date. The response headers mean partners can see their remaining budget before enforcement starts.
3. **Enforce.** Flip to returning 429. Watch the dashboard for a week.

### What we'll watch

- Rejections per partner per minute (alert if a partner is being rejected continuously; that's either abuse or a limit set too low).
- Redis limiter latency (the Lua call adds one round trip per request; should be sub-millisecond).
- Fail-open count (should be zero; non-zero means Redis trouble).
- Mobile p95 latency, which is the number the incident actually hurt.

## For product

- One partner can no longer slow the app down for everyone. That's the point.
- Partners will start seeing 429s if they exceed 100 rps sustained. They need to be told before enforcement; this plan includes a shadow period so we can tell them whether they're currently over.
- No partner-specific tiers yet. If a partner needs more, that's a per-tenant quota, which is a known follow-up and a small change.
- Mobile users see no change.

## For eng

- Work is roughly: Lua script + Redis key layout, middleware, response headers, metrics, shadow-mode flag, tests. Estimate: one engineer, about a week including shadow-mode instrumentation.
- Tests should cover: burst allowed up to 200 then rejected; refill at 100/sec; `Retry-After` math; fail-open when Redis is down; mobile requests bypass.
- `docs/design.md` (transaction export) proposes a per-IP in-process counter for exports. That contradicts the decisions above and should be updated to use this limiter. Exports are a good first candidate for a stricter per-endpoint limit later.

## Follow-ups (not in v1)

- Per-partner quotas, once shadow data shows whether partners differ enough to need them.
- Per-endpoint limits (e.g. stricter on export, looser on balance reads).
- Per-user limit on mobile, only if abuse shows up.

## Decisions this plan makes

Recording these so they land in `NOTES.md` once agreed:

1. Token bucket, 100 rps sustained / 200 burst, same for every partner.
2. Mobile app exempt from rate limiting in v1.
3. Fail open when Redis is unavailable.
4. Shadow mode before enforcement.
