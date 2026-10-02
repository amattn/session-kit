# Rate limiting plan for the ledgerd API

Status: proposed, 2026-10-02. Two decisions and one number need sign-off before enforcement starts (see "Decisions needed").

## Summary

Last month one partner sent about 2,000 requests per second and the mobile app slowed down for everyone. Nothing in ledgerd stops that from happening again.

This plan puts a cap on how fast each partner API key can call the API. A partner that goes over the cap gets an HTTP 429 response telling it how long to wait. Other partners and the mobile app are unaffected.

The limit is the same for every partner, and it applies to partner keys only at first. We run the limiter for a week in a mode that records what it would have blocked without blocking anything, confirm the number against that data, tell partners, and then turn it on.

## What partners and mobile users will see

**Partners under the limit:** no change.

**Partners over the limit:** requests beyond the cap return `429 Too Many Requests` with a `Retry-After` header giving the number of seconds to wait. Requests are rejected, not queued, so the partner sees the problem immediately and can slow down. Once the partner slows down, requests succeed again within a second or two.

**Mobile app users:** no change in the first release. Mobile traffic is not limited (see decision 1).

**Outbound webhooks** (ledgerd calling partners) are not affected. This plan covers inbound requests only.

## Decisions already made

These are recorded in `NOTES.md` and this plan follows them.

| Decision | Reason |
|---|---|
| Limits are counted per API key, not per IP address | Partners share outbound IPs, so counting by IP would throttle unrelated partners together |
| Counters live in Redis | There are three replicas and the count has to be shared between them |
| Over-limit requests get 429 with `Retry-After` | The mobile client already backs off on 429; queueing silently would hide the problem from partners |
| One fixed default rather than a set of configuration options | Pick a default now and revisit |

## Decisions needed

### 1. Does the mobile app get limited in the first release?

**Recommendation: no. Limit partner keys only.**

The problem we are solving is partners crowding out mobile. Limiting partners fixes it. Limiting mobile adds risk without addressing the incident: if the mobile app's requests all arrive under one shared key, a per-key limit would throttle all 40k daily users as a single client.

I could not confirm how mobile requests are identified, because the route handlers are not in the checkout I worked from. Whoever owns mobile auth should confirm this before we revisit. If each user or device has its own key, a mobile limit is straightforward to add later.

### 2. Do different partners get different limits?

**Recommendation: no. One limit for all six partners.**

This is the current default in `NOTES.md`. Per-partner quotas need somewhere to store them, a way to change them, and a commercial conversation about who gets what. None of that is needed to stop a repeat of last month. If the observation week shows one partner with a legitimate need well above the others, we revisit then.

### 3. The limit itself

**Proposed: 50 requests per second per key, with bursts up to 100.**

This number is a starting point, not a measured one. I have no data on normal partner traffic. The only figure available is the 2,000 requests per second that caused the incident. The proposed limit is 40 times lower than that, and if all six partners hit it at once the total is 300 requests per second.

Two things have to be true for the number to be right, and the observation week checks both:

- It is above every partner's normal peak, so no well-behaved partner gets blocked.
- Six partners at the limit together do not slow down mobile.

If either fails, we change the number before enforcing.

## How it works

**Algorithm: token bucket.** Each API key has a bucket that holds up to 100 tokens and refills at 50 tokens per second. Each request takes one token. A request that finds the bucket empty is rejected with 429. This allows short bursts, which partner batch jobs produce, while holding the average rate to 50 per second.

**Where it runs.** A FastAPI middleware that runs after authentication, so the API key is known, and before the route handler. It applies to every authenticated route with one bucket per key across all routes. Health checks are exempt.

**Redis.** One hash per key (`ratelimit:{api_key_id}`) holding the token count and the time of the last refill. The check and the update happen in a single Lua script so that two replicas handling requests for the same key at the same moment cannot both spend the last token. The script reads the time from Redis, not from the replica, so clock differences between replicas do not matter. Keys expire after a few seconds of inactivity, so idle partners cost no memory.

**`Retry-After` value.** The number of seconds until one token is available, rounded up, with a minimum of 1.

**If Redis is unavailable, requests are allowed through.** The alternative is to reject every partner request whenever Redis has a problem, which turns a cache outage into an API outage. The cost is that there is no protection during a Redis outage. The limiter's Redis call gets a short timeout so that a slow Redis does not slow every request, and failures raise an alert.

**The 30-second balance freshness rule is unaffected.** The limiter rejects requests. It never serves a cached or older balance in place of a fresh one.

**Cost.** One extra Redis round trip on every partner request. The added latency has not been measured. The observation week measures it.

**Constants, not configuration.** The rate and burst size are constants in code. The one switch is observe-only versus enforce, and it is removed once enforcement is stable.

## Rollout

1. **Build.** Middleware, Lua script, and tests. The tests cover: bursts up to the bucket size pass, sustained traffic over the rate is rejected, `Retry-After` is correct, two keys do not affect each other, concurrent requests cannot overspend the bucket, and a Redis failure allows the request.
2. **Observe for one week.** Deploy with the limiter counting but not blocking. It logs each request it would have rejected, by key. From this we get each partner's real peak rate, which partners would have been blocked and how often, and the added latency.
3. **Confirm the number.** Review the week's data against the two checks in decision 3. Adjust the limit if needed.
4. **Tell partners.** Product sends each partner the limit, the 429 and `Retry-After` behavior, and the enforcement date. Any partner the observation week showed going over the limit gets a direct conversation before the date.
5. **Enforce.** Turn on blocking. Watch 429 counts per key and mobile latency for the first days.

To roll back, switch to observe-only. No data migration is involved.

## Monitoring

- Requests allowed and rejected, per API key.
- Latency of the limiter's Redis call.
- Limiter Redis errors, with an alert, because during those the API is unprotected.
- A partner that is continuously rejected for more than a few minutes is worth a look. It usually means a retry loop that ignores `Retry-After`.

## Not in this plan

- Per-partner limits (decision 2).
- Limits on mobile traffic (decision 1).
- Different limits for different endpoints.
- Headers that report remaining quota on successful responses. Partners get `Retry-After` on 429 only.
- Protection against floods of unauthenticated or invalid-key requests. The limiter runs after authentication, so these never reach it. This is a separate problem, usually handled at the load balancer.

## Related: transaction export design

`docs/design.md` says the rate limiting approach is undecided and proposes a per-IP counter in process memory for export requests. That conflicts with the decisions above on both points: per-IP throttles partners that share IPs, and in-process counters are not shared across the three replicas. Export requests should go through this limiter. Because one export is far more expensive than one balance lookup, exports may need their own lower limit, which belongs in the export design. That document needs updating.
