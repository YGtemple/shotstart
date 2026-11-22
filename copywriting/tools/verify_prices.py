# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
d = json.load(io.open(ROOT/"tools"/"i18n_zh.json", encoding="utf-8"))
z = d["zh-CN"]
print("total keys:", len(z))

RESIDUAL = [
    "Mini Ball Head — $11.99", "Mini Ball Head ($11.99)",
    "Magnetic Mount — $9.99", "Microfiber 3-Pack — $8.99", "Shot List Cards — $6.99",
]
for bad in RESIDUAL:
    hits = [k for k in z if bad in k]
    print("residual", repr(bad), "->", hits)

NEW = [
    "Mini Ball Head — $12.99. Level and lock the frame between shots with one twist.",
    "Magnetic Mount — $11.99. Snap your phone on and off for quick desk setups.",
    "Microfiber 3-Pack — $6.99. Three spare soft cloths for between-take lens and screen cleaning.",
    "Shot List Cards — $8.99. Four-shot prompt cards paired with your ShotStarter script draft.",
]
for k in NEW:
    print("new in:", k in z, "|", z.get(k, "")[:30])

# cleaning kit 9.99 keys still present (unchanged)
ck = [k for k in z if "Lens Cleaning Kit ($9.99)" in k]
print("cleaning-kit 9.99 keys kept:", len(ck))
