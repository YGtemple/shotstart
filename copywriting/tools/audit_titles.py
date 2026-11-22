# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
aud = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_diff.json", encoding="utf-8"))
live = aud["live"]
src = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"i18n_zh.json", encoding="utf-8"))["zh-CN"]
keys = ["Magnetic Mount","Mini Ball Head","Microfiber 3-Pack","Shot List Cards",
        "Magnetic Mount — Snap Your Phone On and Off in Seconds",
        "Magnetic Mount: Snap your phone on and off for quick desk setups."]
for k in keys:
    print(repr(k))
    print("  live:", live.get(k, "—"))
    print("  src :", src.get(k, "—"))
