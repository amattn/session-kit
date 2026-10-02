# Owner rulings on the deferred findings

Ruled 2026-10-02, after stage 2.

| Question | Findings | Ruling | Applied |
|---|---|---|---|
| Session count in the intro | E-F1, U-F1, E-F5, U-F9 | "hundreds of sessions" | Yes, in stage 2 |
| Which skill first | E-F3, E-F6 | Reorder by usefulness: stable-label, fast-chat, multi-adversarial-review, notes, red-pen, warmup, dictation, feedback-foo, in all four README sections | Yes |
| Install copies the eval workspaces | stage 2 E-F1 | Skip `*-workspace` directories | Yes: `rsync --exclude` in options 2 and 3 |
| /dictation example corrects "Maine" silently | E-F2, U-F6 | Keep: "the Maine branch" is the unambiguous case the confirm rule exempts | No change; finding closed as `rejected` on the owner's ruling |
| /notes section claims | stage 2 E-F8 | Soften to what the evals showed | Yes: "a common failure mode", "much less likely", "the same suggested sections" |
| /stable-label example adds "(p95)" | U-F4 | Make the example consistent without the p95 | Yes, in README and HELP.md; /stable-label v0.1.2 |
| "8+ parts" in Origin | E-F5, U-F9 | Not yet ruled | Open |
