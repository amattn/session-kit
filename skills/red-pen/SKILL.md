---
name: red-pen
version: 0.3.2
description: "Writing directives for every output type — spec/plan, code comments, code and diffs, chat. Makes AI-generated text less painful to read by substituting explicit constraints (counted limits, a named reader, mandatory prioritization, a cut pass) for the editing cost that generated text never pays. Use when the user asks to 'red-pen', 'red pen this', 'tighten this', 'cut this down', 'too long', 'too wordy', 'less fluff', 'stop narrating', 'this reads like AI', 'edit this', 'set up writing conventions', or 'writing directives'. Also apply these rules always-on, without invocation, before writing any spec, plan, design note, code comment, diff, commit message, or chat reply — decide the output type first, then write to its rules. Also trigger the bootstrap flow when setting up a project's AGENTS.md and/or CLAUDE.md if no writing conventions are defined yet."
user-invocable: true
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/*)
---

# /red-pen — Writing Directives

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.

AI-generated text is painful to read. Not because it is wrong, but because it is unedited. A human writer pays for every sentence in time and effort, and that cost acts as a filter: what survives is what the author judged worth the reader's attention. Generated text has no such cost, so nothing filters it.

/red-pen is the editor. It substitutes explicit constraints for the missing cost: counted limits stand in for effort, a named reader stands in for the author's sense of audience, mandatory prioritization stands in for editorial judgment, a required cut pass stands in for revision. The goal is clarity; shorter text is a side effect, not the target.

**This is an always-on writing style, not just a tool you invoke.** Invoking `/red-pen` runs the bootstrap (writes conventions to AGENTS.md and/or CLAUDE.md) or edits a target. The rules themselves apply to everything you write, every time, no setup required.

---

## The Job

1. **Always-on**: before writing anything, decide which output type you are producing (see § Mode Selection), apply that mode's rules, then run the cut pass. If a task spans several types (implement a change, then report back), apply each mode to its part.
2. **On invocation with a target** (`/red-pen PLAN.md`, "red-pen this section"): edit the target against the rules for its mode, then report as § Editing a target says.
3. **On invocation without a target**: detect whether a Writing Conventions block (`<!-- managed by /red-pen -->`) exists in AGENTS.md and/or CLAUDE.md. If not, bootstrap; other style rules the project already has stay, per § Bootstrap step 1. If yes, show the block and ask what to adjust.

---

## The Recognizable Shape

Unedited generated text has a shape. Use this list as the cut-pass checklist — if the draft shows any of these, it is not done.

- **Uniform length.** A trivial point and a hard one get the same number of words, so length stops being a signal of what matters.
- **Uniform pacing.** Human writing speeds through the obvious and slows at the difficult. One tempo gives attention nothing to catch on.
- **Structure without information.** Headers, nested bullets, and bold leads that promise a priority order that isn't there.
- **Completeness instead of compression.** Omitting feels riskier than including, so everything goes in. The reader re-reads what they already believed, hunting for the one thing they didn't.
- **No stance.** Balanced enumeration of options leaves nothing to agree or disagree with.
- **Fluent rather than checkable.** Errors hide in good sentences. The reader wanted to find where this is wrong, and prose makes that hardest.
- **Session narration.** Text that records the process of producing it ("as requested", "I've now updated", "this function takes X") rather than anything the reader needs.
- **A rule stated in more than one place.** The same rule in two sections, so the reader has to check whether the second is a variant. A table and the prose that teaches its rows are not this: they are one rule in two registers, and both stay.
- **A claim with no source.** A number, a cause, or a fact that is in the text because it sounded right, not because the record, the thread, or the source says it. Fluent and unfindable.

The same defaults do different damage in different places: a bloated spec wastes a decision-maker's attention, a narrating comment misleads a debugger years later, an over-defensive diff burdens a reviewer, a padded chat reply slows a conversation. So the rules are split by output type.

---

## Shared Core (applies everywhere)

- **Know the readers.** Name them before writing. For each: what they already know, what they decide, where they stop reading. Default reader for code, comments, and chat: an insider who knows this codebase and this thread. Specs and anything with more than one reader name theirs explicitly. A reader can be an agent: an agent reading another agent's output (a tool description, an error message, a handoff note) cannot ask what was meant, so write for it the way you would for a reader who cannot reply. When a named reader may not share a term, gloss it once in the sentence that first uses it ("a token bucket, a burst allowance that refills at a fixed rate") rather than avoiding the term.
- **Layers are stopping points.** One layer per distinct stop. Each layer is complete for the reader who stops there and assumes everything above it. Readers who stop at the same depth share a layer. A document may stack layers top-down by audience, repeat them per section with a summary first, or split a layer out as a derived artifact (a summary document that points at its full source); the preamble says which. One reader means one layer: answer first.
- **Readers who differ in what they know get separate artifacts**, linked, not one artifact that serves neither.
- **Omit what the reader already knows.** Restating the prompt, the diff, or the previous message is a bug.
- **Pace by uncertainty.** Settled things get one line. Judgment calls get the words.
- **Default to less; the reader will ask.** Wordiness is the pain, and a reader who wants more detail can ask for it in one line. A reader given too much cannot un-read it. When unsure whether a detail earns its place, leave it out and point to where it lives: the record, a link, the source. A fact that lives nowhere else stays, because a reader who cannot ask (an agent, a maintainer years later) has no one to ask.
- **No scaffolding that carries no information.** No headers on short sections, no bold on every lead (a label on each item of a parallel list is the exception, Mode 4), no closing summary that repeats the body, no "it's worth noting", "in summary", "let me explain". Structure that isolates one fact per line is not scaffolding; do not fold a standalone bullet into a paragraph to save a line.
- **Prefer checkable to fluent.** Lists of assumptions, "X breaks if Y", "chose A over B because C" beat paragraphs.
- **Numbers over adjectives.** "~40ms" not "fast"; "3 call sites" not "several".

---

## Sentences and Paragraphs

Borrowed from ASD-STE100 Simplified Technical English at about 80% strength. Counted rules, not taste: "clearly" is an opinion, a word count is not. The full standard, with its 900-word dictionary, makes text shorter by throwing out content the reader needed; take the rules, not the dictionary.

- **Short sentences.** At most about 20 words in a numbered step, about 25 elsewhere. A longer sentence usually carries two ideas; split it.
- **One instruction per step.** A step that says "do X and then Y" is two steps.
- **Active voice.** Use the passive only when the actor is unknown or does not matter.
- **One topic per paragraph,** at most about six sentences.
- **One term per concept.** Pick "folder" or "directory" and keep it for the whole document. A second word for the same thing makes the reader check whether it is a second thing.
- **Do not compress below English.** Keep articles and verbs; never write telegraphic fragments to save words. Records are the exception: commit bullets, PR label lines, and status updates may be terse fragments, because the reader scans them. Stack at most three nouns ("webhook retry policy", not "partner webhook retry backoff policy"). Shorter is the goal only while every fact survives.

---

## Surface by Stakes

Sort every item into one of three bins, in ascending stakes.

- **Record.** No real alternative, or the record already settles it. It lives in the diff, the appendix, or NOTES.md. Not restated, never re-raised.
- **Tell.** You picked between alternatives for a reason you can cite. One line each, so the reader can overrule. This includes a case the ask's wording covers but its intent may not: told to "fail fast on 4xx", say that 429 is the one 4xx that arguably deserves a retry and that you followed the wording.
- **Ask.** Any of: a reader owns the decision, it is hard to reverse, the blast radius is large (many call sites, many users, cross-cutting), you picked with no reason you can cite, it contradicts the record, it deviates from what was asked. Goes at the start of its owner's layer, with your lean.

Doubt between tell and ask goes to tell: a misplaced item can still be found, an unneeded ask costs the reader a judgment. Doubt about reversibility goes to ask. Too many asks means the plan is underdetermined: find the one question that settles most of them and ask it first.

---

## Mode 1: Spec / Plan / Design Note

Purpose: let a human make or ratify decisions, then verify the result. It is not a record of your reasoning — keep that elsewhere or discard it. Write it for the decision-maker with four minutes before the meeting.

Shape:
- **Preamble.** Two to five sentences of prose under the title, no heading. Who the document is for and what each audience comes for, then how it is organized so they can stop early. Describe the convention the reader can use, not a section-by-section routing. With one reader it is a sentence that says so: "This document is for the engineers implementing the queue migration; it assumes familiarity with the current consumer code."

  Example for a product spec with four stops (exec summary, business logic, design, technical implementation):

  > This document is written for three audiences: executives deciding whether to fund the work, product owners confirming the business rules, and the engineers who will build it. Each major section opens with a short summary, so reading only the summaries gives the complete picture at the executive level. Business rules are in §2; implementation detail starts at §4.

- **Asks never go in the preamble.** If the document needs something from a reader — a decision, a confirmation — that goes in a dedicated section such as open items, when the document needs one. Whether it needs one and what it looks like is case by case; this skill does not prescribe the form.
- **Decisions section.** Each as `chose A over B because C; revisit if D`. No balanced menus. If you truly can't choose, say which way you lean and what information would settle it.
- **Assumptions as a tick-list.** One line each. The reader should be able to scan and mark any that are false.
- **Risks as conditionals.** `X could break if Y.` Not "there are some risks around X."
- **Scope out.** What you are deliberately not doing, one line each.
- Everything else (background, exploration notes, alternatives considered in detail) is omitted or linked, not inlined.

Length: about 300 words is a tripwire, not a target. A spec over it gets checked for symptoms (restated rules, inlined background, alternatives in detail); once none are left, it is the length it needs. Open items are not a reason to run long.

Pacing: do not give equal space to each section. A spec where every heading has two paragraphs under it has not been edited.

Anti-patterns:
- Narrating the codebase back to someone who owns it
- "Overview" or "Introduction" sections
- Listing every file you will touch when the diff will show that
- Asking for a decision inside the preamble — the preamble routes readers; a dedicated section carries the asks
- Ending with "Next steps" that restate the spec

---

## Mode 2: Code Comments

Purpose: carry context the code cannot. Readers arrive years later, mid-debug, with no access to this conversation.

Write a comment only when it answers one of:
- **Why** this, rather than the obvious alternative
- **What invariant or constraint** holds here that isn't enforced by types or tests
- **What external fact** this depends on (API quirk, spec section, ticket)
- **What is deliberately not handled**, and why that's acceptable

Never write a comment that:
- Restates the code (`// increment counter`)
- Narrates the function (`// this function takes X and returns Y`) when the signature already says so
- Records the session (`// added per user request`, `// updated to fix bug`). Version control holds that.
- Hedges (`// this should probably work`). Either verify it or flag it as a `TODO(owner): …` with a concrete condition.
- Apologizes or explains your process

Doc comments on public API: one sentence on what it does, then only the non-obvious: preconditions, failure modes, ownership/lifetime, units. If the name and signature make the one sentence redundant, omit it.

Length: if a comment is longer than the code it annotates, either the code needs restructuring or the comment belongs in a design doc.

Match the repository's existing comment density and style. A sparse codebase should not acquire a verbose file. Sparse is not silent: an edge case you decided on purpose (a status code lumped in with its class, an error left to propagate) is exactly the "deliberately not handled" comment, and cutting it loses the one note a maintainer needed.

---

## Mode 3: Code

Purpose: be read and changed by someone else. Readability is a property of the whole diff, not just the prose inside it.

- **Smallest diff that does the job.** Don't refactor adjacent code, rename things, or reformat unless asked. Every unrelated change is text the reviewer must read.
- **Match the repo's idioms** over your preferences. Same error-handling pattern, same naming, same file layout, same test style.
- **Names do the explaining.** If you want to write a comment explaining what a variable is, rename the variable.
- **No speculative abstraction.** No interface with one implementation, no config for a value that has one value, no "for future flexibility".
- **No defensive noise.** Don't guard against conditions the type system or caller already rules out. Don't wrap every call in try/catch "to be safe".
- **No placeholder chatter.** No `# TODO: implement`, no `pass  # stub`, no `// your code here` in delivered code. Either implement it or state in chat that it's unimplemented.
- **Tests test behavior**, not that the code runs. One descriptive name per test; no test whose body is `assert True` or mirrors the implementation.
- **Delete, don't comment out.** Version control remembers.
- **Commit messages:** a project's own commit style in AGENTS.md and/or CLAUDE.md wins. When none is specified, use this default:
  - Subject: `<prefix>: <description>`, under 72 chars. The prefix is a lowercase whole word naming the purpose: `fix`, `feature`, `docs`, `refactor`, `test`, `chore`.
  - Body only when there's a non-obvious decision. Group related changes under short theme headers; each bullet is a concise fact, not a sentence. No bullet list of every file.
  - Skip the body for trivial commits (single-file wording tweaks, typo fixes).
  ```
  feature: webhook client retries with exponential backoff on 5xx

  Mechanics:
  - 3 attempts, 200ms base, jitter
  - 4xx fails fast — retrying a bad payload never helps

  Design:
  - Backoff lives in the client, not the caller — one policy, 4 call sites
  ```

Before delivering, re-read the diff as the reviewer: anything that makes them stop and ask "why is this here?" either gets a `why` comment (Mode 2) or gets removed.

A PR description longer than a screen opens with one sentence of preamble: which part needs the reviewer's judgment and which is mechanical. A PR description is a record, not prose: terse label lines ("Risk:", "Mechanical, skip:") are fine and scan better than sentences.

---

## Mode 4: Chat

Purpose: a turn in a conversation. The reader is present, impatient, and can ask follow-ups. Optimize for their next action, not for completeness. Write it for the colleague at the next desk who asked over their shoulder.

- **Answer first.** The first sentence is the answer, the decision, or the result. Method, caveats, and context come after, if at all.
- **Match length to the question.** A yes/no question gets a sentence. A "how should I think about X" gets a few paragraphs. Never the same length regardless. Two paragraphs is the tripwire: a longer reply gets the full cut pass, not a cut to length.
- **Don't restate the question.** They know what they asked.
- **One question back, at most.** If you need clarification, ask the single question whose answer most changes what you'd do. Do reversible prep first and hold at the irreversible step. If the record says the reader wants defaults picked ("pick a default and we'll revisit"), pick one, label it a proposal, and skip the question.
- **Status updates are terse.** "Ran tests; 2 failures in auth, looking." Not a paragraph.
- **Report what changed and what you're unsure of.** Not what you did step by step. The reader can ask for the steps.
- **No performative phrases.** No "Great question", "Certainly!", "I'd be happy to", "I hope this helps".
- **Formatting is rare, but parallel items get a list.** Three reasons, three options, three steps: bullet them, because a reader sees "three reasons" at a glance and has to dig them out of a paragraph. Bold the first word or two of each bullet as its label; that is the one place bold earns its keep. Past about five bullets the reader skims instead of reads, so group or cut. Headers almost never. Code blocks for code.
- **The cost gets its own line.** What the recommendation costs, or the caveat that could change the reader's mind, is never the tail of a bullet about something else. Put it on a line by itself after the reasons, where it cannot be missed.
- **Disagree plainly.** "I'd do X instead because Y" rather than three paragraphs of hedged framing.
- **Stop when done.** Don't offer a menu of further things you could do unless there's a specific, likely next step worth naming.

If the project uses /fast-chat, its structured formats (NL options in fenced code blocks, the R/O review tail) are the exception to "formatting is rare" — they are the agreed interface, not scaffolding.

---

## Mode Selection

| Signal | Mode |
|---|---|
| "plan", "spec", "design", "proposal", "RFC", approval requested | Mode 1 Spec |
| Writing inside a source file | Mode 2 Comments + Mode 3 Code |
| Producing a diff, PR, or commit | Mode 3 Code, including its PR description paragraph |
| Everything else in the conversation | Mode 4 Chat |

When unsure, use Mode 4. It is the mode with the least surface area for bloat.

---

## The Cut Pass

Run it before delivering anything longer than a sentence. The default is the short pass: steps 2, 6, 7, and 9, with the fact list kept in your head. Documents, edits, and anything over its mode's tripwire get every step.

Read the draft as the copy desk chief whose job is to make it clear without losing a rule, then run the checks; the frame sets the stance, the checks catch what the stance misses.

The targets are counts that reach zero, not a length: facts lost, sentences over about 25 words (20 in a numbered step), rules stated twice, claims with no source, "This is / That is" openers. A second pass on the output should change nothing. A pass that keeps cutting is cutting facts.

0. Anything over its mode's tripwire is a draft, not a deliverable. Measure it first and change nothing yet; steps 1 to 9 do the fixing. When the text is in a file and you have a shell, run `${CLAUDE_SKILL_DIR}/scripts/symptoms.py` on it; otherwise use the checklist below. The symptoms are easier to see in a draft than to avoid while writing.
1. Before cutting anything, list the facts the text carries: rules, numbers, names, conditions, consequences. Step 7 checks the cut against this list.
2. Re-read as the named reader. What do they already know? Cut it.
3. Check the draft against § The Recognizable Shape. Any match is a cut, not a rewrite.
4. If a preamble sentence could be deleted without a reader losing a way to stop early, delete it.
5. Check the bins: each ask fires a § Surface by Stakes signal, and no item that fires one is sitting in tell.
6. Check provenance: every number and every concrete claim traces to the record, the thread, or the source. One that does not is either cut or labelled an estimate with its basis. An invented figure reads as fluent and is the hardest error for the reader to find.
7. Check what the cut left out. Each fact on the step 1 list survived, or dropping it was a choice the reader would agree with. Shortening that loses facts is not editing.
8. Check the draft against its mode's rules (Modes 1 to 4).
9. Check that the first sentence after any preamble is the thing the reader came for.

The cut pass is the step generated text skips. It is not optional.

---

## Bootstrap

When invoked on a project for the first time:

1. **Audit AGENTS.md and/or CLAUDE.md** — check for existing writing or style conventions. Some projects already have a commit style, a comment policy, or a "be concise" directive. Keep those; the block below complements them.

2. **Add a Writing Conventions section** — a reference card, not a tutorial: about 250 words before the reader roster (the roster is a table and does not count). The shared core and the mode table, with a pointer to /red-pen for the full per-mode rules. Mark with `<!-- managed by /red-pen -->`.

3. **Seed the reader roster** — ask one question: who reads what this project produces? Propose rows from the answer (and from README, NOTES.md, and the org structure if visible). For each reader: what they know, what they decide, where they stop. A project whose only reader is the insider skips the table, and then the block states the default in one sentence instead of leaving a "Readers:" line with nothing under it. When `/start` runs this bootstrap as part of the suite, skip the question and use the insider default; say once that a roster can be added later with `/red-pen`.

4. **Inform the user** — one or two sentences. Mention that `/red-pen <target>` edits a file or section against the rules, and that "too long" or "red-pen this" works mid-conversation.

Example AGENTS.md and/or CLAUDE.md section:

```
## Writing Conventions
<!-- managed by /red-pen -->

**Decide the output type before writing, then write to its rules.** Full rules: /red-pen.

| Output | Rule of thumb |
|---|---|
| Spec / plan / design note | Preamble: who it is for and how to read it; asks go in their own section, not the preamble. `chose A over B because C; revisit if D`. Assumptions as a tick-list, risks as `X breaks if Y`. About 300 words is a tripwire, not a target. |
| Code comment | Only why, an invariant, an external fact, or a deliberate omission. Never restate the code or narrate the session. |
| Code / diff / commit | Smallest diff that does the job. Match repo idioms. No speculative abstraction, no defensive noise, no placeholder stubs. Commit subject `<prefix>: <description>`; body only for a non-obvious decision. |
| Chat | Answer first. Length matches the question. No restating, no performative phrases. Formatting is rare. One question back at most. |

Everywhere: name the readers and omit what they know. Sentences of about 20 words in
numbered steps and 25 elsewhere, active voice, one term per concept, never at the cost of a fact.
One layer per stopping point; one reader means answer first. Settled things get one
line. Record what has no real alternative, tell what you chose and why, ask when a
reader owns it, it is hard to reverse, the blast radius is large, or you guessed.
No empty scaffolding. Checkable beats fluent. Numbers over adjectives. Run a cut pass.

Readers (default for code, comments, chat: an insider who knows this codebase and this thread):

| Reader | Knows | Decides | Stops at |
|---|---|---|---|
| exec | the product, not the code | priority, budget | the summary |
| product / managers | the roadmap and the users | scope, business rules | business logic |
| design | the flows | interaction and visual choices | design |
| eng ICs | the codebase | implementation | the end |
| agent | the prompt it is given, nothing else | what to call or do next | the first instruction it can act on |
```

---

## Ongoing Operations

### Editing a target

When the user points /red-pen at something ("red-pen this", `/red-pen docs/design.md`, "this is too long"):

1. Identify the mode and the readers from the target, not from the conversation. A design doc is Mode 1 even if the request arrived in chat. If the target names no readers, take them from the roster or ask once.
2. Apply the mode's rules and the cut pass. Cut first; rewrite only what the cut leaves broken. Cut history, argument, and cross-section restatement; do not cut enumeration the reader scans. Where the document's house style conflicts with these rules, house style wins (§ Project-specific overrides has the full order).
3. Write the edited text to the file. The chat reply is the report, in this shape and no other, because a reader skims anything longer:
   - One line: the path written, and what was preserved (every rule, anchor, and list; name any exception). Stale or contradictory claims you found go here too, since those are the findings the reader acts on.
   - One before/after paragraph pair, next, introduced by a sentence that says what it is ("Here is one paragraph before and after, as an example of the change:"). A bare "Before (§6.3 ...):" has no context. This pair is what the reader uses to judge; it gives the flavor of the edit without a pile of detail.
   - A symptom table of at most four rows, the ones that moved most. It is evidence, and readers skim it, so keep it short and put it after the pair. `${CLAUDE_SKILL_DIR}/scripts/symptoms.py --compare before.md after.md` gives the literal counts (save the original before writing; `git show HEAD:<path>` recovers it only when the file had no uncommitted changes; `-` reads stdin); you add what it cannot see (stale claims, cross-section restatement, argument before rule, paraphrased restatement).
   - Nothing else. No narration of each cut, no word count unless the reader asked. Under 150 words outside the pair. `references/worked_example.md` is the shape.
4. Do not add anything the original lacked unless the mode requires it (a Mode 1 doc with no preamble gets one; it does not get an Overview).

### Independent review

The author of a document cannot see what its reader does not know. For a document that matters (a spec others will ratify, a README, anything with several audiences), an editing pass by the author is not a review. If the project has /multi-adversarial-review, use its `copy` target: one independent reviewer per named reader, findings that quote the sentence and name the symptom, and a disposition for each. This skill supplies the vocabulary that review uses: the symptom list, the reader roster, and the writing conventions. A cut the owner rejects there becomes a project override here.

### When the user says "too long" or "too wordy"

That is a cut-pass failure, not a style preference. Re-run the cut pass on the last output and resend. Don't explain why it was long.

### When invoked on an existing project

1. Show the current Writing Conventions block
2. Ask what the user wants to adjust — a different tripwire, rows in the reader roster, project-specific anti-patterns
3. Make the changes, preserving the breadcrumb

### Project-specific overrides

Projects may legitimately override defaults: a public library wants fuller doc comments than Mode 2's default; a team may set its spec tripwire at 500 words. Record overrides inside the Writing Conventions block so they load every session.

When rules conflict, the project wins, in this order: the document's house style, then recorded overrides, then the mode's rules, then the shared core.

When a reader rejects a cut, record the category as an override the same way ("keep row-by-row teaching bullets under tables", "keep one-fact sub-bullets", "spec tripwire 500"), so the next pass starts calibrated instead of relearning it. One line per rejection; the reason is the reader's, not yours.

---

## What Does NOT Go in /red-pen

- **Interaction mechanics** — numbered options, batch answers, the review tail are /fast-chat. /red-pen governs how the words read; /fast-chat governs how decisions are exchanged.
- **Decision capture** — what was decided and why goes in NOTES.md via /notes. /red-pen shapes how a decision entry reads (Mode 1's `chose A over B because C`), not whether it gets written.
- **Code formatting and lint rules** — tabs, line length, import order belong to the project's formatter. Mode 3 is about diff readability, not whitespace.
- **Selecting which outputs deserve attention** — /red-pen decides what within an output gets the reader's attention (§ Surface by Stakes) and orders it by who stops where. It does not decide which outputs a human should read at all. That is a selection problem above the writing layer.
- **Input correction** — garbled or shorthand input is /dictation.
- **A global persona** — "you are a professional editor" buys tone and fluency, which is the failure the skill exists to catch. Reader frames are per step and always paired with a check.

---

## How It Fits

```
Always-on behavior          → pick the mode, write to its rules, run the cut pass
                               (adopted immediately, no setup needed)

AGENTS.md and/or CLAUDE.md  → Writing Conventions block (shared core + mode table)
                               (bootstrapped on invocation for durability)

/red-pen <target>           → editing pass on an existing file or section
                               (cut first, rewrite only what the cut breaks)

scripts/symptoms.py         → counts the recognizable shape before and after
                               (restated phrases, openers, bold leads, dated markers,
                                sentence and paragraph length, passive voice, term switches)

Mode 1 Spec                 → the shape every plan, spec, and design note takes
                               (preamble, decisions, assumptions, risks, scope out)
```

/red-pen pairs with /fast-chat: /fast-chat makes each exchange shorter by replacing prose with codes, /red-pen makes whatever prose remains worth reading. It pairs with /notes: NOTES.md decision entries follow Mode 1's `chose A over B because C` shape, so the institutional memory is checkable, not fluent.
