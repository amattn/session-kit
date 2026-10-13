Three rate-limiting decisions are settled: the count lives in Redis, it is kept per API key, and over-limit requests get a 429 with a `Retry-After` header. The limiter exists to protect the mobile app (~40k daily users) from partner traffic. Last month one partner hit ledgerd at 2k requests per second, and the app slowed down for everyone.

- **Count in Redis (2026-09-10).** ledgerd runs three replicas behind a load balancer. A counter inside each process would give each replica its own count, so no one would enforce the real limit. Redis holds one shared count. Sticky sessions (pinning a client to one replica) were rejected because partners don't send cookies.
- **Per API key, not per IP (2026-09-12).** Partners share egress IPs, so an IP-based limit would throttle different partners together.
- **429 + `Retry-After` (2026-09-12).** `Retry-After` tells the client how many seconds to wait. 503 was rejected because the mobile client already backs off on 429. Silently queueing excess requests was rejected because it hides the problem from partners.

Still open, per NOTES.md:

- **Per-partner quotas.** Not decided. For now, all partners share one limit.
- **A separate mobile limit.** Whether the mobile app gets its own, higher limit.
- **The algorithm and the numbers.** NOTES.md records neither. `draft_reply.md` leans toward a token bucket (a burst allowance that refills at a fixed rate), but that is a draft, not a decision.

The owner's standing preference: pick a default rather than add a config knob, and revisit later.

One trap: `docs/design.md` § Rate limiting is stale. It calls the approach undecided and proposes a per-IP, in-process counter, which contradicts two of the three decisions. Trust NOTES.md over it. I can update that section to match if you want.
