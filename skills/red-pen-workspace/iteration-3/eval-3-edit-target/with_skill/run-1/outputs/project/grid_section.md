## 6. The grid — how slots are offered

The grid is the set of start times a client can be offered. It is not the same thing as how long the meeting is:

- **Duration** — how long the meeting occupies the advisor. A fact about the work.
- **Grid (interval)** — the clock rhythm start times land on: :00 and :30, or every :15. A presentation and packing decision.

They're independent. A 45-minute meeting on a 30-minute grid consumes two consecutive slots and strands 15 minutes after it. A 15-minute meeting on the same grid consumes one slot and strands the other 15.

### 6.1 Today's grid

The grid is a property of the **meeting type**, set by the firm, not chosen by the booker or the advisor. (The booking UI currently departs from this; see §6.5.)

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The 30-minute default is working. Two cases worth understanding:

- **Office drop-in is a 15-minute meeting on a 30-minute grid** — deliberate, so the front desk gets predictable half-hour arrival waves instead of a trickle every quarter hour. The clearest existing proof that grid is a business lever, not a derived value.
- **Workshops and other on-site sessions sit on a 15-minute grid** because meeting-room time is the scarcest resource and packing it tightly matters most.

### 6.2 What's needed: finer placement, not new rhythms

The requirement is usually stated as "support 15- and 45-minute blocks." Those are two different asks, and only the first is a grid question.

**15 minutes is a grid question.** Four meeting types already use a 15-minute grid, so extending it to more types is a product decision about density. A 15-minute grid roughly doubles the start times a coordinator sees per day, which interacts with the "show three slots by default, ranked by closeness to noon" behavior in §7.5: only three are shown today because a wall of times is harder to book from.

**45 minutes is not.** As a *step size* — 9:00, 9:45, 10:30, 11:15 — 45 produces a rhythm that repeats only every three hours and doesn't divide office hours evenly. As a **span placed on the existing 15-minute lattice**, it is well-behaved:

- **45 is exactly three 15-minute units**, so a 45-minute meeting starting on any 15-minute boundary also *ends* on one. It never strands a fragment smaller than the lattice.
- **Two 45s tile a 90-minute block exactly**, with nothing wasted.

So the capability needed is to **fit a 45-minute meeting into the space that exists**, in two ways:

1. **Fill a dedicated 90-minute gap.** Recognize a 90-minute opening as the home for two 45-minute meetings, and offer it as such rather than as an arbitrary run of 30-minute slots.
2. **Align dynamically to existing bookings.** Anchor a 45-minute meeting to the edges the advisor's already-booked day creates — in particular the boundaries left by 15-minute appointments — instead of to a clock rhythm.

Both are placement problems, which makes the engine change smaller: keep 15 minutes as the underlying lattice, and let meeting length be a span measured against it.

### 6.3 Why this matters for calendar packing

Three mechanisms shape how densely an advisor's day fills:

- **Advisor start-time rules** — an advisor can require that appointments start only at certain minutes past the hour. These stay coherent as long as start times land on a consistent lattice, an argument for spans-on-a-lattice over per-type rhythms.
- **"Slot score"** — every offered slot carries a Strong / Fair / Weak / Busy badge, with arrow icons and a legend popover, and the three slots shown by default are chosen using it. It scores distance from noon: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond. Despite the name, it says nothing about whether a slot leaves an unfillable gap.
- **Adjacent-slot checking** — the engine can test whether the slots either side of a candidate are free. Built to drive gap-aware ranking and deprecated with it. The code remains in the availability engine; nothing calls it.

**Closeness to noon replaced edge-based ranking on purpose.** Edge scoring (rank a placement by how few new gaps it creates) was tried and deprecated because advisors rejected having their days filled from the outside in: on a mostly-empty day the only solid edges are the start and end of the working block, so the first bookings were pushed to 8:00am and the last slot before 6:00pm, and the day filled inward. Closeness to noon fills from the centre outward and is the better rule for the common case, a day with plenty of room.

Edge scoring is wrong for sparse days, not for fragmented ones, where a middle-of-the-gap placement turns a usable 90-minute opening into two fragments. A dynamic rule — closeness to noon by default, shifting toward edge-awareness once gaps rather than time of day are the binding constraint — is a parked idea, **explicitly not a priority**. It would need a defined trigger (how many gaps, or how much fragmented time) and a choice between a hard switch and a sliding weighting.

**45-minute support is a placement change, not a ranking change.** The two are separate problems:

- **Placement — where can this meeting physically go?** Finding that a 45-minute meeting fits a 90-minute opening, or lands on the edge an existing 15-minute booking left, is a *feasibility* question. The engine already reasons about consecutive free slots to answer it for long appointments.
- **Ranking — of the places it fits, which should coordinators see first?** Closeness to noon, as above.

45-minute support widens the set of start times offered; it does not reorder them and does not need the deprecated ranking back. What should not happen is shipping 45 as a standalone rhythm (§6.2), which adds stranded time without adding anything that can see or use it.

### 6.4 The grid may not stay a fixed per-type constant

Everything above assumes the grid is a property of the meeting type. An alternative under consideration is an **adaptive grid** — finer granularity surfaced only where it's useful, rather than applied to the whole day. Two shapes:

- **Grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the coarser grid. Density where density helps, without doubling the button count for every booking.
- **Grid follows the gap.** A finer slot is offered only where the advisor's day already has an opening that aligns to it — a 15-minute hole between two appointments surfaces a 15-minute start time that wouldn't otherwise be offered.

The second is gap-packing from the placement side. Edge-based ranking tried to avoid *creating* stranded time; an adaptive grid *reclaims* it by exposing start times that fit the orphans already there, without reordering what coordinators see first. It needs the same engine as §6.2: one that finds where a span fits in the day that actually exists.

### 6.5 Duration and grid are currently entangled

The booking UI lets a coordinator pick a **duration** of 15, 30, 45, 60, 75, 90, or 120 minutes, and that duration currently flows through as the **grid** as well, in place of the meeting type's configured grid. Picking 45 minutes appears to shift the day onto a 45-minute rhythm rather than booking a 45-minute meeting on the type's 30-minute grid.

**This may be work in progress rather than a defect** — an early, partial step toward the adaptive behavior in §6.4, or something already under design review. It needs a deliberate answer either way: if the grid is going to become contextual, the relationship between the duration control and the grid is the first thing to define. The attached correctness question (§10.3) should be checked regardless of direction.

---
