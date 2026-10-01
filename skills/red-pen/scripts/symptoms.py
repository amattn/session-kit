#!/usr/bin/env python3
"""Count the recognizable-shape symptoms in markdown prose.

    symptoms.py FILE [FILE ...]            report per file
    symptoms.py --compare BEFORE AFTER     report both and the delta
    symptoms.py --section 'HEADING' FILE   restrict to one section (H2/H3 text match)
    symptoms.py --json ...                 machine-readable

Counts are signals, not verdicts. A table and the prose that teaches its rows
are one rule in two registers; a repeated phrase inside a code block is code.
Restatement is matched literally (5-word runs); paraphrased restatement, the
kind that matters most, is not detected and has to be counted by the reader.
"""
import argparse, json, re, statistics, sys
from collections import defaultdict

OPENERS = r"\b(?:This is|That is|That's|It is worth|It's worth|Note that|Importantly|In other words|Crucially|Essentially|Basically)\b"
HEDGES = r"\b(?:probably|likely|may well|appears to|seems to|presumably|should probably|arguably|more or less)\b"
DATED = r"\b(?:DECIDED|RESOLVED|ANSWERED|Refined|Updated|Amended|Superseded)\b[^.\n]{0,20}\(?\d{4}-\d{2}-\d{2}|\bas of \d{4}-\d{2}-\d{2}"
FORWARD = r"\b(?:see below|as described above|as noted (?:above|earlier)|described above|discussed above|more on this below|as we will see)\b"
NARRATION = r"\b(?:as requested|I've now|I have now|we've now|per (?:the|your) (?:request|instruction)|in this (?:document|section) we|this (?:document|section) (?:describes|covers|explains|will))\b"
SCAFFOLD = r"^#{1,6}\s+(?:Overview|Introduction|Summary|Conclusion|Background|Next steps)\b"

def strip_code(text):
    return re.sub(r"```.*?```", "\n", text, flags=re.S)

def section(text, heading):
    lines = text.split("\n"); out = []; on = False; level = None
    for ln in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", ln)
        if m:
            if on and len(m.group(1)) <= level: break
            if not on and heading.lower() in m.group(2).lower():
                on = True; level = len(m.group(1))
        if on: out.append(ln)
    return "\n".join(out)

def sentences(prose):
    body = re.sub(r"^#{1,6}.*$", "", prose, flags=re.M)
    body = re.sub(r"\|.*\|", "", body)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z`*\"(])", body)
    return [re.sub(r"\s+", " ", p).strip() for p in parts if len(p.split()) >= 6]

def normalize(s):
    return re.findall(r"[a-z0-9']+", s.lower())

def restated(sents, n=5, min_count=2):
    """Phrases of n words that recur in distinct sentences. Returns the longest runs."""
    where = defaultdict(set)
    toks = [normalize(s) for s in sents]
    for i, t in enumerate(toks):
        for j in range(len(t) - n + 1):
            where[tuple(t[j:j+n])].add(i)
    hits = {k: v for k, v in where.items() if len(v) >= min_count}
    # merge overlapping shingles into longer phrases
    phrases = {}
    for k, v in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        key = frozenset(v)
        if key in phrases and any(" ".join(k) in p for p in phrases[key]): continue
        phrases.setdefault(key, []).append(" ".join(k))
    out = []
    for key, ps in phrases.items():
        ps.sort(key=len, reverse=True)
        out.append((ps[0], len(key)))
    out.sort(key=lambda x: (-x[1], -len(x[0])))
    return out

def analyze(text):
    prose = strip_code(text)
    words = len(re.findall(r"\S+", prose))
    heads = re.findall(r"^(#{1,6})\s+(.*)$", prose, flags=re.M)
    sent_heads = [h for _, h in heads if len(h.split()) >= 8 or re.search(r"[.!?]$|\s[-—]\s", h)]
    bold_leads = len(re.findall(r"^(?:[-*]\s+|\d+\.\s+)?\*\*[^*\n]+\*\*", prose, flags=re.M))
    sec_lengths = []; n = 0; started = False
    for ln in prose.split("\n"):
        if re.match(r"^#{2,3}\s", ln):
            if started and n > 0: sec_lengths.append(n)
            started = True; n = 0
        else:
            n += len(ln.split())
    if started and n > 0: sec_lengths.append(n)
    sents = sentences(prose)
    rest = restated(sents)
    r = {
        "words": words,
        "headers": len(heads),
        "words_per_header": round(words / len(heads)) if heads else None,
        "sentence_headers": len(sent_heads),
        "scaffold_headers": len(re.findall(SCAFFOLD, prose, flags=re.M | re.I)),
        "bold_leads": bold_leads,
        "openers": len(re.findall(OPENERS, prose)),
        "hedges": len(re.findall(HEDGES, prose, flags=re.I)),
        "dated_markers": len(re.findall(DATED, prose)),
        "forward_refs": len(re.findall(FORWARD, prose, flags=re.I)),
        "narration": len(re.findall(NARRATION, prose, flags=re.I)),
        "em_dashes_per_1k": round(prose.count("—") / words * 1000, 1) if words else 0,
        "restated_phrases": len(rest),
        "restated_top": [{"phrase": p, "sentences": c} for p, c in rest[:8]],
        "section_words": {"n": len(sec_lengths), "min": min(sec_lengths) if sec_lengths else 0,
                           "median": int(statistics.median(sec_lengths)) if sec_lengths else 0,
                           "max": max(sec_lengths) if sec_lengths else 0},
    }
    return r

ROWS = [("words","words"),("headers","headers"),("sentence_headers","headers that are sentences"),
        ("scaffold_headers","Overview/Summary/Next steps headers"),("bold_leads","bold leads"),
        ("openers","'This is / That is / Note that' openers"),("hedges","hedges"),
        ("dated_markers","dated status markers"),("forward_refs","'see below / as noted above'"),
        ("narration","session narration"),("restated_phrases","phrases restated across sentences"),
        ("em_dashes_per_1k","em-dashes per 1k words")]

def render(label, r):
    lines = [f"== {label}"]
    for k, name in ROWS:
        lines.append(f"  {name:<42} {r[k]}")
    s = r["section_words"]
    lines.append(f"  {'section words min/median/max':<42} {s['min']}/{s['median']}/{s['max']} (n={s['n']})")
    if r["restated_top"]:
        lines.append("  restated, most frequent:")
        for t in r["restated_top"]:
            lines.append(f"    x{t['sentences']}  \"{t['phrase']}\"")
    return "\n".join(lines)

def render_compare(a, b):
    lines = ["== delta (before -> after)"]
    for k, name in ROWS:
        lines.append(f"  {name:<42} {a[k]} -> {b[k]}")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--compare", nargs=2, metavar=("BEFORE","AFTER"))
    ap.add_argument("--section")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    files = a.compare or a.files
    if not files: ap.error("give FILE(s) or --compare BEFORE AFTER")
    results = {}
    for f in files:
        text = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        if a.section: text = section(text, a.section)
        results[f] = analyze(text)
    if a.json:
        print(json.dumps(results, indent=2)); return
    for f, r in results.items(): print(render(f, r))
    if a.compare:
        print(render_compare(results[files[0]], results[files[1]]))

if __name__ == "__main__":
    main()
