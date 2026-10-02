# CHANGELOG

All notable changes to session-kit. Versions track the plugin version in `.claude-plugin/plugin.json`.

## [Unreleased]

### Changed
- README: skill table links to each How to Use entry; R/O and the reviewer tool names glossed; rename history cut from the table (first `copy` review, stage 1)
- `/notes` v0.1.3: HELP.md lists the suggested sections in the current order
- README (copy review, stage 2): intro says "hundreds of sessions"; Install says what installing activates; setup claim qualified; /fast-chat and /red-pen examples match their skills; routes reference linked; one command per fence in option 3
- `/red-pen` v0.2.3: HELP.md example shows the current report shape
- README: skills ordered by usefulness in every section (stable-label first, feedback-foo last); install commands skip the `*-workspace` eval directories; /notes claims softened; /stable-label example made consistent
- `/stable-label` v0.1.2: HELP.md example no longer adds a p95 the user did not ask for
- README Origin: generic ("hundreds of AI-assisted development sessions"); plet-skills link and "8+ parts" removed

### Added
- `/multi-adversarial-review` v0.2.0: `copy` target for reviewing documents as writing
  - `references/copy-review.md`: named readers as the lenses, plus record and fidelity lenses
  - Finding kinds drawn from /red-pen's symptom list, with `over-cut` as a finding
  - Output contract: overall, strong, needs work, fidelity, judgment and mechanical, readiness per reader
  - Reviewers never change meaning; a `meaning` finding goes to the owner
  - `/red-pen` v0.2.2 points to it for independent review
- `/multi-adversarial-review` v0.1.0 (alias `/mar`): ported from vog_kit, Claude copy
  - Doctrine, routes, disposition panel, and spec-review references carried over; Vog-specific lines generalized to examples
  - session-kit is canonical from here; vog_kit mirrors. Codex variant stays in vog_kit for a later port
  - HELP.md, README entries, How They Fit Together, Origin attribution
- `/red-pen` v0.1.0: writing directives for every output type, incorporated from `WRITING_DIRECTIVES.md`
  - Always-on: decide the output type (spec/plan, code comment, code/diff, chat), write to its rules, run a cut pass
  - `/red-pen <target>` edits a file or section against the rules and reports what was cut
  - Bootstrap adds a concise Writing Conventions block (shared core + mode table + reader roster) to CLAUDE.md; full per-mode rules stay in SKILL.md
  - Reader axis: name the readers, one layer per distinct stopping point, separate artifacts for readers who differ in what they know
  - Mode 1 opens with a prose preamble (who it is for, how to read it); asks go in a dedicated section when the document needs one, form unprescribed
  - Surface by Stakes: every item is sorted into record, tell, or ask by ownership, reversibility, blast radius, whether a reason can be cited, the record, and deviation from the request
  - README: skill table row, The Skills entry, How to Use entry, How They Fit Together line
  - README § Origin: attribution to Ayman Nadeem's "Plan Mode Is Dead"
  - `scripts/symptoms.py`: counts restated phrases, sentence openers, bold leads, sentence-length headers, dated markers, forward references, hedges; `--compare` for before/after
  - Self-edit loop: any output over its mode's budget is drafted, measured, cut, then delivered
  - `references/worked_example.md`: a before/after pair with its symptom table
  - Rejected cuts are recorded as project overrides; reader frames per step, no global persona
  - v0.2.1 after a third iteration (blind preference 6 of 8): the cost of a recommendation gets its own line; bold bullet labels; a lead-in sentence for the before/after pair; open items do not justify running over budget; worked example replaced with a text unrelated to the eval inputs
  - v0.2.0 after two eval iterations (blind preference 5 of 8 for the skill): parallel items get a list with a five-bullet ceiling; a literal-reading edge case is a tell; sparse comments are not silent; PR descriptions are records; edit report leads with the before/after pair and a four-row table; provenance check in the cut pass

## [0.9.0] — 2026-05-27

### Added

#### New skill: `/start` v0.1.0 — unified suite bootstrap

- Single entry point that runs the per-skill bootstraps with smart defaults and one approval (plus a `.claude/settings.json` multi-select sub-prompt when /warmup hits the propose path)
- **Tiers:**
  - `minimal` — /warmup
  - `standard` — /warmup + /notes + /stable-label + /fast-chat *(default)*
  - `full` — all six skills
- **Sub-skills activated via the Skill tool**, not `Read` as on-disk files — `/start` never opens sub-skill SKILL.md files directly; each is invoked through the proper skill-loading machinery
- Re-runnable — picks up only what's missing
- SKILL.md and HELP.md under `skills/start/`

#### `/notes` v0.2.0 — template-driven bootstrap

- **Inline NOTES.md template** lives in `skills/notes/SKILL.md` under § NOTES.md Template → § Template content (self-contained skill — no external asset file, no permission-prompted read)
- **Pre-seeded content:**
  - Default stable-label prefix table (`DEC`, `ICR`, `INS`, `OPN`, `MON`, `TAX`, `FOO`)
  - Quick Reference front-matter with always-present Sections TOC
  - Entry header format: `### PREFIX_N: YYYY-MM-DD - Title`
- **New sections in SKILL.md:**
  - § NOTES.md Template — describes the inline scaffold and the variable-substitution flow
  - § Scaling: Hierarchical Prefixes for Large Projects (`NOTES_DES_1` pattern)

#### `/warmup` v0.2.0 — project scaffolding + combined canary

- **Project scaffolding bootstrap** — new § Project Scaffolding Files with **asymmetric rules** per file:
  - `.gitignore` — **skip-if-exists.** Creates with `.DS_Store` only when missing; never touches an existing file.
  - `.claude/settings.json` — **propose, never automatic.** /warmup proposes additions via a /fast-chat multi-select (A: `permissions.allow`, B: `includeCoAuthoredBy: false`, C: `env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, D: `enabledPlugins: session-kit@session-kit-marketplace`) when the file is missing, empty, or contains only `enabledPlugins` (the marketplace-install shape). For any other content, leaves the file alone. User approves all, some, or none; writes are additive and never overwrite existing values.
- **Combined canary (recommended default)** — folds acknowledgment + git status into one line at session start; existing acknowledgment / behavioral / content canaries preserved as alternatives

#### README

- `/session-kit:start` → `/start` everywhere in marketing copy (table, section headers, prose, ASCII diagram)
- "One approval" softened to surface the `.claude/settings.json` sub-prompt when /warmup hits the propose path — settings changes are never automatic
- Example transcript updated to show the multi-select sub-prompt and the second `O` approval

#### Cross-platform discovery

- OpenCode discovery options in README — `.opencode/`, `~/.config/opencode/`, and agent-compatible `.agents/skills/` paths

### Changed

#### `/stable-label` v0.1.3 — section labels vs IDs disambiguation

- **New § Section labels vs IDs** — distinguishes bare-prefix section labels (`## Invariants (ICR)`) from IDs (`ICR_1`); section labels are not subject to the one-grep rule
- **Bootstrap split into two branches:**
  - Branch A — prefix table already pre-seeded by /notes (the common case under /start)
  - Branch B — no table exists, propose one
- Convention block reinforced with the no-shorthand rule — always use the full registered prefix

#### Plugin and marketplace `description` field

- Both descriptions now lead with `/start` instead of `/session-kit:start`, consistent with the README normalization

#### Project conventions

- **Commit style** switched from verb-first (`Add /foo: …`) to prefix-first (`feature: …`)
  - Lowercase whole-word prefixes (`feature`, `fix`, `chore`, `refactor`, `docs`, `performance`, etc.) — never `feat` or `perf`
  - Body layout: optional prose summary → themed bullet lists → optional trailing prose
  - Commits before 2026-05-27 use the older style

## [0.8.0] — 2026-04-03

### Changed
- `/sharpen` renamed to `/feedback-foo` v0.2.0 — FOO = Feedback, Observation, Oversight
  - "Sharpen" was too conceptual; natural inclination is "add an observation" or "add a feedback item"
  - `/foo`, `/feedback`, and `/observation` as aliases — all four invoke the same skill
  - `/feedback-foo` as primary (self-documenting), `/foo` as quick alias
  - Artifact renamed: `SHARPEN.md` → `FEEDBACK_FOO.md`
  - Item prefix renamed: `SPI_N` → `FOO_N`
  - Directory renamed: `skills/sharpen/` → `skills/feedback-foo/`
  - Updated all cross-references in README, NOTES.md, PLAN.md
  - Marketplace metadata bumped to 0.4.0 (user-visible skill name change)
  - Plugin and marketplace descriptions now list both `/foo` and `/feedback` for discoverability
  - Keywords synced between plugin.json and marketplace.json

## [0.7.0] — 2026-03-24

### Changed
- `/fast-chat` v0.2.0: redesigned standard review prompt based on live trial feedback (FOO_5)
  - Stable tail simplified to R/O (recommendations / ok) — dropped S and the old A-E layout
  - "Silence is not approval" as the headline rule — re-present after every change until explicit O
  - R always produces NL-formatted options in review context
  - O implicitly accepts simple displayed recommendations
  - Free-form input needs no prefix — just type instructions
  - Updated HELP.md with new review flow examples
- `/warmup` v0.1.2: added concrete language-strengthening tactics to the escalation ladder (FOO_4)
  - Bold directives, imperative qualifiers, standalone sentences, cost framing, remove hedging
- `/notes` v0.1.2: reordered suggested starting sections for better reading flow (FOO_6)
  - New order: Project Context → Invariants → Concepts → Taxonomy → Key Design Decisions
  - Stable reference material first, growing decision log after

### Added
- FEEDBACK_FOO.md: FOO_6 (notes default section order)

## [0.6.0] — 2026-03-14

### Added
- HELP.md files for all 6 skills — lightweight quick reference seeded from README How to Use content
- Quick Reference blockquote in each SKILL.md pointing to HELP.md with usage directive and escalation path
- README: examples added to each skill in How to Use section

## [0.5.0] — 2026-03-14

### Added
- README: How to Use section with setup and ongoing usage for each skill
- README: "Best for" closing lines in The Skills section

### Changed
- Consistent skill ordering across all README sections: warmup, fast-chat, dictation, notes, stable-label, foo
- Replaced "bootstrap" with "setup" in user-facing README language

### Removed
- Plugin bundles (`session-kit-core`, `session-kit-refine`) and `plugins/` directory — skills are inert without explicit setup, so bundles add complexity without value

## [0.4.0] — 2026-03-14

### Added
- `/foo` (was `/sharpen`) skill: process improvement through pattern detection, observation tracking, and discipline creation (merged /patterns EX_4 into /foo EX_2)
- Prose-vs-tooling escalation pattern: disciplines are prose-based; supplement with scripts when prose drifts
- Eval workspaces for all 6 skills (58 total eval pairs with baseline comparisons)
- Plugin bundles: `session-kit-core` (/warmup, /fast-chat, /dictation) and `session-kit-refine` (/notes, /stable-label, /foo) — subsets via symlinks to root skills/
- PLAN.md for tracking project progress
- Eval discipline in CLAUDE.md (save all eval artifacts to disk)
- Decision Cascade and Before You Commit sections in CLAUDE.md
- CHANGELOG.md
- Things to Monitor section in NOTES.md

### Changed
- `/notes` v0.1.1: "quote the user, paraphrase everything else" guidance; bootstrap offers to seed Open Questions
- `/dictation` v0.1.1: structured disambiguation is the primary differentiator; bootstrap focuses on project-specific jargon
- `/stable-label` v0.1.1: added "When to assign IDs — and when not to" (read/analyze vs create/modify heuristic); lifecycle eval findings (split, merge, promote, crosscut)
- `/warmup` v0.1.1: fixed over-trigger on unrelated requests; adopted cross-file reinforcement loop and content quality diagnosis from baseline evals
- `/fast-chat`: added compounding value note (seconds compound across sessions and projects)
- Value-add paragraphs moved from skill files to README (skills stay lean, README does marketing)
- README expanded with per-skill sections, install instructions, How They Fit Together diagram, bundle install options
- Marketplace metadata bumped to 0.2.0 (new plugins added to listing)

### Removed
- `/patterns` skill — merged into `/foo` (was `/sharpen`)
- "Where X Adds Value" sections from skill files (moved to README)

## [0.3.0] — 2026-03-14

### Added
- `/dictation` skill: correction table for voice errors, recurring typos, and emergent shorthand
- README skill table, per-skill descriptions, install instructions, origin and acknowledgments
- CC BY-SA 4.0 license

## [0.2.0] — 2026-03-14

### Added
- `/fast-chat` skill: structured interaction patterns (NL/NLR/1b1, batch answers, standard review prompt)

## [0.1.0] — 2026-03-13

### Added
- `/notes` skill: institutional memory with Notes Discipline
- `/warmup` skill: session bootstrap and compaction recovery
- `/stable-label` skill: greppable stable references with XXX_N convention
- Plugin metadata (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`)
- Scaffolding for 7 placeholder skills (later reduced to 6)
- CLAUDE.md with project config, NOTES.md discipline, versioning rules, commit style

### Also in this release
- `/discipline` skill dropped — responsibilities split across `/warmup` (format/enforcement) and `/foo` (detection/creation)
