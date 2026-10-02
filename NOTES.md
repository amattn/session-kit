# NOTES.md — session-kit

## Project Context

session-kit is a suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time. Extracted from patterns discovered during hundreds of sessions of plet-skills development. 8 skills total: `/notes`, `/warmup`, `/stable-label`, `/fast-chat`, `/dictation`, `/foo`, `/red-pen`, `/multi-adversarial-review`.

**Origin:** Extracted from patterns discovered during plet-skills development (`../plet-skills/`).

---

## Invariants & Critical Requirements

*(None yet)*

---

## Important Concepts & Insights

### From the user

- "should a skill be a noun or verb?" — led to the nouns-for-systems principle
- "label is more than the labels. it's stable references." — drove the /stable-label rename
- "i love that b rhymes, makes it memorable but maybe too cute?" → decided it's a feature, not a bug
- "i'm not worried about long. the claude code ui is awesome at autocomplete" — length of slash commands is not a concern; clarity and descriptiveness win
- "feedback foo is the least useful of the session kit tools in practice. the most useful are stable label, fast chat, and then small gap and then notes. and then a big gap and the rest." (2026-10-01) — ranking after months of real use. Pattern: the top three each produce a concrete artifact or format (IDs, codes, NOTES.md entries); the bottom tier is process/meta skills whose value is invisible when they work.
- "the baseline tends to be too wordy in general. that's part of the pain. i will ask for more detail if i need it." (2026-10-02) — after the blind review. Wordiness itself is the pain, not only unscannable length; the default is less, and detail is on request. Added to /red-pen's shared core.
- Fenced code blocks in README should be one command per block — GUI clients allow easy copy-paste of a whole fenced area, so combining unrelated commands in one block forces users to manually select

---

## Taxonomy / Conventions

### Skill roster (in progress — names under review)

| # | Current name | Status | Source |
|---|-------------|--------|--------|
| 1 | /notes | **Implemented** | Existing |
| 2 | /fast-chat | **Implemented** | EX_1 |
| 3 | /foo (was /sharpen) | **Implemented** | EX_2 + EX_4 |
| 4 | /dictation | **Implemented** | EX_3 |
| 5 | /warmup | **Implemented** | EX_5 |
| 6 | ~~/patterns~~ | Merged into /foo (was /sharpen) | EX_4 |
| 7 | ~~/discipline~~ | Folded into /warmup + /foo | EX_6 |
| 8 | /stable-label | **Implemented** | EX_7 |
| 9 | /red-pen | **Implemented** | WRITING_DIRECTIVES.md |
| 10 | /planner (name TBD) | Planned | plet-style planning |
| 11 | /multi-adversarial-review (alias: mar) | **Implemented**; `copy` target added 2026-10-02 | vog_kit |

---

## Key Design Decisions

### Suite scope and skill roster (2026-03-13)

Originally planned 7 extractable skills plus `/notes` (8 total). After merging /patterns into /foo (was /sharpen) and folding /discipline into /warmup + /foo, final count is 6 skills.

### Skill naming philosophy: nouns for systems, verbs for actions (2026-03-13)

Most skills in this suite are noun-shaped — they manage a system or artifact, not perform a one-shot action. `/notes` means "engage the notes system," not "take a note." Verb-form names (like `/mark`) undersell system-oriented skills by implying a one-shot action.

### Suite name: session-kit (2026-03-13)

Kept the original name. The suite name doesn't need to carry the value prop — the individual skill names already do that (`/fast-chat`, `/stable-label`, `/foo`). The suite name just says "here's a collection of session tools."

- **Rejected:** `/steady-session` — follows the [value]-[domain] pattern but feels ostentatious, "too much bragging." Promises a result rather than describing what the tool does.
- **Rejected:** `/session-craft` — aspirational but unnecessary weight
- **Chosen:** `session-kit` — neutral, modest, lets the skills do the branding

**Key insight:** Value-prop naming works for individual skills but not for the suite. Suite names should be modest containers; skill names should sell.

### /fast-chat naming (2026-03-13)

Renamed from `/chatux` (EX_1). The core value is speed — structured codes (1A, 2B, 3 with caveats) replace prose paragraphs, making communication dramatically more efficient.

- **Rejected:** `/chatux` — "ux" is jargon, doesn't convey the speed benefit
- **Rejected:** `/options` — names the mechanism (structured options) but misses the value prop
- **Rejected:** `/ask` — too vague
- **Rejected:** `/shorthand` — accurate mechanism name but doesn't convey speed
- **Chosen:** `/fast-chat` — mixes the value prop ("fast") with the domain ("chat"). Says exactly what it delivers.

**Key insight:** Skill names should mix the value proposition into the name, not just describe the mechanism. `/options` describes what you see; `/fast-chat` describes what you get.

### /sharpen naming (2026-03-13) — later renamed to /foo (2026-04-03)

Renamed from `/feedback` (EX_2). The skill tracks meta-observations about process and tooling, with resolution lifecycle and promotion paths. The value prop is process improvement, not just collecting feedback.

- **Rejected:** `/feedback` — implies feedback TO someone; these are self-observations about process. Also confusable with product feedback.
- **Rejected:** `/observe` — describes the mechanism, not the value
- **Rejected:** `/process-sharpen` — descriptive but artifact name (`PROCESS-SHARPEN.md`) reads like a command, not a document
- **Rejected:** `/process-tuning` — reads naturally but redundant within session-kit (every skill is about process)
- **Chosen:** `/sharpen` → `SHARPEN.md` — conveys value prop (your process gets sharper), bold artifact name, suite context provides the "process" framing

**Caveat:** "sharpen" isn't an obvious destination for users who think in terms of "feedback" or "meta-feedback." The skill definition will need strong trigger words covering those synonyms. If SHARPEN.md sees low adoption, may need more user-facing guidance to connect the concept. Monitor this.

### /stable-label naming (2026-03-13)

Renamed from `/label` (EX_7). The skill is more than labels — it's a system for stable, greppable cross-references that never renumber and always resolve to exactly one definition. The labeling is the mechanism, but the value is the reference system.

- **Rejected:** `/label` — accurate for the mechanism but misses the "stable references" value
- **Rejected:** `/tag` — implies categorization (like git tags), leans verb
- **Rejected:** `/id` — too specific to the artifact format, not the system
- **Rejected:** `/ref` — accurate but doesn't convey the stability guarantee
- **Rejected:** `/ref_ids` — too specific, underscore in command name unusual
- **Chosen:** `/stable-label` — self-documenting ("the labels are stable"), memorable rhyme is a feature not a bug. User: "i love that b rhymes, makes it memorable"

### /notes eval findings and adjustments (2026-03-14)

Ran 10 eval pairs (with-skill vs baseline) on /notes. Key findings:

**Biggest differentiator:** Bootstrap — CLAUDE.md + discipline block is the killer feature. The baseline creates a reasonable NOTES.md but nothing persists the behavior to future sessions.

**Second differentiator:** User quotes. The skill consistently captures the user's exact words; the baseline paraphrases. User preference: quote the user, paraphrase everything else (agent reasoning, conversation context, rationale, rejected alternatives).

**Non-discriminating tests:** Add-a-note, implicit decisions, near-miss questions, and multi-decision bursts all performed similarly with and without the skill. Claude is already good at these — the skill doesn't need to over-specify them.

**Adjustments made:**
- Added "Where /notes Adds Value" section — focuses the skill on its unique value (discipline, structure, quotes) rather than things Claude handles well natively
- Strengthened quote guidance: "Quote the user, paraphrase everything else" — user's voice should stand out from surrounding summary
- Bootstrap now seeds Open Questions from project context (the with-skill bootstrap was emptier than baseline on this)
- Bootstrap step 5 (CLAUDE.md discipline) marked as "the most important step"

### /warmup eval findings and adjustments (2026-03-14)

Ran 9 eval pairs on /warmup. Key findings:

**Full layered infrastructure is the differentiator.** The baseline handles individual concepts (compaction recovery, required reading) but doesn't build the complete system (Required Reading + canaries + post-compaction rule + breadcrumbs + auto-memory guidance) as integrated infrastructure.

**Eval 6 over-trigger.** The skill's proactive description caused it to bootstrap warmup on an unrelated "add an endpoint" request. Fixed by removing proactive bootstrap triggers and adding explicit "Do NOT proactively bootstrap when the user is asking about something unrelated."

**Baseline innovations adopted:**
- Cross-file reinforcement loop (eval 3 baseline): CLAUDE.md and NOTES.md point to each other, creating mutual recovery after compaction. Added as a /warmup tactic.
- Content quality diagnosis (eval 4 baseline): checking wording motivation, edge case handling, and cost framing — not just infrastructure. Added to diagnostic checklist.

**AGENTS.md creation is unique to the skill (eval 8).** Baseline never created AGENTS.md for cross-platform compatibility.

**Baseline was surprisingly creative on strengthen/diagnose (evals 3-4).** The two-file reinforcement loop and content-specific diagnosis were insights the skill didn't produce. The skill was more systematic; the baseline was more creative. Both innovations now incorporated into the skill.

### /warmup design decisions (2026-03-14)

**Scope:** /warmup uses every tactic available to make skills load reliably at session start and after compaction. It's not just a CLAUDE.md helper — it's the reliability layer.

**Three jobs:**
1. Bootstrap CLAUDE.md with compaction-resistant wording, Required Reading, and discipline blocks
2. Loading canaries — verification that files were actually consumed, not just referenced
3. Reliability guidance — strategies for when system prompts or compaction fight CLAUDE.md directives

**Tactics** (use whatever works):
- CLAUDE.md wording and structure (discipline blocks, Required Reading sections)
- Auto-memory entries for non-negotiable behaviors (strongest tactic — loads before CLAUDE.md)
- Loading canaries for verification
- Breadcrumbs in CLAUDE.md (e.g., `<!-- managed by /warmup -->`) so users know what /warmup created and can invoke it to add/edit more

**Visibility model:**
- At runtime: canaries and discipline blocks do the talking. No splash screen.
- In CLAUDE.md: breadcrumbs marking /warmup-managed sections so users discover the skill organically.

**Mid-session compaction role:** auditor, not executor. The Post-Compaction Rule handles re-reading files. /warmup checks whether the rule exists and was followed, flags issues, offers to strengthen. Does not re-read files itself.

**Agent Harness Reference:** extracted to `references/harnesses.md` to keep SKILL.md lean and make the reference independently updatable. Covers Claude Code, Codex CLI, OpenCode, Cursor. Cross-platform strategy: AGENTS.md as single source of truth, strongly direct Claude Code to read it.

**Description pushiness:** per skill-creator best practices, description includes proactive triggers — fresh session with no canary, compaction detected mid-conversation, project with directive files but no loading structure.

### /stable-label eval findings and adjustments (2026-03-14)

Ran 11 eval pairs on /stable-label. Key findings:

**Convention enforcement is the biggest win.** Baseline invents its own format — kebab-case, dashes, zero-padding (`[DB-POSTGRES]`, `DEC-001`). The skill enforces `XXX_N` consistently.

**Over-assignment problem (eval 4).** When asked "list the top 5 features," the skill assigned FEA_1-FEA_5 and created a new prefix — but this was a brainstorm, not a commitment. Permanent append-only IDs on exploratory content creates orphans.

**Fix: read/analyze vs create/modify heuristic.** Read/analyze operations (list, summarize, explore) produce responses — no IDs. Create/modify operations (add, decide, commit) produce artifacts — assign IDs. Added "When to assign IDs — and when not to" section with examples.

**Deprecation lifecycle is a genuine differentiator.** The skill's tombstone pattern (REQ_5 deprecated with pointer to DEC_6) is more principled than baseline strikethrough.

**Token savings hypothesis (unconfirmed).** Eval 8 showed the with-skill run used MORE tokens (richer output). But the hypothesis is about long-term downstream savings (grep `REQ_3` vs restating the full requirement), not single-eval token counts. Worth monitoring in real multi-session usage.

**Non-discriminating tests.** Assign ID (eval 1), cross-reference (eval 6), implicit ID (eval 10), and show existing convention (eval 5) all performed similarly — when the convention already exists, Claude follows it fine without the skill.

**Lifecycle operations are the strongest differentiator (evals 11-14).** Every lifecycle test showed meaningful skill advantage:
- Split (eval 11): skill adds provenance notes ("split from REQ_3") + consistency pass; baseline omits both
- Merge (eval 12): skill keeps retired ID as tombstone redirect (DEC_4 still greppable); baseline absorbs into merged entry, losing standalone entry
- Promote (eval 13): skill creates bidirectional cross-references (OBS_1 ↔ REQ_4) + consistency pass; baseline does one-way pointer
- Crosscutting (eval 14): skill creates domain-specific faceted IDs (API_1, DBA_1) cross-referenced with REQ_5; baseline adds prose to REQ_5 without domain IDs

### /foo (was /sharpen) eval findings (2026-03-14)

Ran 8 eval pairs on /sharpen. **First skill where the eval confirmed the design rather than revealing problems.** No adjustments needed.

**Important caveat:** These evals test /sharpen's infrastructure and methodology (routing, discipline creation, escalation), NOT proactive pattern detection. Detection — the agent noticing patterns without being told — is the highest-value capability and can only be validated through real multi-session usage.

**Strongest differentiators (evals 5-6):** When told about recurring failures, the skill treats them as process improvement opportunities — creates observations, strengthens disciplines, flags prose→tooling escalation. The baseline just apologizes and offers to fix the immediate problem. This is the core /sharpen value.

**Routing works (eval 2).** The skill correctly routed a project decision to NOTES.md + CLAUDE.md and explicitly reasoned that SHARPEN.md should not be touched.

**`[escalated]` annotation emerged naturally (eval 6).** The skill used `[escalated]` as a status within the open state — not a formal lifecycle state, but an acceptable annotation. Similarly `[reopened]` in the test data. These annotations within the two-state model (open/resolved) are fine practice without adding formal states.

**Baseline's four-stage lifecycle (eval 0) was interesting but unnecessary.** Baseline invented observed→validated→discipline→retired. Our two-stage model is simpler and sufficient — observation bodies capture confirmation context without a separate state.

**No baseline innovations to adopt.** Unlike /warmup, the baseline didn't produce creative approaches worth incorporating.

### /stable-label design decisions (2026-03-14)

**Convention:**
- Three-letter prefixes default (`XXX_N`), two-letter acceptable when unambiguous
- Underscore separator — greppable + double-click selectable
- Append-only, never renumber, never reuse
- Full prefix required — shorthand strictly forbidden (FOO_7)

**Prefix table location:** convention rules (behavioral directives) go in AGENTS.md and/or CLAUDE.md; prefix table (living reference data) goes in NOTES.md under Taxonomy / Conventions. Split because rules are directives, the table is reference data.

**Consistency passes:** defined as suggested approaches at different scales (Quick, Standard, Sweep, Structural), not rigid levels. Other skills can follow the guidelines independently — /stable-label doesn't police them.

**ID Lifecycle:** five patterns — splitting, merging, deprecation, promotion, crosscutting. All follow the same principle: retired IDs always resolve to meaningful content. Light guidelines, not hard rules — agent judgment is sufficient in most cases.

**Crosscutting:** when a concern spans multiple domains, each domain gets its own ID with domain-relevant content. Not duplicates — different facets. Cross-reference between them.

**Filenames:** zero-padded IDs optional guidance. Tradeoffs: two conventions (padded vs unpadded) + padding width is a guess (breaks at 1000). Let users decide.

### Value-add context belongs in README, not in skills (2026-03-14)

After /notes and /dictation evals, we added "Where X Adds Value" sections to each skill describing what the skill does better than baseline Claude. Removed them after realizing two problems:

1. **Dilution risk** — telling the agent "Claude already handles X well natively" could cause it to deprioritize the skill's instructions. The skill-creator explicitly warns about undertriggering; a preface that says "the baseline is fine" works against that.
2. **Wrong audience** — eval findings are development insights for humans deciding whether to install, not behavioral instructions for the agent. Skills should confidently tell the agent what to do.

**Chosen:** move value-add context to README per-skill descriptions ("What it adds over baseline Claude" paragraphs). Skills stay lean and confident. Eval findings stay in NOTES.md as institutional memory for future development.

### /dictation eval findings and adjustments (2026-03-14)

Ran 8 eval pairs on /dictation. Key findings:

**Biggest differentiator:** Bootstrap format — skill puts the table in CLAUDE.md with breadcrumb. Baseline created a YAML file in an ad-hoc location. Format matters because CLAUDE.md is loaded every session.

**Second differentiator:** Structured disambiguation. When input was garbled beyond the table (eval 2) or ambiguous in context (eval 6, "Maine" in a logistics project), the skill presented lettered options. Baseline guessed without asking.

**"What Does NOT Go" works:** Eval 5 showed the skill correctly reasoning that k8s/img are abbreviations, not correction table entries. The boundary is load-bearing.

**Non-discriminating tests:** Silent correction (eval 1), learning loop (eval 3), one-off typo (eval 4), and existing table (eval 7) performed similarly with and without the skill.

**Adjustments made:**
- Added "Where /dictation Adds Value" section — bootstrap format, structured disambiguation, boundary clarity
- Pattern matches /notes eval: infrastructure and edge cases are the unique value, not single-shot behavior

### /dictation design decisions (2026-03-14)

**Scope broader than the name:** /dictation covers voice-to-text errors (primary use case), recurring typos, and emergent shorthand (like "1b1" for one-by-one). Kept the name because voice input is still the core value — the broader scope is noted in the intro and README rather than reflected in the name.

**Seed table focus:** Bootstrap should emphasize project-specific jargon over common tech terms. JSON/API/CLI are usually recoverable without a table — the value is in project names, internal tools, and compound terms voice engines split.

**Silent correction with a safety valve:** Most corrections applied silently. But when a correction changes meaning in a way that affects the action taken (e.g., "Maine" → "main"), briefly confirm.

### /fast-chat eval findings (2026-03-14)

Ran 8 eval pairs on /fast-chat. Key findings:

**Behavioral activation is the primary value.** The baseline had identical CLAUDE.md conventions but didn't follow them (evals 4, 5). The skill makes Claude *act* on the patterns, not just know about them. This suggests the skill's value isn't the patterns themselves (Claude knows them) — it's the activation energy to consistently apply them.

**Strongest differentiators:**
- Single question → letters only + stable tail (eval 4): skill structured, baseline answered in prose
- Open-ended avoidance (eval 5): skill used NL-style clarifying options, baseline asked open-ended questions despite CLAUDE.md saying not to
- Review prompt structure (eval 3): skill used situational + stable tail, baseline gave suggestions without structure

**Eval limitation: eval 6 (informational over-trigger).** The with-skill agent appended a review prompt to a pure informational answer ("explain how FastAPI handles async"). This has never been observed in actual usage — likely an artifact of single-turn eval stripping conversational context. In real sessions, the agent has enough context to know when a review prompt is appropriate. Noted under Things to Monitor rather than adjusted in the skill.

**Compounding value.** The per-interaction savings from structured options over prose are small — seconds per decision. But across hundreds of decisions per session and hundreds of sessions per project, those seconds compound tremendously. The skill's value isn't visible in a single eval; it's in the cumulative time saved across the project's lifetime.

**Non-discriminating when conventions exist:** When CLAUDE.md already had interaction conventions (evals 1, 2, 7), both with-skill and baseline followed them. The skill's bootstrap value is in creating those conventions; once they exist, the gap narrows.

### /fast-chat design decisions (2026-03-14)

**Standard review prompt structure:** The review prompt has two parts — a variable number of situational options (could be 2, 3, 4, whatever fits) adapted to context, followed by a stable tail (Recommendations + Ok) that appears in nearly every review. The situational options default to Add/Change/Remove for artifact reviews, but the count and content change per situation. The stable tail is always the last two letters, regardless of how many situational options precede them.

**Always-on framing:** /fast-chat is an always-on communication style, not just a bootstrap tool. The patterns should be adopted immediately in every interaction where decisions are being made — no explicit invocation required. Invoking `/fast-chat` runs bootstrap (persists conventions to AGENTS.md/CLAUDE.md), but the behavior is immediate.

**NLR formats:** Two common formats identified so far — inline marker (`← recommended`) and rationale paragraph at the end — but these aren't exhaustive. Other formats may emerge. NLR (agent proactively marking its pick when presenting options) is explicitly distinguished from the review prompt's "Recommendations" option (user asking the agent to surface concerns after seeing work). Different direction of flow.

**Patterns are grouped, not counted:** Originally "10 patterns," reduced when "fenced code blocks" folded into NL as a formatting rule, and the review prompt was promoted to its own top-level section. The mechanics/principles grouping does the organizational work — the exact count doesn't matter.

### Disciplines: prose first, tooling when prose drifts (2026-03-14)

From EXTRACTABLE.md EX_6 and PLET.md § "Skills for Judgment, Code for Compliance": disciplines are prose-based, and prose is re-interpreted each invocation — it drifts. When a prose discipline keeps getting violated (especially format compliance, schema rules, consistency checks), supplement with tooling (validation scripts shipped in `scripts/`). Escalation pattern: prose first → if agents drift → build a tool. Not every discipline needs this — most won't — but /foo should recognize when prose alone isn't working. /warmup's canaries are already an example of this pattern — prose says "load these files," canaries verify it happened. /stable-label's consistency passes are the most likely candidate for future tooling (a validation script enforcing no-duplicate-definitions, no-orphaned-references, no-renumbered-IDs). No tooling gaps are urgent yet, but /foo should recognize these patterns when drift appears.

### Skill scripts: allowed-tools and portability (2026-03-14)

Skills can ship scripts in `scripts/` and pre-approve them via `allowed-tools` in SKILL.md frontmatter — eliminates permission prompts. `${CLAUDE_SKILL_DIR}` resolves to the skill's install location regardless of where it's installed (personal, project, plugin).

**Portable approach for Python scripts:** use path-based allowed-tools rather than language-based. `Bash(${CLAUDE_SKILL_DIR}/scripts/*)` approves only shipped scripts regardless of whether the system calls it `python` or `python3`. Scripts use `#!/usr/bin/env python3` shebangs and `chmod +x`. This is cleaner and more secure than `Bash(python *)` which would approve arbitrary python commands.

**`python3` is the safe shebang.** On all modern systems that ship Python, the `python3` binary exists (macOS, Ubuntu, Fedora, Homebrew). The plain `python` binary is increasingly absent — removed from macOS 12.3, no default in Fedora since 26, intentionally not symlinked by Homebrew. PEP 394 recommends `python3` for scripts that require Python 3. `#!/usr/bin/env python3` is the right choice.

No scripts needed in session-kit yet, but when /stable-label consistency passes or other enforcement tooling is warranted, this is the pattern to follow.

### CLAUDE.md prose drift: Before You Commit and cascade (2026-03-14)

**Observed:** PLAN.md and CHANGELOG.md drifted during the plugin bundle work — the bundle was committed without updating either. Caught during a consistency pass, not during the commit.

**Root causes:**
1. Before You Commit was positioned at the bottom of CLAUDE.md — last section, deprioritized under task pressure
2. Language was suggestive ("check if") not imperative ("update")
3. PLAN.md and CHANGELOG.md were removed from the Decision Cascade as "bookkeeping" — which meant they weren't in the checklist the agent scans

**Fix applied:** moved Before You Commit above Versioning, made language imperative, added PLAN.md and CHANGELOG.md back to Decision Cascade. This is exactly the escalation pattern /warmup teaches: tighten wording → improve positioning → add redundancy.

**Meta-observation:** this is session-kit's own process eating its own dogfood. The cascade and before-you-commit disciplines are the same pattern /warmup and /foo teach to users. When they drifted in our own project, we applied the same fix the skills recommend.

### /foo (was /sharpen) detection sources (2026-03-14)

Detection sources are broader than just NOTES.md scanning. Five sources: conversation patterns (repeated corrections, consistent preferences), user interaction style (terse answers, shorthand, frustration signals), agent self-observation (own mistakes, inefficient workflows), project artifacts (git history, directive drift, code review comments), and cross-session signals (prior NOTES.md, recurring FEEDBACK_FOO.md entries, stale auto-memory). NOTES.md remains the single intake *destination* for writing observations down, but these are the *inputs* that feed detection.

### /patterns merged into /foo (was /sharpen) (2026-03-14)

Merged /patterns (EX_4) into what was then /sharpen (EX_2), now /foo. Both skills deal with process improvement — /patterns detects recurring patterns proactively, /foo tracks process observations with a resolution lifecycle. The user shouldn't have to choose between them when thinking "this process thing should be captured."

**Merged skill features:**
- Proactive detection ("I've seen this twice") — from /patterns
- Resolution lifecycle (open → resolved) — from /foo (was /sharpen)
- Promotion paths (→ CLAUDE.md, → NOTES.md) — from both
- Discipline creation ("express this as a named discipline") — from /patterns

**Name** was /sharpen at the time of this merge, later renamed to /foo (2026-04-03).

**Artifact:** `FEEDBACK_FOO.md` (was `SHARPEN.md`) — observations with IDs, lifecycle states, and promotion paths.

**Result:** 6 skills total instead of 7.

### /discipline folded into /warmup + /foo (was /sharpen) (2026-03-14)

Dropped /discipline as a standalone skill. Its responsibilities split across two existing skills:

- **/warmup** gets the **format and enforcement** — discipline block structure (scannable, enforceable, composable), writing blocks into AGENTS.md and/or CLAUDE.md, loading and verifying via Required Reading and canaries
- **/foo** (was /sharpen) gets the **detection and creation** — recognizing "this workflow should be a discipline," helping users express informal habits as named disciplines, the meta-pattern of identifying what needs formalization

Individual skills (like /notes) create their own discipline during bootstrap, proving no separate /discipline skill is needed.

- **Rejected:** standalone /discipline skill — too much overlap with /warmup (format, enforcement) and /patterns (detection)
- **Chosen:** split across /warmup (infrastructure) and /foo (recognition)

### /fast-chat review prompt redesign (2026-03-24)

Redesigned the standard review prompt based on live trial feedback from a 16-section, ~25-decision-point spec review (FOO_5). The old A-E layout (Add/Change/Remove/Recommendations/Ok) didn't match actual usage.

**Key findings:**
- A/B/C (add/change/remove) are never used as letter codes — users just type prose instructions
- "Recommendations" was ambiguous — unclear if user is requesting recs or accepting displayed recs
- S ("something else") was dead weight — never used in trial

**New design:**
- **Stable tail: R/O** — "R. Show me recommendations" and "O. Ok, approve"
- **"Show me recommendations"** wording chosen over "More recommendations" (implies prior recs) and plain "Recommendations" (ambiguous — category label vs request). "Show me" is unambiguously a user request to the agent.
- **Silence is not approval** — the headline rule. Re-present after every change until explicit O.
- **O implicitly accepts simple recs** — context-dependent and natural
- **Free-form input needs no prefix** — just type instructions
- **R always produces NL-formatted options** in review context — prose recs are less useful
- **Scoped to reviews** — do not attach the review prompt to informational answers or explanations (eval 6 flagged over-triggering on these)

**Rejected:** S/R/O tail (S dropped after trial showed it was never used). Rejected: separate "Y" code for accepting recs (O covers simple recs; non-trivial recs get discussed via prose or NL options). Rejected: redundant summary section at end of review prompt — every bullet was a restatement of what's already explained above.

### /warmup language-strengthening tactics (2026-03-24)

Added concrete tactics to the escalation ladder's "tighten wording" step (FOO_4). The original guidance ("make it shorter, bolder, more imperative") was too vague — agents interpreted it as "change a word or two." Now includes specific moves: bold directives, imperative qualifiers (MUST/ALWAYS/NEVER), standalone sentences over paragraphs, cost framing, remove hedging. Framed as a toolkit to pick from ("pick the moves that fit the specific failure"), not a checklist — with explicit encouragement for the agent to try its own ideas.

### /notes default section order (2026-03-24)

Reordered "Suggested Starting Sections" to put stable reference material before the growing decision log (FOO_6). New order: Project Context → Invariants → Concepts → Taxonomy → Key Design Decisions. Rationale: a new reader or agent recovering from compaction gets high-signal orientation context before hitting the detailed (and often very long) decision history. Session-kit's own NOTES.md already follows this order after a reorg.

### `publish:` prefix for distribution commits (2026-04-03)

Added a `publish:` prefix exception to the verb-first commit style. Distribution commits (version bumps, marketplace releases) were hard to spot in `git log` — they looked identical to routine updates. The prefix makes them scannable via `git log --grep="^publish:"`. Releases also get a `git tag v<version>`. Inspired by plet-skills' noun-prefix commit convention, but only adopted for distribution — the verb-first style stays for everything else.

### Versioning section strengthened in CLAUDE.md (2026-04-03)

Ported patterns from plet-skills' SemVer Discipline: timing rule ("bump when you change, not later"), "what to bump when" table, "where versions live" table, "distribution versions are human-directed only" rule, and "don't forget" multi-location checklist. The existing section had the version definitions but lacked the operational discipline that prevents drift.

### /warmup bootstraps project scaffolding files (2026-05-27)

/warmup now creates `.gitignore` and `.claude/settings.json` when they don't already exist. The framing: these aren't loading mechanisms themselves but materially affect how reliably session-kit operates across the project's lifetime — `enabledPlugins` ensures session-kit loads for any collaborator, the permissions allowlist reduces prompt friction so sessions actually flow, and the privacy/quiet defaults match how most session-kit users want Claude Code to behave.

**Defaults chosen:**
- `.gitignore` — single entry `.DS_Store`. Other common ignores (`settings.local.json`, `CLAUDE.local.md`) are intentionally not added; that's the user's call.
- `.claude/settings.json` — `permissions.allow` covers read-file Bash (`cat`/`head`/`tail`), read-only git (`status`/`log`/`diff`/`show`/`blame`), and `grep`. Plus `includeCoAuthoredBy: false`, `env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1"`, and `enabledPlugins: { "session-kit@session-kit-marketplace": true }`.

**Never touches existing files.** If `.gitignore` or `.claude/settings.json` already exists, /warmup skips it entirely — no read, no offer to merge, no surfacing missing keys. Existing files are the user's domain; /warmup only acts when the file is absent. Avoiding the offer-to-edit path keeps the bootstrap predictable and prevents /warmup from sprawling into a general settings.json maintenance tool.

**Rejected alternatives:**
- Mirror this repo's full `.gitignore` (`settings.local.json`, `CLAUDE.local.md`) — too opinionated for a starter; users vary
- Mirror this repo's settings.json (broad git write permissions like `git add`/`git commit`/`git checkout`) — write permissions deserve explicit user thought, not silent grants

**Version bump:** /warmup 0.1.2 → 0.2.0 (new bootstrap step + new Tactics subsection = MINOR).

### /session-kit:start invokes sub-skills via the Skill tool, not Read (2026-05-27)

The initial `/session-kit:start` SKILL.md (v0.1.0) had a § "Delegation to Sub-Skill SKILL.md Files" section that said /start "reads the sub-skills' SKILL.md files and follows their bootstrap sections." That's the wrong mechanism — it bypasses Claude Code's skill-loading machinery, fires a Read-tool permission prompt, and pulls SKILL.md in as a regular file read instead of a system reminder.

**Fix:** section renamed to § "Invoking Sub-Skills via the Skill Tool." /start now activates each sub-skill via `Skill(skill: "warmup")`, `Skill(skill: "notes")`, etc. — that's the proper mechanism. The exact invocation name comes from the runtime available-skills list (plain `name` for personal skills, `plugin:name` for plugin-namespaced ones — for session-kit users, typically `session-kit:warmup` etc.).

**Why:** the Skill tool is what makes sub-skills usable. It loads SKILL.md as a system reminder, threads it into the conversation correctly, and doesn't require an out-of-band permission prompt. Reading SKILL.md as a regular file is a category error.

**Reinforced wording:** "Do not use the Read tool on `skills/<name>/SKILL.md` to look up sub-skill behavior. Sub-skills are activated, not read." The bold negative directive is intentional — agents have already shown the wrong instinct here.

**Cascade:** Bootstrap Order intro now points to § Invoking Sub-Skills via the Skill Tool; § What Does NOT Go entry updated to reference Skill-tool activation; Bootstrap Order step 2 updated (after the template inlining decision below).

**Version:** No bump needed — folded into the same release as the initial /start v0.1.0 work. The Skill-tool delegation rule supersedes the prior Read-the-SKILL.md framing *before* the next publish, so there is no separate patch number to assign.

---

### /notes template inlined into SKILL.md; assets/ folder removed (2026-05-27)

User: *"I want to move the template into the skill and remove it from the assets folder. I don't like that it needs to ask permission. the skills should be as self contained as possible."*

Removed `skills/notes/assets/notes-template.md` and inlined the full template into `skills/notes/SKILL.md` under a new § NOTES.md Template → § Template content sub-section. The template content sits inside a fenced markdown block; the bootstrap writes NOTES.md by substituting `{{PROJECT_NAME}}`, `{{DATE}}`, and `{{PROJECT_DESCRIPTION}}` as it writes, never reading an external file.

**Why:** when /notes ran as part of /session-kit:start, reading the assets file fired a Read-tool permission prompt mid-bootstrap. With the template inlined, the Skill-tool invocation already brings it into context — no extra read, no permission prompt, no risk of the file being missing. The principle is broader than this one skill: **skills should be self-contained** so loading the skill loads everything the skill needs to do its job.

**Tradeoff acknowledged:** SKILL.md grows by ~140 lines. Acceptable — the template is consumed every time /notes bootstraps, so in-context is the natural place for it. Self-containment > marginal context savings.

**Cascade:**
- /notes Bootstrap step 1 rewritten to write inline content rather than copy a file
- § "Default Template" renamed to § "NOTES.md Template"; new § "Template content" sub-section holds the literal template inside a four-backtick fence (preserving inner triple-backtick fence safety)
- /start SKILL.md Bootstrap Order step 2 reworded — drops `assets/notes-template.md` reference, says "writes NOTES.md … from /notes' inline template"
- `skills/notes/assets/` directory removed entirely
- CHANGELOG entry for the next release will describe the inline template (the asset-file line was reverted locally; PLAN.md → Next publish lists the wording to use)

**Rejected alternative:** keep the asset file but suppress the permission prompt via `allowed-tools` in SKILL.md frontmatter. Rejected because the user's framing is principled — self-containment is the goal, not just permission-prompt suppression. An inline template also can't go missing or get out of sync with the SKILL.md that references it.

**Version:** No bump needed — folded into the same release as the initial /notes v0.2.0 template-driven bootstrap work. The inline template supersedes the asset-file approach *before* the next publish, so /notes v0.2.0 ships with the template inlined from the start (no intermediate v0.2.1).

---

### /warmup settings.json: propose, never automatic; eligible when near-empty (2026-05-27)

The original /warmup 0.2.0 rule was blanket skip-if-exists for `.claude/settings.json`. That broke the marketplace-install flow: when a user enables session-kit through Claude Code's plugin UI, the harness writes `.claude/settings.json` with just an `enabledPlugins` entry. The file *exists*, so /warmup's blanket skip never adds the permissions allowlist, privacy defaults, or env entries — the very things /warmup is supposed to set up. The "user's domain" framing was right in spirit but missed this real-world chicken-and-egg.

User: *"clause settings changes should not be automatic. if the settings is empty or only contains the enabledPlugins, then warmup should propose the additions. user can approve all or some."*

**New rule** — applies *only* to `.claude/settings.json`; `.gitignore` keeps its blanket skip-if-exists (marketplace install doesn't auto-create one, so the failure mode doesn't apply):

- **Eligible for proposal** — file missing, empty (`{}` or zero-byte), OR contains only `enabledPlugins`. The last case is the marketplace-install shape — *the file exists but isn't user-curated.*
- **Not eligible — leave alone** — file has any other content. Treat it as the user's domain.
- **Proposal is multi-select.** /warmup uses /fast-chat NL form with four options (A: permissions.allow, B: includeCoAuthoredBy, C: env, D: enabledPlugins). User picks all / some / none. Apply additively — never overwrite any value the user already has.
- **Never automatic.** Even when the file is missing, /warmup proposes rather than auto-creating. This was the user's stated headline rule: "settings changes should not be automatic."

**Why not just detect the marketplace-install shape via a flag/marker?** No reliable marker exists (the harness doesn't tag its writes). The shape heuristic (only `enabledPlugins`) is fragile but observable; the user accepts the brittleness in exchange for keeping settings.json writes out of the silent-automatic path.

**Cascade:**
- /warmup SKILL.md § Project Scaffolding Files: intro rewritten to call out the asymmetry (`.gitignore` skip vs. `.claude/settings.json` propose); § `.claude/settings.json` subsection completely rewritten with eligibility states, proposal format, additive-merge semantics
- /warmup SKILL.md Bootstrap step 2: summary updated to point at the new rule
- /warmup HELP.md Setup section: rewritten to reflect propose-multi-select for settings.json
- /start SKILL.md: no change — /start invokes /warmup via the Skill tool, so it picks up the new behavior automatically. The "one approval" model now has a sub-proposal when settings.json is eligible; this is the right tradeoff (settings choices deserve explicit consent, not a silent rollup).

**Rejected alternatives:**
- *Additive merge, automatic* — rejected because it violates the user's "never automatic" rule for settings.
- *Additive merge with one yes/no confirm* — rejected because the user explicitly wanted "approve all or some," i.e., per-option granularity rather than a single accept/reject.
- *Special-case only the marketplace shape; keep blanket skip otherwise* — too narrow (breaks the moment a user adds one other key) and doesn't match the user's broader "settings should not be automatic" principle. The propose-when-eligible rule covers both cases under one principle.

**Version:** No bump needed — folded into the same release as the initial /warmup v0.2.0 scaffolding work. The propose-multi-select rule supersedes the skip-if-exists rule for `.claude/settings.json` *before* the next publish, so /warmup v0.2.0 ships with the corrected semantics from the start (no intermediate v0.2.1).

---

### /sharpen renamed to /feedback-foo (2026-04-03)

"Sharpen" was too conceptual — users naturally say "add an observation" or "add a feedback item," not "sharpen this." The monitoring note from the original naming decision proved correct: the name wasn't intuitive for the "feedback" mental model.

**New name:** `/feedback-foo` — FOO = Feedback, Observation, Oversight. A bucket concept for items observed in the wild that need triage or action. The `foo` metavariable reference is intentional and easy to disambiguate in context.

- **Aliases:** `/foo`, `/feedback`, `/observation` — all four invoke the same skill
- **Artifact:** `SHARPEN.md` → `FEEDBACK_FOO.md`
- **Item prefix:** `SPI_N` → `FOO_N`
- **Directory:** `skills/sharpen/` → `skills/feedback-foo/`
- **Primary name swap:** initially chose `/foo` as primary, then swapped to `/feedback-foo` — eval 0 baseline showed that "foo" alone is opaque (baseline agent didn't know what it meant). `/feedback-foo` is self-documenting while `/foo` stays as the quick alias.
- **`/observation` alias:** added because "add an observation" is the other natural verb alongside "add a feedback item"

---

### Writing directives skill: new skill, not a fold (2026-10-01)

Source: `WRITING_DIRECTIVES.md` (user's standalone file). Inspiration: Ayman Nadeem, "Plan Mode Is Dead" — https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html. Attributed in README § Origin, alongside the Ralph attribution for /fast-chat. Thesis: AI text is painful because it is unedited — nothing filters it. The file substitutes explicit constraints (word budgets, named reader, mandatory prioritization, cut pass) for the missing cost. Four output modes: §1 spec/plan, §2 code comments, §3 code, §4 chat, plus a shared core and a mode-selection table.

- **Chose new always-on skill over folding into /fast-chat** — /fast-chat is interaction mechanics (codes, review tail); only §4 Chat overlaps. §1/§2/§3 have no home in any existing skill, and folding would bloat /fast-chat. Rejected /warmup (explicitly excludes content). Revisit if the skill ends up only ever used for chat.
- **Bootstrap shape:** concise CLAUDE.md block (shared core + mode table, ~150 words) with the full per-mode rules in SKILL.md — same tradeoff /fast-chat makes. Rejected copying the full file into the project + Required Reading (heavier, duplicates the skill).
- **"Why this file exists" preamble:** compressed into SKILL.md as the "recognizable shape" checklist (the diagnosis list is operational — it's what to avoid); long-form rationale goes to README per "value-add context belongs in README."
- **Integration point:** §1 Spec is the natural bridge to the planned planner skill (plet-style planning) — the planner produces the artifact, §1 says how it should read.
- **Commit messages (Mode 3):** a project's own commit style wins; when none is specified, session-kit's own style is the default (`<verb> <what>: <brief description>`, themed bullet body only for non-obvious decisions, no body for trivial commits). User: "defers to a project's own commit style, but use session-kit's commit style as the default when not specified." Rejected: the source file's bare rule ("first line is what changed and why, under 72 chars") — too thin to produce consistent subjects.
- **Name:** `/red-pen` — see next entry.

### /red-pen reader axis and layering rule (2026-10-01)

The source file collapsed the reader into one default (an insider who knows the codebase and the thread). User: "A spec may have different readers. exec team, product team, eng team, design team, end users of different flavors, etc. any writing actually may have different readers."

- **Reader is a second axis.** Mode = output type, sets the shape. Reader = who, sets what to omit, vocabulary, depth. The insider default stays for code, comments, chat.
- **Layers are stopping points.** User: "for a spec, the pyramid is clear, exec summary, biz logic, design and tech implementation. roughly. I think a general editor/reader triage would need to identify the primary readers (execs, managers, ICs, etc.) to define how many layers the pyramid should have." Refinement: layer count = number of distinct stops among the readers, not number of reader types — readers who stop at the same depth share a layer. One reader → one layer → answer first, which unifies Mode 1's hinge and Mode 4's answer-first.
- **Readers who differ in what they know get separate linked artifacts.** This is the conventional position (Diátaxis splits by reader need); layering by audience is the extension, and it only works when readers share vocabulary and differ in depth.
- **Reader roster** in the Writing Conventions block: knows / decides / stops at, one row per reader type. Seeded at bootstrap with one question. Rejected: a per-artifact reader interview — ceremony, and the human won't enumerate what they know anyway.
- **Rejected for now:** Mode 5 for outsider-facing docs (README, user guide, release notes). Their shape is sequential, not pyramidal, so the rule set differs; hold until there is a real one to design against.
- **Attention triage:** resolved by the preamble + open items entry below. Calibration must not route through /feedback-foo.

### /red-pen preamble and open items (2026-10-01)

Resolves the attention-triage question: how does a long generated artifact tell a human what deserves their attention?

- **Chose a preamble + open items section over per-item triage tags** (decide / overrule / fyi). Tags scale badly — thirty tagged items is tag soup. A short block at the top scales to any length.
- **Preamble is prose, guidance only.** User: "The preamble should be more like 'This document is written for 3 primary audiences...' and describe them and maybe give guidance on structure." Two to five sentences: who it is for, what each audience comes for, how it is organized so they can stop early. No heading. Rejected: a per-reader routing line ("Exec: §1. Product: §1-2. Design: §3.") — user: "this is too prescriptive of structure."
- **Named "preamble."** User: "it's both for the benefit of authors, editors and readers." Rejected: "author's guidance" (names only one party), "reading guide," and no name at all.
- **Never omitted.** User: "a preamble saying this is only for X is useful." One reader → one sentence saying so.
- **Asks live in open items, not the preamble.** User: "I don't like mixing the job to be done (needs a decision) in the preamble, which should be author/reader guidance. if there is discrete action to be taken, doesn't a dedicated open items section make more sense?" Open items: one line each — owner, item, where it lives, author's lean. Everything not listed is settled. Numbered if /fast-chat, IDs if /stable-label — this is the fast-chat × red-pen intersection the question started from.
- **Preamble rule says nothing about section order.** User cut "Open items follows, then Decisions, Assumptions, Risks, Scope out" from the rule: "too much structure and scope for general writing guides."
- **Open items is conditional and unprescribed.** User: "open items is a conditional section. it should be in documents where it is needed, but that is a case by case. and I don't want to be prescriptive in this document about what those lines or structure looks like." Red-pen keeps only the writing rule — asks never go in the preamble; a dedicated section carries them when the document needs one — and says nothing about the section's form. The numbered/ID'd open-items format (the fast-chat × stable-label integration) is a candidate for the planner's spec template, not a writing rule.
- **Fractal pyramid allowed.** The user's "executive summary at the H3 level for each H2" is a per-section stop rather than one global pyramid by audience; the layering rule now allows either, and the preamble states which.
- **"Open with the hinge" retired** as a rule — satisfied structurally by open items.

### /red-pen dogfood on vog_specs: calibration (2026-10-01)

Three editing passes on vog_specs sections (VTS_SMV, VCI_PIP, VLS_ZON), parked in the session scratchpad, not applied. Findings that changed the skill:

- **Enumeration is not duplication.** User, on the calling-matrix bullets I collapsed into one sentence: "the sentence is better, but as an addendum to the 5 bullet points, not a replacement." And on a sub-bullet folded into a paragraph: "Mirrors as its own bullet point is better to me." A table and the prose that teaches its rows are one rule in two registers (the vog writing guide's own "same rule in both registers" pattern). Dedup applies across sections, not across registers. Structure that isolates one fact per line is scannable, not scaffolding.
- **Report by symptom, not word count.** User: "the dogfooding mentions word reduction, but I don't yet know how that translated to 'making AI generated content less painful.'" Word count is what the agent can measure; the symptom list is what the reader feels. The editing-pass report now counts rules met more than once, stale statements, history on top of rules, and argument in front of rules.
- **House style wins on conflict.** The vog repo forbids em-dashes, prefers prose over bullets, bans DEC citations from canonicals, soft-wraps. Red-pen's "prefer checkable lists" would have violated the first; its instinct to offload rationale to the decision log violated the third. Now stated in the editing-pass rule.
- **Layers can be derived artifacts.** User: "VLS and C4_VLS are kind of their own pyramid." The C4 rung is the stopping point for orientation and its "read VLS_X before..." line is a preamble. Layering rule extended.
- **Cuts that held:** cross-section restatement (the admission rule six times in VCI_PIP, the error rule four times in VTS_SMV), stale prose contradicting the record (host language still framed as open), dated session markers, decision-record argument in a teaching register.

### /red-pen premise test on unedited AI text (2026-10-01)

User asked the real question: "are the items in the 'Why this file exists' solvable? does red-pen make AI generated content less painful?" The vog_specs passes could not answer it - those documents were human-edited over months and showed none of the listed symptoms; the pain there was history and drift. So the next pass ran on unedited AI-drafted requirements text, the kind the premise is about.

- **The symptoms were present on unedited text.** In one section of about 1,800 words (the shape of the edit-target eval input): one fact ("edge ranking was deliberately replaced") stated 10 times, 197 words under its own header on a topic the section calls "explicitly not a priority," 9 sentences opening "This is / That is," three sentence-length H4s under one H3, 18 bold leads. Defensive restatement - the author anxious the reader would think deprecated code was unfinished.
- **The cut was judged good.** User, on the before/after of one H4 block (4 paragraphs to 1): "this is an objectively good improvement for that H4 example you showed me." First unqualified yes of the dogfood.
- **Contrast with the vog passes:** there, two of three shown cuts were rejected (enumeration collapsed, sub-bullet folded). The difference is the input: compression rules pay off on unedited generated text and over-cut on edited text. Red-pen's value is highest exactly where the premise says it is.
- **Report by symptom worked.** The table of counts (restatements 10 to 2, non-priority words 197 to 2 sentences, openers 9 to 0) plus one before/after paragraph is the reporting shape that let the user judge.
- **Eval implication (PLAN #16):** run the with/without comparison on unedited generated text, judged by preference on paired paragraphs, not on word count and not on mature specs.
- **Still unanswered:** whether the always-on rules prevent the symptoms at generation time, as opposed to the editing pass removing them afterward. An editing pass tests the editor; the eval must test the author.

### /red-pen improvements after the premise test (2026-10-01)

User: "how else can we improve the skill? can we give the skill personas? like 'as a professional editor'." Five changes, in the order built:

- **Symptom script** (`scripts/symptoms.py`): the prose-to-tooling escalation from the 2026-03-14 decision, first use in session-kit. Counts what the judged-convincing table counted: restated phrases (5-word shingles recurring across sentences), "This is / That is" openers, bold leads, sentence-length headers, dated status markers, forward references, hedges, em-dash density, section-length spread. `--compare` prints the delta. Path-based `allowed-tools` per the portability decision. Known blind spots, stated in the skill: stale claims, cross-section restatement, argument in front of a rule.
- **Self-edit loop**: anything over its mode's budget is a draft; measure, cut, deliver. This is the only in-skill answer to the open question (prevent vs. remove); the eval still has to test it.
- **Worked example** (`references/worked_example.md`): a before/after pair with its symptom table and the two rejected vog cuts as the counter-example. (Replaced on 2026-10-02 with a text unrelated to any eval input.)
- **Calibration overrides**: a rejected cut is recorded in the Writing Conventions block as a one-line override.
- **Personas, qualified.** Chose per-step reader frames (copy desk chief for the cut pass, decision-maker with four minutes for Mode 1, colleague at the next desk for Mode 4, the 2am maintainer already in Mode 2) over a global "you are a professional editor." Rejected the global persona: role prompts move tone and fluency, not accuracy, and fluency is the failure the skill exists to catch. Today's evidence: what the user accepted was checkable counts; what they rejected was judgment. Recorded in What Does NOT Go.

### /multi-adversarial-review joins session-kit (2026-10-01)

User: "I'd be open to adding mar to session-kit. It's up there with stable labels and fast chat as a 'most used'." MAR is the sequential multi-model review chain from vog_kit (`vog_kit/.claude/skills/multi-adversarial-review`, alias `mar`): a lead commits a stable state, independent reviewer families inspect it one at a time, the lead dispositions and commits between stages.

- **Port the Claude copy as-is, generalize the Vog-specific lines to examples** (chose over a rewrite: it is the user's most-used review method, so the doctrine ports faithfully; only frontmatter, Quick Reference, Vog mentions, and the prior-art pointer change). Rejected for now: adding a `copy` target for /red-pen in the same cut - design work, not porting; it comes after the port settles (red-pen's review mode will be a MAR target rather than its own doctrine).
- **Name:** `skills/multi-adversarial-review/` primary, "mar" as a description trigger. The /foo lesson: an opaque alias needs a self-documenting primary. Rejected: `skills/mar/` primary; a stub directory like vog_kit's.
- **session-kit becomes canonical.** vog_kit's copy mirrors it from now on, the way fast-chat already flows session-kit to vog_kit. Rejected: two sources of truth for a skill edited often.
- **Codex variant deferred.** User: "ignore codex for now. that would be a future porting effort." Claude copy only; README notes the Codex version lives in vog_kit.
- **Prior art stays a pointer** (11,757 words in vog_kit), not a copy.

### /red-pen eval iteration 1 (2026-10-01)

8 cases, with-skill vs no-skill, same model. Pass rate 90% vs 48% over 48 assertions; +17s and +17k tokens per task. Workspace: `skills/red-pen-workspace/iteration-1`.

- **The premise question answered for these prompts:** the always-on rules prevented the symptoms at generation time. fresh-spec with skill: 348 words, preamble, asks in their own section, settled decisions left settled. Baseline: 1,070 words with the anti-patterns under renamed headers.
- **User review (feedback.json):** every with-skill output "not painful" or better; every baseline "too verbose", "painful", or "hard to parse". On the baseline bootstrap: "This is exactly the kind of long output that makes AI generated text hard to read." On the with-skill fresh spec: "it's concise and clear." User flagged their own bias: "the fact that I know which were generated with the skill and without it is probably biasing me."
- **Two substantive notes.** edit-target with skill: "I just skimmed the output until the last paragraph" - the reply was 825 words of prose with the before/after pair at the end. Fix: a fixed report shape (one line, symptom table, one pair, nothing else, under 200 words outside the pair). too-long with skill: "Token bucket" is jargon to a non-engineer "but this would be jargony to anyone without that background." Fix: gloss a term once when a named reader may not share it.
- **Three skill failures were self-inflicted:** bootstrap block over its own 250-word budget once the roster is added (budget now excludes the roster table); over-budget note went in chat instead of the document (rule now says the document's first line); edit report led with word count (fixed by the report shape).
- **Uncaught failure class: invented content**, in both configurations (a ~1.4s backoff figure, an open question not in the source, invented test contents). Added "a claim with no source" to the symptom list and a provenance check to the cut pass; iteration 2 asserts it.
- **too-long does not discriminate** (4/5 both). Sharpened toward what differed: the baseline restated settled decisions, invented default numbers, and closed with "want me to implement it?".
- **Baselines were often deeper but undisciplined**: better project grounding on chat-answer (with a SameSite factual error), more reader-facing flags on edit-target, a deeper review of stale-draft (but no edit), six tests on code-comments (with a comment that misdescribed its own backoff). Depth is not the skill's job; discipline is.
- **Iteration 2 review is blind:** configurations shown as A/B with a key held back, per the user's bias note.

### /red-pen eval iteration 2, blind (2026-10-02)

Same 8 cases, updated skill, sharpened assertions. Graders: 78% vs 42% over 59 assertions (iteration 1 was 90% vs 48% on easier assertions). User review was blind and side-by-side, left/right randomized per case, key sealed until submit (`iteration-2-blind/`).

- **Blind preference: skill 5, baseline 1, neither 1, both fine 1.** Skill preferred on bootstrap ("the right is so long and wordy"), fresh-spec ("left is just too much content to be useful"), edit-target (slight), stale-draft ("too many bullet points ... i just skim"), pr-description ("the conciseness of right is correct"). The earlier unblinded result held up without the labels.
- **Baseline won too-long**, narrowly: "very easy to see that there are three reasons to go token bucket." The skill run wrote the same reasons as prose. "Formatting is rare" was over-applied; parallel items get a list. Rule rewritten, with a ceiling: past about five bullets the reader skims.
- **Neither on code-comments.** The baseline surfaced that 429 is the one 4xx that arguably deserves a retry; the skill run followed the wording silently and was "under-commented." Two fixes: Surface by Stakes' tell now covers a case the ask's wording covers but its intent may not; Mode 2 says sparse is not silent.
- **Both fine on chat-answer** though the baseline was twice as long: "the total length isn't detrimental and the organization (such as bullet points) helps." Bullets rescued it, but the user's follow-up corrects the reading: "the baseline tends to be too wordy in general. that's part of the pain." Scannable is necessary, shorter is still better.
- **Edit report:** "neither Left's long list of bullets or Right's table is all that useful or actionable ... i just skim right past it ... i do like the example paragraph. it gives a flavor without overwhelming the human maintainer." Report shape reordered: one line, then the pair, then a table of at most four rows.
- **Graders and the user disagreed on pr-description.** Graders failed the skill run (3/6) for colon-label lines as "renamed scaffolding"; the user preferred it: "this is not prose. PRs are more like documentation and records." The assertion was wrong, not the output. Mode 3 now says so.
- **Lesson on the method:** the assertion pass rate tracks rule-compliance; the blind preference tracks pain. They agreed on 5 of 8 and diverged exactly where a rule was over-applied (prose over bullets, sparse over informative). Preference is the measure; assertions are the regression net.
- **Retained artifacts:** the edit-target runs from iterations 1 and 2 are not kept. The committed benchmarks cover the other seven cases: 92% vs 49% for iteration 1, 79% vs 41% for iteration 2. The case reruns in iteration 3.
- **Still uncaught:** invented content persists in both configurations (an invented NOTES.md fact in the baseline; "constants hardcoded" claimed in the skill PR description). The provenance check checked numbers, not claims.

### /red-pen eval iteration 3, blind (2026-10-02)

Same 8 cases, skill v0.2.0, 67 assertions. Graders: 84% vs 48%. Blind side-by-side preference: skill 6, baseline 1, both fine 1 (iteration 2 was 5 / 1 / 1 neither / 1 both fine). Cost fell to +2s and +11k tokens per task. Workspace: `iteration-3/`, `iteration-3-blind/`.

- **The iteration 2 fixes held.** code-comments went from "neither" to the skill: the 429 edge is now surfaced in the reply and in a comment. too-long went from a baseline win to "both fine". pr-description, stale-draft, bootstrap, fresh-spec, and edit-target were preferred with the skill.
- **Baseline won chat-answer.** User: "the 'cost' is buried in the bullets. easy to miss. the left bold formatting is helpful as well." The skill run tacked the CSRF cost onto the end of a reason; the baseline gave it its own line and bold bullet labels. Two rules added: the cost gets its own line; bold the label of each bullet. "Bold almost never" was over-applied the same way "formatting is rare" was.
- **Edit report needs a lead-in.** User, on a bare "Before (§6.3 ...):" line: "that line has no context. there should be a 'here is an example of the audience-focused style change applied:' or similar." The pair is now introduced by a sentence saying what it is.
- **"Too wordy" is still the baseline's failure**: "right is still waaaay too wordy" on edit-target, where the baseline made the file longer.
- **Eval leaking into itself:** the with-skill edit-target run took a number for its report from the skill's worked example, which described the same section as the eval input. The worked example is now a different text (a cache TTL block) and also shows the report shape.
- **From the graders, fixed:** the 300-word budget's escape clause was too cheap (a 415-word doc passed by saying so); the bootstrap block left a dangling "Readers:" line when there was no roster; a reply asked a question although the record says "pick a default and we'll revisit".
- **From the graders, open:** graders still disagree with the user on pr-description (3/7 on length and a per-file list; the user preferred it). Several assertions do not discriminate (code-comments 8/8 vs 7/8, too-long 9/9 vs 8/9). Invented or unsupported claims still appear in both configurations.
- **Skill at v0.2.1.** These changes are untested; a fourth iteration would confirm them.

### README Origin made generic (2026-10-02)

User: "plet is getting deprecated. i think this needs to be very generic like during hundreds of sessions or something like that." Origin now says the suite was developed and refined over hundreds of AI-assisted development sessions. Dropped the plet-skills link and the unsourced "8+ parts". The /dictation examples still use "plet" as a sample jargon term; left as is, since an example term does not need a live project behind it.

### README skill order: most used first (2026-10-02)

Chose usefulness order over the earlier infrastructure-first order (warmup, fast-chat, dictation, notes, stable-label, foo; 2026-03-14), in all four README sections, keeping the same-order-everywhere rule. Order: stable-label, fast-chat, multi-adversarial-review, notes, red-pen, warmup, dictation, feedback-foo. The top four and the last follow the user's usage ranking; red-pen, warmup, and dictation were placed by Claude and approved. Prompted by the first `copy` review, whose evaluator reader had no way to tell which skill to try first. Rejected: table-only reorder, which would break the rule that a reader who learns the order in the table finds sections in the same order below. Cost accepted: How They Fit Together no longer opens with /warmup as the foundation.

### First `copy` review: the README (2026-10-02)

Two stages, GLM then Codex, two reader lenses each (evaluator, existing user) plus the record lens. 23 findings after dedup: 14 fixed by the editor, 1 rejected (summary and detail are two layers, not duplication), 8 deferred to the owner, of which 7 are now ruled. Record: `skills/multi-adversarial-review-workspace/copy-readme/`.

- **What only the record lens found:** an unsourced "500+ sessions", install commands that copied the eval workspaces, and four README examples that had drifted from their skills' current behavior. None of these is visible from the README alone.
- **What sequencing found:** Codex corrected a claim in GLM's review and one in the stage 1 disposition (the install fences were not one command per block).
- **Lesson for the target:** meaning findings dominate on a mature document; stage 2 sent 6 of 15 to the owner. Expected, since the editor must not change claims, but worth batching as one set of questions at the end of the chain.
- **Claude's own provenance slip:** while fixing a gloss, Claude added a link it could not source, and removed it before committing. The record lens applies to the editor too.

### /multi-adversarial-review gains a `copy` target (2026-10-02)

The review method the user uses most for code, applied to prose. Follows the port decision that /red-pen's review would be a MAR target rather than its own doctrine.

- **Lenses are the readers.** One reviewer per named reader, blind to each other within a stage, each reporting where they stopped, what they reread, what they did not understand, and what they already knew. Chose readers over topical lenses (clarity, concision, structure) because every finding in this project's evals that mattered was tied to a reader.
- **Two non-reader lenses:** record (stale and unsourced claims; this is the invented-content class the evals kept missing) and fidelity (nothing lost when reviewing an edit).
- **A named reader is a route precondition.** No reader, `route-failed: reader-undefined`. Mirrors the spec target's authority coverage gate.
- **`over-cut` is a finding kind and Strong is a required section.** Both guard against the failure the user caught in the dogfood, where compression rules over-cut edited text. A reviewer told only to find cuts behaves like a reviewer told only to find bugs.
- **Reviewers never change meaning.** A fix that would alter a rule or a decision is a `meaning` finding, deferred to the owner. Same split as spec mode's editor versus maintainer.
- **`copy` versus `spec`:** spec reviews what the text proposes, copy reviews whether readers can use it. Both can apply to one file; spec first.
- **Rejections feed back.** A rejected cut is recorded as a one-line override in the project's writing conventions, which is /red-pen's calibration rule.
- **Cross-family reviewers for prose is a hypothesis.** The evidence so far supports independent-context readers; the reference says so and asks the lead to record which ran.
- **Review output has its own budget** (about 300 words before findings), since a wordy review of a wordy document fails its own test.
- **Not yet run.** No copy review has been executed with this target.

### /red-pen Surface by Stakes (2026-10-01)

The agent-side heuristic for what deserves a reader's attention — the "selection problem above the writing layer" the source file left out. User: "**Surface by stakes.** is a very very good heuristic."

- **Three bins, ascending stakes:** record (no real alternative, or settled by the record), tell (picked between alternatives for a citable reason, one line), ask (a reader owns it / hard to reverse / large blast radius / no citable reason / contradicts the record / deviates from the request). Asks go at the start of their owner's layer, with the agent's lean.
- **Position, not deletion.** User: "one thing about the pyramid is that you don't necessarily have to worry about losing data. it may just be 'mis-layered'." The heuristic's output is a placement; the record is the bottom layer. Rejected: an omit bin.
- **Doubt goes to tell**, except doubt about reversibility goes to ask — a misplaced item can still be found, an unneeded ask costs the reader a judgment.
- **Too many asks = underdetermined plan.** Ask the one question that settles the most of them first (fast-chat's "one question back," applied to a document).
- **Blast radius is a separate signal from reversibility.** A rename across 40 call sites is easy to reverse and still worth asking about. Added at the user's request.
- **Rewrite history:** first draft used top/middle/bottom, which collided with the pyramid's reader layers (user: "what is top/middle? of the pyramid?"). Second draft described bins by position before criteria. Third named the bins and put criteria first, which exposed a hole: "absent from the record" sent nearly everything to ask, and "guess" defined as not-following-a-pattern left tell empty. Fixed by making the axis "were there alternatives, and did you have a reason to pick."
- **Calibration:** overruled tells mean under-asking, waved-through asks mean over-asking. Adjusted within the session; persists via the reader roster and NOTES.md, not /feedback-foo.
- **Lives as its own section** after the shared core, not a bullet — too long for one.

### /red-pen naming (2026-10-01)

The feeling to convey: "makes AI writing less painful." User: "red-pen is short memorable and clever."

- **Chosen:** `/red-pen` — says an editor now exists, which is the file's one-line thesis (generated text is painful because nothing filters it). Memorable without bragging. Covers §3 Code and diffs, which "prose" names exclude.
- **Rejected:** `/tight-prose` — the anchor; idiomatic and matches the [value]-[domain] shape of /fast-chat and /stable-label, but "prose" excludes the code and diff rules
- **Rejected:** `/crisp-prose` — names the result, not the cut; same "prose" problem
- **Rejected:** `/high-signal` — the user's own vocabulary, but no domain word
- **Rejected:** `/second-draft`, `/easy-reading` — evocative but conceptual (the /sharpen lesson)
- **Rejected:** `/no-fluff` — reads like a marketing tagline (the /steady-session objection)
- **Rejected:** `/word-budget` — names the lever, not the value (the /options objection)

---

## Open Questions

- ~~Suite name~~ → resolved: session-kit
- ~~Skill 2 (/chatux) naming~~ → resolved: /fast-chat
- ~~Skill 3 (/feedback) naming~~ → resolved: /feedback-foo (renamed from /sharpen → /foo → /feedback-foo as primary)
- ~~Opencode compatibility~~ → resolved: OpenCode auto-discovers from `.claude/skills/` (same as Claude Code), so no duplication needed. Single `skills/` directory works for both.
- ~~Writing directives skill name~~ → resolved: /red-pen
- ~~/red-pen attention triage tags~~ → resolved: preamble + open items section instead of tags
- /red-pen Mode 5 for outsider-facing docs — held until a real example exists
- Planner skill (plet-style planning) — name TBD, deferred until /red-pen evals are done. The /red-pen inspiration article ("Plan Mode Is Dead") is also relevant reading for this one.
- ~~Plugin subsets~~ → resolved: symlinks work. See below.

### Plugin bundle design (2026-03-14)

Three bundles planned:
- **session-kit-core**: `/warmup` + `/fast-chat` + `/dictation` — session experience layer (loading, communication, input)
- **session-kit-refine**: `/notes` + `/stable-label` + `/foo` — knowledge management layer (decisions, references, process improvement)
- **session-kit** (full): all 6

**Thematic split:** core makes each individual session smoother (immediate benefit). Refine builds institutional memory that compounds across sessions (long-term benefit).

**Rejected alternatives for the knowledge bundle name:**
- `session-kit-process-improvement` — descriptive but long
- `session-kit-compound` — the value compounds, but sounds financial
- `session-kit-knowledge` — accurate but generic
- `session-kit-continuity`, `session-kit-evolve`, `session-kit-craft`, `session-kit-practice`, `session-kit-meta`, `session-kit-rigor` — various degrees of close but not quite right
- **Chosen:** `session-kit-refine` — concise, matches /foo's ethos, conveys iterative improvement

**Rejected alternative for the session bundle name:**
- `session-kit-session` — redundant
- `session-kit-flow`, `session-kit-live`, `session-kit-ux` — too vague or niche
- **Chosen:** `session-kit-core` — the foundation you build on

**Rejected bundle groupings:**
- **Two bundles (core + knowledge):** clean split but "knowledge" was too generic for the bundle name
- **Three bundles with /foo standalone:** /foo depends on /notes (NOTES.md as intake) — incomplete without it
- **By use case (voice, docs, process):** too many bundles, creates "which one do I install?" confusion
- **Essentials (/notes + /warmup) + full:** only two tiers but essentials leaves out /fast-chat which most users want immediately
- **Chosen:** core (session experience) + refine (knowledge management) + full — two meaningful subsets plus the complete suite

### Quick Reference / HELP.md convention (2026-03-14)

**Problem:** When a user asks "how do I use /notes?", the agent reads the entire SKILL.md (hundreds of lines) — expensive and slow for a simple question. Inspired by plet-skills observation that skills need a `--help` equivalent.

**Decision:** Each skill gets two things:
1. A `HELP.md` file alongside SKILL.md, seeded with the corresponding How to Use section from README (nearly verbatim)
2. A short Quick Reference section near the top of SKILL.md pointing to HELP.md

**Ownership:** session-kit convention, not upstream to skill-creator. We implement it in our skills and document the pattern.

- **Rejected:** Quick Reference only in SKILL.md (no separate file) — still forces the agent to load the full SKILL.md to find it
- **Rejected:** README as the runtime source — README is for humans browsing GitHub, Quick Reference is for the agent at runtime
- **Chosen:** HELP.md seeded from README content — lightweight file the agent can read without touching SKILL.md

### Bundles dropped (2026-03-14)

Bundles are unnecessary because no skill does anything without an explicit setup step (running `/skill-name`). Installing all 6 is harmless — unused skills sit inert. Bundles added complexity (symlinks, three plugin.json files, extra install instructions) without solving a real problem. Removed from README; marketplace bundle removal to follow.

### Symlinks confirmed working for plugin bundles (2026-03-14)

**Tested:** installed `session-kit-core` via marketplace. Claude Code cloned the repo into `~/.claude-*/plugins/marketplaces/session-kit-marketplace/`, then the plugin cache resolved the relative symlinks (`../../../skills/dictation`) to absolute paths pointing at the marketplace clone's root `skills/` directory. All three core skills (`/warmup`, `/fast-chat`, `/dictation`) loaded correctly.

**How it works:** cache directory contains symlinks → marketplace clone's `skills/` directory (source of truth). Claude Code follows the symlinks and reads SKILL.md from the resolved targets. No duplication, single source of truth.

**plet-skills "symlink issues" did not reproduce.** The issues plet-skills encountered may have been specific to their directory layout or an older version of the plugin system. For session-kit's structure (root `skills/` + bundle `plugins/` with symlinks), it works cleanly.

---

## Things to Monitor

- **/feedback-foo is the least useful skill in practice** (user ranking, 2026-10-01: /stable-label > /fast-chat > small gap > /notes > big gap > the rest, with /feedback-foo last). Consistent with the earlier monitor note that proactive detection is untestable in evals, and with FOO_1 (extracted skills lose integration context). Don't build new mechanisms that depend on /feedback-foo for calibration. Candidate for a rethink or merge into /notes if the ranking holds.
- **/foo proactive detection** — single-turn evals can only test infrastructure and methodology, not proactive pattern detection. Detection ("I noticed you've done this twice") requires multi-session real-world usage to validate. The evals explicitly test "response to being told about a pattern," which is fundamentally different from the agent noticing on its own. This is the most important capability to monitor in real usage.
- **Fast-chat review prompt on informational answers** — eval 6 showed the skill appending a review prompt to a pure explanation. Not seen in real usage (likely eval artifact from single-turn context stripping). If this appears in actual multi-session usage, add "don't append review prompts to informational answers" guidance to the skill.
- **Stable-label token savings hypothesis** — IDs should save tokens in downstream usage (grep `REQ_3` vs restating full requirements). Unconfirmed — single evals can't measure cumulative cross-session savings. Monitor in real multi-session projects.
- **/notes SKILL.md size after template inlining** — inlining the NOTES.md template (2026-05-27) grew /notes SKILL.md by ~140 lines. Every /notes invocation now pays that token cost, even for ongoing operations (the common case — bootstrap is rare). Watch for /notes feeling heavier in long sessions or showing up in context-budget pressure. Mitigations if the cost becomes visible: (1) load the template only when bootstrap is detected (agent self-elides on ongoing-ops invocations), (2) extract to a sibling file the agent reads *only* when bootstrapping (re-introduces the asset model, but scoped behind a bootstrap gate), (3) accept the cost as the price of self-containment. Default disposition: **accept** — self-containment > marginal token savings — but revisit if real-world usage contradicts.
- ~~**/sharpen adoption of the name**~~ → resolved by renaming to /foo (2026-04-03). The monitoring proved correct — "sharpen" wasn't intuitive for the "feedback" mental model.

---

## Artifact Approval Status

*(None yet)*
