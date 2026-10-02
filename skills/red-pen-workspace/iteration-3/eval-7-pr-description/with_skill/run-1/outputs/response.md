````markdown
Add retry to webhook client: exponential backoff on 5xx

Needs your judgment:
- `send()` now returns a `DeliveryResult` (status, attempts, last_error) instead of `bool`. This goes beyond the ask ("add retry to the webhook client"); it is there so the caller can log attempt counts. One call site, `src/api/webhooks.py`, now reads `.ok`. Lean: keep. The alternative is to keep `bool` and log attempts inside the client.
- 429 is treated like any other 4xx: no retry, and the partner's `Retry-After` is ignored. Say so if a rate-limited delivery should be retried.
- The two `_fmt` renames and the import reorder have nothing to do with retry; the formatter flagged them. I can move them to their own PR if you want this one retry-only.

Behavior:
- 5xx: up to 3 attempts, exponential backoff from a 200ms base, with jitter.
- 4xx: fails fast.
- Repeat deliveries are safe: delivery is already at-least-once and partners dedupe on `event_id`.

Risk: `send()` is synchronous, so a partner endpoint returning 5xx now holds the caller through the backoff sleeps (about 0.6s before jitter, if the delay doubles) on top of the request time for each attempt.

Tests: 4 new tests for retry behavior in `tests/test_webhook_client.py`.

Mechanical, skip:
- `src/api/transactions.py`, `src/api/balances.py`: `_fmt` renamed to `_format_amount`.
- `src/api/__init__.py`: import order.
````

I wrote this from `changes.md` alone: `src/webhook_client.py` in this working copy still has the old `bool`-returning `send()`, so nothing above is checked against the code.

Two things to confirm before you post it:
- **Timeouts and connection errors.** `changes.md` only mentions 5xx and 4xx, so the description says nothing about whether a timeout is retried. Add a line either way.
- **The 0.6s figure.** It is my estimate (200ms + 400ms), assuming the delay doubles between attempts. Correct it if the multiplier differs.
