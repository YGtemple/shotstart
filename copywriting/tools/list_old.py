# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]
pats = ["Check your inbox", "received your message", "reply by email", "sharp",
        "in! Check", "Refill reminder", "restock", "you're subscribed", "hear from"]
for k, v in z.items():
    if any(p.lower() in k.lower() for p in pats):
        print(repr(k), "=>", repr(v))
