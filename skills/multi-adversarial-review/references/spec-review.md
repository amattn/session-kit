# Spec Review Target

Use this target for design specifications, RFCs, design notes (such as Vog VDNs), architecture decisions,
protocol contracts, and normative design notes. A spec is neither code nor an
implementation plan: review the meaning being proposed, its fit with the
project's principles and canon, its evidence, and its readiness for maintainer
ratification.

## Authority and role

The review lead is the artifact editor; the maintainer is the design authority.
Reviewers recommend and expose tradeoffs. They do not ratify an OPEN decision.
The lead may correct contradictions, status overclaims, terminology, evidence,
and edit cascades, but must not silently choose a design fork without authority.

Treat an explicitly OPEN item as honest design state, not automatically a defect.
Report it as a finding when the artifact hides or misclassifies it, lacks the
information needed to decide it, or lets downstream text depend on it as settled.

When a project has a named design-note type (a Vog VDN, for example), select spec
automatically even when the user says only "review this note." Do not relabel it
plan.

## What to read

Before reviewing:

1. Read project directives and the artifact in full.
2. Identify the authority order: durable principles, current canonical specs,
   decision logs, implementation constraints, and historical notes.
3. Read the durable principles in full when available.
4. Read the relevant canonical sections and dependencies deeply enough to verify
   the artifact's claims.
5. Distinguish normative authority from history, evidence, implementation
   observations, and generated summaries.

Example, Vog VDNs (the origin project):

- Read vog_design_principles.md in full. Use the VDP as the primary lens.
- Read relevant full VLS, VTS, VGS, or VCI sections when the concise rung is
  insufficient, plus applicable NOTES decisions and dependent VDNs.
- Treat current specs as canon-for-now: expose and justify divergence, but do not
  reject a proposal merely because it improves current canon in service of VDP.
- Treat closed VDNs, spikes, and backend behavior as history or evidence unless
  current canon delegates authority to them.
- Cite stable labels and anchors, not line numbers where labels exist.

### Authority coverage gate

Treat load-bearing authority as a route precondition, not a review caveat. Before
launching a reviewer, the lead must:

1. Resolve the artifact, project directives, durable principles, relevant canon,
   and named dependencies to absolute paths.
2. Put those paths in the reviewer prompt under `Required authority`.
3. Grant the route read access to every containing directory. When authorities
   span sibling repositories, use their smallest safe common ancestor as the
   review root; for Claude CLI, also pass it with `--add-dir`.
4. Require the response to begin with `Authority coverage: complete` followed by
   the files actually read.

If any required authority cannot be read, the reviewer must stop before making a
substantive assessment and return `route-failed: authority-unavailable` with the
missing path. The lead corrects the route scope and retries; a canon-incomplete
review does not count as a completed MAR stage. Optional evidence may remain
unavailable when the response names the narrower limit, but missing evidence is
never folded into `Strong`.

## Review lens

Judge the artifact as a whole:

- Is the problem real and scoped, with non-goals and bundled questions visible?
- Does the proposed mechanism align with the durable principles overall?
- Does it convert silent failure to loud failure, keep consequential choices
  explicit, make errors first-class, and preserve one obvious semantic path?
- Are semantics coherent across types, lifecycle, ownership, failure boundaries,
  terminology, and examples?
- Are alternatives and one-way doors treated honestly?
- Do DECIDED, RECOMMENDED, OPEN, LOG, "resolves," and "distills" match the actual
  evidence and remaining premises?
- Are implementation capabilities and cross-target behavior proved or named as
  gates rather than assumed?
- Do citations and spikes prove only what the prose claims?
- Is the canon/edit cascade complete and correctly gated?
- Is the result understandable, diagnosable, locatable, and hard for a human or
  agent to misuse?

Give one high-level principle-alignment judgment. Cite the few principle labels
that actually drive the result, but do not produce a principle-by-principle
scorecard or chapter.

## Concise output contract

Do not restate the artifact. Default to a compact review: one to three assessment
paragraphs, then short evidence-rich sections. Expand only when a finding needs
the evidence.

### Overall assessment

Lead with a direct judgment in the style of:

- sound and strongly aligned with the design principles;
- promising direction but needs design work;
- structurally weak or misaligned;
- blocked on evidence or an external decision.

State usefulness, overall principle alignment, readiness, and the decisive reason. This
is not a numeric score.

### Strong

Give up to seven bullets naming the load-bearing parts worth preserving. Anchor
each in a concrete mechanism, canon label, or high-level principle rationale. If none
survives the evidence bar, say so; do not manufacture praise or praise prose
style.

### Needs work

Preserve panel-style findings. Order by severity and give each:

- identifier and severity;
- concrete evidence with stable anchors;
- why it matters to the spec or principle alignment;
- revision direction, verification, or maintainer question.

Distinguish bad design, good direction without mechanics, missing evidence,
status/canon drift, and mechanical cleanup. Do not force findings.

### Viability

State whether the proposal can actually be implemented under the current
compiler, runtime, and target commitments. Name required new machinery,
non-trivial analysis, cross-target proof gaps, and a safe fallback when one
exists. Keep this short and separate from whether the design is desirable.

### Open design vs mechanical work

Use two short lists:

- Open design: genuine maintainer choices, tradeoffs, dependencies, and what
  would close them.
- Mechanical: cascade edits, status/terminology corrections, generated summaries,
  and cleanup that does not decide semantics.

A mechanical fix must never make an unsettled design look ratified.

### Readiness

For each major topic, state ready, needs design work, or blocked. Say what can be
ratified now, what remains conditional, and whether the artifact is ready to
distill.

"No findings" is allowed but is not the same as ready. Name the weakest remaining
assumption and any untested area.

## Disposition guidance

Use the normal MAR states:

- accepted-fixed for a confirmed document correction;
- accepted-deferred for real OPEN design work, with tradeoff, dependency,
  authority/owner, and future home;
- rejected when source or authority does not support the claim;
- unclear-blocked with the exact missing evidence or ruling;
- contested with both arguments preserved for maintainer judgment.

Tag accepted findings as design, evidence, status/canon, or mechanical. For a
high-severity principle misalignment, status overclaim, or design-defeating
contradiction, use the normal one-shot audit before crediting the fix.

## Route prompt overlay

Append or adapt this text in the external reviewer prompt. Do not merely tell the
reviewer to open this reference unless it is installed in the target repo:

    Target mode: spec.

    Required authority: <absolute artifact/directive/principle/canon/dependency
    paths>. Read every listed file. Begin the response with `Authority coverage:
    complete` and the files read. If any listed path is inaccessible, stop and
    output `route-failed: authority-unavailable — <path>`; do not review from a
    partial authority set.

    This is normative specification review, not code review or plan review. Read
    the artifact, its authority hierarchy, and its dependencies in full. Evaluate
    the proposal through the durable design principles overall. If the project has
    a durable-principles document (for a Vog VDN, vog_design_principles.md), read it
    in full and use it as the primary lens, then
    verify against relevant full canon, decisions, dependencies, and evidence.

    Do not ratify OPEN choices. Keep the response concise and do not restate the
    document. Output: Overall assessment; Strong; Needs work with severity-ranked
    panel-style findings; Viability; Open design; Mechanical work; and Readiness
    by topic. Cite only the principle labels that materially drive the overall judgment;
    do not produce a principle-by-principle breakdown. No findings is allowed but
    does not imply readiness.
