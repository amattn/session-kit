# CLAUDE.md

## Required Reading
<!-- managed by /warmup -->

**Load these files at the start of every session and after any context compaction:**

- `NOTES.md` — institutional memory (decisions, rationale, conventions)
- `PLAN.md` — current priorities and completed work

## Post-Compaction Rule
<!-- managed by /warmup -->

**After context compaction, immediately re-read all files listed in § Required Reading.** Acknowledge what was loaded before continuing work.

## Session Start Canary
<!-- managed by /warmup -->

**At the start of every session, run `git status` and summarize unstaged changes, staged changes, and untracked files.** Report this before doing any other work. If there are none, say so.

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

## Decision Cascade

After every decision, **cascade it through all affected artifacts before moving to the next topic.** NOTES.md Discipline handles *capturing* the decision. This section handles *propagating* it.

Trace each decision through these artifacts:

1. **NOTES.md** — the decision itself, rationale, rejected alternatives (always — per NOTES.md Discipline)
2. **SKILL.md** — if it changes a skill's behavior, update the skill definition
3. **README.md** — if it changes what the user sees (skill descriptions, install instructions, How They Fit Together)
4. **PLAN.md** — if it completes work, changes priorities, or adds new steps
5. **CHANGELOG.md** — if it triggers a version bump or adds/removes features

Not every decision touches all 5. Most touch 1-2. But always ask: "does this decision affect any other artifact?" The cost of checking is seconds. The cost of missing one is a consistency pass failure discovered later.

## Before You Commit

**Stop and verify before every commit:**

- Update `PLAN.md` to reflect completed work or changed priorities
- Update `CHANGELOG.md` if any version was bumped or features were added/changed/removed
- Ensure `plugin.json` and `marketplace.json` versions are in sync if either changed

This is not optional. These artifacts drifted when this checklist was positioned at the bottom of CLAUDE.md and used suggestive language ("check if"). It is now imperative: update, not check.

## Versioning

Three independent version numbers, each following semver (PATCH/MINOR/MAJOR):

- **PATCH** (0.1.x): bug fixes, wording tweaks, formatting changes, internal refactors
- **MINOR** (0.x.0): new subcommands, new sections, meaningful feature additions
- **MAJOR** (x.0.0): breaking changes to formats, removed subcommands, anything that would surprise an existing user

### Skill version (`version` in each SKILL.md frontmatter)

Bump when that specific skill's behavior changes. Scoped to the individual skill — a change to `/notes` doesn't bump `/warmup`'s version.

### Plugin version (`version` in `plugin.json` and `marketplace.json` plugins entry)

Bump when any skill changes. These two must stay in sync. The plugin version tracks the suite as a whole.

### Marketplace version (`metadata.version` in `marketplace.json`)

Bump when the marketplace listing itself changes, independent of any individual plugin:

- **PATCH**: description or metadata wording updates, keyword changes
- **MINOR**: adding a new skill to the `plugins` array
- **MAJOR**: removing a skill, restructuring the listing in a breaking way

## Evals

Evals are primarily generated with guidance from the official `skill-creator` skill. Load it for eval design, test case generation, and the with-skill vs baseline comparison framework.

All eval definitions (evals.json), test projects, and subagent outputs must be saved to disk in the corresponding `skills/<skill>-workspace/` directory. Eval artifacts are reference material — they document what was tested, how, and what the results were. Create the evals.json BEFORE running evals, not after.

**Reproducibility is critical.** Eval results are the evidence behind skill adjustments. If the artifacts aren't saved, future sessions can't verify findings, re-run comparisons, or build on previous iterations. Every eval should be re-runnable from what's on disk.

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

Skip the body for trivial commits (single-file wording tweaks, typo fixes). Commit eval workspaces in a separate commit from the eval findings they support.
