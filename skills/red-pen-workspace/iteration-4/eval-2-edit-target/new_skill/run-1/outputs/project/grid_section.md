## 6. The grid — how slots are offered

The grid is the set of start times a client can be offered. It is separate from how long the meeting is:

- **Duration** — how long the meeting occupies the advisor. A fact about the work.
- **Grid (interval)** — the clock rhythm start times land on: :00 and :30, or every :15. A presentation and packing decision.

The two are independent. On a 30-minute grid, a 45-minute meeting consumes two consecutive slots and strands 15 minutes after it; a 15-minute meeting consumes one slot and strands the other 15.

### 6.1 Today's grid

The firm sets the grid per **meeting type**; neither the booker nor the advisor chooses it.

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The 30-minute default works. Two cases are deliberate:

- **Office drop-in** is a 15-minute meeting on a 30-minute grid, so the front desk gets half-hour arrival waves instead of a trickle every quarter hour. It is the clearest proof that the grid is a business lever, not a value derived from duration.
- **Workshops and other on-site sessions** use a 15-minute grid because meeting-room time is the scarcest resource, and packing it tightly matters most.

### 6.2 What's needed: finer placement, not new rhythms

"Support 15- and 45-minute blocks" is two asks, and only the first is a grid question.

**15 minutes is a product decision about density.** Four meeting types already use a 15-minute grid, so the concept is supported. A 15-minute grid roughly doubles the start times a coordinator sees per day. That interacts with §7.5: three slots are shown by default, ranked by closeness to noon, because a wall of times is harder to book from.

**45 minutes is not a grid question.** As a step size (9:00, 9:45, 10:30, 11:15), 45 realigns with the hour only every three hours and does not divide office hours evenly. Most of the apparent difficulty comes from this model.

As a **span on the existing 15-minute lattice**, 45 behaves well:

- 45 is three 15-minute units, so a 45-minute meeting that starts on a 15-minute boundary also ends on one. It never strands a fragment smaller than the lattice.
- Two 45-minute meetings fill a 90-minute opening exactly, with nothing wasted.

The capability needed is to **fit a 45-minute meeting into the space that exists**, in two ways:

1. **Fill a 90-minute gap.** Offer a 90-minute opening as the home for two 45-minute meetings, not as an arbitrary run of 30-minute slots.
2. **Align to existing bookings.** Anchor a 45-minute meeting to the edges the advisor's booked day creates, especially those left by 15-minute appointments, not to a clock rhythm.

Both are placement problems, not rhythm problems. The smaller engine change: keep 15 minutes as the lattice, and measure meeting length as a span on it.

### 6.3 Why this matters for calendar packing

Three mechanisms bear on how densely an advisor's day fills:

- **Advisor start-time rules** — an advisor can require that appointments start only at certain minutes past the hour. These stay coherent only while start times land on one consistent lattice, which favours spans-on-a-lattice over per-type rhythms.
- **"Slot score"** — every offered slot carries a Strong / Fair / Weak / Busy badge, with arrow icons and a legend popover. It picks the three slots shown by default, and it ranks by closeness to noon, not by fill.
- **Adjacent-slot checking** — the engine can test whether the slots either side of a candidate are free. It was built for gap-aware ranking and deprecated when that approach was dropped. The code remains; nothing calls it.

#### "Slot score" scores closeness to noon — and that was a deliberate replacement

Slot score rates distance from noon: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond. Despite the name, it says nothing about whether a slot leaves an unfillable gap.

It replaced an edge-based algorithm, which ranked a placement by how many new gaps it created: an exact fill best, a middle-of-the-gap placement worst. Advisors rejected it because it filled their days from the outside in. On a mostly empty day the only edges are the start and end of the working block, so the first bookings went to 8:00am and the last slot before 6:00pm, on exactly the quietest days. Closeness to noon fills days from the centre outward into a compact mid-day block. It is the rule in production.

#### Where edge-awareness still has a claim

Edge scoring is not wrong in general; it is wrong for sparse days. On a fragmented day, with gaps between real appointments, a middle-of-the-gap placement is the bad one: it splits a usable 90-minute opening into two fragments.

A future answer would likely be dynamic: rank by closeness to noon by default, and shift toward edge-awareness when gaps, not time of day, are the binding constraint. Still to define: the trigger (how many gaps, or how much fragmented time), and whether it is a hard switch or a sliding weight.

**This is not a priority.** Advisors prefer the current behaviour. It is recorded because the deprecated code is still in the availability engine, and the 45-minute work in §6.2 touches the same machinery. The edge-based approach was rejected on purpose, not left unfinished.

#### Placement and ranking are separate problems

The 45-minute requirement does not need the deprecated ranking back:

- **Placement — where can this meeting physically go?** Whether a 45-minute meeting fits a 90-minute opening, or lands on the edge a 15-minute booking left, is a feasibility question. The engine already answers it for long appointments by reasoning about consecutive free slots.
- **Ranking — of the places it fits, which do coordinators see first?** Closeness to noon won here.

**45-minute support is a placement change, not a ranking change.** It widens the set of start times offered, without reordering them or bringing back outside-in filling. Shipping 45 as a standalone rhythm (§6.2) is the outcome to avoid: it adds stranded time and nothing that can see or use it.

### 6.4 The grid may not stay a fixed per-type constant

Today the grid is configured per meeting type, but that may not be the right long-term model. Under consideration is an **adaptive grid**, which surfaces finer start times only where they help. Two shapes:

- **Grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the coarser grid. This adds density where it helps, without doubling the start-time buttons for every booking.
- **Grid follows the gap.** A finer start time is offered only where the advisor's day already has an opening that aligns to it: a 15-minute hole between two appointments surfaces a 15-minute start time.

The second is the more interesting one. Edge-based ranking (§6.3) tried to avoid *creating* stranded time and was deprecated. Grid-follows-the-gap *reclaims* stranded time that already exists, from the placement side, without reordering what coordinators see first. It reaches §6.2's conclusion from the other direction: the engine should find where a span fits in the actual day, not impose a rhythm.

### 6.5 Duration and grid are currently entangled

The booking UI lets a coordinator pick a **duration** of 15, 30, 45, 60, 75, 90, or 120 minutes. That duration currently also sets the **grid**, in place of the meeting type's configured grid. Picking 45 appears to put the day on a 45-minute rhythm, instead of booking a 45-minute meeting on the type's 30-minute grid.

This may be work in progress rather than a defect: a partial step toward the adaptive grid in §6.4, or something already in design review. Either way it needs a deliberate answer. If the grid becomes contextual, the relationship between the duration control and the grid is the first thing to define. A related correctness question (§10.3) should be checked regardless.

---
