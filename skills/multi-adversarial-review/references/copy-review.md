# Copy Review Target

Use this target when a document written for human readers needs review as
writing: a README, a guide, release notes, a long PR description, or the prose
of a plan or spec. The question is not whether the content is right. It is
whether each named reader can find what they need, trust it, and stop early,
without a rule being lost on the way.

`copy` and `spec` are different reviews of what may be the same file. `spec`
judges the meaning being proposed. `copy` judges whether readers can use the
text. A design note that needs both gets `spec` first, then `copy` on the
settled text.

A chat reply or a short message is not a `copy` target. Edit it and move on.

## Authority and role

The lead is the editor. The author or maintainer owns the meaning. Reviewers
propose cuts, moves, merges, and glosses; they never change what the document
says. A finding whose fix would change a rule, a number, or a decision is a
`meaning` finding: it goes to the owner, and the editor does not resolve it.

## What to read

Before reviewing, and as a route precondition:

1. The artifact in full.
2. **The named readers.** The lead must state who reads this, what each already
   knows, what each decides, and where each stops. Take them from the project's
   reader roster when one exists, or from the document's own preamble. A review
   with no named reader is `route-failed: reader-undefined`, because "is this
   clear" has no answer without a reader.
3. The project's writing conventions and house style, when they exist. House
   style wins over this reference where they conflict.
4. The record the text makes claims about: the decision log, the specs or code
   it cites, the previous version when the review is of an edit.

Put the artifact, the readers, the conventions, and the record paths in the
reviewer prompt under `Required authority`, and require the response to begin
with `Authority coverage: complete` and the files read. A reviewer that could
not read the record cannot raise a stale-claim finding, so a record-incomplete
review does not count as a completed stage.

## Lenses

The lenses are the readers. Within a stage, run one reviewer per named reader,
blind to each other until all finish. Each reads as that reader and reports:

- where they stopped, and whether they had what they came for by then;
- what they had to read twice, and why;
- what they did not understand, including terms nobody defined for them;
- what they already knew, which is the cut list for their layer.

Two lenses are not readers and run alongside them when the stakes warrant:

- **Record.** Every number and concrete claim traces to the record, the code,
  or the source. Report claims that contradict the record and claims with no
  source at all.
- **Fidelity.** When the artifact is an edit of an earlier version: every rule,
  anchor, number, and list in the source survives, or its removal is named.

Default to one reviewer, reading as the primary reader and holding the record
lens. Add a reviewer per further reader when the document has several
audiences, and the fidelity lens when reviewing an edit.

Model diversity works as it does for the other targets: a reviewer from the
author's own model family is a sanity pass, not an independent gate. For prose
the case for cross-family reviewers rests on less evidence than it does for
code; an independent reader with a different context already catches most of
what the author cannot see. Record which you ran.

## Finding kinds

Name the kind. It tells the editor what the fix is.

| Kind | What the reader experiences |
|---|---|
| `restated` | The same fact or rule again, and a check for whether it differs |
| `stale` | A claim that contradicts the record |
| `unsourced` | A number or fact with nothing behind it |
| `history` | The path to a rule, sitting on top of the rule |
| `argument-first` | Reasoning to wade through before the point |
| `buried` | An ask, a cost, or a caveat inside something else |
| `undefined` | A term this reader was never given |
| `scaffolding` | Headers, bold, or summaries that carry nothing |
| `no-route` | No preamble, or no way to tell where to stop |
| `over-cut` | A rule, a step, or an enumeration the reader scans, gone or collapsed |

`over-cut` is a finding like any other. A review that only ever asks for less
is half a review.

## Evidence bar

Each finding quotes the sentence or names the anchor, names the reader it
affects, gives its kind, and proposes one change: cut, move, merge, gloss, or
refer to the owner. "Tighten this section" is not a finding. Do not force
findings. "No findings" is allowed and must name the weakest paragraph.

## Concise output contract

Do not restate the artifact. Keep the assessment under about 300 words before
the findings. A review of a wordy document that is itself wordy has failed its
own test.

### Overall

One short paragraph: which readers the document works for, which it does not,
and the decisive reason.

### Strong

Up to five things that must survive any edit: the rule a reader came for, a
table that teaches, an example that carries the why, an enumeration readers
scan. This section is the guard against over-cutting. If nothing qualifies, say
so; do not praise style.

### Needs work

Findings in severity order: identifier, kind, quoted evidence with its anchor,
the reader affected, and the proposed change.

### Fidelity

Only when reviewing an edit against its source: what did not survive, and
whether each loss was named by the editor.

### Judgment and mechanical

Two short lists. Judgment: cuts and moves the owner should see before they
happen, including every `meaning` finding. Mechanical: sweeps that change no
reader's understanding.

### Readiness

Per reader: ready, needs work, or blocked. Say what blocks.

## Disposition guidance

Use the normal states. Tag each accepted finding as `cut`, `reorder`, `stale`,
`provenance`, `gloss`, `meaning`, or `mechanical`.

- `accepted-fixed`: the text was changed.
- `accepted-deferred`: a `meaning` finding handed to the owner, with its home.
- `rejected`: with the reason, quoted from the owner where there is one. A
  rejection is a healthy outcome here. "Enumeration is not duplication" is a
  rejection, and it should be recorded where the next pass will see it: the
  project's writing conventions, as a one-line override.
- `no-findings`: names the weakest paragraph.

After the disposition, the edit is one change to the artifact and one commit,
the same as any other stage. The disposition record says what was cut and what
was kept on purpose.

## Route prompt overlay

Append or adapt this text in the external reviewer prompt:

    Target mode: copy.

    Required authority: <absolute paths: the artifact, the reader roster or
    preamble, the writing conventions, and the record it cites>. Read every
    listed file. Begin with `Authority coverage: complete` and the files read.
    If the readers are not named, stop and output
    `route-failed: reader-undefined`. If a listed path is inaccessible, stop and
    output `route-failed: authority-unavailable — <path>`.

    You are reviewing this document as writing, not as design. Read it as
    <reader: what they know, what they decide, where they stop>. Report where
    you stopped, what you read twice, what you did not understand, and what you
    already knew. Check every number and concrete claim against the record.

    Do not change what the document says. A fix that would alter a rule, a
    number, or a decision is a `meaning` finding for the owner. Every finding
    quotes its sentence, names its kind (restated, stale, unsourced, history,
    argument-first, buried, undefined, scaffolding, no-route, over-cut), names
    the reader affected, and proposes one change.

    Keep the assessment under 300 words before the findings and do not restate
    the document. Output: Overall; Strong (what must survive any edit); Needs
    work, by severity; Fidelity (only if this is an edit of an earlier
    version); Judgment and mechanical; Readiness per reader. No findings is
    allowed and must name the weakest paragraph.
