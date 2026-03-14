---
name: warmup
version: 0.1.0
description: "Session bootstrap and compaction recovery. Ensures skills, disciplines, and key files load reliably at session start and survive context compaction. Sets up canaries to verify loading and keep the user informed. Use when the user asks to 'warmup', 'bootstrap', 'start session', 'reload context', 'set up required reading', or when the user says 'I lost context', 'reload after compaction', 'this keeps getting forgotten', 'make sure X loads reliably'. Also trigger when a skill needs reliable loading or when AGENTS.md and/or CLAUDE.md needs compaction-resistant structure. Also proactively trigger at the start of a fresh session if no acknowledgment canary fires, when you detect a compaction event mid-conversation and Required Reading may need reloading, or when you notice a project has AGENTS.md and/or CLAUDE.md but no Required Reading section or compaction recovery rules — these are projects that would benefit from /warmup even if the user hasn't asked for it."
user-invocable: true
---

# /warmup — Session Bootstrap & Compaction Recovery

Ensure skills, disciplines, and key files load reliably at session start and survive context compaction. /warmup is the reliability layer — it uses every tactic available to guarantee that what matters gets loaded.

---

## The Job

1. Detect the current state of the project's AGENTS.md and/or CLAUDE.md
2. Assess what's already set up: Required Reading, discipline blocks, canaries, auto-memory
3. Bootstrap what's missing, or modify what's not working reliably

---

## Tactics

/warmup uses whatever works. These are ordered from deepest (most reliable) to shallowest:

### 1. Auto-Memory Entries

The strongest tactic where available. Auto-memory loads before or alongside project-level directive files — it's present from the very first message of every session, even before the agent reads project files. For example, Claude Code loads memory before CLAUDE.md; Codex CLI runs an async extraction pipeline at startup that populates MEMORY.md. Native in Claude Code and Codex CLI; plugin-based in OpenCode; not available in Cursor. See § Agent Harness Reference for details.

Use for:
- Non-negotiable behaviors that must never be forgotten (e.g., "always read NOTES.md")
- Compaction-critical rules that get lost when context is compressed
- Behavioral seeds that should be present even in projects without AGENTS.md or CLAUDE.md

When bootstrapping auto-memory:
- Write entries to the project's auto-memory directory
- Keep entries short — prefer pointers to existing artifacts (AGENTS.md, CLAUDE.md, NOTES.md) over duplicated content. Full duplication of a discipline or directive is acceptable as a fallback when the pointer/reference tactic isn't working reliably.
- One behavior per memory file
- Use the `feedback` or `user` memory type as appropriate
- Update MEMORY.md index

### 2. AGENTS.md and/or CLAUDE.md Structure

The primary project-level mechanism. /warmup helps structure AGENTS.md and/or CLAUDE.md with sections that load reliably and survive compaction.

#### Required Reading Section

A list of files the agent must read at session start and re-read after compaction:

```
## Required Reading
<!-- managed by /warmup -->

Load these files at the start of every session and after any context compaction:

- `NOTES.md` — institutional memory
- `[other key files as needed]`
```

#### Discipline Blocks

Named behavioral rule sets that enforce specific practices. The discipline framing works well in AGENTS.md and/or CLAUDE.md because it's:
- Scannable — each discipline has a name and numbered rules
- Enforceable — rules are imperative, not suggestive
- Composable — disciplines can reference each other

Example discipline block:

```
## NOTES.md Discipline
<!-- managed by /warmup -->

**Update NOTES.md after every decision, before moving to the next topic.**
[... rules ...]
```

#### Post-Compaction Rule

Explicit instruction for what to do after compaction:

```
## Post-Compaction Rule
<!-- managed by /warmup -->

After context compaction, immediately re-read all files listed in § Required Reading.
Acknowledge what was loaded before continuing work.
```

#### Loading Canaries

Canary rules live in AGENTS.md and/or CLAUDE.md alongside Required Reading. They verify that loading actually happened. See § Loading Canaries below for canary types and setup guidance.

### 3. Loading Canaries

Verification mechanisms that prove files were actually consumed, not just referenced. A canary is a piece of content that, if the agent hasn't loaded it, will be obviously missing from its behavior.

Types of canaries:

- **Acknowledgment canary** — a rule in AGENTS.md and/or CLAUDE.md requiring the agent to explicitly acknowledge what it loaded. If the acknowledgment is missing, the files weren't read. Example:
  ```
  ## Session Start
  <!-- managed by /warmup -->

  After reading all Required Reading files, respond with:
  "Loaded: [list files read]. Ready."
  ```

- **Behavioral canary** — a rule that produces visible behavior. Absence of the behavior = files weren't loaded. Examples:
  - Begin every session by stating the current project name and the number of open questions in NOTES.md.
  - Start each session with a short joke.
  - Open with a one-line summary of the current git status.

- **Content canary** — a specific fact or convention in a loaded file that, if unknown, proves the file wasn't consumed. Examples:
  - A convention defined only in NOTES.md (e.g., "we call the deployment target 'nimbus'"). If the agent doesn't know the term, NOTES.md wasn't loaded.
  - "Summarize the most important and critical directives as you understand them from AGENTS.md and/or CLAUDE.md." If the summary is vague or generic, the file wasn't consumed.

When setting up canaries:
- Prefer behavioral canaries — they're self-verifying without requiring the user to check
- Keep canaries lightweight — they should verify loading, not add overhead
- Place canary rules in AGENTS.md and/or CLAUDE.md near the Required Reading section

### 4. Reliability Guidance

Sometimes system prompts, context limits, or agent behavior fight against AGENTS.md and/or CLAUDE.md directives. /warmup includes guidance for these situations:

- **Wording that survives compaction** — use imperative, bold, short sentences. Long paragraphs get summarized away; punchy rules persist.
- **Redundancy** — critical rules appear in both auto-memory and AGENTS.md and/or CLAUDE.md. Belt and suspenders.
- **Positioning** — put the most critical content near the top of AGENTS.md and/or CLAUDE.md. Content at the top is more likely to survive aggressive compaction.
- **Specificity** — concrete instructions resist summarization. Example:
  - Weak: "Keep context loaded."
  - Strong: "**Read NOTES.md before answering any question.**"

---

## Bootstrap

When invoked on a project for the first time:

1. **Audit AGENTS.md and/or CLAUDE.md** — detect which exists. If neither exists, create AGENTS.md for cross-compatibility, plus a minimal CLAUDE.md that points to it. Read the current state. Identify what's already set up (discipline blocks, key file references, etc.) and what's missing.
2. **Set up auto-memory** — create memory entries for non-negotiable behaviors (deepest layer first).
3. **Add Required Reading section** — list files that must be loaded every session. Include any files already referenced as "key files."
4. **Add Post-Compaction Rule** — explicit re-read instruction.
5. **Set up canaries** — add at least one acknowledgment canary. Suggest behavioral canaries if appropriate.
6. **Add breadcrumbs** — mark /warmup-managed sections with `<!-- managed by /warmup -->` comments so users know what the skill created.
7. **Inform the user** — explain what was set up, how canaries work, and how to invoke /warmup to add more. Mention that /warmup takes feedback: if any rule seems inconsistently loaded or applied, the user can invoke /warmup to strengthen wording or escalate tactics to increase efficacy.

---

## Ongoing Operations

### Adding a new skill to the loading chain

When another skill needs reliable loading (e.g., /notes needs NOTES.md loaded every session):

1. Add the file to the Required Reading section in AGENTS.md and/or CLAUDE.md
2. Optionally add a discipline block for the skill's behavioral rules
3. Optionally add an auto-memory entry for the skill's most critical behavior
4. Mark new sections with `<!-- managed by /warmup -->`

### Editing existing warmup configuration

When invoked on a project that already has /warmup set up:

1. Show what's currently configured (Required Reading, disciplines, canaries, auto-memory)
2. Ask what the user wants to add, change, or remove
3. Make the changes, preserving breadcrumbs

### Mid-session compaction

When compaction happens mid-conversation, /warmup's role is auditor, not executor. The Post-Compaction Rule (set up during bootstrap) handles re-reading Required Reading files. /warmup checks whether that rule exists and was followed:

1. Verify the Post-Compaction Rule is present in AGENTS.md and/or CLAUDE.md
2. Check canary status — did acknowledgments fire after compaction?
3. If the rule is missing or wasn't followed, flag it and offer to set up or strengthen the rule

/warmup does not re-read files itself — that's the Post-Compaction Rule's job.

### Diagnosing loading failures

When something isn't loading reliably:

1. Check canary status — are acknowledgments present? Are behavioral canaries firing?
2. Check auto-memory — are entries present and correctly typed?
3. Check AGENTS.md and/or CLAUDE.md positioning — is critical content near the top?
4. Check wording — is it imperative and specific, or vague and summarizable?
5. Suggest fixes based on findings

### Strengthening a rule

When a user reports that a rule is inconsistently loaded or applied, escalate through tactics in order:

1. **Tighten wording** — make it shorter, bolder, more imperative
2. **Improve positioning** — move it higher in AGENTS.md and/or CLAUDE.md
3. **Add redundancy** — add the rule to a second location (e.g., both a discipline block and Required Reading)
4. **Promote to auto-memory** — create a memory entry that loads before everything else
5. **Duplicate as fallback** — if pointers aren't working, duplicate the full directive into auto-memory

Each step is a stronger tactic. Start with the lightest intervention that works.

---

## Breadcrumbs

Every section /warmup creates or manages in AGENTS.md and/or CLAUDE.md gets an HTML comment marker:

```
<!-- managed by /warmup -->
```

This serves two purposes:
- **Discoverability** — users see the marker and learn they can use `/warmup` to modify the section
- **Convenience** — /warmup can quickly find its own sections when they're marked

**Breadcrumbs are not load-bearing.** /warmup must be able to audit and operate on AGENTS.md and/or CLAUDE.md by recognizing section structure and content, not just scanning for markers. If someone deletes the comments, /warmup still works — it reads the file and understands what's there. Breadcrumbs are helpful hints, not dependencies.

---

## What Does NOT Go in /warmup

- **Skill-specific logic** — /warmup helps skills load, it doesn't define what they do
- **Skill implementation** — /warmup sets up discipline blocks and Required Reading entries for other skills, but it doesn't write SKILL.md files
- **Content** — /warmup manages the loading structure (Required Reading, canaries, discipline blocks, compaction-resistant wording) within AGENTS.md and/or CLAUDE.md. It doesn't write project documentation or define project-specific conventions.
- **Task tracking** — /warmup isn't a session planner or task manager

---

## How It Fits

```
Auto-memory            → deepest layer, loads before everything
                         (non-negotiable behaviors)

AGENTS.md and/or CLAUDE.md  → project-level config, loaded early
                         (Required Reading, disciplines, canaries)

Key files (NOTES.md…)  → loaded per Required Reading
                         (institutional memory, context)

Canaries               → verification that loading actually happened
                         (acknowledgments, behavioral checks)
```

/warmup is the reliability layer that makes the rest of session-kit trustworthy. Without it, skills depend on agent discretion to read, import, and follow directives in those files. With it, loading is verified and compaction-resistant.

---

## Agent Harness Reference

Different agent harnesses (Claude Code, Codex CLI, OpenCode, Cursor) have different conventions for directive files, discovery, and auto-memory. Read `references/harnesses.md` for the full breakdown of each harness and the cross-compatibility strategy.

Key takeaway: use AGENTS.md as the single source of truth for cross-platform projects. See the reference file for details.
