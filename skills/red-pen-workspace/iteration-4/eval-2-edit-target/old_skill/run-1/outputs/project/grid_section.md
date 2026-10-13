## 6. The grid — how slots are offered

The grid is the set of start times a client can be offered. It is independent of how long the meeting is:

- **Duration** — how long the meeting occupies the advisor. A fact about the work.
- **Grid (interval)** — the clock rhythm start times land on: :00 and :30, or every :15. A presentation and packing decision.

A 45-minute meeting on a 30-minute grid consumes two slots and strands 15 minutes; a 15-minute meeting on a 30-minute grid consumes one and strands 15.

### 6.1 Today's grid

The firm sets the grid per **meeting type**; neither the booker nor the advisor chooses it.

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The 30-minute default works. Two cases show the grid is a business lever, not a derived value:

- **Office drop-in is a 15-minute meeting on a 30-minute grid**, so the front desk gets half-hour arrival waves instead of a trickle every quarter hour.
- **Workshops and other on-site sessions use a 15-minute grid** because meeting-room time is the scarcest resource.

### 6.2 What's needed: finer placement, not new rhythms

"Support 15- and 45-minute blocks" is two asks, and only one is a grid change.

**15 minutes is a grid question, and a product decision about density.** Four meeting types already use it. Extending it to more types roughly doubles the start times a coordinator sees per day, which interacts with the three-slot default in §7.5; that default exists because a wall of times is harder to book from.

**45 minutes is a placement question.** As a step size (9:00, 9:45, 10:30, 11:15) it realigns with the hour only every three hours and doesn't divide office hours evenly. As a span on the existing 15-minute lattice it is well-behaved:

- **45 is exactly three 15-minute units**, so a 45-minute meeting starting on a 15-minute boundary ends on one and never strands a fragment smaller than the lattice.
- **Two 45s tile a 90-minute block exactly.**

The capability needed is fitting a 45-minute meeting into the space that exists, in two ways:

1. **Fill a 90-minute gap.** Offer a 90-minute opening as the home for two 45-minute meetings, not as a run of 30-minute slots.
2. **Align to existing bookings.** Anchor a 45-minute meeting to the edges the advisor's booked day creates, especially those left by 15-minute appointments, instead of to a clock rhythm.

The engine change: keep 15 minutes as the lattice and measure meeting length as a span against it. Do not ship 45 as a standalone rhythm; it adds stranded time and nothing that can use it.

### 6.3 Why this matters for calendar packing

Three mechanisms shape how densely an advisor's day fills:

- **Advisor start-time rules** — an advisor can require appointments to start only at certain minutes past the hour. These stay coherent only while start times land on a consistent lattice, which favours spans-on-a-lattice over per-type rhythms.
- **"Slot score"** — a Strong / Fair / Weak / Busy badge on every offered slot (arrow icons, legend popover) that picks the three slots shown by default. It scores distance from noon: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond. Despite the name, it says nothing about whether a slot leaves an unfillable gap.
- **Adjacent-slot checking** — the engine can test whether the slots either side of a candidate are free. Built for gap-aware ranking and deprecated with it; the code remains and nothing calls it.

**Closeness to noon is deliberate.** Edge-based ranking (score a placement by how many new gaps it creates) was tried and deprecated because advisors rejected days filled from the outside in: on a mostly empty day the only edges are the start and end of the working block, so first bookings went to 8:00am and the last slot before 6:00pm. Closeness to noon fills days from the centre outward and is in production.

**Edge-awareness is wrong for sparse days, not wrong.** On a fragmented day, placing a meeting mid-gap does turn a usable 90-minute opening into two fragments. A future version could rank by closeness to noon by default and shift toward edges once a day is fragmented enough; what would need defining is the trigger (how many gaps, or how much fragmented time) and whether it is a hard switch or a sliding weight. **Not a priority**: advisors prefer the current behaviour. It is recorded because the deprecated code is still in the availability engine and the §6.2 work touches the same machinery.

**Placement and ranking are separate problems.** Placement asks where a meeting can physically go; the engine already finds consecutive free slots for long appointments. Ranking asks which of those places coordinators see first; that is where closeness to noon won. 45-minute support is a placement change: it widens the set of start times offered, does not reorder them, and does not need edge-based ranking back.

### 6.4 The grid may not stay a fixed per-type constant

An alternative under consideration is an **adaptive grid**: finer granularity offered only where it helps. Two shapes:

- **Grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the coarser grid, so most bookings don't double their button count.
- **Grid follows the gap.** A finer start time is offered only where the day already has an opening aligned to it: a 15-minute hole between two appointments surfaces a 15-minute start time that wouldn't otherwise be offered.

The second is the stronger. It reclaims stranded time from the placement side, by exposing start times that fit existing gaps, without the reordering that got edge-based ranking deprecated.

### 6.5 Duration and grid are currently entangled

The booking UI lets a coordinator pick a **duration** of 15, 30, 45, 60, 75, 90, or 120 minutes, and that duration currently also becomes the **grid**, overriding the meeting type's. Picking 45 minutes appears to put the day on a 45-minute rhythm instead of booking a 45-minute meeting on the type's 30-minute grid.

This may be work in progress toward the adaptive grid in §6.4 rather than a defect; either way it needs a deliberate answer. If the grid becomes contextual, the duration control's relationship to the grid is the first thing to define. A correctness question attached to it (§10.3) should be checked regardless.

---
