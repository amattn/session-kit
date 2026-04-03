# /feedback-foo — Quick Reference

**Setup:** Run `/feedback-foo` (or `/foo`, `/feedback`, `/observation`) in your project. It creates FEEDBACK_FOO.md (a tracker for process observations with open/resolved lifecycle) and adds a Self-Improvement directive to CLAUDE.md telling the agent to notice and surface patterns proactively.

**Ongoing:** Always-on detection — the agent notices recurring patterns, drift, and friction without being asked. When it detects something, it surfaces a lightweight proposal ("I've noticed X twice — want me to note it in NOTES.md or promote it to a CLAUDE.md discipline?"). Invoke `/foo` when you want to:
- Review open observations in FEEDBACK_FOO.md
- Promote a confirmed pattern to a CLAUDE.md discipline
- Create a named discipline block for a workflow you want enforced

**Example:**
```
Agent: I've noticed you always ask me to check for stale imports
       after moving files — that's the third time this session.
       Want me to track this in NOTES.md, or is it confirmed
       enough for a CLAUDE.md discipline?

You: discipline

Agent: Added to CLAUDE.md:
       ## Post-Move Discipline
       **After moving any file, grep for stale imports and update them.**
       Created FOO_3 in FEEDBACK_FOO.md → [resolved] promoted to discipline.

You: (later, during a code review discussion)
     that's a great insight — every time we add a new API route we
     forget to update the OpenAPI spec. add a foo for that

Agent: Added FOO_4 to FEEDBACK_FOO.md:
       ### FOO_4: OpenAPI spec falls behind when adding routes [drift]
       Observed during code review. Routes added without updating
       the OpenAPI spec. Not yet a discipline — monitoring frequency.
```

**Migrating from /sharpen:** If you previously used `/sharpen`, rename `SHARPEN.md` → `FEEDBACK_FOO.md`, update `<!-- managed by /sharpen -->` breadcrumbs to `<!-- managed by /foo -->` in CLAUDE.md, and rename any `SPI_N` prefixes to `FOO_N`. The skill behavior is unchanged — only the name and artifact format changed.
