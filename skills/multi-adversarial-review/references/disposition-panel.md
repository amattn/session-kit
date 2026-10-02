# Disposition Panel — bounded cross-examination (escalation only)

Read this file when the convene gate in the core skill (`../SKILL.md`
§ Pushback / Re-Review) fires. The panel escalates a **contested finding**
after a one-shot disposition audit deadlocks; it is never the next review
stage and never generates findings. It is a **recommender**, not a judge: it
must never resolve in favor of the party that merely holds out, and an
unresolved guarded finding is carried to the maintainer, never dropped.
(Rationale and the failure modes each rule closes: the prior-art document,
§ Panel vs Chain.)

## Convene Gate

Convene when both hold — or when the maintainer requests a debate (which
overrides the gate):

- Either the reviewer **or** the implementer rates the finding high-severity
  or security-sensitive (auth, crypto, payments, permissions, data loss),
  **and** the implementer's draft disposition is `rejected`,
  `accepted-deferred`, or `unclear-blocked`. A split rating convenes (the
  higher governs) — the motivated party cannot downrate its way out.
  `unclear-blocked` is included so a guarded finding cannot be parked as
  "need more info" to dodge the panel.
- No cheap up-front probe or source citation settles it (if one does, use it
  and do not convene; evidence surfacing *during* debate is the empirical
  trump).

The gate also fires on a **failed fix**: a guarded `accepted-fixed` is not
credited until the one-shot audit returns `resolved`; a `still open` /
`rejection not accepted` verdict re-enters this gate as `rejected`. Never
convene to generate findings, to audit a `no-findings`, or as a substitute
for the next stage. Default off.

## Roles

- **Parties** — the raising reviewer and the implementer; these two, and only
  these two, are the convergence parties.
- **Judge** — the maintainer, never a debating party. The panel produces an
  auditable recommendation the maintainer rules on. In autonomous mode no
  party adjudicates its own finding and the panel self-certifies no winner —
  it carries to the maintainer audit, which is the *expected* close, not a
  degraded fallback.
- **Advisory third voice** — with 3+ families and a round-one deadlock, a
  neutral family (neither author nor raiser) joins from round two, speaking
  DEFEND / RETRACT / REVISE with its own evidence. It is **not** a vote or
  tiebreak (consensus is never the verdict) — it adds a neutral read to the
  record the maintainer audits.

## Timing and Thread Location

Run after all stage lenses finish and dispositions are drafted, before the
disposition commit. Keep the verbatim thread **out of the committed tree**
(scratch, not tracked); only the disposition *summary* is committed. If a
project uses an in-tree `panel` shape (`<record>.panel.discussion.md`), prune
it before the disposition commit, or exclude the `*.panel.discussion.md` glob
from a **re-convened panel's** inputs. Committed progress/status dispositions
are *not* excluded — the next review stage reads them; only the raw panel
thread is withheld, and only from another panel on the same finding.

## Protocol, Per Finding

- **Round one is an evidence bar:** the raiser gives concrete evidence for
  the finding *and* its severity, or it auto-**RETRACT**s. This is what makes
  the symmetric convene trigger safe against a noisy reviewer.
- Each round is **DEFEND / RETRACT / REVISE with new evidence**; pure
  restatement of a rebutted point forfeits that round. A party that decays
  into restatement converges the finding to the other side — persistence
  alone wins nothing.
- **Convergence (two-party):** both agree real → `accepted-fixed` or
  `accepted-deferred` (split fix-vs-defer defaults to `accepted-deferred`
  unless the implementer commits to fix); both agree not → `rejected`.
- **`unclear-blocked` is a convene input, never a panel output** for the
  guarded population: the panel must terminate a guarded finding at fixed /
  deferred / rejected / `contested`. "Still can't decide" after a full panel
  (including a decay onto an implementer's `unclear-blocked`) *is* a standoff
  → `contested`.
- REVISE does **not** reset the count. Hard cap: **three rounds**. An
  empirical trump (probe/citation surfacing mid-debate) ends it either way at
  any round.
- **Non-convergence does not pick a winner.** A genuine standoff (new
  evidence and a fresh rebuttal every round, neither conceding) terminates as
  `contested` — the distinct unresolved-standoff state, *not*
  `accepted-deferred` or `rejected` (either would pick a side) — recorded
  with both sides' evidence and the third voice's read, and surfaced for
  maintainer audit. Never silently `rejected`.
- **`contested` blocks release, never the next review stage**, so the chain
  always advances. Carries are the maintainer's audit queue; shipping with
  unreviewed carries is an explicit **degraded, ship-at-risk** state naming
  the N items, never a silent pass.

## Two Invariants That Survive the Panel

- A debate-confirmed finding still gets the normal fix discipline (verify
  against source, failing check first). A debate verdict is not verification —
  agreeing models can share a blind spot.
- The panel **thread** stays out of the committed tree: a raw debate
  transcript is noise for later readers, and a fresh *panel* on a later
  finding should not anchor on a prior panel's argument. This is the one
  blindness that survives — the normal review chain is cumulative and reads
  prior findings freely, but a *panel participant* that argued a finding
  cannot be that same finding's fresh panelist (use a new one-shot instance,
  reorder, or mark degraded). Committed dispositions are fair game for the
  next review *stage*; they are withheld only from a re-convened *panel* on
  the same contested finding.
