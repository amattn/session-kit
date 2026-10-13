Wrote `grid_section.md`. Every subsection anchor (§6.1–6.5), the grid table, every list, and the §7.5 and §10.3 references are kept. Exceptions: the three `####` subheads in §6.3 became bold-led paragraphs, and "don't ship 45 as a standalone rhythm" moved from §6.3 into §6.2, where the rule belongs. Two findings for you:

- **§6.5 contradicts §6.2.** It calls duration-as-grid possible work toward the adaptive grid, but what it does (put the day on a 45-minute rhythm) is the model §6.2 says not to ship. I kept the claim; it needs an owner's answer.
- **Slot score bands are lopsided.** With an 8am–6pm day, Fair covers 8am–4pm, so only 4–6pm is ever Weak and early-morning slots outrank late-afternoon ones. Confirm that's intended.

Here is one block before and after, as an example of the change:

> #### "Slot score" scores closeness to noon — and that was a deliberate replacement
>
> Coordinators already have a strong/fair/weak guide on every slot, named **"Slot score"**, driving which three options surface by default. What it scores is **distance from noon**: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond.
>
> Despite the name, it carries no information about whether a slot leaves an unfillable gap. **That is not an oversight.** An edge-based algorithm — rank a placement by how many new gaps it creates, so an exact fill is best and a middle-of-the-gap placement is worst — was tried and **deprecated in favour of closeness to noon, because advisors rejected having their days filled from the outside in.**
>
> The reason it behaves that way is structural. Edge scoring rewards placements that sit flush against something solid, and **on a mostly-empty day the only solid edges are the start and end of the working block.** So the first bookings of any day get pushed to 8:00am and the last slot before 6:00pm, and the day fills inward from the extremes. That is close to the worst possible outcome for an advisor, and it happens precisely when a day is quietest.
>
> Closeness to noon inverts it: days fill from the centre outward, keeping a compact mid-day block instead of scattered bookings at the edges. For the common case — a day with plenty of room — it is simply the better rule, and it is the one in production.

> **Closeness to noon is deliberate.** Edge-based ranking (score a placement by how many new gaps it creates) was tried and deprecated because advisors rejected days filled from the outside in: on a mostly empty day the only edges are the start and end of the working block, so first bookings went to 8:00am and the last slot before 6:00pm. Closeness to noon fills days from the centre outward and is in production.

(The scoring bands moved up into the "Slot score" bullet, which already described the badge.)

| Symptom | Before | After |
|---|---|---|
| Slot score explained | twice (bullet + subsection) | once |
| "That is / This is" openers | 9 | 0 |
| "See below" / cross-section restatement | 3 + §6.4's recap of §6.2 | 0 |
| Words | 1,839 | 1,092 |
