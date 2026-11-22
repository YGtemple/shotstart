# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
z = json.load(io.open(ROOT / "tools" / "i18n_zh.json", encoding="utf-8"))["zh-CN"]
for k, v in z.items():
    if "contact us for details" in k or "pending final confirmation" in k or "legal review" in k:
        print(repr(k), "=>", repr(v))
