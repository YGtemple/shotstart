# -*- coding: utf-8 -*-
import json, io, pathlib, sys
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
sys.path.insert(0, str(ROOT / "tools"))
from shotstart_content import PAGES
from build_shotstart import publish_text
z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]
for fname, blocks in PAGES.items():
    if not fname.startswith("product-"):
        continue
    for blk in blocks:
        if blk[0] == "faq_a":
            r = publish_text(blk[1], fname)
            print(("IN " if r in z else "OUT"), "|", fname, "|", r)
