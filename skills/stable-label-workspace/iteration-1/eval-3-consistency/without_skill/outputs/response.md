# Consistency Pass — DEC_3 Rename

## What changed

DEC_3 was renamed from "Deployment" to "Cloud hosting" for clarity. The underlying choice (Fly.io) is unchanged.

## References found

| Location | Text | Status |
|---|---|---|
| NOTES.md line 6 | `Satisfies REQ_3 (real database testing).` | OK — unrelated to DEC_3 |
| NOTES.md line 33 | `The deployment pipeline (DEC_3) runs tests via GitHub Actions (DEC_4) before deploying to Fly.io.` | OK — still accurate, DEC_3 is about Fly.io deployment |
| NOTES.md line 35 | `All error responses include a machine-readable error code per DEC_3.` | **INCONSISTENT** — DEC_3 is about cloud hosting / Fly.io, not error response formats |

## Issues

1. **Line 35 — wrong label reference.** The sentence "All error responses include a machine-readable error code per DEC_3" cites the deployment decision for an API response formatting rule. DEC_3 (Cloud hosting — Fly.io) has nothing to do with error code formats. This is likely a stale or incorrect reference. Candidates for the correct label:
   - REQ_2 (Proper HTTP status codes) — closest match for error response behavior
   - REQ_4 (snake_case JSON responses) — covers response format conventions
   - Or a new decision label (e.g., DEC_5) may be needed if "machine-readable error codes" was a distinct decision that was never recorded

## Recommendation

Fix line 35 to reference the correct label, or create a new DEC_5 for the machine-readable error code decision if it was intentional and distinct from REQ_2/REQ_4.
