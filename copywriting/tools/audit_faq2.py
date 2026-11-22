# -*- coding: utf-8 -*-
import json, io, pathlib, sys, re
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
sys.path.insert(0, str(ROOT / "tools"))
from shotstart_content import PAGES
from build_shotstart import publish_text, inline_for, PH_RE

z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]

miss = []
n = 0
for fname, blocks in PAGES.items():
    if not fname.startswith("product-"):
        continue
    last_q = None
    for blk in blocks:
        if blk[0] == "faq_q":
            last_q = blk[1]
        elif blk[0] == "faq_a":
            n += 1
            online = publish_text(blk[1], fname)
            if online not in z:
                miss.append((fname, last_q, online))
print("faq_a total:", n, "| missing after fallback:", len(miss))
for f, q, a in miss:
    print("MISS", f, "|", q, "|", a)
