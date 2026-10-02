#!/usr/bin/env python3
"""Mechanical facts about an eval run's outputs, for the grader.
usage: check.py <run_dir>   (run_dir contains outputs/)"""
import json, os, re, sys, glob

run = sys.argv[1]; out = os.path.join(run, "outputs")
def read(p):
    try: return open(p, encoding="utf-8").read()
    except Exception: return ""
def words(t): return len(re.findall(r"\S+", re.sub(r"```.*?```", "", t, flags=re.S)))
def facts(t):
    body = re.sub(r"```.*?```", "", t, flags=re.S)
    return {
      "words": words(t),
      "words_incl_code": len(re.findall(r"\S+", t)),
      "headers": re.findall(r"^#{1,6}\s+(.*)$", body, flags=re.M),
      "scaffold_headers": re.findall(r"^#{1,6}\s+(Overview|Introduction|Summary|Conclusion|Background|Next steps).*$", body, flags=re.M|re.I),
      "openers": len(re.findall(r"\b(?:This is|That is|That's)\b", body)),
      "performative": re.findall(r"Great question|I hope this helps|Certainly|I'd be happy|Happy to help|Let me know if", body, flags=re.I),
      "apology_or_meta": re.findall(r"\b(?:sorry|apolog\w+|too long|too wordy|my previous|the previous reply|earlier reply)\b", body, flags=re.I),
      "bold_leads": len(re.findall(r"^(?:[-*]\s+|\d+\.\s+)?\*\*[^*\n]+\*\*", body, flags=re.M)),
      "redpen_breadcrumb": "managed by /red-pen" in t,
      "first_sentence": re.split(r"(?<=[.!?])\s", body.strip(), maxsplit=1)[0][:200] if body.strip() else "",
    }
res = {"run": run, "files": sorted(os.path.relpath(p, out) for p in glob.glob(out+"/**/*", recursive=True) if os.path.isfile(p))}
resp = read(os.path.join(out, "response.md")); res["response"] = facts(resp)
for p in glob.glob(out+"/project/**/*.md", recursive=True):
    res[os.path.relpath(p, out)] = facts(read(p))
# eval-specific
gs = glob.glob(out+"/project/**/grid_section.md", recursive=True)
if gs:
    t = read(gs[0]); body = re.sub(r"```.*?```", "", t, flags=re.S)
    res["grid_section"] = {
      "replacement_fact_mentions": len(re.findall(r"deliberate|not an oversight|on purpose|rejected|withdrawn|deprecated|won and edge|replaced", body, flags=re.I)),
      "openers": len(re.findall(r"\b(?:This is|That is|That's)\b", body)),
      "h3_sections": re.findall(r"^###\s+(.*)$", body, flags=re.M),
      "has_90_minute_gap": bool(re.search(r"90-minute", body)),
      "has_align_to_edges": bool(re.search(r"edge|align", body, flags=re.I)),
      "has_closeness_to_noon": "noon" in body,
      "has_adaptive_grid_two_shapes": bool(re.search(r"follows the meeting", body)) and bool(re.search(r"follows the gap", body)),
      "has_entanglement": bool(re.search(r"entangl", body, flags=re.I)),
      "duration_grid_bullets_kept": bool(re.search(r"^- \*\*Duration\*\*", body, flags=re.M)) and bool(re.search(r"^- \*\*Grid", body, flags=re.M)),
      "mechanism_bullets_kept": bool(re.search(r"^- \*\*Advisor start-time rules\*\*", body, flags=re.M)),
    }
ds = glob.glob(out+"/project/**/design.md", recursive=True)
if ds:
    t = read(ds[0])
    res["design_md"] = {"scaffold_headers": re.findall(r"^#{1,6}\s+(Overview|Background|Next steps).*$", t, flags=re.M|re.I),
                        "narration": bool(re.search(r"In this document we will|This document describes", t)),
                        "db_open_claim_kept": bool(re.search(r"database choice .{0,40}(still open|open)", t, flags=re.I)),
                        "rl_undecided_claim_kept": bool(re.search(r"rate limiting approach .{0,40}not (yet )?been decided|has not yet been decided", t, flags=re.I)),
                        "storage_section": bool(re.search(r"^#{1,6}\s+.*(Storage|Open)", t, flags=re.M|re.I))}
wc = glob.glob(out+"/project/**/webhook_client.py", recursive=True)
if wc:
    t = read(wc[0])
    res["webhook_client"] = {"comments": re.findall(r"#.*$", t, flags=re.M), "todo": bool(re.search(r"TODO|FIXME|pass\s*#", t)),
                             "has_backoff": bool(re.search(r"sleep|backoff", t, flags=re.I)), "mentions_4xx_or_5xx": bool(re.search(r"5\d\d|4\d\d|status_code", t))}
print(json.dumps(res, indent=2))
