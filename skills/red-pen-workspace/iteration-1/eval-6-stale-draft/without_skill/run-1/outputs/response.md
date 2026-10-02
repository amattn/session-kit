**Red pen: `docs/design.md`**

The big problem is that this draft is stale against `NOTES.md`. Two sections say decisions are "still open" that were actually settled in mid-September, and the rate-limiting proposal directly contradicts three of them.

**Blocking (contradicts recorded decisions)**

1. **Line 17, "The rate limiting approach for ledgerd has not yet been decided"** — it has. NOTES.md records three decisions dated 2026-09-10 and 2026-09-12:
   - State lives in **Redis** (shared across the three replicas; in-process counters were explicitly rejected because the limit must be shared).
   - Keyed **per API key, not per IP** (partners share egress IPs; per-IP throttles them together).
   - Rejections are **429 + `Retry-After`**.

   The draft's proposed "simple per-IP counter in process memory" is the exact design that was rejected, on both axes. Each replica would keep its own count (so the effective limit is 3x), and partners behind a shared NAT would throttle each other. Replace the section with: export requests use the existing Redis-backed, per-API-key limiter and return 429 + `Retry-After`. The only genuinely open question for exports is whether they get a separate (lower) bucket from normal API calls, since one export is far more expensive than one `/transactions` page — that's worth stating as the open question instead.

2. **Line 13, "The database choice for ledgerd itself is also still open"** — it isn't. CLAUDE.md and NOTES.md both state Postgres for storage, Redis for caching, three replicas. Delete the sentence; it makes the doc look older than the project.

3. **Line 13, storage for export files** — the draft lists three options and picks none. Your own stated preference in NOTES.md is "pick a default and we'll revisit." The doc already gives the deciding fact: local filesystem "does not work across replicas," and the download URL has to be servable by whichever replica the partner hits. That rules out local disk. Pick one of the remaining two (S3 is the conventional answer for 24-hour-expiring download URLs — presigned URLs do the expiry for free; Postgres large objects would put bulk CSV traffic on the primary) and move the other to "Alternatives considered." As written, "Decide on storage" in Next steps is the doc deferring its own job.

**Should be in the doc and isn't**

4. **Webhook delivery semantics.** `src/webhook_client.py` says delivery is at-least-once and partners dedupe on `event_id`. The export-complete webhook (line 21) needs an `event_id`, and the doc should say what happens if the partner never acks (does the export file still exist for 24h regardless? can they re-request the URL?). Also note `changes.md` describes retry-with-backoff landing on the `webhook-retry` branch; the export design should rely on that rather than describe its own retry.

5. **Noisy-neighbor protection.** NOTES.md: "one of them hammered us at 2k rps last month and the mobile app got slow." A bulk export is the single most expensive thing a partner can trigger. The doc says "background job" but not where it runs or how many can run concurrently. If export jobs read from the same Postgres the mobile app's balance path uses, a few concurrent large exports can recreate the incident. State a concurrency cap (one in-flight export per partner is a sane default) and whether the job reads from a replica.

6. **Scope of an export.** Nothing says what a partner can ask for: all history? a date range? one account or all accounts under their key? This determines job size, file size, and whether pagination inside the CSV is needed. One sentence fixes it.

**Padding to cut**

- Line 5: "In this document we will cover the motivation, the proposed approach, alternatives considered, and next steps." — table-of-contents-as-prose; the headings already do this. Also "alternatives considered" doesn't exist as a section.
- Line 9: "This has been a pain point for some time, and addressing it is important for partner satisfaction." — says nothing the first sentence didn't.
- Line 13: "Each option has trade-offs." — delete.
- Line 21: "This is a reasonable default." — either justify 24h in half a sentence (e.g., long enough to survive a partner's overnight batch window) or just state it.
- Next steps, lines 25-26: "Decide on storage / Decide on rate limiting" — these go away once items 1 and 3 are fixed; a design doc's next steps should be implementation steps, not the decisions the doc was supposed to make.

**Minor**

- Line 9 says `/transactions` paging "is slow for large accounts." Slow for whom — the partner's wall clock, or our DB? If the latter, that's a second argument for the export running off a replica (item 5).
- Title says "Transaction Export" but the doc never says the format beyond "a CSV." Column set, timezone of timestamps, and amount formatting (NOTES/changes.md mention `_format_amount`) will be the first partner question.

**Net:** the Approach section is fine as a skeleton. Fix items 1-3 and the doc goes from "list of open questions" to an actual design. I haven't edited the file — say the word and I'll apply the rewrite (rate-limiting section pulled from NOTES.md, storage defaulted to S3 with Postgres LO under alternatives, filler removed).
