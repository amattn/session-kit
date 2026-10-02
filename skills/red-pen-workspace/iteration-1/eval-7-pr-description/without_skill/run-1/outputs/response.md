Here's the PR description. One caveat up front: the working tree I have only contains the pre-change `src/webhook_client.py` — `src/api/*` and `tests/test_webhook_client.py` aren't present — so this is written from `changes.md`, the existing client, and NOTES.md. Two details below are marked as things to confirm against the actual diff before you post.

---

# Webhook client: retry 5xx with exponential backoff

## What

`WebhookClient.send()` now retries partner deliveries that fail with a 5xx response: up to 3 attempts, 200ms base delay, exponential backoff with jitter. 4xx responses fail immediately with no retry.

`send()` now returns a `DeliveryResult` dataclass (`status`, `attempts`, `last_error`) instead of a `bool`. The one caller (`src/api/webhooks.py`) reads `.ok` from the result.

## Why

Partner endpoints occasionally return transient 5xx errors, and a single failed POST meant the event was lost until something else re-delivered it. Delivery is already documented as at-least-once with partners deduping on `event_id`, so retrying is safe from a duplication standpoint.

The return-type change was not in the original ask ("add retry to the webhook client"). It's here because a bare `bool` can't tell the caller how many attempts a delivery took or what the final error was, and we want that in the logs to see how often partners are flaking. It's a small, contained API change with exactly one call site.

## Changes

- `src/webhook_client.py` — retry loop with backoff; `DeliveryResult` dataclass; `send()` return type changed
- `src/api/webhooks.py` — call site updated to use `result.ok`
- `tests/test_webhook_client.py` — 4 new tests covering retry behavior (5xx retried, 4xx fails fast, attempt counting, exhaustion)

Incidental, no behavior change:
- `src/api/transactions.py`, `src/api/balances.py` — `_fmt` renamed to `_format_amount` (formatter flagged it)
- `src/api/__init__.py` — import order fixed by the formatter

## Things to check in review

- **Worst-case latency.** The client timeout is 5s per attempt. With 3 attempts plus backoff, a dead partner endpoint can hold `send()` for ~15s. If `src/api/webhooks.py` calls `send()` synchronously inside a request handler, that's a long time to block a request — worth confirming the call is off the request path (or that 15s is acceptable there).
- **What counts as retryable.** Per `changes.md` only 5xx responses are retried. Connection errors and timeouts (`httpx.TransportError`) are the more common transient failure for partner endpoints; confirm whether the diff handles them, and if not, whether that's intentional for this PR.
- **429 from partners.** Not covered by either the 4xx or 5xx rule in a useful way — currently fails fast. Probably fine for now; noting it so it's a decision, not an oversight.

## Not in this PR

- Persistent retry / dead-letter for deliveries that exhaust all attempts. Those still get dropped (with a logged `DeliveryResult`).
- Any change to the retry parameters being configurable. Per NOTES.md, we picked a default and will revisit.

---

If you'd rather keep the renames out of this PR entirely, they're mechanical and could be split into their own commit so the reviewer's diff is just the webhook change.
