Wrote `grid_section.md`. Every rule, anchor, table, list, number, and cross-reference (§7.5, §10.3) is preserved. It is still over the 300-word spec budget: this is one section of a larger BRD, and cutting further would drop rules. One contradiction for you to settle: §6.5 suggests the duration-sets-grid behaviour may be a step toward §6.4's adaptive grid, but neither §6.4 shape produces a 45-minute rhythm, and §6.2–6.3 say 45 as a standalone rhythm should not ship. The observed behaviour is the model the section rejects.

Here is one block before and after, as an example of the change:

**Before** (§6.3, "Slot score" subsection):

> Coordinators already have a strong/fair/weak guide on every slot, named **"Slot score"**, driving which three options surface by default. What it scores is **distance from noon**: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond.
>
> Despite the name, it carries no information about whether a slot leaves an unfillable gap. **That is not an oversight.** An edge-based algorithm — rank a placement by how many new gaps it creates, so an exact fill is best and a middle-of-the-gap placement is worst — was tried and **deprecated in favour of closeness to noon, because advisors rejected having their days filled from the outside in.**
>
> The reason it behaves that way is structural. Edge scoring rewards placements that sit flush against something solid, and **on a mostly-empty day the only solid edges are the start and end of the working block.** So the first bookings of any day get pushed to 8:00am and the last slot before 6:00pm, and the day fills inward from the extremes. That is close to the worst possible outcome for an advisor, and it happens precisely when a day is quietest.
>
> Closeness to noon inverts it: days fill from the centre outward, keeping a compact mid-day block instead of scattered bookings at the edges. For the common case — a day with plenty of room — it is simply the better rule, and it is the one in production.

**After:**

> Slot score rates distance from noon: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond. Despite the name, it says nothing about whether a slot leaves an unfillable gap.
>
> It replaced an edge-based algorithm, which ranked a placement by how many new gaps it created: an exact fill best, a middle-of-the-gap placement worst. Advisors rejected it because it filled their days from the outside in. On a mostly empty day the only edges are the start and end of the working block, so the first bookings went to 8:00am and the last slot before 6:00pm, on exactly the quietest days. Closeness to noon fills days from the centre outward into a compact mid-day block. It is the rule in production.

| Symptom | Before | After |
|---|---|---|
| "Edge scoring was rejected on purpose" stated | 4 times | twice |
| Sentences opening "That is / This is" | 9 | 1 |
| Prose sentences over 25 words | 19 | 5 |
| "See below" pointers | 3 | 0 |
