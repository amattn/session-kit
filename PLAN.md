# PLAN.md — session-kit

## Current Status

All 6 skills implemented. Evals completed and findings applied for 4 of 6 skills: `/notes`, `/dictation`, `/stable-label`, `/fast-chat`.

## Completed

### 1. Re-evaluate EXTRACTABLE.md ✓

Found the "Skills for Judgment, Code for Compliance" insight — prose disciplines drift, supplement with tooling when needed. Applied to /sharpen.

### 2. Eval: /notes ✓

10 test pairs. Key finding: CLAUDE.md discipline block is the killer feature. Adjustments: "quote the user, paraphrase everything else," bootstrap seeds Open Questions as an offer. Value-add sections moved from skills to README.

### 3. Eval: /dictation ✓

8 test pairs. Key finding: structured disambiguation is the main differentiator. Bootstrap format (CLAUDE.md with breadcrumb) matters. Adjustments applied.

### 4. Eval: /stable-label ✓

15 test pairs (11 + 4 lifecycle). Key findings: convention enforcement is the biggest win, lifecycle operations (split, merge, promote, crosscut) are the strongest differentiator. Added read/analyze vs create/modify heuristic for when NOT to assign IDs.

### 5. Eval: /fast-chat ✓

8 test pairs. Key finding: behavioral activation is the primary value — Claude knows the patterns but doesn't consistently use them without the skill. Eval 6 over-trigger noted as eval artifact, added to Things to Monitor.

## Next Steps

### 6. Eval: /warmup ✓

9 test pairs. Key finding: full layered infrastructure is the differentiator — baseline handles individual concepts but doesn't build the complete system. Fixed over-trigger on unrelated requests. Adopted two baseline innovations: cross-file reinforcement loop and content quality diagnosis.

### 7. Eval: /sharpen (hardest)

Test pattern detection, observation tracking (SHARPEN.md lifecycle), discipline creation, and the routing model (NOTES.md as intake → SHARPEN.md for tracking → CLAUDE.md for enforcement). Hardest because always-on detection is inherently multi-turn.

### 8. Description optimization

After all evals complete, run the skill-creator trigger optimization loop on each skill's description to improve triggering accuracy.

### 9. Publish

Push to GitHub, set up marketplace listing.
