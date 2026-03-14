# Consistency Pass: DEC_3 Rename

## Approach

Quick consistency pass — grepped all occurrences of `DEC_3` in NOTES.md and CLAUDE.md after the user reported renaming it.

## Occurrences of DEC_3

| Location | Line | Text | Status |
|----------|------|------|--------|
| NOTES.md | 11 | `### DEC_3: Deployment — Fly.io` (definition) | Stale heading — says "Renamed to 'Cloud hosting' for clarity" but the heading still reads "Deployment — Fly.io" |
| NOTES.md | 33 | `The deployment pipeline (DEC_3) runs tests via GitHub Actions (DEC_4)...` | OK — contextually consistent with deployment/cloud hosting |
| NOTES.md | 35 | `All error responses include a machine-readable error code per DEC_3.` | Wrong reference — DEC_3 is about deployment/cloud hosting, not error response formats. Likely should reference REQ_4 (JSON response conventions) or a decision not yet captured |
| CLAUDE.md | — | No occurrences | N/A |

## Issues Found

1. **Stale heading (NOTES.md line 11):** The definition heading still says "Deployment — Fly.io" despite the inline note that it was renamed to "Cloud hosting." The heading should be updated to match the new name, e.g., `### DEC_3: Cloud Hosting — Fly.io` or `### DEC_3: Cloud Hosting`.

2. **Misattributed reference (NOTES.md line 35):** "All error responses include a machine-readable error code per DEC_3" makes no sense — DEC_3 covers deployment, not API response formatting. This reference either:
   - Should point to REQ_4 (snake_case JSON responses, error key conventions), or
   - Refers to a decision about machine-readable error codes that hasn't been formally captured yet (which would need a new DEC_N).

## Recommended Fixes

- Update the DEC_3 heading to reflect "Cloud hosting"
- Fix the line 35 reference — confirm with the user whether it should point to REQ_4 or if a new decision (DEC_5) should be created for machine-readable error codes
