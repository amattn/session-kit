# Rate Limiting Plan

**Status:** proposal, ready for review
**Audience:** product and engineering
**Owner:** TBD

## Why

Last month one partner sent ~2k requests/sec and the mobile app got slow for everyone. ledgerd has no protection against this today: a single integration can consume the capacity that 40k daily mobile users depend on. Rate limiting puts a ceiling on what any one caller can do so that one partner's bug or traffic spike does not degrade the app for everyone else.

The goal is **isolation, not revenue control.** We are not building metered billing or tiered plans. We are making sure the noisy neighbor only hurts themselves.

## What is already decided

These were settled in September and are recorded in `NOTES.md`. This plan builds on them and does not reopen them.

| Decision | Why |
|---|---|
| Limiter state lives in Redis | Three replicas share one limit; an in-process counter would give each partner 3x the limit. Sticky sessions were rejected because partners do not send cookies. |
| Limited requests get `429 Too Many Requests` with a `Retry-After` header | The mobile client already backs off on 429. 503 would be ambiguous and silently queueing hides the problem from partners. |
| Limit is keyed per API key, not per IP | Partners share egress IPs. Keying by IP would throttle several partners together. |

## Proposal

### Algorithm: token bucket

Each API key gets a bucket that refills at a steady rate and holds up to a fixed number of tokens. Every request takes one token; a request that finds the bucket empty gets a 429.

Why token bucket over the alternatives:

- Partners are bursty. A batch job that fires 300 requests in two seconds and then nothing for a minute is normal and fine. Token bucket lets that burst through as long as the *average* stays under the limit. A fixed window would reject half of it for no benefit.
- It is one Redis key per API key and one Lua script per request. Sliding-window-log is more precise but stores a timestamp per request, which at 2k rps is real memory for no practical gain.
- The parameters are easy to explain to a partner: "you can sustain N requests per second and burst to M."

### Defaults

Per the preference for "pick a default and revisit" rather than config knobs, the proposal is **one limit for all partners**, hardcoded, with a single override mechanism (see Per-partner limits below).

| Parameter | Default | Rationale |
|---|---|---|
| Sustained rate | **100 requests/sec** per API key | Comfortably above any legitimate partner traffic we have seen outside of the incident, and 20x below the 2k rps that caused the outage. |
| Burst capacity | **500 requests** | Lets a partner's batch job run for ~5 seconds at full speed before the sustained rate kicks in. |

**These numbers are a starting point, not a measurement.** Before enforcing, we will run the limiter in shadow mode (below) and look at real per-key traffic for a week. If a legitimate partner would have been throttled, we raise the default before turning it on. The plan is to ship with one number we are confident is safe, not to guess perfectly.

### Response contract

Every response (limited or not) carries:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 37
```

A limited response is:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 1
Content-Type: application/json

{"error": "rate_limited", "retry_after_seconds": 1}
```

`Retry-After` is computed from the bucket's refill rate: how long until at least one token is available, rounded up to a whole second. It is never longer than a few seconds under the proposed defaults.

### Scope: which requests are limited

- **All partner API traffic** (every request authenticated with a partner API key), on every endpoint. There is no reason to exempt specific endpoints; the expensive ones are the ones we most want to protect.
- **Mobile app traffic is not subject to the partner limit.** See Open decisions below for what the mobile app gets instead.
- Health checks and internal endpoints are not limited.

### Where it sits

A FastAPI middleware in `src/api/`, running after authentication (so the API key is known) and before the route handler. Order matters: an unauthenticated request should get a 401, not a 429, and a limited request should never reach Postgres.

### Redis details

- One key per API key: `ratelimit:{api_key_id}`, holding the token count and last-refill timestamp.
- Check-and-decrement happens in a single Lua script so it is atomic across the three replicas. This is the standard pattern; no new infrastructure.
- Keys expire after `burst / rate` seconds of inactivity (5s at the proposed defaults), so idle partners cost nothing.
- **Redis is shared with the balance cache.** The 30-second balance freshness invariant depends on that cache. The limiter adds one small Redis round-trip per request, which is well within headroom, but we will confirm Redis latency does not move during shadow mode. If it does, the limiter moves to its own Redis instance before we enforce.

### Failure mode: fail open

If Redis is unreachable or the Lua call times out (budget: 10ms), the request is **allowed through** and a metric is incremented. Rationale: if Redis is down the balance cache is down too, and we have a bigger problem that rate limiting will not fix. Failing closed would turn a Redis blip into a full partner outage.

This is a deliberate trade-off. During a Redis outage a noisy partner is unthrottled. We accept that because the outage itself is the thing to fix, and the alert on the fail-open metric will fire alongside it.

## Open decisions

These are listed as open in `NOTES.md`. Each one has a recommendation so that review can be a yes/no rather than a discussion from scratch.

### 1. Per-partner limits

**Recommendation: not now, but leave the door open.**

Ship with one limit for everyone. Store an optional per-key override in the same place API keys live (the partner record in Postgres), defaulting to null. If null, the hardcoded default applies. This is one nullable column, not a configuration system. We do not build an admin UI for it; if a partner needs a higher limit, an engineer sets it.

This gives us a release valve for the first partner who legitimately needs more, without committing to tiered plans.

### 2. Mobile app limit

**Recommendation: a separate, per-user limit, generous enough that no real user hits it.**

The mobile app should not share a bucket with partners (a single app-wide bucket for 40k users would be the noisy-neighbor problem again, just inside the app). Instead, key on the authenticated user and set a limit well above anything a human on a phone can generate: proposed **20 requests/sec sustained, burst 60**. This catches a broken client in a retry loop without ever touching a normal user.

Phase this in *after* partner limiting ships. Partners are the known problem; the mobile limit is defense in depth.

## Rollout

| Phase | What happens | Exit criteria |
|---|---|---|
| **1. Shadow mode** (1 week) | Limiter runs on every request and records what it *would* have done. No 429s are sent. Dashboard shows per-key would-be-reject counts. | No legitimate partner would have been throttled at the proposed defaults, or defaults are adjusted until that is true. Redis latency unchanged. |
| **2. Partner notice** (2 weeks before enforcement) | Email each of the 6 partners with the limit, the headers, and the 429 contract. Product owns the message; engineering supplies the numbers. | All 6 partners acknowledged. |
| **3. Enforce for partners** | Flip from shadow to enforce. Per-key overrides available for anyone who asked for one in phase 2. | One week with no unexpected 429s to partners who were not the source of excess traffic. |
| **4. Mobile per-user limit** | Shadow for a week, then enforce. | Zero real users hit the limit in shadow. |

The shadow phase is the important one. It turns the default from a guess into a number we have checked against real traffic.

## What product needs to decide or own

- Approve the partner-facing message and send it (phase 2).
- Confirm the stance on per-partner limits: engineer-set override on request, no self-serve, no tiers. If product wants tiers in the next two quarters, say so now, because it changes where the limit is stored.
- Decide whether the rate limit is documented publicly in the partner API docs (recommendation: yes, with the headers and the 429 example above).

## What engineering will build

1. Token-bucket Lua script and a small `RateLimiter` class wrapping it, with unit tests against a real Redis.
2. Middleware in `src/api/` with shadow/enforce switch (one environment variable; the only knob).
3. Response headers and the 429 body.
4. Metrics: per-key allowed/limited/would-be-limited counts, Redis call latency, fail-open count. One dashboard, one alert on fail-open.
5. Nullable per-key override column, read at request time (cached per key for 60s so it is not a Postgres hit per request).
6. Per-user mobile limiter (phase 4), reusing the same class with a different key prefix and defaults.

Rough estimate: items 1 through 4 are about a week of engineering work plus the shadow week. Item 5 is a day. Item 6 is a couple of days.

## Out of scope

- Metered billing, quotas per month, or anything that looks like a pricing feature.
- Limiting by endpoint cost (weighting expensive calls more). Revisit if shadow data shows a partner staying under the request limit while still hurting us.
- Queueing or smoothing (leaky bucket). Rejected in September: it hides the problem from partners.
- The transaction export design (`docs/design.md`) proposes a per-IP in-process counter for export requests. That section predates the September decisions and should be updated to use this limiter instead; it is noted here so it does not get built separately.

## Decisions to record in NOTES.md once approved

- Algorithm: token bucket, 100 rps sustained / 500 burst per API key.
- Fail open on Redis errors.
- Mobile: separate per-user limit, not the partner limit.
- Per-partner overrides: nullable column on the partner record, engineer-set, no UI.
