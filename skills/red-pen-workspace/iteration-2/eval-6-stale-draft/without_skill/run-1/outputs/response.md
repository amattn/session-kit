**Red-pen review of `docs/design.md`**

The big problem is that this draft is stale. It says three things are undecided that the project has already decided, and it proposes a rate limiter that contradicts all three recorded rate-limiting decisions in `NOTES.md`. Below, by section, with line numbers.

**Stale / contradicts the record (fix these first)**

- **L13, Storage — "The database choice for ledgerd itself is also still open; this design assumes Postgres but should be revisited if that changes."** Not open. `CLAUDE.md` states Postgres for storage, Redis for caching. Delete the sentence.
- **L13, Storage — local filesystem listed as a live option.** The doc itself says it "does not work across replicas," and the project runs three replicas (`CLAUDE.md`, `NOTES.md`). That rules it out; say so and drop it from consideration instead of leaving it as one of three "trade-offs."
- **L17, Rate limiting — "The rate limiting approach for ledgerd has not yet been decided."** It has, and the proposal here is wrong on every axis of what was decided:
  - *"in process memory"* — `NOTES.md` 2026-09-10: limiter state lives in Redis, specifically because an in-process counter can't be shared across three replicas.
  - *"per-IP"* — `NOTES.md` 2026-09-12: keyed per API key, not per IP, because partners share egress IPs and per-IP would throttle them together.
  - No response behavior specified — `NOTES.md` 2026-09-12: 429 + `Retry-After`.
  
  Replace the paragraph with: export requests use the existing limiter (Redis-backed, keyed per API key, 429 + `Retry-After`), and state whether exports count against the partner's normal quota or get a separate, lower one. That second question is the only genuinely open one, and it matters given the user's "noisy neighbor" concern (one partner at 2k rps slowed the mobile app).
- **L26, Next steps — "Decide on rate limiting."** Moot; remove. L25 "Decide on storage" should be narrowed to "Postgres large objects vs S3."

**Missing from the Approach (L21)**

- The webhook client is documented as at-least-once with partner dedup on `event_id` (`src/webhook_client.py` L3-4). The payload description doesn't mention `event_id`. Either the export-complete event carries one or partners will get duplicate "your export is ready" notifications under the retry work on the `webhook-retry` branch.
- "The URL expires after 24 hours" presupposes a signed/expiring URL, which is an S3-shaped feature. If that's the intent, it's effectively a storage decision; say so rather than leaving storage open on L13 and assuming it on L21.
- No failure path: what the partner sees if the job fails, and whether a failed export is retried or must be re-requested.
- No scope: columns in the CSV, date-range or account filters, max rows, and whether a partner can have more than one export in flight. The last one is a rate-limiting question in disguise.

**Prose to cut (says nothing)**

- L5: "In this document we will cover the motivation, the proposed approach, alternatives considered, and next steps." Delete; the headings already do this. Also, there is no "alternatives considered" section.
- L9: "This has been a pain point for some time, and addressing it is important for partner satisfaction." Delete. The preceding sentence (paging through `/transactions` is slow for large accounts) is the actual reason.
- L13: "Each option has trade-offs." Delete.
- L17: "as a starting point, which can be revisited later." Delete even after the rewrite; `NOTES.md` records the user's preference to pick a default and revisit, so it doesn't need restating per decision.
- L21: "This is a reasonable default." Delete, or replace with the reason 24h was chosen.

**One structural note**

The doc has a Storage section and a Rate limiting section before it has an Approach section. Reorder to Overview, Background, Approach, then the open decisions, so a reader knows what the export *is* before reading about where its files live.

I haven't changed the file. Want me to apply the stale-decision fixes and the prose cuts, leaving the genuinely open items (Postgres LO vs S3, export quota) as explicit open questions?
