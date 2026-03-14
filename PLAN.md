# PLAN.md — session-kit

## Current Status

All 6 skills implemented: `/notes`, `/warmup`, `/stable-label`, `/fast-chat`, `/dictation`, `/sharpen`. First eval pass completed on `/notes` — findings applied.

## Next Steps

### 1. Re-evaluate EXTRACTABLE.md

Review `../plet-skills/EXTRACTABLE.md` with fresh eyes now that all 6 skills are built. The original extractable list was written before implementation — some patterns may have shifted, new patterns may have emerged during the build, and the sparkboard reference implementation may suggest gaps or overlaps we didn't see before.

**Goal:** Identify anything we missed, anything that should change, and confirm the current skill set is complete.

### 2. Eval: /dictation (easiest)

Run evals on `/dictation`. Test bootstrap (correction table seeding), silent correction application, disambiguation behavior, and the learning loop (offering to add new corrections). Smallest skill, most straightforward behavior.

### 3. Eval: /stable-label

Run evals on `/stable-label`. Test bootstrap (prefix table creation), ID assignment, consistency passes, and lifecycle operations (split, merge, deprecation).

### 4. Eval: /fast-chat

Run evals on `/fast-chat`. Test NL/NLR formatting, batch answer parsing, review prompt generation, and the always-on communication style (does it adopt the patterns without being asked?). The always-on behavior makes this trickier to eval than the explicitly-invoked skills.

### 5. Eval: /warmup

Run evals on `/warmup`. Test bootstrap, compaction recovery, canary setup, and loading diagnostics. Compare with-skill vs baseline. Harder to eval because the value is cross-session — hard to test in a single subagent run.

### 6. Eval: /sharpen (hardest)

Run evals on `/sharpen`. Test pattern detection (does it notice things?), observation tracking (SHARPEN.md lifecycle), discipline creation, and the routing model (NOTES.md as intake → SHARPEN.md for tracking → CLAUDE.md for enforcement). Hardest because the always-on detection is the core value and it's inherently multi-turn.

### 7. Apply eval findings

After all evals complete, apply findings to each skill (as done with /notes). May include description optimization via skill-creator's trigger optimization loop.
