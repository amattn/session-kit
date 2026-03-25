# CHANGELOG

All notable changes to session-kit. Versions track the plugin version in `.claude-plugin/plugin.json`.

## [0.7.0] — 2026-03-24

### Changed
- `/fast-chat` v0.2.0: redesigned standard review prompt based on live trial feedback (SPI_5)
  - Stable tail simplified to R/O (recommendations / ok) — dropped S and the old A-E layout
  - "Silence is not approval" as the headline rule — re-present after every change until explicit O
  - R always produces NL-formatted options in review context
  - O implicitly accepts simple displayed recommendations
  - Free-form input needs no prefix — just type instructions
  - Updated HELP.md with new review flow examples
- `/warmup` v0.1.2: added concrete language-strengthening tactics to the escalation ladder (SPI_4)
  - Bold directives, imperative qualifiers, standalone sentences, cost framing, remove hedging
- `/notes` v0.1.2: reordered suggested starting sections for better reading flow (SPI_6)
  - New order: Project Context → Invariants → Concepts → Taxonomy → Key Design Decisions
  - Stable reference material first, growing decision log after

### Added
- SHARPEN.md: SPI_6 (notes default section order)

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
- Consistent skill ordering across all README sections: warmup, fast-chat, dictation, notes, stable-label, sharpen
- Replaced "bootstrap" with "setup" in user-facing README language

### Removed
- Plugin bundles (`session-kit-core`, `session-kit-refine`) and `plugins/` directory — skills are inert without explicit setup, so bundles add complexity without value

## [0.4.0] — 2026-03-14

### Added
- `/sharpen` skill: process improvement through pattern detection, observation tracking, and discipline creation (merged /patterns EX_4 into /sharpen EX_2)
- Prose-vs-tooling escalation pattern: disciplines are prose-based; supplement with scripts when prose drifts
- Eval workspaces for all 6 skills (58 total eval pairs with baseline comparisons)
- Plugin bundles: `session-kit-core` (/warmup, /fast-chat, /dictation) and `session-kit-refine` (/notes, /stable-label, /sharpen) — subsets via symlinks to root skills/
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
- `/patterns` skill — merged into `/sharpen`
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
- `/discipline` skill dropped — responsibilities split across `/warmup` (format/enforcement) and `/patterns` (detection/creation)
