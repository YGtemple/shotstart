# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
aud = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_diff.json", encoding="utf-8"))
live = aud["live"]
src = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"i18n_zh.json", encoding="utf-8"))["zh-CN"]
keys = ["Home","Shop","About","Contact","Contact Us","Newsletter","Subscribe","Support",
        "Policies","More links","FAQ","Account","Cart","View cart","Continue shopping",
        "Browse Creator Kits","Shop All Gear","Add to Cart","Add to cart","Search","Search products"]
for k in keys:
    print(f"{k!r:26} live={live.get(k,'—')!r:18} src={src.get(k,'—')!r}")
