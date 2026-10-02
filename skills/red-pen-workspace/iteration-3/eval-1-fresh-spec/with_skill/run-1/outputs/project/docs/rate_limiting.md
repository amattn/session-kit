# Rate Limiting Plan

Over the 300-word budget: three decisions are still open.

This plan is for product, who own the limits and what partners experience, and for the engineers who will build it. Product can stop after "Open items"; the rest is implementation. Already settled in `NOTES.md` and not reargued here: partners over the limit get a 429 with `Retry-After` (seconds to wait), limits are per API key, and the counters live in Redis.

## Open items

All three are product's.

1. **The partner limit.** Lean: 100 requests/second per API key, bursts to 200. This is a guess: the only traffic figure on record is the 2k rps incident. The log-only phase replaces it with a measured number before anyone is throttled.
2. **Is the mobile app limited?** Lean: no, exempt it in v1. The problem on record is partners, and one shared mobile limit would throttle all ~40k daily users at once.
3. **One limit for all 6 partners, or per-partner quotas?** Lean: one limit; revisit when a partner has a legitimate need above it.

## Decisions

- Chose a token bucket (a burst allowance that refills at a fixed rate) over a sliding-window counter because partner traffic is bursty and short bursts are harmless; revisit if bursts alone slow the mobile app.
- Chose log-only for a period, then enforcement, over enforcing on day one, because the limit in item 1 is unmeasured.
- Chose to let requests through when Redis is unreachable over rejecting them, because a limiter outage should not become an API outage; revisit if an outage coincides with abuse.
- Chose hardcoded limits over configuration, per "pick a default and we'll revisit"; revisit if item 3 goes per-partner.

## Assumptions

- [ ] Every partner request carries an API key.
- [ ] Mobile traffic can be told apart from partner traffic. Item 2 depends on it.
- [ ] Product tells partners before enforcement starts.
- [ ] Partner clients honor `Retry-After`. The mobile client already backs off on 429.

## Risks

- A partner integration breaks if its normal peak is above the limit and log-only was too short to see it.
- Every request slows down if Redis is slow: the limiter adds one round trip per request.
- Nothing is limited while Redis is down.

## Scope out

- Per-endpoint limits.
- Partner-facing quota headers or a usage dashboard.
- Fixing `docs/design.md`, whose "Rate limiting" section proposes a per-IP in-process counter and contradicts `NOTES.md`.
