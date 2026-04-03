---
name: feedback-foo
version: 0.2.0
description: "Process improvement — pattern detection, observation tracking, and discipline creation. FOO stands for Feedback, Observation, Oversight — a bucket concept for items observed in the wild that need triage or action. Proactively notices recurring patterns and tracks process observations with a resolution lifecycle. Use when the user asks to 'feedback-foo', 'feedback', 'foo', 'observation', 'meta-feedback', 'process observation', 'track friction', 'add pattern', 'create discipline', 'improve process', 'add an observation', 'add a feedback item', or notices a recurring process issue. Also proactively trigger when you notice a pattern that's appeared twice or more but isn't written down, when process friction keeps recurring without being tracked, when an informal habit should be formalized as a named discipline, or when the user corrects your behavior in a way that suggests a missing convention. These observations are most valuable while the context is fresh — surface them immediately, don't save them for later."
user-invocable: true
---

# /feedback-foo — Process Improvement

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.

Make the process itself get better over time. FOO = **F**eedback, **O**bservation, **O**versight — a bucket concept for items observed in the wild that need triage or action. /feedback-foo combines three capabilities: detecting patterns the agent notices, tracking observations with a resolution lifecycle, and formalizing important workflows as named disciplines.

The core insight: if you've seen it twice, it's a pattern. If it's not written down, it will be forgotten by the next session.

---

## The Job

1. **Always-on detection**: notice recurring patterns, conventions, drift, or friction that isn't captured in project instructions. Surface observations immediately — the context is most valuable while it's fresh.
2. **On explicit invocation**: show current observations, their lifecycle states, and available actions (add, promote, resolve, create discipline).

---

## The Three Capabilities

### 1. Pattern Detection

Proactively notice what's not written down. This applies to everything: naming conventions, commit patterns, file organization, review workflows, testing strategies, communication preferences. The responsibility to notice and propose is the agent's — the human approves all changes.

**Detection sources:**

- **Conversation patterns** — the user repeatedly corrects the same behavior, always rejects a certain kind of suggestion, or consistently asks for something a specific way. These are conventions waiting to be written down.
- **User interaction style** — how the user responds reveals preferences: terse answers, shorthand use, frustration with ceremony. These are /fast-chat or /dictation entries waiting to happen, or process observations worth capturing.
- **Agent self-observation** — you notice you made the same mistake twice, or that a workflow you follow is inefficient. You're a source of observations too.
- **Project artifacts** — git history reveals commit patterns, AGENTS.md and/or CLAUDE.md directives that aren't being followed reveal drift, code review comments reveal recurring concerns.
- **Cross-session signals** — prior NOTES.md entries, existing FEEDBACK_FOO.md entries that keep recurring after being resolved, auto-memory entries that feel stale or incomplete.

**Detection triggers:**
- You've done the same thing twice without it being documented
- The user corrects your behavior — suggests a missing convention
- You notice drift between what's documented and what's practiced
- A workflow has recurring friction at the same point
- A resolved FEEDBACK_FOO.md entry keeps coming back — the fix didn't stick

**When you detect something**, surface it immediately with a concrete proposal. Don't just observe — propose where to write it down and what to write. The user decides whether to accept.

### 2. Observation Tracking

Not every observation is ready to become policy. Some need to be captured, watched, and confirmed before they're worth formalizing. FEEDBACK_FOO.md is the holding area — observations with IDs, lifecycle states, and promotion paths.

#### FEEDBACK_FOO.md Format

```
# FEEDBACK_FOO.md
<!-- managed by /foo -->

## Open

### FOO_1: Agents keep skipping the consistency pass after renames [convention]

Noticed twice (sessions 3 and 5). After renaming a file or variable, agents
proceed without checking for stale references. May need a discipline or a
CLAUDE.md rule.

### FOO_2: Review cycles take 3 round-trips when 1 would suffice [friction]

The "anything else?" pattern forces multiple rounds. /fast-chat's review
prompt helps but agents don't always use it.

## Resolved

### FOO_3: Commit messages inconsistent across sessions [convention]

`[resolved]` → Added commit style section to CLAUDE.md. Themed bullet lists
with verb-prefixed subject lines.
```

#### Entry Format

Each entry has:
- **ID** — `FOO_N` (Feedback/Observation/Oversight), append-only (follows /stable-label convention). If the project uses /stable-label, add `FOO` to the prefix table during bootstrap.
- **Title** — concise description of the observation
- **Tags** — category tags in brackets: `[convention]`, `[friction]`, `[drift]`, `[workflow]`, `[tooling]`
- **Body** — what was observed, how many times, context
- **Resolution** — what changed and where

#### Lifecycle States

Entries live in sections by state:

- **Open** — observed but not yet acted on. May need more data points before acting.
- **Resolved** — artifact changes committed. Note which files changed and what was done. Optionally note confidence: `[resolved, unverified]` if the fix hasn't been tested in a real session yet, or just `[resolved]` once confirmed working.

Move entries between sections as their state changes. Resolved entries can be archived or kept as a record.

### 3. Discipline Creation

A discipline is a named set of behavioral rules that makes a specific practice reliable. When a pattern is confirmed and important enough to enforce, /foo helps express it as a discipline block for AGENTS.md and/or CLAUDE.md.

**Discipline block structure:**

```
## [Name] Discipline
<!-- managed by /foo -->

**[One-sentence imperative stating the core rule.]**

1. First rule — specific, actionable
2. Second rule — specific, actionable
3. ...

[Optional: rationale paragraph explaining why this discipline exists]
```

**What makes a good discipline:**
- **Scannable** — each rule is numbered and imperative
- **Enforceable** — rules are concrete enough to verify compliance
- **Composable** — disciplines can reference each other

**Disciplines are prose-based, and prose has limits.** Disciplines work well for judgment calls, adaptation, and decision-making — where non-determinism is a feature. But when a discipline enforces format compliance, schema adherence, or consistency rules, agents may drift over many invocations because prose is re-interpreted each time. If a prose discipline keeps getting violated, consider supplementing it with tooling (e.g., a validation script shipped alongside the skill in `scripts/`). The escalation pattern: define the rule in prose first → if agents drift → build a tool that makes compliance automatic. Not every discipline needs tooling — most won't — but recognizing when prose alone isn't working is part of /foo's job.

**When to create a discipline:**
- A pattern has been observed multiple times and confirmed
- The stakes of non-compliance are high (lost work, consistency failures, wasted cycles)
- A simple NOTES.md entry isn't sufficient — the behavior needs to be enforced every session

Individual skills (like /notes) can create their own disciplines during bootstrap. /foo handles disciplines that don't belong to any specific skill — cross-cutting process rules.

**Breadcrumb ownership:** when a discipline block is managed by both /foo (content) and /warmup (loading), the breadcrumb lists both: `<!-- managed by /warmup and /foo -->`. No need to pick one.

---

## Bootstrap

When invoked on a project for the first time:

1. **Check for existing process observations** — scan AGENTS.md and/or CLAUDE.md, NOTES.md, and conversation history for informal observations, corrections, or conventions that aren't written down.

2. **Create FEEDBACK_FOO.md** — initialize with any observations found during the scan. If none found, create an empty scaffold. The scaffold should note its origin and purpose:

   ```
   # FEEDBACK_FOO.md
   <!-- managed by /foo -->

   Process observations that need active lifecycle tracking. FOO = Feedback,
   Observation, Oversight — items observed in the wild that need triage or
   action. Observations start in NOTES.md; promote here when they need
   monitoring across sessions. See /foo for detection sources, routing, and
   discipline creation.

   ## Open

   ## Resolved
   ```

3. **Add self-improvement directive to AGENTS.md and/or CLAUDE.md** — a concise directive telling the agent to notice and surface patterns proactively. Mark with `<!-- managed by /foo -->`.

   ```
   ## Self-Improvement
   <!-- managed by /foo -->

   When you notice a recurring pattern, convention, drift, or friction not yet
   captured in project instructions — surface it immediately and propose where
   to write it down. If you've seen it twice, it's a pattern.

   The human approves all changes. Your job is to notice and propose.
   ```

4. **Inform the user** — explain the three capabilities (detection, tracking, disciplines) and that /foo is always-on for detection, invocable for tracking and discipline management.

---

## Ongoing Operations

### Routing observations

All observations start in **NOTES.md** — both project decisions and process observations. NOTES.md is the single intake point. /foo doesn't maintain a separate intake queue.

From NOTES.md, process observations can be:
- **Promoted to FEEDBACK_FOO.md** — when they need lifecycle tracking (open → resolved). Not everything needs this — only observations worth actively monitoring.
- **Promoted to AGENTS.md and/or CLAUDE.md** — when a pattern is confirmed and ready to enforce as a directive or discipline.

/foo should periodically scan NOTES.md for process-relevant entries that might benefit from tracking or formalization — patterns hiding in plain sight that haven't been promoted yet.

### Promoting observations

When an observation is ready to move:

1. **NOTES.md → FEEDBACK_FOO.md** — a process observation in NOTES.md needs active tracking. Create a FOO entry, cross-reference the NOTES.md entry.
2. **NOTES.md → AGENTS.md and/or CLAUDE.md** — a pattern in NOTES.md is confirmed and ready to enforce. Write a directive or discipline directly.
3. **FEEDBACK_FOO.md → AGENTS.md and/or CLAUDE.md** — a tracked observation is resolved by writing a directive or discipline. Mark the FEEDBACK_FOO.md entry as resolved with a pointer to what changed.

### When invoked on an existing project

1. Show current FEEDBACK_FOO.md state — open observations, recently resolved
2. Ask what the user wants to do — add an observation, promote one, create a discipline, review open items
3. Operate accordingly

### Suggesting observations proactively

When detection fires, keep the suggestion lightweight. One or two sentences, a concrete proposal, and move on. Don't interrupt the user's flow with a ceremony.

Good: "I've noticed we always run a consistency pass after renaming — want me to note that in NOTES.md, or is it confirmed enough for a CLAUDE.md discipline?"

Bad: "I have detected a potential process improvement opportunity. Let me create a detailed analysis of the pattern I've observed across multiple sessions..."

---

## What Does NOT Go in /foo

- **Project decisions** — project decisions stay in NOTES.md. Process observations start in NOTES.md too, but get promoted to FEEDBACK_FOO.md when they need lifecycle tracking. "We chose PostgreSQL" stays in /notes. "The agent keeps forgetting to check the migration" starts in /notes and gets promoted to FEEDBACK_FOO.md if it needs active monitoring.
- **Bug reports** — /foo is about process friction, not code defects. A bug is a code problem; a process observation is about how you work.
- **Skill implementation** — /foo can identify that a skill's behavior is inconsistent, but the fix goes in the skill's SKILL.md, not in FEEDBACK_FOO.md.
- **Content for other artifacts** — /foo routes observations to the right place. It doesn't own the content once it arrives at NOTES.md or CLAUDE.md.

---

## How It Fits

```
Always-on detection         → notices patterns, drift, friction
                               (proactive — doesn't wait to be asked)

NOTES.md                    → single intake point for all observations
                               (project and process, captured together)

FEEDBACK_FOO.md             → process observations that need tracking
                               (promoted from NOTES.md, open → resolved)

AGENTS.md and/or CLAUDE.md  → disciplines and directives
                               (promoted from confirmed patterns)
```

/foo is the feedback loop that makes everything else improve. Without it, process observations live in conversation and die with the session. With it, friction becomes tracked observations, confirmed patterns become disciplines, and the process improves over time.
