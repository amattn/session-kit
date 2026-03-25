# SHARPEN.md
<!-- managed by /sharpen -->

Process observations that need active lifecycle tracking. Observations
start in NOTES.md; promote here when they need monitoring across sessions.
See /sharpen for detection sources, routing, and discipline creation.

## Open

### SPI_1: Extracted skills lose integration context from source project [drift]

Observed while comparing /fast-chat (session-kit) against the NL/NLR conventions in plet-skills (the source project). The plet-skills version works significantly better and more consistently because:

1. **Review discipline is chained, not standalone.** plet-skills has a 4-step flow: show content → surface recommendations → approval → notes + consistency pass. /fast-chat defines "show work, then recommend" as a principle but doesn't chain it into post-approval workflows.

2. **"Anything to add, change, or remove?" is a specific, battle-tested prompt.** /fast-chat generalizes this as "situational options + stable tail" — correct but less actionable. The specific wording is what agents actually follow.

3. **NLR is integrated with surrounding disciplines.** In plet-skills, NLR connects to Notes Discipline (capture the decision), Decision Discipline (cascade it), and Consistency Passes (verify it). /fast-chat extracted the communication layer but not the integration points.

**Pattern:** When extracting a skill from a mature project, the skill captures the *mechanics* but loses the *integration* — the connections to surrounding workflows that make the mechanics effective. The source project's conventions are load-bearing context that doesn't come across in generalization.

**Implications for other skills:** Worth auditing /stable-label and /sharpen for similar integration loss. /stable-label's consistency passes may work better in plet-skills because they're connected to Decision Discipline and Notes Discipline there.

**Potential fixes:**
- A. Skills could document their integration points ("pairs well with /notes for post-decision capture")
- B. /fast-chat could include the full review chain, not just the communication format
- C. Accept that extracted skills are lighter — the full integration lives in project-specific CLAUDE.md

### SPI_2: Zero-padded stable-label IDs in filenames vs single-grep rule [tension]

Zero-padding IDs (e.g., `REQ_003` instead of `REQ_3`) preserves lexical sort order in filenames — `ls` and file explorers show them in numeric order without special sorting. This is genuinely useful when stable-label IDs appear in filenames (e.g., `REQ_003_auth_flow.md`).

**The tension:** /stable-label's core promise is "one grep always finds the definition." `grep REQ_3` matches both `REQ_3` and `REQ_003` and `REQ_30` — but `grep REQ_003` only matches the padded form. If some references use `REQ_3` and others use `REQ_003`, the one-grep guarantee breaks. You'd need to know which form was used where.

**User instinct:** "zero padding is allowed when it makes sense, like in filenames to preserve lexical order."

**Considerations:**
- A. **Canonical form is unpadded, padding is display-only.** `REQ_3` is the ID everywhere (prose, cross-references, grep). Filenames can zero-pad for sorting (`REQ_003_...`) but the ID *in content* is always `REQ_3`. Grep the canonical form, filenames are a convenience layer.
- B. **Canonical form is padded from the start.** Choose a padding width at prefix creation time (e.g., 3 digits). All references use `REQ_003`. Consistent but: padding width is a guess (breaks at 1000), and early IDs look odd (`REQ_001`).
- C. **No padding anywhere.** Simplest rule, one form only. Sacrifice lexical filename order for zero ambiguity.
- D. **Per-prefix decision.** Some prefixes (especially file-oriented ones) get padding; others don't. Documented in the prefix table.

**Current NOTES.md guidance (from design decisions):** "zero-padded IDs optional guidance. Tradeoffs: two conventions (padded vs unpadded) + padding width is a guess. Let users decide." — this is correct but doesn't address the grep tension explicitly.


### SPI_5: /fast-chat review prompt layout doesn't match actual usage patterns [implemented]

The current review prompt design (SPI_3 proposed A/B/C/D/E for add/change/remove/rec/ok) is awkward in practice. Three problems:

1. **A/B/C (add/change/remove) are never used as letter codes.** In practice the user just says what they want: "add X, fix Y, remove Z." Giving them individual letter options collapses back to one action — the user types prose regardless. Letter codes don't help here.

2. **"Recommendations" is ambiguous.** Sometimes the agent presents recommendations at the bottom unprompted, and "D" gets interpreted as "implement the recommendations you already gave me." Other times "Recommendations" means "I'm asking you to give me recommendations." The direction of flow is unclear — is the user requesting recs, or accepting recs the agent already surfaced?

3. **The real usage patterns are two modes:**

**Mode 1 — Simple review:**
- Free-form add/remove/modify instructions (prose, not letter codes)
- Ask agent for recommendations
- Ok to approve

**Mode 2 — Recommendation-driven review:**
- Agent presents Rec 1 with A/B/C options
- Agent presents Rec 2 with A/B/C options
- ...
- Ask for more recs
- Ok to approve

In Mode 2, the letter codes *do* work — but they're scoped to each recommendation, not to the review as a whole. The user picks options within each rec, not across a flat A-E list.

**User quotes:** "ABC are never used in practice. instead i just say add this and fix that and remove that. they essentially get collapsed back to one thing." / "the UX for recommendations is vague. is it the user asking for recommendations? sometimes the agent presents recommendations at the bottom and thus D is interpreted as implement the recommendations you gave me."

**Supersedes SPI_3** — SPI_3 identified the symptom (rec not selectable). This identifies the structural issue (the flat A-E layout doesn't match how reviews actually flow).

**Stable tail for both modes:** Regardless of mode, every review ends with two fixed shortcuts:
- **R** — ask for (more) recommendations
- **O** — ok, approve

These are always the same, always at the bottom, always available. The variable part is everything above them — prose instructions in Mode 1, per-rec lettered options in Mode 2. The tail is stable; the body is flexible.

**S for "something else":** Instead of A/B/C for add/change/remove (which collapse to prose anyway), a single **S** — "something else" — covers all free-form input. The user types `S add a note about X` or just launches into prose. S signals "I have instructions that don't fit the presented options" without needing three separate letters for actions the user always describes in words.

**Full stable tail:** S (something else), R (more recs), O (ok approve). Always present, always last.

**Silence is not approval.** Very often the agent treats the first instruction (e.g., "add X") as the user's only input and implicitly approves the rest of the section. The default should be: after executing an instruction, re-present the item for further input. The review stays open until the user explicitly says O. This is the /fast-chat principle that "unanswered items stay open — silence is never treated as approval" but applied *within* a single review item, not just across items.

**User quote:** "very very often, the agent will take the first thing I do such as add this and while my intention is to continue working on this section it assumes ok approve after I add something. the default behavior should be not to approve until explicitly told."

**Action:** Redesign the review prompt around the two actual modes rather than a single flat option list. S/R/O as the stable tail. Silence-is-not-approval as a core rule.

**Live trial feedback (2026-03-23, GTC spec review in plet-skills — 16 sections, ~25 decision points):**

What worked well:
- **S/R/O tail is clean and fast.** Minimal cognitive load, easy to type/dictate.
- **Silence-is-not-approval** kept the review flowing — re-presenting after changes felt natural, not redundant. The user always knew where they were.
- **R producing NL-formatted recs** worked naturally when the user asked for it.
- **O implicitly accepts simple recs.** When the agent shows a small, obvious recommendation (e.g., "add GUI tools to JUS_2"), O naturally means "ok, including the rec." This was the most common case — ~70% of recs were simple enough that O covered them. No extra letter needed.

What needs work:
- **Non-trivial recs need an explicit accept code.** When the rec is substantial (e.g., "add three-tier exit codes"), O is ambiguous — does it mean "approve as-is without the rec" or "approve including the rec"? The user had to say "add that rec" or "do all those please" in prose. Candidate fixes: (a) add **Y** when a rec is displayed, (b) context-dependent O (O after a rec = accept rec, O without rec = approve as-is), (c) accept that prose is fine for non-trivial recs since they need confirmation anyway.
- **R → NL formatting isn't automatic.** When the user said "R", the agent sometimes gave prose recs instead of NL-formatted options. "R NL" or "R as options" worked but shouldn't be necessary — R in a review context should default to NL format.

**Emerging pattern:** Simple rec → O covers it. Non-trivial rec → user wants NL options to pick from, not just "accept/reject." The two modes from SPI_5 (simple review vs rec-driven review) map to these: simple recs stay in Mode 1 (prose + O), substantial recs shift to Mode 2 (per-rec NL options).

**Post-session analysis (2026-03-24):**

Reviewed all ~25 decision points. Revised findings:

1. **S is dead weight.** The user never typed S. Free-form input doesn't need a prefix — the user just says what they want. Prose is the default, not an option to select. Drop S from the tail.

2. **O has two natural meanings based on context:**
   - O *without* a displayed rec = "approve section as-is"
   - O *with* a simple displayed rec = "approve, including the rec"
   - This is not ambiguous — it's context-dependent and felt natural throughout the review. The user never had to clarify which meaning they intended for simple recs.

3. **Non-trivial recs shift to NL format naturally.** When the user wants to engage with a rec (not just accept/reject), they say "let's discuss" or "R" and the agent presents NL options. The transition is conversational, not structural. No extra letter code needed.

4. **R should always produce NL-formatted options in a review context.** Prose recs are less useful — the user wants to pick, not read a paragraph. This should be a rule, not a behavior the user has to request.

5. **The real stable tail is R/O, not S/R/O:**
   - **R** — give me (more) recommendations (always NL-formatted)
   - **O** — ok, approve (implicitly includes any displayed simple rec)

   Two codes, not three. Simpler is better.

6. **Silence-is-not-approval is the most important rule.** More important than the tail letters. It's what kept the review flowing and prevented the agent from racing ahead. This should be the headline rule for review prompts.

7. **Mode 1 vs Mode 2 distinction is less important than expected.** In practice, the review flowed between modes fluidly — simple sections got O, interesting sections got discussion or R, substantial recs got NL. The user didn't "choose a mode" — they just responded naturally and the agent adapted. The stable tail (R/O) works for both.

**Revised design:**
- Stable tail: **R/O** (drop S)
- R always produces NL-formatted options in review context
- O implicitly accepts simple displayed recs
- Silence is not approval (the core rule)
- Free-form input needs no prefix — just type

**Resolution (2026-03-29):** Implemented in /fast-chat v0.2.0. Final wording:
- **"R. Show me recommendations"** — chosen over "More recommendations" (implies prior recs exist) and plain "Recommendations" (ambiguous category label vs request). "Show me" is unambiguously a user request to the agent.
- **"O. Ok, approve"** — period-capitalized format for consistency
- **Silence is not approval** as the headline rule, positioned before the stable tail
- **Scoped to reviews** — "Do not attach it to informational answers or explanations" (eval 6 over-trigger)
- **Redundant summary section removed** — every bullet was a restatement
- **R example uses NL-formatted recs with A/B options** per recommendation, so batch syntax (1A, 2B) is valid
- User testing confirms the design is superior to the old A-E layout. Keeping `[implemented]` for continued monitoring.

## Resolved

### SPI_3: Review prompt recommendation is not a selectable option [superseded by SPI_5]

During section-by-section reviews, the agent produces a form like:

```
1. §7 Agent Flows
   A. ok as-is
   B. add/change/remove something

   REC: B — add AFL_4 for plan session milestone...
```

The recommendation is displayed but isn't selectable — there's no letter code to accept it or ask for more recommendations. The user sees the REC but has to rephrase it as a manual instruction rather than just picking a code.

**Expected stable tail:** The review prompt should have selectable options for the common actions:
- A. Add something
- B. Change something
- C. Remove something
- D or R. Accept recommendation (do what REC says)
- E or O. Ok as-is

This way batch responses work naturally: "1D, 2O, 3D, 4A add a note about X" — accept rec, ok, accept rec, add with details.

**Also missing:** a code to ask for *more* recommendations on an item — "I don't love the rec but I don't know what I want either, give me more options."

**User quote:** "the rec is shown but i can't easily select it. or ask for more recs."

**Not yet a pattern** — noted from a single review session. Promote to /fast-chat skill adjustment if this keeps surfacing.

**Resolution (2026-03-24):** Superseded by SPI_5, which identified the structural issue (flat A-E layout doesn't match actual review flow) and was implemented with the R/O tail design.

### SPI_4: /warmup escalation lacks concrete language-strengthening tactics [resolved 2026-03-24]

/warmup's escalation ladder says "tighten wording — make it shorter, bolder, more imperative" but doesn't give the agent concrete tactics for *how* to strengthen language. In practice, when a directive is being ignored or dropped after compaction, the fix is often mechanical:

- **Bold the directive** — `**Always do X**` survives compaction better than plain text
- **Use MUST/ALWAYS/EVERY TIME** — imperative qualifiers signal non-negotiable rules
- **Move from paragraph to standalone sentence** — short punchy rules resist summarization
- **Add redundancy** — repeat the rule in multiple places (CLAUDE.md + auto-memory + inline in the section it governs)

These are the actual moves a user or agent makes when strengthening wording. The current SKILL.md mentions the concept but leaves the agent to figure out the specifics. Adding a concrete "strengthening toolkit" to /warmup would make the escalation ladder actionable instead of aspirational.

**User quote:** "strengthen language make them bold or use stronger must always or every time kind of wording"

**Tension:** Prescriptive tactics risk mechanical over-application (bold everything, MUST everything). But vague guidance gets interpreted as "change a word or two" — which is why the escalation ladder isn't working. The advantage of agent discretion is situational awareness (don't bold what's already bold, pick the tactic that fits the gap). The disadvantage is that if agents were good at this judgment, /warmup wouldn't need to exist.

**Resolution (2026-03-24):** Added concrete tactics to warmup SKILL.md § Strengthening a rule. Framed as a toolkit ("pick the moves that fit the specific failure"), not a checklist. Added encouragement for the agent to try its own ideas when it has a better approach for the specific situation.

### SPI_6: /notes default section order doesn't match natural reading flow [resolved 2026-03-24]

The /notes SKILL.md "Suggested Starting Sections" lists Key Design Decisions first, followed by Invariants, Concepts, and Taxonomy. But after reorganizing session-kit's own NOTES.md, the better reading order is:

1. **Project Context** — what is this (already near top)
2. **Invariants & Critical Requirements** — non-negotiable rules, scan first
3. **Important Concepts & Insights** — principles and user values
4. **Taxonomy / Conventions** — canonical vocabulary
5. **Key Design Decisions** — the largest, most active section, grows into a log

**Rationale:** Invariants, concepts, and taxonomy are stable reference material — you scan them to orient yourself. Key Design Decisions is a growing log that can get very long. Putting the stable sections first means a new reader (or agent after compaction) gets the high-signal context before hitting the detailed decision history.

**Current SKILL.md order:** Key Design Decisions → Invariants → Concepts → Taxonomy (positions 1-4 of "most important")

**Proposed order:** Invariants → Concepts → Taxonomy → Key Design Decisions

**Also affects:** the bootstrap flow — when /notes creates a new NOTES.md, it should scaffold in this order. And the "float stale content down" guidance in § Size Management already supports this principle.

**Resolution (2026-03-24):** Updated /notes SKILL.md § Suggested Starting Sections to the new order. Project Context promoted to #1, Key Design Decisions moved to #5.
