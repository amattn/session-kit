---
name: start
version: 0.1.0
description: "One-shot bootstrap for the session-kit skill suite. Sets up multiple session-kit skills (warmup, notes, stable-label, fast-chat, dictation, foo) together in a single pass — eliminating the per-skill bootstrap loop and the retro-labeling gap that occurs when /notes captures content before /stable-label runs. Three tiers: minimal (warmup only), standard (warmup + notes + stable-label + fast-chat), full (all six). Use when the user asks to 'start session-kit', 'init session-kit', 'set up session-kit', 'bootstrap session-kit', 'install session-kit on this project', or runs the skill directly. Also trigger when a user just installed session-kit and wants to enable it on a project, when they want a fresh project scaffolded with session-kit conventions, or when they mention multiple session-kit skills together. Skip when only a single sub-skill bootstrap is appropriate, when the project already has session-kit set up (AGENTS.md contains /warmup or /notes breadcrumbs), or when the user is asking how the suite works rather than wanting to apply it."
user-invocable: true
---

# /session-kit:start — Unified Session-Kit Bootstrap

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.

Bootstrap the session-kit suite in one pass instead of running `/warmup`, `/notes`, `/stable-label`, etc. one at a time. Solves three problems:

1. **Bootstrap order matters but is annoying to get right** — `/notes` needs `/warmup` to load it; `/stable-label`'s prefix table lives in NOTES.md. Doing them individually means remembering the order.
2. **Retro-labeling gap** — running `/notes` before `/stable-label` creates content that has to be labeled afterward. A unified bootstrap eliminates the gap.
3. **Decision fatigue** — each skill's bootstrap asks 2-4 questions. Running 3-6 skills in a row means 10+ questions for what's usually a routine setup. Smart defaults + one confirm replaces the loop.

---

## The Job

1. Detect tier (default: `standard`) and current project state
2. Plan the full set of files and changes
3. Present the plan to the user as one approval prompt with three escape hatches (approve / tweak / customize interactively)
4. Execute atomically — create all files and edits in a single pass, in the right order

---

## Tiers

| Tier         | Skills bootstrapped                                                       |
|--------------|---------------------------------------------------------------------------|
| **minimal**  | /warmup                                                                   |
| **standard** | /warmup + /notes + /stable-label + /fast-chat *(default)*                 |
| **full**     | /warmup + /notes + /stable-label + /fast-chat + /dictation + /feedback-foo |

**Why these groupings:**
- **minimal** — just the reliability scaffold. For projects that already have their own NOTES.md or convention story, or where the user only wants Required Reading + canaries.
- **standard** — the "I want session-kit on this project" default. Adds institutional memory (`/notes`), greppable cross-references (`/stable-label`), and structured interaction (`/fast-chat`). Covers most use cases.
- **full** — adds voice-input corrections (`/dictation`), process observation tracking (`/feedback-foo`). Useful for long-running projects, voice-input users, and teams doing process improvement.

---

## The Flow

### Step 1 — detect and plan

1. Check whether `AGENTS.md` and/or `CLAUDE.md` already exists. If either contains `<!-- managed by /warmup -->` (or another session-kit breadcrumb), session-kit is already set up — switch into "augment existing setup" mode (see § Re-running on an Existing Setup).
2. Determine the tier — default `standard` unless the user said otherwise.
3. Gather smart defaults from the project context:
   - **Project name** — directory basename (`basename "$PWD"`)
   - **Today's date** — `YYYY-MM-DD` format
   - **Project description** — one line from README if present, otherwise empty placeholder for the user
   - **Git status** — for the canary line in the Session Start block

### Step 2 — present the plan as one approval prompt

Show the user exactly what will be created and changed. Use /fast-chat formatting (fenced code block, lettered options, R/O tail):

```
About to bootstrap session-kit (standard tier) for `<project>`:

Files to create:
- AGENTS.md         (Required Reading, Post-Compaction Rule, Session Start canary, NOTES.md Discipline, Stable Label Convention, /fast-chat Interaction Conventions, Self-Improvement)
- CLAUDE.md         (pointer to AGENTS.md)
- NOTES.md          (from /notes template, with Stable Label Prefixes table pre-seeded: DEC, ICR, INS, OPN, MON, TAX, FOO)
- .gitignore        (.DS_Store) — only if missing
- .claude/settings.json (read-file Bash + read-only git + grep allowlist, includeCoAuthoredBy=false, CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1, enabledPlugins) — only if missing

Auto-memory entries:
- project-<name>.md     (project description, TBD flags)
- warmup-session-canary.md (combined acknowledgment + git status canary)
- MEMORY.md         (index)

A. Approve — write everything as planned
B. Switch tier (minimal | full)
C. Customize interactively — walk through each sub-skill's bootstrap one at a time

R. Show me recommendations
O. Ok, approve
```

### Step 3 — execute (depending on the user's choice)

- **A or O** — write all files atomically in the order: AGENTS.md → CLAUDE.md → NOTES.md → auto-memory entries → MEMORY.md. Then emit the standard /warmup Session Start canary so the user can see it working.
- **B** — re-present the plan with the new tier's contents.
- **C (customize)** — switch into interactive mode (see § Interactive Mode below). Walk through `/warmup`, `/notes`, `/stable-label`, then any tier-specific extras in dependency order.
- **Anything else (prose, edits)** — apply the edit, re-present the plan. (Per /fast-chat: silence is not approval. The plan stays open until the user says O.)

---

## Bootstrap Order

The unified bootstrap invokes sub-skills via the Skill tool (see § Invoking Sub-Skills via the Skill Tool) in this order, regardless of tier:

1. **/warmup** — establishes AGENTS.md scaffolding (Required Reading, Post-Compaction Rule, combined Session Start canary), CLAUDE.md pointer, auto-memory directory
2. **/notes** — writes `NOTES.md` to project root from /notes' inline template (substitutes `{{PROJECT_NAME}}`, `{{DATE}}`, `{{PROJECT_DESCRIPTION}}`), adds NOTES.md to Required Reading, adds NOTES.md Discipline block to AGENTS.md
3. **/stable-label** — detects the pre-seeded prefix table from /notes (Branch A of /stable-label's bootstrap), adds Stable Label Convention rules to AGENTS.md. *No prefix table re-proposal* — defaults come from /notes' template.
4. **/fast-chat** — adds Interaction Conventions block to AGENTS.md
5. **/dictation** *(full tier only)* — scans project for jargon, proposes correction table, writes to AGENTS.md
6. **/feedback-foo** *(full tier only)* — creates FEEDBACK_FOO.md scaffold, adds Self-Improvement directive to AGENTS.md

Steps 1-3 are tightly coupled: /notes' template seeds /stable-label's table; /warmup's Required Reading needs /notes' NOTES.md path. Run them in this order to avoid retro-edits.

---

## Smart Defaults

To eliminate per-project decisions, /session-kit:start applies these defaults:

| Concern                  | Default                                                                       |
|--------------------------|-------------------------------------------------------------------------------|
| Project name             | Directory basename                                                            |
| Project description      | First sentence of README, or empty placeholder                                |
| Directive file           | `AGENTS.md` (canonical) + `CLAUDE.md` (one-line pointer)                      |
| Canary style             | Combined: `Loaded: <files>. Git: <status>. Ready.`                            |
| Required Reading         | `NOTES.md` (added by /notes step)                                             |
| Stable Label prefix set  | `DEC, ICR, INS, OPN, MON, TAX, FOO` (from /notes template)                    |
| Open Questions seeding   | Empty by default; offer to seed *after* bootstrap completes                   |
| FEEDBACK_FOO.md location | Project root *(full tier only)*                                               |
| Dictation seeds          | Project name + obvious jargon scanned from README *(full tier only)*          |

**All defaults are overridable** in interactive mode (Step 3 choice C) or by editing files after bootstrap.

---

## Interactive Mode

When the user picks C ("customize interactively"), walk through each sub-skill in dependency order, presenting that skill's actual bootstrap questions (not /session-kit:start's plan). This is equivalent to running `/warmup`, then `/notes`, then `/stable-label`, etc. in sequence — except /session-kit:start handles the sequencing and lets sub-skills know they're part of a unified bootstrap (so e.g. /stable-label takes Branch A and doesn't re-propose the prefix table).

Tell the user up front: "Switching to interactive mode. I'll walk through each skill's bootstrap individually. Say `skip` to skip a sub-skill, `defaults` to accept that skill's defaults and continue, or answer the questions to customize. You can also exit interactive mode at any time and approve the rest."

---

## Re-running on an Existing Setup

If the project already has session-kit (detected by `<!-- managed by /warmup -->` or similar breadcrumbs in AGENTS.md or CLAUDE.md), do not re-bootstrap. Instead:

1. Audit what's installed (which sub-skills' breadcrumbs are present)
2. Compare to the requested tier — identify what's missing
3. Offer to bootstrap only the missing sub-skills
4. Never overwrite existing breadcrumbed sections without explicit user approval

---

## Invoking Sub-Skills via the Skill Tool

/session-kit:start does **not** duplicate, inline, or `Read` the bootstrap logic of each sub-skill. Instead, it activates each sub-skill by calling the **Skill tool** — e.g. `Skill(skill: "warmup")`, `Skill(skill: "notes")`, `Skill(skill: "stable-label")`, `Skill(skill: "fast-chat")`, `Skill(skill: "dictation")`, `Skill(skill: "feedback-foo")`. The exact invocation name comes from the available-skills list at runtime (plain `name` for personal skills, `plugin:name` for plugin-namespaced ones — session-kit ships as a plugin, so `session-kit:warmup` etc. is the typical form). Each call loads that skill's SKILL.md into context the proper way — as a system reminder — and the sub-skill's own Bootstrap section then drives its setup.

**Do not use the Read tool on `skills/<name>/SKILL.md` to look up sub-skill behavior.** Sub-skills are activated, not read. Reading SKILL.md as a regular file bypasses the skill-loading machinery and pulls in content that wasn't meant to be consumed that way.

This avoids drift: each sub-skill remains the single source of truth for its own behavior, and /session-kit:start is the orchestrator that sequences the Skill-tool calls, applies smart defaults, and signals "unified mode" so e.g. /stable-label takes Branch A (table already seeded by /notes) and doesn't re-propose the prefix table.

If a sub-skill changes its bootstrap (e.g., /notes adds a new default section), /session-kit:start picks up the change automatically the next time it invokes that skill.

---

## What Does NOT Go in /session-kit:start

- **Sub-skill bootstrap logic** — that lives in each sub-skill, loaded via the Skill tool. /session-kit:start orchestrates the calls; it does not redefine or inline the sub-skills' bootstraps.
- **Project-specific content** — the smart defaults are opinionated starter values, not project content. Users edit NOTES.md, AGENTS.md, etc. after bootstrap to put real content in.
- **Ongoing operations** — once bootstrap is done, /session-kit:start steps out. Use the individual skills (`/notes`, `/stable-label`, etc.) for ongoing work.
- **Skill installation** — /session-kit:start assumes the session-kit plugin is already installed. It doesn't install plugins.

---

## How It Fits

```
User runs /session-kit:start
        ↓
Detect tier + project state, apply smart defaults
        ↓
Present unified plan (one approval prompt)
        ↓
Execute in dependency order:
    /warmup → /notes → /stable-label → /fast-chat → [/dictation → /foo]
        ↓
All files written atomically, canary line emitted
        ↓
Ongoing work uses the individual skills directly
```

/session-kit:start is the on-ramp to session-kit. The individual skills remain independently usable — but for a fresh project or a fresh install, /session-kit:start replaces the multi-step ritual with one approval.
