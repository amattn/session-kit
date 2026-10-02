#!/usr/bin/env python3
"""Build a blind side-by-side review page for an iteration.
usage: sidebyside.py <iteration-dir> <out-dir> [seed]
Writes <out-dir>/sidebyside.html and <out-dir>/key.json (left/right -> configuration)."""
import json, os, random, glob, html, sys
src, out = sys.argv[1], sys.argv[2]; random.seed(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
os.makedirs(out, exist_ok=True); cases = []; key = {}
for e in sorted(glob.glob(f"{src}/eval-*")):
    name = os.path.basename(e); meta = json.load(open(f"{e}/eval_metadata.json"))
    confs = ["with_skill", "without_skill"]; random.shuffle(confs); key[name] = {"left": confs[0], "right": confs[1]}
    sides = []
    for conf in confs:
        od = f"{e}/{conf}/run-1/outputs"; files = [("Reply to the user", open(f"{od}/response.md").read(), "md")]
        for p in sorted(glob.glob(f"{od}/project/**/*", recursive=True)):
            if os.path.isfile(p) and not p.endswith(".gitkeep"):
                rel = os.path.relpath(p, f"{od}/project"); files.append((rel, open(p).read(), "code" if rel.endswith(".py") else "md"))
        sides.append(files)
    cases.append({"name": name, "prompt": meta["prompt"], "sides": sides})
json.dump(key, open(f"{out}/key.json", "w"), indent=2)
esc = html.escape; parts = []
for i, c in enumerate(cases):
    cols = []
    for label, files in zip(("Left", "Right"), c["sides"]):
        blocks = "".join(f'<details open><summary>{esc(f)}</summary>' + (f'<pre><code>{esc(t)}</code></pre>' if k == "code" else f'<div class="md" data-md="{esc(t)}"></div>') + '</details>' for f, t, k in files)
        cols.append(f'<div class="col"><h3>{label}</h3>{blocks}</div>')
    parts.append(f'''<section id="c{i}"><h2>{i+1}. {esc(c["name"])}</h2>
<details class="prompt"><summary>Prompt and setup</summary><pre>{esc(c["prompt"])}</pre></details>
<div class="row">{cols[0]}{cols[1]}</div>
<div class="fb"><label>Prefer: <select data-case="{esc(c["name"])}" class="pref"><option value="">—</option><option>Left</option><option>Right</option><option>Neither</option><option>Both fine</option></select></label>
<textarea data-case="{esc(c["name"])}" placeholder="What you like / dislike about Left and Right"></textarea></div></section>''')
title = esc(os.path.basename(os.path.normpath(src)))
page = f'''<!doctype html><html><head><meta charset="utf-8"><title>{title} blind side-by-side</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<style>
body{{font:15px/1.45 -apple-system,Helvetica,Arial,sans-serif;margin:0;padding:16px 24px;color:#222;background:#fafafa}}
h2{{margin:40px 0 8px;border-top:3px solid #333;padding-top:16px}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start}}
.col{{background:#fff;border:1px solid #ddd;border-radius:6px;padding:12px 16px;min-width:0}}
.col h3{{margin:0 0 8px;color:#555}} details{{margin:8px 0}} summary{{cursor:pointer;font-weight:600;color:#444}}
.md{{overflow-wrap:anywhere}} .md table{{border-collapse:collapse}} .md td,.md th{{border:1px solid #ccc;padding:3px 8px;vertical-align:top}}
pre{{background:#f4f4f4;padding:10px;overflow:auto;white-space:pre-wrap;font-size:13px}} .prompt pre{{background:#fff8e1}}
.fb{{margin-top:12px}} textarea{{width:100%;height:90px;margin-top:6px;font:14px inherit;padding:8px;box-sizing:border-box}}
#bar{{position:sticky;top:0;background:#333;color:#fff;padding:10px 24px;margin:-16px -24px 0;z-index:9;display:flex;gap:16px;align-items:center}}
#bar button{{font-size:15px;padding:6px 14px}} #bar a{{color:#9cf}}
</style></head><body>
<div id="bar"><b>{title} — blind, side-by-side</b> <span>Left/Right randomized per case. Feedback autosaves locally.</span><button id="export">Export feedback.json</button><span id="nav"></span></div>
{"".join(parts)}
<script>
document.querySelectorAll('.md').forEach(d=>{{d.innerHTML=window.marked?marked.parse(d.dataset.md):'<pre>'+d.dataset.md.replace(/</g,'&lt;')+'</pre>'}});
const KEY='blind-fb-{title}'; let fb={{}}; try{{fb=JSON.parse(localStorage.getItem(KEY)||'{{}}')}}catch(e){{}}
document.querySelectorAll('textarea,select.pref').forEach(el=>{{const c=el.dataset.case,k=el.tagName==='SELECT'?'prefer':'feedback';
  if(fb[c]&&fb[c][k])el.value=fb[c][k]; el.addEventListener('input',()=>{{fb[c]=fb[c]||{{}};fb[c][k]=el.value;try{{localStorage.setItem(KEY,JSON.stringify(fb))}}catch(e){{}}}})}});
document.getElementById('nav').innerHTML=[...document.querySelectorAll('section')].map((s,i)=>`<a href="#${{s.id}}">${{i+1}}</a>`).join(' ');
document.getElementById('export').onclick=()=>{{const rows=[...document.querySelectorAll('section')].map(s=>{{const c=s.querySelector('textarea').dataset.case;return{{case:c,prefer:(fb[c]||{{}}).prefer||'',feedback:(fb[c]||{{}}).feedback||''}}}});
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({{reviews:rows,status:'complete'}},null,2)],{{type:'application/json'}}));a.download='feedback.json';a.click()}};
</script></body></html>'''
open(f"{out}/sidebyside.html", "w").write(page); print("written", f"{out}/sidebyside.html")
