# Ledger: copy review of README.md

Append-only. Two records per stage: launch and terminal.

- LAUNCH stage-1-glm | baseline 3c81a3f | target copy | route pi zai/glm-5.3 thinking high, text mode | lenses: reader-evaluator, reader-user (parallel, blind to each other), each with the record lens | capability: No Writing Anywhere (tools read,grep,find,ls; outer sandbox nono, so prompt-plus-audit) | worktree: scratch, detached at baseline | started 2026-10-02T22:09Z | ceiling 20m
- TERMINAL stage-1-glm | completed | both lenses exit 0 | outputs 623 and 582 words | write audit clean (primary and worktree) | note: one reviewer reported its grep and find tools failed and fell back to direct reads | findings 8 after dedup: 5 fixed, 2 deferred to owner, 1 rejected | ended 2026-10-02T22:12Z
- LAUNCH stage-2-codex | baseline be4d8f6 | target copy | route codex exec, CLI default model, reasoning effort high, -s danger-full-access under the confirmed outer sandbox (nono) | lenses: reader-evaluator, reader-user (parallel), each with the record lens; cumulative on the stage-1 disposition | capability: No Writing Anywhere (prompt-plus-audit) | worktree: scratch, detached at baseline | started 2026-10-02T22:12Z | ceiling 25m
- TERMINAL stage-2-codex | completed | both lenses exit 0 | model gpt-6-astra, effort high (CLI default tier, recorded, not pinned) | write audit clean | findings 15 after dedup: 9 fixed, 6 deferred to owner (1 already ruled), 0 rejected | ended 2026-10-02T22:17Z
