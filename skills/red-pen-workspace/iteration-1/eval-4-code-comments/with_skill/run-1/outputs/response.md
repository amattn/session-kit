Done. One file touched, `src/webhook_client.py`; `send()` still returns bool, and no constructor knobs (NOTES.md: pick a default).

One question: timeouts and refused connections still raise rather than retry, since the ask named 5xx. For webhooks they are the more common failure, and I'd retry them too. Want that?

Chose:
- 200ms base, doubling, plus up to 200ms jitter, so the three replicas don't retry a partner in lockstep
- Worst case per `send()` goes from 5s to ~16s (3 slow 5xx at the 5s timeout + ~1s sleep); anything calling it on the request path blocks that long

Checked with a stubbed httpx: 200 → 1 call; 503,503,200 → True in 3; 503×3 → False; 503,400 → False in 2. No tests added; the repo has none and no test deps.

Commit message:

```
Add retry to webhook client: exponential backoff on 5xx

Mechanics:
- 3 attempts, 200ms base, doubling, up to 200ms jitter
- 4xx fails fast — payload or partner config won't change on retry
- Transport errors still raise, not retried

Design:
- No constructor knobs; defaults per NOTES.md "pick a default and we'll revisit"
```
