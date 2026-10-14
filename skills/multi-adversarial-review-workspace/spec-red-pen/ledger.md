# Ledger: spec review of /red-pen v0.3.0

Append-only. Two records per stage: launch and terminal.

- LAUNCH stage-1-glm | baseline b58cc31 | target spec (a skill: instructions an agent follows) | route pi zai/glm-5.3 thinking high, text mode | one reviewer | capability: No Writing Anywhere (tools read,grep,find,ls; outer sandbox nono, so prompt-plus-audit) | worktree: scratch, detached at baseline; WRITING_DIRECTIVES.md snapshot sha256 e4647810 | started 2026-10-13 | ceiling 25m
- TERMINAL stage-1-glm | route-failed | pi exited 0 with stdout empty and stderr "Connection error." | smoke prompt failed the same way; cn fallback failed the same way ("Connection error."); api.z.ai fails TLS through the sandbox proxy ("certificate has expired"); TLS checks were not bypassed | OpenCode not installed | write audit clean | findings: none (no review ran) | ended 2026-10-14T01:52Z | chain degraded: GLM family absent
- LAUNCH stage-1b-claude | baseline b58cc31 | target spec | route Claude subagent (general-purpose), same host as the lead: a sanity pass, not an independent gate | same prompt as stage-1 | capability: No Writing Anywhere (prompt-plus-audit) | worktree: scratch, detached at baseline | started 2026-10-14T01:55Z | ceiling 25m
