# Diagnosis: NOTES.md Discipline Not Being Followed

## Problem

The agent keeps forgetting to update NOTES.md after decisions, despite the discipline being present in CLAUDE.md. This has recurred across three consecutive sessions.

## Findings

Applying /warmup's diagnostic checklist against the current CLAUDE.md:

### 1. No canaries — loading is unverified

There are no acknowledgment, behavioral, or content canaries. There is no way to confirm whether CLAUDE.md or NOTES.md were actually read at session start. The agent may be starting sessions without ever consuming the discipline.

### 2. No auto-memory — the deepest tactic is unused

Auto-memory loads before CLAUDE.md and survives compaction. The NOTES.md discipline exists only in CLAUDE.md, which is the weakest single point of enforcement. If CLAUDE.md is skimmed, summarized, or partially compacted, the discipline vanishes.

### 3. No Post-Compaction Rule

There is no instruction telling the agent to re-read Required Reading after context compaction. If compaction occurs mid-session, the discipline is lost with no recovery path.

### 4. Discipline wording is too thin and summarizable

The entire NOTES.md Discipline block is a single bold sentence:

> **Update NOTES.md after every decision, before moving to the next topic.**

This is vague enough to be summarized away during compaction. It lacks:
- Numbered, imperative rules
- Definition of what counts as a "decision"
- Explicit statement that this is non-optional and non-deferrable
- Consequences or self-check instructions

### 5. No redundancy

The discipline appears in exactly one location (CLAUDE.md). There is no backup in auto-memory, no repetition in a different section, no reinforcement elsewhere. A single point of failure.

### 6. Positioning is suboptimal

The discipline is in the middle of the file, below Required Reading and above Key Files. Critical content should be near the top of CLAUDE.md to maximize survival during aggressive compaction.

## Recommended Fixes (ordered by /warmup escalation ladder)

1. **Tighten wording** — Expand the discipline block with numbered rules, concrete examples of "decisions," and explicit non-deferral language. Make it punchy and resistant to summarization.

2. **Improve positioning** — Move the NOTES.md Discipline block to immediately after the Project section, before Required Reading. Top-of-file content is most compaction-resistant.

3. **Add a Post-Compaction Rule** — Add an explicit instruction to re-read all Required Reading files after compaction and acknowledge what was loaded.

4. **Add canaries** — Add at least an acknowledgment canary ("After reading Required Reading, respond with: Loaded: [files]. Ready.") so the user can verify loading happened.

5. **Promote to auto-memory** — Create an auto-memory entry for the NOTES.md discipline so it loads before CLAUDE.md and persists through compaction. This is the strongest fix and directly addresses the three-session recurrence.

6. **Add redundancy** — With the discipline in both auto-memory and CLAUDE.md, there are two independent loading paths. Even if one fails, the other catches it.

## Root Cause Summary

The discipline exists but has no enforcement mechanism, no compaction resilience, no loading verification, and no redundancy. It is a single thin sentence in the middle of a file with no backup. Three sessions of failure is the expected outcome of this configuration, not an anomaly.
