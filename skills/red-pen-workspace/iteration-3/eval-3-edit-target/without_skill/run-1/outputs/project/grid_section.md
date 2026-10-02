## 6. The grid — how slots are offered

**In brief**

- The grid (which start times are offered) and the duration (how long the meeting lasts) are separate settings. Each meeting type has a 30- or 15-minute grid, set by the firm.
- "Support 15- and 45-minute blocks" is two different asks. Extending the 15-minute grid to more meeting types is a product decision about how many start times coordinators see. 45 minutes should not be a grid at all; it should be a meeting length that starts on the 15-minute grid.
- Supporting 45-minute meetings changes which start times are offered, not the order they are shown in. Ranking stays as it is: closeness to noon. Ranking by gaps was tried and withdrawn because advisors rejected it.
- Today the duration a coordinator picks appears to override the meeting type's grid (§6.5). That needs a deliberate answer before anything else in this section is designed.

**Decisions this section asks for**

1. Which additional meeting types, if any, move to a 15-minute grid (§6.2).
2. Whether 45-minute meetings are supported as a placement on the 15-minute grid, in the two cases described in §6.2, rather than as a 45-minute grid.
3. How the duration control relates to the grid (§6.5).
4. Whether to pursue an adaptive grid (§6.4).

Not asked for now: changing how slots are ranked on fragmented days (§6.3).

---

The grid is the most visible piece of booking UX: it is the set of start times a client can be offered. It is not the same thing as how long the meeting is, and the rest of this section depends on keeping the two apart.

- **Duration** is how long the meeting occupies the advisor. It is a fact about the work.
- **Grid** is the set of clock times a meeting can start on: :00 and :30, or every :15. It is a decision about presentation and about how tightly the day packs.

The two are independent. A 45-minute meeting on a 30-minute grid takes two consecutive slots and leaves 15 minutes after it that nothing can be booked into. A 15-minute meeting on a 30-minute grid takes one slot and leaves the other 15 minutes unusable. This section calls that leftover **stranded time**.

### 6.1 Today's grid

The grid is a property of the meeting type. The firm sets it; neither the booker nor the advisor chooses it. (In practice the duration control currently appears to override it; see §6.5.)

| Grid | Meeting types |
|---|---|
| **30 min** | Kickoff, follow-up, plan review, review follow-up, office drop-in, hold |
| **15 min** | Intro call, quick check-in, workshop, other on-site session |

The 30-minute default is working and is not the problem. Two cases show that the grid is a business choice rather than something derived from meeting length:

- **Office drop-in is a 15-minute meeting on a 30-minute grid.** This is deliberate: the front desk gets predictable half-hour arrival waves instead of a trickle every quarter hour.
- **Workshops and other on-site sessions are on a 15-minute grid** because meeting-room time is the scarcest resource and packing it tightly matters most.

### 6.2 What's needed: finer placement, not new grids

The requirement is usually stated as "support 15- and 45-minute blocks." Those are two different asks, and only the first is about the grid.

**15 minutes is a grid question.** Four meeting types already use a 15-minute grid, so the concept is supported. Extending it to more types is mostly a product decision about density. A 15-minute grid roughly doubles the number of start times a coordinator sees per day, which bears directly on the "show three slots by default, ranked by closeness to noon" behavior in §7.5. More options are not automatically better: only three are shown today because a wall of times is harder to book from.

**45 minutes is not a grid question.** A 45-minute grid would offer 9:00, 9:45, 10:30, 11:15. That pattern returns to the top of the hour only every three hours and does not divide office hours evenly. Thinking of 45 as a grid is the source of most of the apparent difficulty.

Treated instead as a meeting length that starts on the 15-minute grid, 45 behaves well:

- 45 minutes is exactly three 15-minute units, so a 45-minute meeting that starts on a 15-minute boundary also ends on one. It never strands less than 15 minutes.
- Two 45-minute meetings fill a 90-minute opening exactly, with nothing wasted.

So the capability needed is the ability to fit a 45-minute meeting into the space that exists, in two specific cases:

1. **Fill a 90-minute gap.** Recognize a 90-minute opening as room for two 45-minute meetings and offer it that way, rather than as a run of 30-minute slots.
2. **Align to existing bookings.** Start a 45-minute meeting where the advisor's already-booked day leaves an opening, in particular at the boundaries left by 15-minute appointments, rather than only at fixed clock times.

Both are questions of where a meeting can go, not of which clock times the day runs on. Framed that way the engine change is smaller: 15 minutes stays the underlying grid, and meeting length is measured against it.

### 6.3 How this relates to slot ranking

Three existing mechanisms shape how densely an advisor's day fills:

- **Advisor start-time rules.** An advisor can require that appointments start only at certain minutes past the hour. These rules stay coherent as long as every start time falls on one consistent grid, which is an argument for the approach in §6.2 over giving each meeting type its own pattern.
- **Slot score.** Every offered slot carries a Strong / Fair / Weak / Busy badge, with arrow icons and a legend popover. The three slots shown by default are chosen using it. It ranks by closeness to noon, not by how well a slot fills the day.
- **Adjacent-slot checking.** The engine can test whether the slots on either side of a candidate are free. This was built for ranking by gaps and was deprecated when that approach was dropped. The code remains, but nothing calls it.

#### Slot score measures closeness to noon, by design

Slot score measures distance from noon: Strong within 2 hours (10am–2pm), Fair within 4 (8am–4pm), Weak beyond that. Despite the name, it says nothing about whether a slot leaves stranded time.

That is not an oversight. An edge-based ranking was tried first. It ranked a placement by how many new gaps it created, so a slot that exactly filled an opening scored best and one in the middle of an opening scored worst. It was deprecated in favour of closeness to noon because advisors rejected having their days filled from the outside in.

Outside-in filling follows from how edge-based ranking works. It rewards slots that sit flush against something already fixed, and on a mostly empty day the only fixed things are the start and end of the working day. The first bookings of the day are pushed to 8:00am and to the last slot before 6:00pm, and the day fills inward from there. That is close to the worst outcome for an advisor, and it happens when the day is quietest.

Closeness to noon does the opposite: days fill from the centre outward, which keeps a compact mid-day block. For the common case, a day with plenty of room, it is the better rule, and it is the one in production.

#### Where edge-based ranking still has a case

Edge-based ranking is wrong for sparse days, not wrong in general. It becomes useful once a day is full enough that the gaps are between real appointments. On a fragmented day, a slot in the middle of a gap really is the bad choice: it turns a usable 90-minute opening into two fragments.

A future answer would likely combine the two: rank by closeness to noon by default, and give more weight to gaps once a day is fragmented enough that gaps, not time of day, are what limit it. That would need a defined trigger (how many gaps, or how much fragmented time, changes the behaviour) and a decision on whether it is a hard switch or a sliding weight.

**This is not a priority.** The current behaviour is working and advisors prefer it. It is recorded here for two reasons: the deprecated code is still in the availability engine, and the 45-minute work in §6.2 touches the same code. Whoever picks that up should know edge-based ranking was evaluated and rejected on purpose, not left unfinished.

#### Placement and ranking are separate problems

The 45-minute requirement in §6.2 could be read as needing edge-based ranking back. It does not.

- **Placement: where can this meeting go?** Whether a 45-minute meeting fits a 90-minute opening, or fits against the boundary an existing 15-minute booking left, is a feasibility question. The engine already answers the same question for long appointments by checking for consecutive free slots.
- **Ranking: of the places it fits, which should coordinators see first?** This is where closeness to noon won and edge-based ranking lost.

**45-minute support is a placement change, not a ranking change.** It widens the set of start times offered. It does not need to reorder them, and it should not bring back outside-in filling.

What should not ship is 45 minutes as its own grid (§6.2). That would add stranded time without adding anything able to use it.

### 6.4 The grid may not stay a fixed per-type setting

Everything above assumes the grid is a property of the meeting type. That is how it is configured today, but it may not be the right long-term model.

An alternative under consideration is an **adaptive grid**: finer start times offered only where they are useful, rather than across the whole day. It could take two forms:

- **The grid follows the meeting being booked.** A 15-minute grid appears only when booking a 15-minute meeting; longer meetings stay on the 30-minute grid. This gives density where it helps without doubling the number of start times shown for every booking.
- **The grid follows the gap.** A finer start time is offered only where the advisor's day already has an opening that fits it. A 15-minute hole between two appointments surfaces a 15-minute start time that would not otherwise be offered.

The second form addresses the same waste that edge-based ranking (§6.3) went after, from the other side. Edge-based ranking tried to avoid creating stranded time by preferring slots that leave none, and was deprecated for filling days outside-in. An adaptive grid reclaims stranded time that already exists by offering start times that fit it, and it does not change which slots coordinators see first. It works through placement rather than ranking, and ranking is the side where the gap-based approach was rejected.

This is the same conclusion §6.2 reaches for 45-minute meetings: the engine should find where a meeting fits in the day as it is actually booked, rather than impose fixed clock times and hope meetings line up with them.

### 6.5 Duration and grid are currently entangled

This affects the design of everything above. The booking UI lets a coordinator pick a duration of 15, 30, 45, 60, 75, 90, or 120 minutes. That duration is currently used as the grid as well, in place of the grid configured for the meeting type. Picking 45 minutes appears to put the day on a 45-minute grid, rather than booking a 45-minute meeting on the type's 30-minute grid.

This may be work in progress rather than a defect: an early, partial step toward the adaptive behavior in §6.4, or something already under design review. It is flagged here because it needs a deliberate answer either way. If the grid is going to become contextual, the relationship between the duration control and the grid is the first thing to define. There is also a correctness question attached (§10.3) that should be checked whichever direction the design goes.

---
