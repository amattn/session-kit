Done. `WebhookClient.send` now retries on 5xx and on transport errors (timeouts, connection reset), and fails fast on any 4xx. Return type is unchanged (`bool`).

**What changed**

`src/webhook_client.py`
- Up to 3 attempts. Backoff is 200ms base, doubling, capped at 2s, with full jitter (`random.uniform(0, cap)`) so the three replicas don't retry a flapping partner in lockstep.
- Retried: 5xx, `httpx.TransportError`. Retrying is safe here because delivery is already at-least-once and partners dedupe on `event_id`.
- Fail fast: any 4xx, including 429. A partner rejected the request; resending the same bytes won't change that.
- The policy is three module-level constants rather than constructor arguments, per your "pick a default and we'll revisit" note.

`NOTES.md`
- Added the decision under Key Design Decisions so the policy and its rationale are on record.

**Verified**
There's no httpx or test suite in this tree, so I ran the client against a stubbed `httpx` (in my scratchpad, not committed) with `time.sleep` patched out: 2xx first try, 4xx/404/429 fail fast after 1 call, 5xx then 2xx succeeds on attempt 2, three 5xx exhausts after exactly 3 calls, transport errors behave the same, 5xx followed by 4xx stops at 2, and every sleep stayed within its attempt's cap. All 10 cases pass.

**Two things to be aware of**
- `changes.md` in the repo describes a `DeliveryResult` return type and call sites in `src/api/` that don't exist in this tree. I left `send()` returning `bool`; if you want attempt counts surfaced to callers, that's a separate change.
- 429 fails fast because you said "fail fast on 4xx", but it's the one 4xx that arguably deserves a retry (with `Retry-After`). Flagged in NOTES.md as a rejected option; easy to revisit.

**Commit message**

```
Retry webhook delivery on 5xx with exponential backoff

WebhookClient.send now makes up to 3 attempts on 5xx responses and
transport errors (timeouts, connection reset), backing off 200ms base,
doubling, capped at 2s, with full jitter so replicas don't retry a
flapping partner in lockstep. Any 4xx fails immediately, including 429.

Retrying is safe because delivery is at-least-once and partners dedupe
on event_id. Policy is fixed constants rather than constructor options,
per the "pick a default and we'll revisit" guidance in NOTES.md.

Return type is unchanged (bool). Decision recorded in NOTES.md.
```
