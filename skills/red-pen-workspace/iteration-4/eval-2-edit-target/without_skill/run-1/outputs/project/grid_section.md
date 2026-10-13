## 6. The grid — how slots are offered

The grid is the set of start times a client can be offered, and it is the most visible part of booking UX. It is **not** the same thing as how long the meeting lasts. Keeping those two ideas apart matters for everything below.

- **Duration** — how long the meeting occupies the advisor. A fact about the work.
- **Grid (interval)** — the clock rhythm start times land on: :00 and :30, or every :15. A presentation and packing decision.

The two are independent. A 45-minute meeting on a 30-minute grid takes two consecutive slots and strands the 15 minutes after it. A 15-minute meeting on a 30-minute grid takes one slot and strands the other 15 minutes.

### 6.1 Today's grid

The grid is set per **meeting type** by the firm. Neither the booker nor the advisor chooses it.

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The 30-minute default works and is not the problem. Two cases are worth understanding:

- **Office drop-in is a 15-minute meeting on a 30-minute grid.** This is deliberate: the front desk gets predictable half-hour arrival waves instead of a trickle every quarter hour. It is the clearest existing proof that the grid is a business lever, not something derived from duration.
- **Workshops and other on-site sessions use a 15-minute grid** because meeting-room time is the scarcest resource and packing it tightly matters most.

### 6.2 What's needed: finer placement, not new rhythms

The requirement usually arrives as "support 15- and 45-minute blocks." Those are two different asks, and only one of them is a grid question.

**15 minutes is a grid question, and a product decision about density.** Four meeting types already use a 15-minute grid, so the capability exists; extending it to more types is the decision. A 15-minute grid roughly doubles the start times a coordinator sees per day, which interacts directly with the "show three slots by default" behavior in §7.5. Only three are shown today because a wall of times is harder to book from, not easier — more options is not automatically better.

**45 minutes is not a grid question.** Treating 45 as a *step size* (9:00, 9:45, 10:30, 11:15) produces a rhythm that realigns with the hour only every three hours and doesn't divide office hours evenly. That model is the source of most of the apparent difficulty.

Treated instead as a **45-minute block placed on the existing 15-minute grid**, it behaves well:

- **45 is exactly three 15-minute units**, so a 45-minute meeting that starts on a 15-minute boundary also ends on one. It never strands a fragment shorter than 15 minutes.
- **Two 45s fill a 90-minute opening exactly**, with nothing left over.

So the requirement is not "a 45-minute grid." It is the ability to **fit a 45-minute meeting into the space that exists**, in two ways:

1. **Fill a 90-minute opening.** Recognize a 90-minute opening as the natural home for two 45-minute meetings and offer it that way, rather than as an arbitrary run of 30-minute slots.
2. **Align to existing bookings.** Start or end a 45-minute meeting at the edges the advisor's booked day already creates — especially the boundaries left by 15-minute appointments — rather than at a fixed clock rhythm.

**Recommendation:** keep 15 minutes as the underlying grid and treat meeting length as a block measured against it. This is a smaller, lower-risk engine change than adding a 45-minute rhythm. Shipping 45 as a standalone rhythm should be avoided: it adds stranded time without adding anything that can see or use it.

### 6.3 Interaction with how slots are ranked

Two existing mechanisms shape how densely an advisor's day fills, and one retired mechanism is still in the code:

- **Advisor start-time rules** — an advisor can require appointments to start only at certain minutes past the hour. These stay coherent as long as all start times share one consistent grid, which is another argument for the 15-minute-grid approach in §6.2 over per-type rhythms.
- **"Slot score"** — every offered slot carries a Strong / Fair / Weak / Busy badge (with arrow icons and a legend popover), and it decides which three slots are shown by default. It scores **closeness to noon**: Strong within 2 hours (10am–2pm), Fair within 4 hours (8am–4pm), Weak beyond.
- **Adjacent-slot checking (deprecated)** — the engine can test whether the slots on either side of a candidate are free. It was built for gap-aware ranking and retired when that approach was dropped. The code remains; nothing calls it.

#### Why "Slot score" ranks by closeness to noon

Despite its name, Slot score says nothing about whether a slot leaves an unfillable gap. **That is deliberate.** Gap-aware ("edge-based") ranking — preferring placements that create the fewest new gaps — was tried and **replaced by closeness to noon because advisors rejected having their days filled from the outside in.**

Edge-based ranking rewards slots that sit flush against something already booked. **On a mostly empty day, the only such edges are the start and end of the working day**, so the first bookings land at 8:00am and just before 6:00pm and the day fills inward from the extremes. That is close to the worst outcome for an advisor, and it happens on exactly the quiet days when it's most avoidable.

Closeness to noon reverses this: days fill from the middle outward into a compact mid-day block. For the common case — a day with plenty of room — it is the better rule, and it is what runs in production.

#### Where gap-awareness could still help (not a priority)

Edge-based ranking is wrong for **sparse** days, not wrong everywhere. Once a day is full enough that gaps sit *between real appointments*, a placement in the middle of a gap genuinely is the bad choice — it turns a usable 90-minute opening into two unusable fragments.

A possible future rule would therefore be **dynamic**: rank by closeness to noon by default, and shift toward gap-awareness once a day is fragmented enough that gaps, not time of day, are the binding constraint. Open questions if this is ever pursued:

- What triggers the shift — number of gaps, or total fragmented time?
- Is it a hard switch or a sliding weighting?

**This is explicitly not a priority.** Current behavior works and advisors prefer it. It is recorded here because the retired code is still in the engine and the 45-minute work in §6.2 touches the same area — whoever picks that up should know edge-based ranking was evaluated and rejected on purpose, not left unfinished.

#### 45-minute support does not need ranking changes

It is easy to read the 45-minute requirement as needing gap-aware ranking back. It does not:

- **Placement — where can this meeting go?** Whether a 45-minute meeting fits a 90-minute opening, or lines up with the edge of an existing 15-minute booking, is a feasibility question. The engine already checks for consecutive free slots to answer this for long appointments.
- **Ranking — of the places it fits, which do coordinators see first?** This is where closeness to noon won.

**45-minute support is a placement change, not a ranking change.** It widens the set of start times offered; it does not reorder them, and it should not bring back outside-in filling.

### 6.4 The grid may not stay fixed per meeting type

Everything above assumes the grid is a fixed property of the meeting type. That is how it's configured today, but it may not be the right long-term model.

An alternative under consideration is an **adaptive grid**: finer start times offered only where they are useful, not across the whole day. Two versions:

- **Grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the coarser grid. Density where it helps, without doubling the number of options for every booking.
- **Grid follows the gap.** A finer start time is offered only where the advisor's day already has an opening that fits it — for example, a 15-minute hole between two appointments surfaces a 15-minute start time that wouldn't otherwise appear.

The second is the more promising. It tackles the same waste edge-based ranking targeted (§6.3), but from the placement side, which is the side that survived: it **reclaims** stranded time by offering start times that fit gaps already there, without reordering what coordinators see first. It points to the same conclusion as §6.2 — the engine should find where a meeting fits in the actual day, not impose a rhythm and hope meetings line up with it.

### 6.5 Open issue: duration and grid are currently entangled

Before any of the above is designed: the booking UI lets a coordinator pick a **duration** of 15, 30, 45, 60, 75, 90, or 120 minutes, and that duration currently also acts as the **grid**, overriding the meeting type's configured grid. Picking 45 minutes appears to put the day on a 45-minute rhythm — the model §6.2 recommends against — instead of booking a 45-minute meeting on the type's 30-minute grid.

**This may be work in progress rather than a defect** — an early step toward the adaptive grid in §6.4, or something already in design review. Either way it needs a deliberate decision: if the grid becomes contextual, the relationship between the duration control and the grid is the first thing to define. There is also a correctness question attached (§10.3) that should be checked regardless of direction.

---
