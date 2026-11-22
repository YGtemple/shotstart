# -*- coding: utf-8 -*-
import json, io, pathlib, sys, os
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
sys.path.insert(0, str(ROOT / "tools"))
from shotstart_content import PAGES

z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]

faq_a, box = [], []
for fname, blocks in PAGES.items():
    if not fname.startswith("product-"):
        continue
    last_q = None
    for blk in blocks:
        kind = blk[0]
        if kind == "faq_q":
            last_q = blk[1]
        elif kind == "faq_a":
            faq_a.append((fname, last_q, blk[1]))
        elif kind == "bullets":
            for item in blk[1]:
                box.append((fname, item))

print("=== FAQ answers:", len(faq_a))
miss = []
for fname, q, a in faq_a:
    if a not in z:
        miss.append((fname, q, a))
        print("MISS", fname, "|", q, "|", a)
print("missing faq_a:", len(miss))

print("\n=== bullets count:", len(box))
bmiss = [(f, i) for f, i in box if i not in z]
for f, i in bmiss:
    print("MISS bullet", f, "|", i)
print("missing bullets:", len(bmiss))
