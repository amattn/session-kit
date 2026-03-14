# Loading Setup Audit — inventory-api

## Summary

The loading setup is **partially configured**. The foundation is there (Required Reading section, NOTES.md Discipline), but several reliability layers are missing. As it stands, loading will work in fresh sessions when the agent cooperates, but there is no verification that loading happened and no recovery mechanism after context compaction.

## What's Working

1. **Required Reading section exists** — lists `NOTES.md` as required at session start.
2. **NOTES.md Discipline block exists** — core rule ("update after every decision, before moving to the next topic") is present and well-worded: imperative, bold, short.
3. **NOTES.md itself is well-structured** — has project context and design decisions, ready to serve as institutional memory.

## What's Missing

### 1. Post-Compaction Rule — HIGH priority

There is no instruction for what to do after context compaction. If the context gets compressed mid-session, the agent has no directive to re-read Required Reading files. NOTES.md and the discipline rules will silently drop out of context.

**Recommendation:** Add a Post-Compaction Rule section:
```
## Post-Compaction Rule
<!-- managed by /warmup -->

After context compaction, immediately re-read all files listed in Required Reading.
Acknowledge what was loaded before continuing work.
```

### 2. Loading Canaries — HIGH priority

There is no mechanism to verify that Required Reading files were actually consumed. Without canaries, a session could proceed with NOTES.md unread, and neither the user nor the agent would notice until a decision gets re-litigated.

**Recommendation:** Add at least an acknowledgment canary:
```
## Session Start
<!-- managed by /warmup -->

After reading all Required Reading files, respond with:
"Loaded: [list files read]. Ready."
```

### 3. Required Reading — incomplete wording

The current wording says "Load these files at the start of every session" but does not mention compaction recovery. It should also say "and after any context compaction" to work in tandem with the Post-Compaction Rule.

### 4. Breadcrumbs — LOW priority

No `<!-- managed by /warmup -->` comments on any section. These are not load-bearing, but they help /warmup quickly find and update its own sections and signal to the user that the section is managed.

### 5. Redundant Key Files Section

`NOTES.md` is listed in both Required Reading and Key Files. The Key Files section adds no information that Required Reading doesn't already cover. Consider removing Key Files or using it only for files that are reference material (not required reading).

### 6. Auto-Memory — situational

No auto-memory entries exist. For a project using Claude Code, auto-memory is the deepest reliability layer and would ensure the NOTES.md discipline survives even aggressive compaction. This is optional but recommended if loading reliability becomes a problem.

## Bottom Line

The setup has the right intent but is missing the verification and recovery layers. Adding a Post-Compaction Rule and an acknowledgment canary would meaningfully improve reliability. Those two additions would take the setup from "works when things go well" to "works and you'll know when it doesn't."
