Here's a PR description for `webhook-retry`. Two things I'd flag before you paste it: the return-type change is the part reviewers need to look at, so I led with it rather than burying it under "retry"; and the `_fmt` renames plus the import-order fix are unrelated to the feature, so I listed them in their own section (you may prefer to split them into a separate PR, which would make this one a two-file diff).

---

## Webhook client: retry on 5xx with exponential backoff

### What

`WebhookClient.send()` now retries partner deliveries that fail with a 5xx response: up to 3 attempts, exponential backoff from a 200ms base, with jitter. 4xx responses fail fast with no retry, since re-sending the same payload won't fix a client-side rejection.

`send()` also changes its return type from `bool` to a `DeliveryResult` dataclass (`status`, `attempts`, `last_error`). The original ask was just "add retry," but once there are multiple attempts the caller needs to know how many it took and why the last one failed, and a `bool` can't carry that. The single call site in `src/api/webhooks.py` is updated to read `.ok` from the result.

### Why

Partner endpoints are flaky in the way any third-party HTTPS endpoint is; a transient 5xx currently drops the delivery outright. Retrying is safe here because delivery is already at-least-once and partners dedupe on `event_id` (see the comment at the top of `webhook_client.py`), so a duplicate delivery from a retry after an ambiguous failure is handled on their side.

### Review notes

- **The `send()` signature change is the one behavioural change outside the client.** It has exactly one caller today; if anything else lands on main that calls `send()` and tests the result for truthiness, it'll need the same `.ok` change.
- **Worst-case latency.** With the client's 5s timeout, three attempts plus backoff is roughly 15–16s of blocking in the worst case. Worth confirming that's acceptable wherever `send()` runs (if it's on a request path rather than a background task, that changes the answer).
- Retry parameters are fixed constants, not config, per the "pick a default and we'll revisit" guidance in NOTES.md.

### Unrelated changes in this diff

Mechanical, no behaviour change, included because the formatter flagged them:

- `src/api/transactions.py`, `src/api/balances.py`: `_fmt` renamed to `_format_amount`.
- `src/api/__init__.py`: import order.

### Tests

`tests/test_webhook_client.py` adds 4 tests covering retry behaviour: success after transient 5xx, exhaustion after 3 attempts, fail-fast on 4xx, and the populated `DeliveryResult` fields.

---

One caveat: I wrote this from `changes.md` and the pre-change `webhook_client.py`; the branch's `src/api/` and `tests/` files aren't in this working tree, so double-check the test list in the last section against what's actually in the file (I inferred the four cases from the description of the feature) and the exact backoff formula if you want it in the description.
