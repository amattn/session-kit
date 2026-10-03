# /session-kit:start — Help

## What it does

Bootstraps the session-kit skill suite (`/warmup`, `/notes`, `/stable-label`, `/fast-chat`, `/red-pen`, `/dictation`, `/feedback-foo`) in one pass instead of running each individually. Smart defaults + one approval replaces the 10+ questions that the per-skill bootstraps would normally ask.

## When to use it

- Fresh project that you want to set up with session-kit
- You just installed the session-kit plugin and want to enable it
- An existing project missing one or more session-kit pieces (re-run picks up only what's missing)

## When NOT to use it

- You only want one specific sub-skill (just run `/notes`, `/warmup`, etc.)
- The project already has session-kit fully set up (re-running is safe but unnecessary)
- You want to learn how the individual skills work — read their HELP.md files instead

## Usage

```
/session-kit:start              # Standard tier (default)
/session-kit:start minimal      # Just /warmup
/session-kit:start full         # All seven skills that have a setup step
```

You can also say it in prose: "bootstrap session-kit on this project", "init session-kit standard", "set up session-kit with the full tier", etc.

## Tiers

| Tier         | Skills bootstrapped                                                                  |
|--------------|--------------------------------------------------------------------------------------|
| **minimal**  | /warmup                                                                              |
| **standard** | /warmup + /notes + /stable-label + /fast-chat + /red-pen *(default)*                 |
| **full**     | /warmup + /notes + /stable-label + /fast-chat + /red-pen + /dictation + /feedback-foo |

`/multi-adversarial-review` has no setup step, so it is in no tier; it is ready once a second reviewer tool is installed.

## The flow

1. The skill detects your project's state and proposes a plan
2. You approve (`O`), tweak tiers (`B`), or drop into interactive mode (`C`) to customize each sub-skill's bootstrap individually
3. Files are written atomically — AGENTS.md, CLAUDE.md, NOTES.md, plus auto-memory entries

## Files created (standard tier)

```
AGENTS.md           — Required Reading, canary, discipline blocks, conventions
CLAUDE.md           — one-line pointer to AGENTS.md
NOTES.md            — from /notes template, with default prefix table pre-seeded
~/.claude/.../memory/project-<name>.md
~/.claude/.../memory/warmup-session-canary.md
~/.claude/.../memory/MEMORY.md (index)
```

## Defaults you get without asking

- **Stable Label prefixes:** `DEC`, `ICR`, `INS`, `OPN`, `MON`, `TAX`, `FOO`
- **Canary line:** `Loaded: <files>. Git: <status>. Ready.`
- **Project name:** directory basename
- **Project description:** first sentence of README (or empty placeholder)

All overridable in interactive mode or by editing the files after bootstrap.

## Customizing later

After bootstrap, use the individual skills for ongoing work:
- `/notes` — update NOTES.md, suggest reorgs
- `/stable-label` — assign IDs, run consistency passes
- `/warmup` — diagnose loading failures, strengthen directives
- `/fast-chat` — adjust interaction conventions
- `/red-pen` — add a reader roster, edit a document against the writing rules
- `/multi-adversarial-review` (`/mar`) — review committed work with an outside model
- `/dictation` — add voice corrections
- `/feedback-foo` — track process observations

## Re-running

Safe to re-run on a project that already has session-kit. The skill detects existing breadcrumbs (`<!-- managed by /warmup -->`, etc.) and offers to bootstrap only the missing pieces. It will never overwrite breadcrumbed sections without explicit approval.
