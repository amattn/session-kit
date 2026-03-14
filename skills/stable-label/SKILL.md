---
name: stable-label
version: 0.1.0
description: "Greppable stable references using the XXX_N convention. Append-only IDs that never renumber and always resolve to exactly one definition. Use when the user asks to 'stable-label', 'label', 'add id', 'add reference', 'define prefix', 'consistency pass', or when cross-referencing artifacts. Also trigger when you notice referenceable items without IDs, when cross-references use fragile text matching instead of stable IDs, when numbered lists would benefit from stable cross-references, when multiple documents reference each other by name or title instead of IDs, or when a project would benefit from greppable references even if the user hasn't asked for them."
user-invocable: true
---

# /stable-label — Greppable Stable References

Give every referenceable thing a greppable ID. Any ID returns exactly one definition and all its references across the project. The convention is trivial to adopt but transforms how both humans and agents navigate a project — cross-referencing goes from fuzzy text matching to precise, machine-verifiable lookups.

Originally designed for PRDs, requirements documents, and specs, but found to be useful for many kinds of documentation — and even in non-documentation codebases, inside comments and docstrings, where stable IDs link code back to the decisions and requirements that drove it.

---

## The Job

1. Detect whether a stable-label convention exists in the project — check AGENTS.md and/or CLAUDE.md for prefix definitions, and scan files for existing `XX_N` or `XXX_N` style IDs that may be in use informally
2. If not, run the bootstrap flow
3. If yes, operate using the convention — assign IDs, validate references, suggest consistency passes

---

## The Convention

### ID Format

```
XXX_N       — three-letter prefix, underscore, sequential number
XXX_YYY_N    — sub-group for namespaced items
```

- **Three-letter prefixes** are the default. They prevent collisions in large docs/repos and improve readability over two-letter prefixes. Two-letter prefixes are acceptable for small projects.
- **Underscore separator** — the `_` is the delimiter. This is what makes IDs greppable: `grep REQ_3` returns exactly one definition and all references. Underscore also means a double-click selects the entire ID in most editors and terminals — no manual mouse manipulation needed to copy-paste. Dashes break word selection in most environments, making them worse for this use case.
- **Append-only numbering** — deleted items leave gaps. Never renumber, never reuse. Gaps are expected and fine. The stability guarantee depends on this: if IDs could be renumbered, every reference in every document becomes suspect after any change. Append-only means an ID means the same thing forever.
- **One definition per ID** — every ID resolves to exactly one definition. If grep returns multiple definition-like results, something is wrong. This is what makes IDs trustworthy as anchors — you never have to wonder "which REQ_3?"

### Examples

```
REQ_1       — first requirement
REQ_2       — second requirement (REQ_1 was later deleted — gap is fine)
DEC_14      — fourteenth design decision
DEC_SCP_3   — third decision in the "scope" sub-group
FB_7        — seventh feedback observation
```

In context, a cross-reference looks like: "As decided in DEC_14, we use PostgreSQL for the event store. See also REQ_2 for the durability requirement that drove this choice." — grepping `DEC_14` finds both the definition and every place it's referenced.

### Prefix Design

Good prefixes are:
- **Mnemonic** — the letters should evoke the thing. `REQ` for requirement, `DEC` for decision. Even better when the prefix forms an acronym: `ICR` for Invariants & Critical Requirements — each letter maps to a word, making it memorable without a lookup table. Pre-existing acronyms like `SLA` for Service Level Agreements are instantly recognizable with zero lookup cost
- **Unique within the project** — no two artifact types share a prefix
- **Three letters** — long enough to be readable and collision-resistant, short enough to not clutter. Two letters are acceptable when unambiguous, but beware collisions — is `QA` quality assurance or quantity assumptions?

A project's prefix table belongs in NOTES.md under Taxonomy / Conventions — it's a living reference that grows with the project. The convention rules (append-only, no renumber) belong in AGENTS.md and/or CLAUDE.md as behavioral directives, with a pointer to the prefix table.

---

## Bootstrap

When invoked on a project for the first time:

1. **Scan the project** — look at existing artifacts (NOTES.md, README, PRDs, specs, etc.) and suggest prefixes based on what's found. Also scan for informal `XX_N` or `XXX_N` style IDs already in use — if found, propose formalizing them with their current prefixes rather than inventing new ones. Examples of suggested prefixes:
   - NOTES.md decisions → `DEC_N`
   - Requirements → `REQ_N`
   - Feedback/observations → `OBS_N`
   - Features → `FEA_N`

2. **Propose a prefix table** — present suggestions to the user for approval. The user may add, remove, or rename prefixes.

3. **Add convention rules to AGENTS.md and/or CLAUDE.md** — write the behavioral directives (append-only, no renumber, no reuse) but not the prefix table. The rules are directives; the table is reference data.

   ```
   ## Stable Label Convention
   <!-- managed by /stable-label -->

   Every referenceable item gets a greppable ID using the XXX_N format.
   Append-only — never renumber, never reuse. Gaps are expected.
   See the prefix table in NOTES.md § Taxonomy / Conventions.
   ```

4. **Add prefix table to NOTES.md** — under Taxonomy / Conventions, where it's a living reference that grows with the project. The table is global (one table, not per-document) to prevent prefix collisions.

   ```
   ### Stable Label Prefixes

   | Prefix | Artifact type |
   |--------|--------------|
   | DEC    | Design decisions |
   | REQ    | Requirements |
   | ...    | ... |
   ```

5. **Inform the user** — explain the convention, how to assign IDs, and that /stable-label can be invoked to add prefixes, validate references, or suggest consistency passes.

---

## Ongoing Operations

### When invoked on an existing project

When /stable-label is invoked and the convention is already set up:

1. Show the current prefix table and convention status
2. Ask what the user needs — assign IDs, add a prefix, run a consistency pass, or something else
3. Operate accordingly

### Assigning IDs

When creating a new referenceable item:

1. Look up the prefix table for the appropriate prefix
2. Find the highest existing number for that prefix
3. Assign the next number
4. If no prefix exists for this artifact type, suggest adding one to the prefix table

### Sub-groups

Use `XXX_YYY_N` or `XXX_YY_N` when a prefix has natural subdivisions. The sub-group qualifier (`_YYY` or `_YY`) goes between the prefix and the number. Three-letter sub-groups are the default; two-letter is acceptable when unambiguous. Sub-groups are optional — only introduce them when categories are emerging and items are getting hard to scan.

Example: `DEC_N` grows and natural clusters appear → split into `DEC_SCP_N` (scope), `DEC_UI_N` (UI), `DEC_DBA_N` (database).

### Adding a new prefix

When a new artifact type needs a prefix:

1. Choose a three-letter prefix (mnemonic, unique)
2. Add to the prefix table in NOTES.md
3. Start numbering at 1
4. Inform the user what was added — offer to undo or modify, then run a Quick consistency pass

Agent judgment is sufficient here. Don't block on approval for routine prefix additions.

### ID Lifecycle

IDs are permanent, but the items they point to evolve. Sometimes items split, merge, get deprecated, or graduate to a different artifact type. The stability guarantee still holds in all cases — retired IDs resolve to a pointer, never to nothing.

**Splitting** (one item becomes two or more): prefer keeping the original ID on one part and assigning new IDs for the split-offs. Add a provenance note: "REQ_23 (split from REQ_5)". The original ID still resolves — no breakage.

**Merging** (two or more items become one): prefer keeping one ID as canonical and retiring the others with pointers: "REQ_7 — merged into REQ_5". All IDs still resolve — one to the live item, the rest to redirects.

**Deprecation** (an item becomes irrelevant): the item wasn't merged or split — it just stopped mattering. Retire with a tombstone: "REQ_5 — deprecated, see DEC_12 for rationale." The ID still resolves, it just resolves to a reason.

**Promotion** (an item graduates across prefixes): an observation becomes a requirement, a question becomes a decision. Retire the old, assign new, leave a pointer: "OBS_3 — promoted to REQ_15."

**Crosscutting** (an item spans two or more prefixes): when a concern belongs to multiple domains (e.g., a security requirement with UI implications), give each domain its own ID with content relevant to that domain's perspective. `SEC_4` covers the security facet ("locked from changes due to compliance policy"), `UI_12` covers the UI facet ("show a lock icon when item is restricted"). Cross-reference between them: "SEC_4 — see also UI_12." Each entry stands on its own with domain-relevant content — they're different facets, not duplicates.

All five follow the same principle: IDs always resolve to meaningful content. These are light guidelines, not hard rules. Agent judgment is sufficient in most cases — only escalate to the user when the decision is unusually unclear. Follow up with a consistency pass (at least Quick, Standard if the item was widely referenced) to catch any stale references.

### Filenames

When IDs appear in filenames, zero-pad the number for lexical sorting:

```
REQ_001.md
REQ_002.md
REQ_010.md
```

The rationale: file browsers and `ls` sort lexically, so `REQ_2.md` would sort after `REQ_19.md` without padding. The tradeoffs:
- Maintaining two conventions (padded in filenames, unpadded in text) adds cognitive overhead
- Padding width is a guess — three digits assumes N stays under 1000. If it exceeds 999, the padding breaks and needs widening, which means renaming existing files

Mention these tradeoffs to users and let them decide — some projects prefer consistency (always pad), others prefer readability (never pad). The in-document convention (`REQ_2`, unpadded) is the primary one; filename padding is optional guidance.

---

## Consistency Passes

A consistency pass verifies that IDs are used correctly across the project — no orphaned references, no duplicate definitions, no stale IDs. These are common approaches at different scales, not rigid procedures. Pick the approach that fits the situation, or create new ones applicable to the project or repo you are working on.

### Approaches

- **Quick** — grep for one specific ID or pattern after a targeted change. Takes seconds. Output: confirmation that the ID resolves correctly, or a flag if something's off.

- **Standard** — grep for stale patterns + cross-reference IDs after a batch of changes. Check that definitions exist for all referenced IDs and vice versa. Output: a list of orphaned references, missing definitions, or duplicates.

- **Sweep** — inventory all instances of a prefix, categorize by usage (definition vs reference), surface orphans and duplicates. For broad convention changes like renaming a prefix or merging sub-groups. Output: a categorized report with proposed fixes. Get user approval before executing changes.

- **Structural** — full semantic scan across all files. Not just grepping for IDs but checking that references make sense in context. Output: findings with context and recommendations. Expensive — confirm with the user before running.

### When to suggest a pass

Suggest a pass when you notice potential drift — a renamed item, a batch of new IDs, a deleted section that might leave orphaned references, or when another skill (like /patterns) flags ID inconsistencies. Match the approach to the scale of the change: targeted edits warrant a Quick check, broader changes warrant Standard or above.

---

## What Does NOT Go in /stable-label

- **Content of labeled items** — /stable-label assigns and tracks IDs, it doesn't own the content they point to
- **Enforcement of other conventions** — /stable-label handles ID conventions only, not naming conventions for code, files, or other artifacts. Exception: unit test names may reference stable-label IDs (e.g., `test_REQ_3_validates_input`) to trace tests back to requirements
- **Renaming or deleting IDs** — assigning new IDs is fine autonomously, but renaming or deleting existing IDs needs user approval since it breaks the stability guarantee
- **Policing other skills** — /stable-label defines consistency pass approaches but doesn't own how other skills use them. Other skills can follow the guidelines independently

---

## How It Fits

```
AGENTS.md and/or CLAUDE.md  → convention rules (append-only, no renumber)
                               (every session knows the rules)

NOTES.md                    → prefix table under Taxonomy / Conventions
                               (living reference, grows with the project)

Labeled artifacts           → items with XXX_N IDs assigned
                               (decisions, requirements, features, etc.)

Cross-references            → grep any ID → one definition, all references
                               (machine-verifiable project navigation)

Consistency passes          → periodic validation that IDs are correct
                               (no orphans, no duplicates, no drift)
```

/stable-label is the foundation that makes cross-referencing reliable. Without it, references are fragile text that breaks when things get renamed. With it, any ID is a permanent, greppable anchor — in docs, in code comments, in docstrings, anywhere text lives.
