## 6. The grid — how slots are offered

The grid is the most visible piece of booking UX: it's the set of start times a client can actually be offered. It is **not** the same thing as how long the meeting is, and keeping those two ideas apart matters for everything below.

- **Duration** — how long the meeting occupies the advisor. A fact about the work.
- **Grid (interval)** — the clock rhythm start times land on: :00 and :30, or every :15. A presentation and packing decision.

They're independent. A 45-minute meeting on a 30-minute grid consumes two consecutive slots and leaves 15 minutes of stranded time after it. A 15-minute meeting on a 30-minute grid consumes one slot and strands the other 15 minutes.

### 6.1 Today's grid

The grid is a property of the **meeting type**, set by the firm, not chosen by the booker or the advisor.

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The default of 30 minutes is working and isn't the problem. The two cases worth understanding:

- **Office drop-in is a 15-minute meeting on a 30-minute grid** — deliberate, so the front desk gets predictable half-hour arrival waves instead of a trickle every quarter hour. This is the clearest existing proof that grid is a business lever, not a derived value.
- **Workshops and other on-site sessions sit on a 15-minute grid** because meeting-room time is the scarcest resource and packing it tightly matters most.

### 6.2 What's needed: finer placement, not new rhythms

The requirement is usually stated as "support 15- and 45-minute blocks," but those are two very different asks and only one of them is really a grid.

**15 minutes is a genuine grid question.** Four meeting types already use a 15-minute grid, so the concept is supported; extending it to more types is mostly a product decision about density. A 15-minute grid roughly doubles the number of start times a coordinator sees per day, which interacts directly with the "show three slots by default, ranked by closeness to noon" behavior in §7.5. More options is not automatically better — the reason only three are shown today is that a wall of times is harder to book from, not easier.

**45 minutes is not a grid question at all.** Treating 45 as a *step size* — 9:00, 9:45, 10:30, 11:15 — produces a rhythm that repeats only every three hours and doesn't divide office hours evenly. That's the wrong model, and it's the source of most of the apparent difficulty.

Treated instead as a **span placed on the existing 15-minute lattice**, 45 is well-behaved:

- **45 is exactly three 15-minute units**, so a 45-minute meeting starting on any 15-minute boundary also *ends* on one. It never strands a fragment smaller than the lattice.
- **Two 45s tile a 90-minute block exactly.** A 90-minute opening is not an awkward leftover — it's a container for precisely two 45-minute meetings with nothing wasted.

So the capability needed is not "a 45-minute grid." It's the ability to **fit a 45-minute meeting into the space that exists**, in two specific ways:

1. **Fill a dedicated 90-minute gap.** Recognize a 90-minute opening as the natural home for two 45-minute meetings, and offer it as such rather than as an arbitrary run of 30-minute slots.
2. **Align dynamically to existing bookings.** Anchor a 45-minute meeting to the edges that the advisor's already-booked day creates — in particular the boundaries left by 15-minute appointments — instead of to an abstract clock rhythm.

Both are placement problems, not rhythm problems. Framed that way the engine change is smaller and better-behaved: keep 15 minutes as the underlying lattice, and let meeting length be a span measured against it.

### 6.3 Why this matters for calendar packing

The firm has three mechanisms that shape how densely an advisor's day fills:

- **Advisor start-time rules** — an advisor can require that appointments start only at certain minutes past the hour. These stay coherent as long as start times land on a consistent lattice, which is an argument for spans-on-a-lattice over per-type rhythms.
- **"Slot score"** — every offered slot carries a Strong / Fair / Weak / Busy badge, with arrow icons and a legend popover, and the three slots shown by default are chosen using it. It ranks by closeness to noon, not by fill. **That is deliberate; see below.**
- **Adjacent-slot checking** — the engine can test whether the slots either side of a candidate are free. Built to drive gap-aware ranking, then **deprecated** when that approach was dropped (see below). The code remains; nothing calls it.

#### "Slot score" scores closeness to noon — and that was a deliberate replacement

Coordinators already have a strong/fair/weak guide on every slot, named **"Slot score"**, driving which three options surface by default. What it scores is **distance from noon**: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond.

Despite the name, it carries no information about whether a slot leaves an unfillable gap. **That is not an oversight.** An edge-based algorithm — rank a placement by how many new gaps it creates, so an exact fill is best and a middle-of-the-gap placement is worst — was tried and **deprecated in favour of closeness to noon, because advisors rejected having their days filled from the outside in.**

The reason it behaves that way is structural. Edge scoring rewards placements that sit flush against something solid, and **on a mostly-empty day the only solid edges are the start and end of the working block.** So the first bookings of any day get pushed to 8:00am and the last slot before 6:00pm, and the day fills inward from the extremes. That is close to the worst possible outcome for an advisor, and it happens precisely when a day is quietest.

Closeness to noon inverts it: days fill from the centre outward, keeping a compact mid-day block instead of scattered bookings at the edges. For the common case — a day with plenty of room — it is simply the better rule, and it is the one in production.

#### Where edge-awareness still has a claim

Edge scoring isn't wrong, it's **wrong for sparse days**. Its logic only becomes meaningful once a day is full enough that gaps exist *between real appointments* rather than between an appointment and the edge of the working block. On a fragmented day, the middle-of-the-gap placement genuinely is the bad one — it turns a usable 90-minute opening into two fragments.

So the likely shape of a future answer is **dynamic rather than either/or**: rank by closeness to noon by default, and shift toward edge-awareness when a day is fragmented enough that gaps, not time of day, are the binding constraint. What would need defining is the trigger — how many gaps, or how much fragmented time, flips the behaviour — and whether it's a hard switch or a weighting that slides.

**This is explicitly not a priority.** The current behaviour is working and advisors prefer it. It's recorded here because the deprecated code is still in the availability engine, and because the 45-minute placement work in §6.2 touches the same machinery — anyone picking that up should know the edge-based approach was evaluated and rejected on purpose, not left unfinished.

#### Placement and ranking are separate problems

It would be easy to read the 45-minute requirement (§6.2) as needing the deprecated edge-based ranking back. It does not, and keeping the two apart is what makes it tractable:

- **Placement — where can this meeting physically go?** Finding that a 45-minute meeting fits a 90-minute opening, or lands cleanly on the edge an existing 15-minute booking left, is a *feasibility* question. The engine already reasons about consecutive free slots to answer exactly this for long appointments.
- **Ranking — of the places it fits, which should coordinators see first?** This is where closeness to noon won and edge scoring lost.

**45-minute support is a placement change, not a ranking change.** It widens the set of start times offered; it does not need to reorder them, and it should not resurrect outside-in filling. What should not happen is shipping 45 as a standalone rhythm (§6.2), which adds stranded time without adding anything that can see or use it.

### 6.4 The grid may not stay a fixed per-type constant

Everything above assumes the grid is a property of the meeting type. That's how it's configured today, but it may not be the right long-term model.

An alternative under consideration is an **adaptive grid** — finer granularity surfaced only when it's actually useful, rather than applied to the whole day. Two shapes of that idea:

- **Grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the coarser grid. Density where density helps, without doubling the button count for every booking.
- **Grid follows the gap.** A finer slot is offered only where the advisor's day already has an opening that aligns to it — a 15-minute hole between two appointments surfaces a 15-minute start time that wouldn't otherwise be offered.

The second is the more interesting one, because **it's gap-packing approached from the opposite direction.** Edge-based ranking (§6.3) tried to avoid *creating* stranded time by preferring slots that don't leave orphans — and was deprecated for filling days outside-in. An adaptive grid instead *reclaims* stranded time by exposing start times that fit the orphans already there, without reordering what coordinators see first. It targets the same waste from the placement side rather than the ranking side, which is the side that survived.

This is the same conclusion §6.2 reaches from the 45-minute side: what's needed is an engine that finds where a span fits in the day that actually exists, rather than one that imposes a rhythm and hopes meetings line up with it.

### 6.5 Duration and grid are currently entangled

Worth knowing before any of the above is designed: the booking UI lets a coordinator pick a **duration** of 15, 30, 45, 60, 75, 90, or 120 minutes, and that chosen duration currently flows through as the **grid** as well, rather than the meeting type's configured grid. Picking 45 minutes appears to shift the day onto a 45-minute rhythm rather than booking a 45-minute meeting on the type's 30-minute grid.

**This may be work in progress rather than a defect** — an early, partial step toward exactly the adaptive behavior described above, or something already under design review. It's flagged here because it needs a deliberate answer either way: if the grid is going to become contextual, the relationship between the duration control and the grid is the first thing that has to be defined. There's also a correctness question attached to it (§10.3) that should be checked regardless of which direction the design goes.

---
