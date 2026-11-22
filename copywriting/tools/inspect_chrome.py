# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
d = json.load(io.open(ROOT/"tools"/"i18n_zh.json", encoding="utf-8"))
z = d["zh-CN"]
cands = ["Filter", "Products", "Availability", "Price", "Sort by", "Recommend",
         "Search products", "In stock", "Out of stock", "Newest in",
         "Pageviews, high to low", "Price, high to low", "Price, low to high"]
for k in cands:
    print(("IN " if k in z else "OUT"), repr(k), "->", z.get(k, ""))
print("--- plural patterns ---")
pp = d.get("_meta", {}).get("plural_patterns", {})
for k, v in pp.items():
    print(repr(k), "->", v)
print("total zh keys:", len(z))
