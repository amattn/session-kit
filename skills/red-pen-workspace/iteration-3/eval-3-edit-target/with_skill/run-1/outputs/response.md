Wrote `grid_section.md`. Every rule, section number (§6.1–6.5), table, and list is preserved; the three H4s under §6.3 became bold leads. One contradiction found: §6.1 says the grid is set per meeting type, not by the booker, while §6.5 says the duration picker currently overrides it. I added a one-line pointer in §6.1 and changed nothing else of substance. Also unresolved: §6.4's "grid follows the meeting" would put the 15-minute office drop-in back on a 15-minute grid, undoing §6.1's deliberate choice.

Before (§6.3, "Where edge-awareness still has a claim", three paragraphs under their own header):

> Edge scoring isn't wrong, it's **wrong for sparse days**. Its logic only becomes meaningful once a day is full enough that gaps exist *between real appointments* rather than between an appointment and the edge of the working block. On a fragmented day, the middle-of-the-gap placement genuinely is the bad one — it turns a usable 90-minute opening into two fragments.
>
> So the likely shape of a future answer is **dynamic rather than either/or**: rank by closeness to noon by default, and shift toward edge-awareness when a day is fragmented enough that gaps, not time of day, are the binding constraint. What would need defining is the trigger — how many gaps, or how much fragmented time, flips the behaviour — and whether it's a hard switch or a weighting that slides.
>
> **This is explicitly not a priority.** The current behaviour is working and advisors prefer it. It's recorded here because the deprecated code is still in the availability engine, and because the 45-minute placement work in §6.2 touches the same machinery — anyone picking that up should know the edge-based approach was evaluated and rejected on purpose, not left unfinished.

After (one paragraph, no header):

> Edge scoring is wrong for sparse days, not for fragmented ones, where a middle-of-the-gap placement turns a usable 90-minute opening into two fragments. A dynamic rule — closeness to noon by default, shifting toward edge-awareness once gaps rather than time of day are the binding constraint — is a parked idea, **explicitly not a priority**. It would need a defined trigger (how many gaps, or how much fragmented time) and a choice between a hard switch and a sliding weighting.

| Symptom | Before | After |
|---|---|---|
| "Edge ranking was replaced on purpose" stated (my count) | 10 | 3 |
| Words on the topic marked "explicitly not a priority" | 197 | 80 |
| Sentences opening "This is / That is / That's" | 9 | 0 |
| Headers | 9 | 6 |
