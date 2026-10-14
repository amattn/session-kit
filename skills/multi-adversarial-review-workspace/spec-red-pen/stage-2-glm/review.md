Authority coverage: complete.
Files read: skills/red-pen/SKILL.md (in full), skills/red-pen/HELP.md, skills/red-pen/references/worked_example.md, skills/red-pen/scripts/symptoms.py, authority/WRITING_DIRECTIVES.md, CLAUDE.md (project context), NOTES.md (all /red-pen sections + Important Concepts & Insights, both halves), CHANGELOG.md, skills/multi-adversarial-review/references/copy-review.md, skills/start/SKILL.md, skills/red-pen-workspace/iteration-4/summary.md, skills/multi-adversarial-review-workspace/spec-red-pen/stage-1b-claude/disposition.md, plus /mar2/range.diff (b58cc31..6b6250c).

## Overall assessment

All 14 stage-1b findings plus V1 landed as dispositioned, and none broke anything I can find: the cut pass is renumbered coherently (fact list = step 1, survival = step 7, short pass cites 2/7/9 correctly under the new numbering), the precedence order appears once and consumers agree with it, "budget" language is purged in favor of tripwire/zero-target language exactly as ruled, and the F8b rejection remains correct. The skill is now internally consistent on every axis the owner ruled. What remains is smaller: two boundary gaps in the cut pass's chat rules, one consumer drift in HELP.md, one overstated number in the eval record, and two low mechanical items.

## Strong

1. **The cut pass is now executable end to end.** Fact list before cutting (step 1), survival check against it (step 7), counted targets that reach zero, and an explicit idempotence criterion ("A second pass on the output should change nothing. A pass that keeps cutting is cutting facts.") — a direct answer to the owner's "will it cut by a third again" fear.
2. **Precedence is stated once, in one place** (§ Project-specific overrides), and both in-skill references (§ Editing a target step 2) and MAR's copy-review.md ("House style wins over this reference") point the same direction.
3. **Over-cut guards are layered and mutually consistent with the rulings**: enumeration-is-not-duplication appears in Recognizable Shape, the editing rules, and the worked example's closing lesson; records are exempt from the no-fragments rule; "sparse is not silent"; "a fact that lives nowhere else stays" resolves default-to-less vs. lost-facts.
4. **The worked example now teaches the method it specifies**: fact list shown before the cut, the one questionable cut named in the report, script-vs-human counts distinguished ("except the restatement row, which the script cannot see"). I re-derived its passive count (5→2) and opener count (3→0) against symptoms.py's regexes; they check out.
5. **Mode routing is closed**: PR descriptions route to Mode 3 including its PR paragraph, unsure → Mode 4, multi-type tasks handled in The Job #1. No output type is left without a mode.
6. **Consumer sync is high**: /start step 5 (insider default, roster later, one mention) matches the bootstrap's /start clause verbatim in intent; copy-review's finding kinds now cover the v0.3.0 sentence rules (`term-switch`, `over-compressed`), matching the ruling.
7. **Evidence discipline in the eval record**: iteration-4 states its limits (one run per config, author-written fact lists, same-family graders, one non-discriminating case), and PLAN adds an idempotence case rather than claiming idempotence as tested.

## Needs work

**F1 (medium, evidence honesty) — iteration-4's length-ratio claim contradicts its own table.**
Evidence: `skills/red-pen-workspace/iteration-4/summary.md`, table and Findings: "the no-skill run kept 46/46 at 2 to 3.5 times the length". From the same table: edit-target 1623 vs 1343 words = 1.2×; explain-notes 493 vs 289 = 1.7×; only explain-code (1076 vs 315 = 3.4×) is in the claimed range. Against old_skill the range is 1.5–3.2×. NOTES ("borrows from ASD-STE100" entry) repeats the 2–3.5× figure.
Why it matters: this is the recorded cost-benefit claim backing the v0.3.0 rules; it overstates the no-skill run's length penalty, i.e., inflates the skill's advantage — the exact class the record lens exists to catch, and F14 fixed a neighboring sentence without checking this one.
Proposed change: recompute and state the actual range ("1.2× to 3.4× depending on case" or "up to 3.4×") in summary.md and the NOTES entry.

**F2 (medium-low, open design) — the short pass drops the provenance check, the guard added for the eval's persistent failure class.**
Evidence: SKILL.md § The Cut Pass intro: "A chat reply of a paragraph or two gets the short pass: steps 2, 7, and 9"; step 6 is the provenance check. NOTES iterations 1–3: invented content was the uncaught class in both configurations, and step 6 was extended to "every concrete claim" precisely because it had checked only numbers. Meanwhile the Shared Core's "Numbers over adjectives" actively pushes concrete figures into chat.
Why it matters: the highest-frequency output type is exempt from the one check targeting the one failure the evals never caught. The ruling chose 2/7/9 over "one pass for everything" vs "no pass for chat" — the option set never included adding step 6, so this is a gap in the options, not a challenge to the choice.
Proposed change: owner call — extend the short pass to steps 2, 6, 7, 9, or scope a one-line provenance rule into Mode 4 ("any number in a reply traces to the thread or is labeled an estimate").

**F3 (medium-low) — no cut pass is defined for chat replies longer than "a paragraph or two".**
Evidence: SKILL.md § The Cut Pass: short pass for "a chat reply of a paragraph or two"; "Documents, edits, and anything over its tripwire get every step." Mode 4 defines no tripwire, and Mode 4 explicitly legitimizes longer replies ("A 'how should I think about X' gets a few paragraphs"). A three-to-five-paragraph reply matches neither bucket.
Why it matters: an agent must guess which pass to run on exactly the replies with the most surface for bloat — the pass most likely to be silently skipped or run half-way.
Proposed change: one clause, e.g. "a chat reply longer than two paragraphs runs every step" (a structural count, consistent with "numbers on symptoms, not length").

**F4 (low, consumer drift) — HELP.md says the bootstrap writes CLAUDE.md only.**
Evidence: HELP.md Setup: "It adds a Writing Conventions section to CLAUDE.md". SKILL.md The Job #3 and § Bootstrap say "AGENTS.md and/or CLAUDE.md"; /start's Bootstrap Order step 5 writes the block to AGENTS.md as canonical.
Why it matters: an agent answering "how do I use this" from HELP.md on an AGENTS.md-canonical project (every /start project) writes to the wrong file.
Proposed change: "to AGENTS.md and/or CLAUDE.md" in HELP.md's Setup line.

**F5 (low, correctness trap) — the `git show HEAD:<path>` fallback can recover the wrong baseline.**
Evidence: § Editing a target step 3: "(save the original before writing, or read it back with `git show HEAD:<path>`…)".
Why it matters: if the target has uncommitted changes (the common case mid-session) or is untracked, `git show HEAD:` returns the last committed version or fails — the `--compare` deltas in the report are then inflated or unavailable, and the report is presented as literal evidence.
Proposed change: condition the fallback ("when the file had no uncommitted changes") or drop it in favor of saving the original.

**F6 (low, mechanical) — CHANGELOG's Unreleased section has no entry for the 6b6250c rulings.**
Evidence: CHANGELOG.md Unreleased stops at v0.3.2 ("default to less…"). The 6b6250c commit changed skill behavior — tripwire reframe, precedence order, short pass, numbered-step rule, MAR kinds, symptoms.py step semantics — while the version stayed 0.3.2 (hold is owner-ruled: "stop bumping until we are totally done").
Why it matters: version 0.3.2 now covers two different content states with nothing in CHANGELOG distinguishing them; a future entry writer working from CHANGELOG alone will miss half the changes.
Proposed change: add Unreleased bullets now (entry text doesn't require a bump), or a one-line note that 6b6250c's rulings ride under 0.3.2 pending the hold.

## Viability

Yes, an agent can follow it as written. The modes are concrete, the cut pass is enumerated with cross-references that resolve, the script is shippable with its estimates labeled, and the report shape is fully specified down to word ceilings. The one place an agent must guess is F3 (long chat replies). Stance rules ("pace by uncertainty", the copy-desk frame) are unverifiable individually but are deliberately paired with counted checks, so drift there is catchable. Silently-skipped candidates: step 8's "the mode's anti-patterns" is literal only for Mode 1 (Modes 2–4 carry their negatives as inline lists, not labeled anti-patterns — agents will generalize, but the reference is loose), and step 4 applies only to documents with preambles.

## Open design vs Mechanical work

Open (owner choices): F2 (short-pass step set — modifies a ruled list, with eval evidence for why); F3's boundary phrasing; nothing else rises to design.
Mechanical: F1 (recompute the ratio in summary.md + NOTES); F4 (HELP.md one-line fix); F5 (one clause); F6 (CHANGELOG bullets); plus one unnumbered nit — the zero-target list names "sentences over about 25 words" but omits "steps over about 20", while the rule and `symptoms.py` (long_steps) both enforce 20 for numbered steps; add the step count to the target sentence.

## Readiness by topic

- Coherence: ready — no surviving contradiction between word figures, lost-facts checks, over-cut guards, or mode vs. core; precedence resolves residual conflict.
- Followability: ready, with F3 as the one undefined branch.
- Fidelity to source and record: ready — every deviation from WRITING_DIRECTIVES.md I checked traces to a recorded ruling (hinge→preamble, budget→tripwire, commit style, lists/bold in chat); nothing inverted or overstated in the skill itself.
- Consumers: needs work — F4 (HELP.md); /start, copy-review.md, worked example, and symptoms.py all match.
- Evidence honesty: needs work — F1; everything else I could re-derive (worked-example counts, 45/46 arithmetic, blind-preference claims) checks out.
- Scope: ready — the long sections (STE rationale, What Does NOT Go, worked example) each carry a load; no cut I'd defend.

Weakest remaining assumption: that the always-on rules hold at generation time outside single-turn evals — the premise-test entry itself flagged "an editing pass tests the editor; the eval must test the author," and no multi-session evidence exists yet; this review is also a same-family pass in a chain whose independent stages have not run.
