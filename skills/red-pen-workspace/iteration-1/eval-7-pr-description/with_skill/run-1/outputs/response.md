```
Add retry to webhook client: exponential backoff on 5xx

One decision needs review: `send()` now returns a `DeliveryResult` instead of `bool`. The rest is the retry policy plus formatter-driven renames.

Retry:
- 3 attempts, 200ms base, jitter; 5xx only
- 4xx fails fast — retrying a bad payload never helps
- Safe to retry: delivery is already at-least-once and partners dedupe on `event_id`
- A partner stuck on 5xx now holds `send()` for 3 round trips plus ~1.4s of backoff; a problem only if the caller is on a request path

Return type (not in the ask):
- `bool` → `DeliveryResult(status, attempts, last_error)` so the caller can log attempt counts
- 1 call site, `api/webhooks.py`, now reads `.ok`
- Revert to `bool` if attempt counts don't need logging; the retry doesn't depend on it

Mechanical, skip on review:
- `_fmt` → `_format_amount` in `api/transactions.py`, `api/balances.py`
- import order in `api/__init__.py`
```

I'd move the two renames and the import fix to their own PR: they're 3 files of noise next to a 1-file behavior change, and the formatter will keep flagging them either way.
