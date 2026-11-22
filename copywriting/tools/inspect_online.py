# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
d = json.load(io.open(ROOT/"tools"/"i18n_zh.json", encoding="utf-8"))
z = d["zh-CN"]

CONF = ["Filter", "Products", "Availability", "Price", "Sort by", "Quantity",
        "Recommend", "Recommended", "In stock", "Out of stock", "Best selling",
        "Checkout", "Subtotal", "Sign in", "Register"]
EXIST = ["Search products", "All Gear", "What's in the Box", "Add to cart"]
SORT = ["Price, low to high", "Price, high to low"]

print("=== confirmed missing list ===")
for k in CONF:
    print(("IN " if k in z else "OUT"), repr(k), "->", z.get(k, ""))
print("=== existing, verify zh ===")
for k in EXIST:
    print(("IN " if k in z else "OUT"), repr(k), "->", z.get(k, ""))
print("=== sort options ===")
for k in SORT:
    print(("IN " if k in z else "OUT"), repr(k), "->", z.get(k, ""))
print("=== plural patterns ===")
for k, v in d["_meta"]["plural_patterns"].items():
    print(repr(k), "->", v)
print("total keys:", len(z))
# near-variants for Sign in / Register / Checkout / Subtotal / Best selling
for probe in ["Sign", "Register", "Checkout", "Subtotal", "Best", "Cart", "Total"]:
    hits = [k for k in z if probe.lower() in k.lower()]
    if hits:
        print("near", repr(probe), "->", hits)
