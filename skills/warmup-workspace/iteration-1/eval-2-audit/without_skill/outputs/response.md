# Loading Setup Audit — inventory-api

## Summary

The current loading setup has significant gaps. Key files will likely load at session start because CLAUDE.md references them, but the setup lacks compaction resilience, verification, and specificity. A session that undergoes compaction will probably lose NOTES.md context with no mechanism to recover or detect the loss.

---

## What's Working

1. **CLAUDE.md exists and references NOTES.md.** The Required Reading section lists `NOTES.md` as institutional memory, and the Key Files section also references it. Claude Code will read CLAUDE.md automatically at session start, so NOTES.md will likely be loaded on the first pass.

2. **NOTES.md Discipline is present.** The imperative rule "Update NOTES.md after every decision, before moving to the next topic" is bolded and direct — good compaction-resistant wording.

3. **NOTES.md itself is well-structured.** Short, scannable, with a clear decision record (PostgreSQL over SQLite). Easy for the agent to consume.

---

## Gaps Found

### 1. No Post-Compaction Rule (Critical)

CLAUDE.md has no instruction telling the agent to re-read Required Reading files after context compaction. When compaction occurs mid-session, the agent will lose the contents of NOTES.md and have no rule telling it to reload. This is the single biggest reliability gap.

**Impact:** After compaction, the agent will forget project decisions (e.g., the PostgreSQL choice) and may re-litigate settled questions.

### 2. No Loading Canaries (Significant)

There is no verification mechanism to confirm that NOTES.md was actually read. No acknowledgment canary ("Loaded: NOTES.md. Ready."), no behavioral canary (e.g., "state the project name and database choice at session start"), and no content canary.

**Impact:** If loading silently fails, neither the user nor the agent will know. The user has to manually check whether the agent knows about PostgreSQL, deployment conventions, etc.

### 3. Required Reading Lacks Compaction Trigger (Moderate)

The Required Reading section says "Load these files at the start of every session" but does not mention compaction. The phrasing should include "and after any context compaction" to establish re-reading as a rule.

### 4. No Auto-Memory Entries (Moderate)

There are no auto-memory entries for critical behaviors. Auto-memory loads before CLAUDE.md and survives compaction by design. The NOTES.md discipline ("update NOTES.md after every decision") is a strong candidate for auto-memory because it's a non-negotiable behavior that gets lost when CLAUDE.md is compacted.

### 5. No Breadcrumbs (Minor)

Sections lack `<!-- managed by /warmup -->` markers. This is cosmetic but means there's no easy way to identify which sections are managed by tooling vs. hand-written.

### 6. Redundant Key Files Section (Minor)

NOTES.md appears in both "Required Reading" and "Key Files" sections. This isn't harmful, but the two sections serve overlapping purposes. "Required Reading" is the actionable one (it tells the agent to load files); "Key Files" is informational. If compaction aggressively summarizes, it may merge or drop one, losing the loading instruction.

---

## Reliability Rating

| Aspect | Rating | Notes |
|---|---|---|
| Initial session load | Fair | CLAUDE.md references NOTES.md; likely loaded but unverified |
| Compaction survival | Poor | No post-compaction rule; no re-read trigger |
| Load verification | None | No canaries of any type |
| Wording resilience | Fair | Discipline block is well-worded; Required Reading is adequate |
| Defense in depth | Poor | Single layer only (CLAUDE.md); no auto-memory backup |

---

## Recommendations

1. **Add a Post-Compaction Rule** to CLAUDE.md instructing the agent to re-read all Required Reading files after compaction.
2. **Add an acknowledgment canary** — e.g., "After reading Required Reading files, respond with: Loaded: [list files]. Ready."
3. **Update Required Reading wording** to include "and after any context compaction."
4. **Create an auto-memory entry** for the NOTES.md discipline as a compaction-resistant backup.
5. **Consider a behavioral canary** such as "Begin each session by stating the database engine choice from NOTES.md" — this makes load failure immediately visible.
