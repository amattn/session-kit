The plan is in `docs/rate_limiting.md`. It follows the decisions already in `NOTES.md` (per API key, Redis, 429 with `Retry-After`, fixed defaults) and needs your sign-off on three things before enforcement starts.

- **Mobile app:** I recommend limiting partner keys only at first. That fixes the noisy-neighbor problem, and it avoids throttling all mobile users as one client if they share a key. I couldn't check how mobile requests are identified because `src/api/` isn't in this checkout.
- **Per-partner quotas:** I recommend one limit for all six partners, as in the current default.
- **The limit:** I proposed 50 requests per second per key with bursts to 100. This is a placeholder, not a measured number, because I have no data on normal partner traffic. The plan includes a week of observe-only running to confirm it before anything is blocked.

Two choices in the plan are mine and not from the notes: a token bucket algorithm, and allowing requests through if Redis is down so a Redis problem doesn't become an API outage.

`docs/design.md` (transaction export) still says rate limiting is undecided and proposes a per-IP in-process counter, which contradicts the recorded decisions. I flagged this in the plan and left that file alone.
