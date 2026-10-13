Here's the rate limiting picture for ledgerd, as recorded in `NOTES.md`.

## Why we rate limit at all

ledgerd serves two kinds of clients: the mobile app (~40k daily users) and 6 partner integrations. Partners are the noisy neighbors. Last month one partner hit us at about 2k requests per second and the mobile app got slow. The limiter exists so one partner's traffic can't degrade everyone else.

## The three decisions

**1. Counters live in Redis, not in each process (2026-09-10)**
We run three replicas behind a load balancer. An in-process counter would give each replica its own count, so a partner could get roughly 3x the intended limit just by spreading across replicas. Redis gives all three a single shared count, and we already run it for caching.
- Rejected: sticky sessions (pinning a client to one replica so a local counter works). Partners don't send cookies, so there's nothing to pin on.

**2. Over-limit requests get `429 Too Many Requests` with a `Retry-After` header (2026-09-12)**
The mobile client already backs off when it gets a 429, so we get correct client behavior for free.
- Rejected: `503`. The notes give the mobile client's existing 429 handling as the reason for choosing 429 over it.
- Rejected: quietly queueing excess requests. That hides the problem from partners. We want them to see they're over the limit and fix it on their side.

**3. Limits are per API key, not per IP (2026-09-12)**
Several partners share egress IPs. Keying by IP would throttle unrelated partners together, so one noisy partner could get its neighbors blocked. The API key identifies who is actually calling.

## What's still open

- **Per-partner quotas.** Not decided. For now every partner gets the same single limit. That follows a standing preference from the project owner: "pick a default and we'll revisit" rather than adding a config knob for everything.
- **A separate, higher limit for the mobile app.** Also undecided.

## Things that will trip you up

- **`docs/design.md` is out of date on this.** Its "Rate limiting" section says the approach "has not yet been decided" and proposes a per-IP counter in process memory. That conflicts with decisions 1 and 3 above. Go by `NOTES.md`. The design doc needs updating.
- **The algorithm isn't decided.** `NOTES.md` doesn't say whether we use token bucket, sliding window, or something else, and it doesn't give the limit number. There's an unsent `draft_reply.md` that recommends token bucket, but it's a draft, not a recorded decision.
- **Don't confuse the limiter with the 30s cache TTL.** The critical invariant in `NOTES.md` is that we never return a balance older than 30 seconds. That's about caching, not rate limiting. They share Redis, but if you're tempted to make throttled clients happy by serving them staler cached data, don't.

I couldn't find the limiter code in this checkout (`src/api/` isn't present), so everything above comes from the notes, not from reading the implementation.
