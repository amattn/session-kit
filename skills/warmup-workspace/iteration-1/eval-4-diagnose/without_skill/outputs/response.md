# Diagnosis: Agent Keeps Forgetting NOTES.md Updates

## The Problem

The agent repeatedly fails to update NOTES.md after decisions, despite the Notes Discipline section being present in CLAUDE.md. This has recurred across three consecutive sessions.

## Root Cause Analysis

The CLAUDE.md Notes Discipline section is too thin to be effective. Comparing the project's current CLAUDE.md to a well-functioning version reveals three specific gaps:

### 1. The instruction is stated but not motivated

The current text is a single bold line:

> **Update NOTES.md after every decision, before moving to the next topic.**

That is the *what* but not the *why* or the *when-it-gets-hard*. A single imperative is easy for the agent to deprioritize when it is deep in a coding task, because nothing explains the consequence of skipping it. The instruction competes with the agent's default drive to answer the user's question, and the default wins.

A working version adds two critical reinforcements:
- "This is not optional and not deferrable" — explicit override of the agent's instinct to batch work.
- "The pattern of 'I'll catch up on notes later' always fails" — names the exact failure mode so the agent can recognize it in itself.

### 2. No guidance for rapid-fire decision sequences

Most note-skipping happens during build/review sessions where the user is making decisions quickly (approve, reject, rename). The current CLAUDE.md gives no protocol for this scenario. The agent falls into a rhythm of processing decisions and never finds a natural pause point to write notes.

A fix would add explicit rules like:
- Each decision gets a NOTES.md entry *before* presenting the next item.
- If you realize you've fallen behind, stop and catch up immediately.
- Batch answers (e.g., "1A, 2C, 3D") still get individual entries.

### 3. No cost framing

The agent has no way to weigh the cost of skipping notes against the cost of the interruption. Adding a concrete framing like "The cost of writing notes is seconds. The cost of lost rationale is re-litigating settled decisions in the next session" gives the agent a heuristic for why the interruption is always worth it.

## Secondary Factor: No Session-Start Verification

The "Required Reading" section tells the agent to load NOTES.md at session start, but there is no instruction to *verify* the file's state or *confirm* understanding of the discipline. The agent loads the file, sees sparse content, and moves on without internalizing the update obligation.

## Recommended Fix

Expand the NOTES.md Discipline section in CLAUDE.md to include:

1. **The explicit override**: "This is not optional and not deferrable."
2. **The named failure mode**: "The pattern of 'I'll catch up on notes later' always fails — decisions accumulate faster than memory, and by the end of a session the rationale is lost."
3. **Rapid-fire protocol**: Per-decision entries before moving on, stop-and-catch-up rule, batch answer handling.
4. **Cost framing**: "The cost of writing notes is seconds. The cost of lost rationale is re-litigating settled decisions in the next session."

These are not new rules. They are the specificity needed to make the existing rule survive contact with real workloads.
