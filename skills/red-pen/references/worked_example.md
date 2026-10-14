# Worked example: one editing pass

An illustration: one block from an operations note written the way unedited AI output reads, the facts it carries, the edit, and the report the reader gets. The reader is the engineer who owns the backup job.

## Before: a header and four paragraphs

> #### Nightly backups are kept for 14 days — and that number was chosen on purpose
>
> Every night at 02:00 UTC, the backup job writes a full database snapshot to the archive bucket. Snapshots are kept for **14 days**, after which the bucket's lifecycle rule deletes them.
>
> It is worth noting that 14 days is not arbitrary. **That is a deliberate choice.** The original window was 7 days, and it was raised to 14 after a bad migration went unnoticed for nine days.
>
> The reason 7 days fails is simple. A data-corrupting change can sit unnoticed for more than a week, especially over a holiday, and by the time someone notices, the last clean snapshot has already been deleted. That is the worst possible moment to discover that the retention window is too short.
>
> Fourteen days covers that case: it is long enough to span two release cycles, and the extra week of storage costs about $40 a month. It is simply the safer value, and it is the one in production.

## The facts, listed before cutting

Nightly at 02:00 UTC · full database snapshot · archive bucket · kept 14 days · the lifecycle rule deletes them · the window used to be 7 days · raised after a bad migration went unnoticed for nine days · by then the last clean snapshot was gone · 14 days spans two release cycles · the extra week costs about $40 a month · 14 days is what runs in production.

Every one survives below; the last survives as the present tense. One claim is cut on purpose: "especially over a holiday" has no source.

## After: one paragraph, no header

> **Backups are kept for 14 days on purpose.** Every night at 02:00 UTC, the backup job writes a full database snapshot to the archive bucket. The bucket's lifecycle rule deletes each snapshot after 14 days. The window was 7 days until a bad migration went unnoticed for nine days, by which time the last clean snapshot had been deleted. Fourteen days spans two release cycles, and the extra week of storage costs about $40 a month.

## The report the reader gets

The edit goes to the file. The chat reply is this and nothing more:

> Wrote `backups.md`. Every number and rule is preserved. One claim was cut as unsourced: "especially over a holiday".
>
> Here is the paragraph before and after, as an example of the change:
>
> *(the pair above)*
>
> | Symptom | Before | After |
> |---|---|---|
> | "14 days was deliberate" stated | 3 times | once |
> | "This is / That is / Note that" openers (script count) | 3 | 0 |
> | Prose sentences over 25 words | 2 | 0 |
> | Passive voice (estimate) | 5 | 2 |

## What this teaches

- The fact list comes first. The cut is checked against it, not against a feeling that nothing important went.
- What went: the second and third telling of "deliberate", the "not arbitrary" reassurance, the header, and a claim with nothing behind it.
- Nothing was added. The report names the one cut that a reader might question, so the reader can overrule it.
- The report leads with what was found, shows one pair with a sentence saying what it is, and keeps the table short. The counts come from `scripts/symptoms.py --compare`, except the restatement row, which the script cannot see.
- The same rules over-cut on mature, human-edited specs. There, a table's row-by-row teaching bullets and a one-fact sub-bullet should both stay. Enumeration is not duplication; structure that isolates one fact per line is not scaffolding.
