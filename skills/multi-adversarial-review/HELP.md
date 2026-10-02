# /multi-adversarial-review — Quick Reference

`mar` is the short name. Same skill.

**Setup:** Nothing to bootstrap. The skill needs at least one reviewer route that is not the host model: `codex exec` for Codex, Pi (or cn / OpenCode) for GLM or another non-family model. `references/routes.md` has the launch recipes; read it before launching any route. Project directives win: if your AGENTS.md or iteration spec defines its own review cadence, that governs.

**Ongoing:** Invoke it when a piece of work is committed and ready for a gate. The chain is sequential: stable commit, reviewer N reads it, you (the lead) disposition every finding and commit, reviewer N+1 reads the new commit. Reviewers are read-only; you verify every finding against source before acting on it.

| Say | What happens |
|---|---|
| `/mar` or `/multi-adversarial-review` | Default chain with the available non-host models, strongest finder last |
| `/mar with Claude, Codex, and GLM 5.3` | The reviewer order you name |
| `/mar to review HEAD against <base>` | Point reviewers at a commit range; the chain is cumulative, prior findings are committed and visible |
| `/mar review <note> as a spec` | Spec target: principle fit, coherence, viability, open vs mechanical, readiness |
| `/mar review <doc> as copy for <readers>` | Copy target: one reviewer per named reader reports where they stopped, what they reread, what they already knew; findings quote the sentence and name a kind |

Targets: `code`, `plan`, `code-vs-plan`, `spec`, `copy`. Dispositions: `accepted-fixed`, `accepted-deferred`, `rejected` (with evidence), `unclear-blocked`, `no-findings` (must name residual risk), `route-failed`, `contested`.

**Example:**
```
You: /mar to review HEAD against main
Agent: Baseline 3f2a1c9 is stable. Launching GLM through Pi in a disposable
       worktree at 3f2a1c9, no writes to the primary checkout.
       ... (awaits terminal state)
       GLM: 3 findings. Verified against source:
       - F1 retry loop swallows TransportError — accepted-fixed, test added
       - F2 "unused import" — rejected, it is used in the type annotation
       - F3 backoff cap unbounded — accepted-deferred, tracked as RSK_4
       Committed 8b77e02: review: Record GLM disposition.
       Launching Codex against 8b77e02 ...

       Review chain
       - 3f2a1c9: stable baseline
       - 8b77e02: after GLM disposition - 1 fixed, 1 rejected, 1 deferred
       - c41d9aa: after Codex disposition - no findings; residual risk: RSK_4
```
