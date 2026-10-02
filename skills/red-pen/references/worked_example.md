# Worked example: one editing pass

An illustration: one block from a design note written the way unedited AI output reads, the edit, and the report the reader gets. The reader is the engineer who owns the service.

## Before: a header and four paragraphs

> #### The cache TTL is 30 seconds — and that was a deliberate choice
>
> Every balance read goes through a cache with a **30-second TTL**. What it bounds is **staleness**: a balance shown to a customer is never more than 30 seconds old.
>
> Despite how short that looks, it is not a placeholder. **That is not an oversight.** A five-minute TTL — the usual default for read-heavy endpoints — was tried and **rejected in favour of 30 seconds, because support kept seeing stale balances after transfers.**
>
> The reason it fails is structural. A transfer changes two balances, and **with a five-minute TTL the sender sees the money gone while the receiver still sees the old balance.** So the receiver refreshes, sees nothing, and opens a ticket. That is close to the worst possible outcome for a payments screen, and it happens precisely when a customer is paying closest attention.
>
> Thirty seconds fixes it: both sides converge inside the time it takes to switch apps. For the common case — a customer checking after a transfer — it is simply the better value, and it is the one in production.

## After: one paragraph, no header

> **The 30-second TTL is deliberate.** Five minutes was tried and withdrawn because support saw stale balances after transfers: the sender saw the money gone while the receiver still saw the old balance, and opened a ticket. Thirty seconds lets both sides converge in the time it takes to switch apps. Raising it is a parked idea, tracked in the open items.

## The report the reader gets

The edit goes to the file. The chat reply is this and nothing more:

> Wrote `design.md`. Every rule and anchor is preserved. One stale claim found: the note says the TTL is "under review", and the decision log settled it in March.
>
> Here is one paragraph before and after, as an example of the change:
>
> *(the pair above)*
>
> | Symptom | Before | After |
> |---|---|---|
> | "The TTL was a deliberate choice" stated | 4 times | once |
> | Sentences opening "That is / It is" | 3 | 0 |
> | The mechanism explained | twice | once |

## What this teaches

- Nothing the reader needs is gone: the rule, the reason in one sentence, the mechanism once, and a pointer to where the parked idea lives.
- What went: the second and third telling, the "not an oversight" reassurance, and the mechanism explained twice.
- The report leads with what was found, shows one pair with a sentence saying what it is, and keeps the table short. Readers skim tables and judge from the pair.
- The same rules over-cut on mature, human-edited specs. There, a table's row-by-row teaching bullets and a one-fact sub-bullet should both stay. Enumeration is not duplication; structure that isolates one fact per line is not scaffolding.
