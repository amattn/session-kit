# NOTES.md — session-kit

## Project Context

session-kit is a suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time. Extracted from patterns discovered during hundreds of sessions of plet-skills development. 6 skills total: `/notes`, `/warmup`, `/stable-label`, `/fast-chat`, `/dictation`, `/sharpen`.

**Origin:** Extracted from patterns discovered during plet-skills development (`../plet-skills/`).

---

## Key Design Decisions

### Suite scope and skill roster (2026-03-13)

Originally planned 7 extractable skills plus `/notes` (8 total). After merging /patterns into /sharpen and folding /discipline into /warmup + /sharpen, final count is 6 skills.

### Skill naming philosophy: nouns for systems, verbs for actions (2026-03-13)

Most skills in this suite are noun-shaped — they manage a system or artifact, not perform a one-shot action. `/notes` means "engage the notes system," not "take a note." Verb-form names (like `/mark`) undersell system-oriented skills by implying a one-shot action.

### Suite name: session-kit (2026-03-13)

Kept the original name. The suite name doesn't need to carry the value prop — the individual skill names already do that (`/fast-chat`, `/stable-label`, `/sharpen`). The suite name just says "here's a collection of session tools."

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

### /sharpen naming (2026-03-13)

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

### /sharpen eval findings (2026-03-14)

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

From EXTRACTABLE.md EX_6 and PLET.md § "Skills for Judgment, Code for Compliance": disciplines are prose-based, and prose is re-interpreted each invocation — it drifts. When a prose discipline keeps getting violated (especially format compliance, schema rules, consistency checks), supplement with tooling (validation scripts shipped in `scripts/`). Escalation pattern: prose first → if agents drift → build a tool. Not every discipline needs this — most won't — but /sharpen should recognize when prose alone isn't working. /warmup's canaries are already an example of this pattern — prose says "load these files," canaries verify it happened. /stable-label's consistency passes are the most likely candidate for future tooling (a validation script enforcing no-duplicate-definitions, no-orphaned-references, no-renumbered-IDs). No tooling gaps are urgent yet, but /sharpen should recognize these patterns when drift appears.

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

**Meta-observation:** this is session-kit's own process eating its own dogfood. The cascade and before-you-commit disciplines are the same pattern /warmup and /sharpen teach to users. When they drifted in our own project, we applied the same fix the skills recommend.

### /sharpen detection sources (2026-03-14)

Detection sources are broader than just NOTES.md scanning. Five sources: conversation patterns (repeated corrections, consistent preferences), user interaction style (terse answers, shorthand, frustration signals), agent self-observation (own mistakes, inefficient workflows), project artifacts (git history, directive drift, code review comments), and cross-session signals (prior NOTES.md, recurring SHARPEN.md entries, stale auto-memory). NOTES.md remains the single intake *destination* for writing observations down, but these are the *inputs* that feed detection.

### /patterns merged into /sharpen (2026-03-14)

Merged /patterns (EX_4) into /sharpen (EX_2). Both skills deal with process improvement — /patterns detects recurring patterns proactively, /sharpen tracks process observations with a resolution lifecycle. The user shouldn't have to choose between them when thinking "this process thing should be captured."

**Merged skill features:**
- Proactive detection ("I've seen this twice") — from /patterns
- Resolution lifecycle (open → resolved) — from /sharpen
- Promotion paths (→ CLAUDE.md, → NOTES.md) — from both
- Discipline creation ("express this as a named discipline") — from /patterns

**Name: /sharpen** — conveys the value prop (your process gets sharper). /patterns is descriptive but flat.

**Artifact: SHARPEN.md** — observations with IDs, lifecycle states, and promotion paths.

**Result:** 6 skills total instead of 7.

### /discipline folded into /warmup + /sharpen (2026-03-14)

Dropped /discipline as a standalone skill. Its responsibilities split across two existing skills:

- **/warmup** gets the **format and enforcement** — discipline block structure (scannable, enforceable, composable), writing blocks into AGENTS.md and/or CLAUDE.md, loading and verifying via Required Reading and canaries
- **/sharpen** gets the **detection and creation** — recognizing "this workflow should be a discipline," helping users express informal habits as named disciplines, the meta-pattern of identifying what needs formalization

Individual skills (like /notes) create their own discipline during bootstrap, proving no separate /discipline skill is needed.

- **Rejected:** standalone /discipline skill — too much overlap with /warmup (format, enforcement) and /patterns (detection)
- **Chosen:** split across /warmup (infrastructure) and /sharpen (recognition)

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
- Fenced code blocks in README should be one command per block — GUI clients allow easy copy-paste of a whole fenced area, so combining unrelated commands in one block forces users to manually select

---

## Taxonomy / Conventions

### Skill roster (in progress — names under review)

| # | Current name | Status | Source |
|---|-------------|--------|--------|
| 1 | /notes | **Implemented** | Existing |
| 2 | /fast-chat | **Implemented** | EX_1 |
| 3 | /sharpen | **Implemented** | EX_2 + EX_4 |
| 4 | /dictation | **Implemented** | EX_3 |
| 5 | /warmup | **Implemented** | EX_5 |
| 6 | ~~/patterns~~ | Merged into /sharpen | EX_4 |
| 7 | ~~/discipline~~ | Folded into /warmup + /sharpen | EX_6 |
| 8 | /stable-label | **Implemented** | EX_7 |

---

## Open Questions

- ~~Suite name~~ → resolved: session-kit
- ~~Skill 2 (/chatux) naming~~ → resolved: /fast-chat
- ~~Skill 3 (/feedback) naming~~ → resolved: /sharpen (monitor adoption — name may not be intuitive for "feedback" mental model)
- Opencode compatibility — skills should work with opencode as well as Claude Code. Need to investigate opencode's skill/plugin format and identify what (if anything) needs to differ.
- Plugin subsets — marketplace.json can list multiple plugins with different `source` paths within one repo. Each subset gets its own directory with its own plugin.json. plet-skills attempted this and hit duplication/symlink issues. Bundle design decided (see below), implementation deferred.

### Plugin bundle design (2026-03-14)

Three bundles planned:
- **session-kit-core**: `/warmup` + `/fast-chat` + `/dictation` — session experience layer (loading, communication, input)
- **session-kit-refine**: `/notes` + `/stable-label` + `/sharpen` — knowledge management layer (decisions, references, process improvement)
- **session-kit** (full): all 6

**Thematic split:** core makes each individual session smoother (immediate benefit). Refine builds institutional memory that compounds across sessions (long-term benefit).

**Rejected alternatives for the knowledge bundle name:**
- `session-kit-process-improvement` — descriptive but long
- `session-kit-compound` — the value compounds, but sounds financial
- `session-kit-knowledge` — accurate but generic
- `session-kit-continuity`, `session-kit-evolve`, `session-kit-craft`, `session-kit-practice`, `session-kit-meta`, `session-kit-rigor` — various degrees of close but not quite right
- **Chosen:** `session-kit-refine` — concise, matches /sharpen's ethos, conveys iterative improvement

**Rejected alternative for the session bundle name:**
- `session-kit-session` — redundant
- `session-kit-flow`, `session-kit-live`, `session-kit-ux` — too vague or niche
- **Chosen:** `session-kit-core` — the foundation you build on

**Rejected bundle groupings:**
- **Two bundles (core + knowledge):** clean split but "knowledge" was too generic for the bundle name
- **Three bundles with /sharpen standalone:** /sharpen depends on /notes (NOTES.md as intake) — incomplete without it
- **By use case (voice, docs, process):** too many bundles, creates "which one do I install?" confusion
- **Essentials (/notes + /warmup) + full:** only two tiers but essentials leaves out /fast-chat which most users want immediately
- **Chosen:** core (session experience) + refine (knowledge management) + full — two meaningful subsets plus the complete suite

---

## Things to Monitor

- **Sharpen proactive detection** — single-turn evals can only test infrastructure and methodology, not proactive pattern detection. Detection ("I noticed you've done this twice") requires multi-session real-world usage to validate. The evals explicitly test "response to being told about a pattern," which is fundamentally different from the agent noticing on its own. This is the most important capability to monitor in real usage.
- **Fast-chat review prompt on informational answers** — eval 6 showed the skill appending a review prompt to a pure explanation. Not seen in real usage (likely eval artifact from single-turn context stripping). If this appears in actual multi-session usage, add "don't append review prompts to informational answers" guidance to the skill.
- **Stable-label token savings hypothesis** — IDs should save tokens in downstream usage (grep `REQ_3` vs restating full requirements). Unconfirmed — single evals can't measure cumulative cross-session savings. Monitor in real multi-session projects.
- **/sharpen adoption of the name** — "sharpen" may not be intuitive for users who think in terms of "feedback" or "meta-feedback." Monitor whether the description triggers correctly for those mental models.

---

## Artifact Approval Status

*(None yet)*
