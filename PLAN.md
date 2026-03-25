# PLAN.md — session-kit

## Current Status

All 6 skills implemented and eval'd. Findings applied to 5 of 6 (sharpen needed none).

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

### 6. Eval: /warmup ✓

9 test pairs. Key finding: full layered infrastructure is the differentiator — baseline handles individual concepts but doesn't build the complete system. Fixed over-trigger on unrelated requests. Adopted two baseline innovations: cross-file reinforcement loop and content quality diagnosis.

### 7. Eval: /sharpen ✓

8 test pairs. First skill where the eval confirmed the design — no adjustments needed. Strongest differentiators: evals 5-6 (recurring failures treated as process improvement, not just apologies). Prose→tooling escalation is unique to the skill. Caveat: proactive detection untestable in single-turn evals, added to Things to Monitor.

### 8. Plugin bundles ✓

Designed and implemented three bundles: session-kit (full), session-kit-core (/warmup, /fast-chat, /dictation), session-kit-refine (/notes, /stable-label, /sharpen). Symlinks from bundle skills/ directories to root skills/. Marketplace metadata bumped to 0.2.0.

### 9. Publish ✓

Published to GitHub marketplace.

### 10. README: How to Use section, skill reordering, drop bundles ✓

Added How to Use section with setup/ongoing for each skill. Added "Best for" lines to The Skills section. Reordered all sections to consistent order (warmup, fast-chat, dictation, notes, stable-label, sharpen). Removed bundle install options — skills are inert without explicit setup, so bundles add complexity without value.

### 11. Remove bundles from marketplace ✓

Removed session-kit-core and session-kit-refine from marketplace.json, deleted bundle directories, bumped plugin version to 0.5.0.

### 12. HELP.md and Quick Reference convention ✓

Added HELP.md files to all 6 skills (seeded from README How to Use section). Added Quick Reference blockquote to top of each SKILL.md with directive to read HELP.md for usage questions and escalation path to full SKILL.md for edge cases. Plugin version bumped to 0.6.0.

### 13. SPI_4, SPI_5, SPI_6 — sharpen-driven skill updates ✓

Applied three process observations from SHARPEN.md:
- SPI_5: /fast-chat review prompt redesigned (R/O tail, silence-is-not-approval, drop S and A-E layout)
- SPI_4: /warmup escalation ladder gets concrete language-strengthening tactics
- SPI_6: /notes suggested section order reordered (stable reference first, decision log after)

## Next Steps

### 14. Description optimization

Run the skill-creator trigger optimization loop on each skill's description to improve triggering accuracy.
