Here is the PR description. I wrote it from `changes.md` alone: the project copy I have does not contain the branch's changes (`src/webhook_client.py` is still the pre-retry version, and `src/api/` and `tests/` are absent), so nothing below is checked against the diff.

```markdown
# Retry webhook delivery on 5xx

## What this does

`WebhookClient.send()` now retries when a partner endpoint returns a 5xx: up to 3 attempts, exponential backoff from a 200ms base, with jitter. A 4xx fails immediately with no retry.

Retrying is safe because delivery is already at-least-once and partners dedupe on `event_id`.

## Change to the `send()` return type

`send()` used to return a `bool`. It now returns a `DeliveryResult` dataclass with `status`, `attempts` and `last_error`, and the caller reads `.ok`.

This was not part of the original ask ("add retry to the webhook client"). It was needed so the caller can log how many attempts a delivery took.

The one existing call site, in `src/api/webhooks.py`, is updated. Any code that still writes `if client.send(...)` will not fail loudly: a dataclass instance is truthy unless it defines `__bool__`, so a failed delivery would read as a success. Please check for callers outside this repo.

## Unrelated changes in this branch

These came from the formatter, not from the retry work:

- `src/api/transactions.py` and `src/api/balances.py`: `_fmt` renamed to `_format_amount`. Mechanical, with no behavior change.
- `src/api/__init__.py`: import order.

I can move these to a separate PR if you would rather keep this one to the retry change.

## Files

| File | Change |
|---|---|
| `src/webhook_client.py` | Retry with backoff; `DeliveryResult` return type |
| `src/api/webhooks.py` | Call site reads `.ok` |
| `src/api/transactions.py` | `_fmt` renamed to `_format_amount` |
| `src/api/balances.py` | `_fmt` renamed to `_format_amount` |
| `src/api/__init__.py` | Import order |
| `tests/test_webhook_client.py` | 4 new tests for retry behavior |

## Testing

4 new tests in `tests/test_webhook_client.py` cover the retry behavior.
```

Three things to settle before you post it:

- **Test status**: `changes.md` says the tests were added but not whether the suite passes, so the Testing section makes no claim about that. Add the result once you have run it.
- **Timeouts and connection errors**: `changes.md` only mentions 5xx. If a timeout or a refused connection is also retried (or deliberately is not), reviewers will want that stated.
- **Truthiness of `DeliveryResult`**: if the dataclass defines `__bool__`, the warning about `if client.send(...)` is wrong and should come out.
