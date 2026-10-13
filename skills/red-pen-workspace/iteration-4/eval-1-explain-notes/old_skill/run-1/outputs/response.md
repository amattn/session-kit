Rate limiting exists to keep partner integrations from starving the mobile app: last month one partner hit us at 2k requests per second and the app slowed down. Three decisions are settled (NOTES.md, 2026-09-10 to 09-12):

- **State lives in Redis.** We run three replicas behind a load balancer, so the count has to be shared; a per-process counter would let each replica count separately. Sticky sessions (pinning a client to one replica) were rejected because partners don't send cookies.
- **Keyed per API key, not per IP.** Partners share egress IPs, so an IP-keyed limit would throttle different partners together.
- **Over-limit requests get 429 with `Retry-After`** (a header telling the client how long to wait). The mobile client already backs off on 429, which is why it beat 503. Silently queueing excess requests was rejected because it hides the problem from the partner causing it.

Still open: per-partner quotas (today every partner gets the same limit) and whether the mobile app gets its own, higher limit. The project owner prefers one default over a config knob per case, revisited later.

One trap: `docs/design.md` (transaction export) still says rate limiting is undecided and proposes a per-IP counter in process memory. That contradicts the first two decisions; NOTES.md is the current record.

NOTES.md doesn't record the limit value or the algorithm; ask the team for those.
