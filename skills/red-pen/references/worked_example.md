# Worked example: one editing pass

An illustration: one section of a requirements document written the way unedited AI output reads, and one editing pass over it. The reader is product management; the product is an advisory firm's booking tool.

## Symptom counts for the whole section (about 1,800 words to about 1,070)

| Symptom | Before | After |
|---|---|---|
| One fact ("edge ranking was replaced on purpose") stated | 10 | 2 |
| Words on a topic the section itself calls "explicitly not a priority" | 197, under its own header | 2 sentences, pointing at the open-items section where it already lived |
| Sentences opening "This is / That is / That's" | 9 | 0 |
| Headers, three of them full sentences under one H3 | 9 | 6 |

The restatement was the defensive kind: the author was anxious the reader would think deprecated code was unfinished, so it said so ten times. For the reader, once is a fact and ten is noise.

## Before: an H4 and its four paragraphs

> #### "Slot score" scores closeness to noon — and that was a deliberate replacement
>
> Coordinators already have a strong/fair/weak guide on every slot, named **"Slot score"**, driving which three options surface by default. What it scores is **distance from noon**: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond.
>
> Despite the name, it carries no information about whether a slot leaves an unfillable gap. **That is not an oversight.** An edge-based algorithm — rank a placement by how many new gaps it creates, so an exact fill is best and a middle-of-the-gap placement is worst — was tried and **deprecated in favour of closeness to noon, because advisors rejected having their days filled from the outside in.**
>
> The reason it behaves that way is structural. Edge scoring rewards placements that sit flush against something solid, and **on a mostly-empty day the only solid edges are the start and end of the working block.** So the first bookings of any day get pushed to 8:00am and the last slot before 6:00pm, and the day fills inward from the extremes. That is close to the worst possible outcome for an advisor, and it happens precisely when a day is quietest.
>
> Closeness to noon inverts it: days fill from the centre outward, keeping a compact mid-day block instead of scattered bookings at the edges. For the common case — a day with plenty of room — it is simply the better rule, and it is the one in production.

## After: one paragraph, no header

The scoring thresholds moved up into the bullet that introduces the slot score.

> **Closeness to noon replaced edge-based ranking on purpose.** Edge scoring (rank a placement by how few new gaps it creates) was tried and withdrawn because advisors rejected having their days filled from the outside in: on a mostly empty day the only solid edges are the start and end of the working block, so the first bookings landed at 8:00am and 6:00pm and the day filled inward. Closeness to noon fills from the centre outward and is the better rule for the common case. A dynamic rule that shifts toward edge-awareness once a day is fragmented is a parked idea, not a priority (§10.3).

## What this pair teaches

- Nothing the reader needs is gone: the rule, the one-sentence reason, the mechanism once, the status of the parked idea, and a pointer.
- What went: the second and third telling, the "not an oversight" reassurance, the mechanism explained twice, and a 197-word subsection whose content is the last sentence above.
- The same rules over-cut on mature, human-edited specs. On those, the owner rejected two of three cuts: a table's row-by-row teaching bullets collapsed into one sentence, and a one-fact sub-bullet folded into a paragraph. Enumeration is not duplication; structure that isolates one fact per line is not scaffolding.
