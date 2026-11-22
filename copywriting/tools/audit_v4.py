# -*- coding: utf-8 -*-
import json, io, pathlib, sys
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
sys.path.insert(0, str(ROOT / "tools"))
from shotstart_content import PAGES
from build_shotstart import publish_text

z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]

FRONT = {"h1", "h2", "p", "bullets", "faq_q", "faq_a", "table"}
cur_h2 = None
buckets = {"title": [], "desc": [], "entry": [], "box_h2": [], "missing_all": []}

def in_dict(s):
    return s in z

for fname, blocks in PAGES.items():
    cur_h2 = None
    for blk in blocks:
        kind = blk[0]
        if kind == "h2":
            cur_h2 = blk[1]
            continue
        if kind in ("note", "price", "setup"):
            continue
        if kind == "p":
            vals = [blk[1]]
        elif kind == "bullets":
            vals = blk[1]
        elif kind in ("faq_q", "faq_a"):
            vals = [publish_text(blk[1], fname)]
        elif kind == "table":
            vals = [c for row in blk[2] for c in row]
        else:
            vals = []
        for v in vals:
            if not v.strip():
                continue
            if not in_dict(v):
                buckets["missing_all"].append((fname, cur_h2, v))
            if cur_h2 == "Product Title":
                buckets["title"].append((fname, v, in_dict(v)))
            elif cur_h2 == "Description Paragraph":
                buckets["desc"].append((fname, v, in_dict(v)))
            elif cur_h2 == "Bundle Entry":
                buckets["entry"].append((fname, v, in_dict(v)))
            elif kind == "h2" and v == "What's in the Box":
                buckets["box_h2"].append((fname, in_dict(v)))

print("=== Product Title ===")
for f, v, ok in buckets["title"]:
    print(("IN " if ok else "OUT"), f, "|", v)
print("\n=== Description Paragraph ===")
for f, v, ok in buckets["desc"]:
    print(("IN " if ok else "OUT"), f, "|", v[:110])
print("\n=== Bundle Entry p ===")
for f, v, ok in buckets["entry"]:
    print(("IN " if ok else "OUT"), f, "|", v[:120])
print("\n=== missing all (front) count:", len(buckets["missing_all"]))
for f, h, v in buckets["missing_all"]:
    print("OUT", f, "|", h, "|", v[:100])
