# /warmup — Quick Reference

**Setup:** Run `/warmup` in your project. It audits your CLAUDE.md (or creates one), then sets up Required Reading, a post-compaction rule, loading canaries, and auto-memory entries. All managed sections are marked with `<!-- managed by /warmup -->` breadcrumbs.

**Ongoing:** You rarely invoke `/warmup` directly after setup. Its infrastructure works in the background — canaries verify files loaded, the post-compaction rule triggers re-reads after context compression. Invoke it again when:
- A rule or file isn't loading reliably (it walks an escalation ladder: tighten wording → improve positioning → add redundancy → promote to auto-memory)
- You want to add a new file to the Required Reading chain
- You suspect compaction dropped something mid-session

**Example:**
```
You: /warmup
Agent: I've audited your CLAUDE.md. Here's what I set up:
       - Required Reading: NOTES.md, PLAN.md
       - Post-Compaction Rule: re-read Required Reading after compaction
       - Session Start Canary: report git status before doing other work
       - Auto-memory entry: "always read NOTES.md"

You: (later) It keeps forgetting to read NOTES.md
Agent: The Required Reading rule is present and auto-memory is set,
       but the rule is positioned at the bottom of CLAUDE.md where
       compaction is likely dropping it. I'll move it to the top
       and strengthen the wording. I'll also add a cross-file
       reinforcement pointer at the top of NOTES.md pointing back
       to CLAUDE.md.
```
