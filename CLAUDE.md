# CLAUDE.md

## Project

session-kit — a suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time.

## Key Files

- `NOTES.md` — institutional memory (decisions, rationale, conventions)
- `skills/` — skill definitions, one subdirectory per skill
- `.claude-plugin/plugin.json` — plugin metadata
- `.claude-plugin/marketplace.json` — marketplace listing

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.** This is not optional and not deferrable. The pattern of "I'll catch up on notes later" always fails — decisions accumulate faster than memory, and by the end of a session the rationale is lost.

During build/review sessions where decisions come rapid-fire:
- Each user decision (approve, reject, rename, reorder, add, remove) gets a NOTES.md entry *before* presenting the next item
- If you realize you've fallen behind, stop and catch up immediately — do not continue accumulating debt
- Batch answers (e.g., "1A, 2C, 3D") still get individual NOTES.md entries for each decision

The cost of writing notes is seconds. The cost of lost rationale is re-litigating settled decisions in the next session.

## Versioning

When a skill's behavior changes, bump the **plugin** version in both `.claude-plugin/plugin.json` (`version` field) and `.claude-plugin/marketplace.json` (the corresponding entry's `version` in the `plugins` array). These two must stay in sync. Do **not** bump the marketplace-level `metadata.version` — that tracks the marketplace listing itself, not the plugin.

- **PATCH** (0.1.x): bug fixes, wording tweaks, formatting changes, internal refactors
- **MINOR** (0.x.0): new subcommands, new sections, meaningful feature additions
- **MAJOR** (x.0.0): breaking changes to formats, removed subcommands, anything that would surprise an existing user

### Marketplace version (`metadata.version` in `marketplace.json`)

Bump when the marketplace listing itself changes, independent of any individual plugin:

- **PATCH**: description or metadata wording updates, keyword changes
- **MINOR**: adding a new skill to the `plugins` array
- **MAJOR**: removing a skill, restructuring the listing in a breaking way

**When any semver changes** (plugin, skill, or marketplace), update `CHANGELOG.md` with the new version, date, and a summary of what changed under Added/Changed/Removed headers.

## Commit Style

Single-line subject: `<verb> <what>: <brief description>`. Common verbs: Add, Update, Fix, Drop, Rename.

Body uses **themed bullet lists** — group related changes under short theme headers. Each bullet is a concise fact, not a sentence. Example:

```
Add /fast-chat skill: structured interaction patterns for efficient communication

Mechanics:
- NL/NLR shorthands with recommendation formats
- Batch answer parsing with "no answer = still open" rule

Design:
- Always-on communication style, not just a bootstrap tool
- Version bumped to 0.2.0
```

Skip the body for trivial commits (single-file wording tweaks, typo fixes).

**Before every commit**, check if `PLAN.md` needs updating to reflect completed work or changed priorities.

## Evals

All eval definitions (evals.json), test projects, and subagent outputs must be saved to disk in the corresponding `skills/<skill>-workspace/` directory. Eval artifacts are reference material — they document what was tested, how, and what the results were. Create the evals.json BEFORE running evals, not after. Commit eval workspaces alongside the findings they support.
