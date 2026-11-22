# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
d = json.load(io.open(ROOT/"tools"/"i18n_zh.json", encoding="utf-8"))
z = d["zh-CN"]
print("FINAL keys:", len(z))

must = ["Filter", "Products", "Availability", "Price", "Sort by", "Quantity",
        "Recommend", "Recommended", "In stock", "Out of stock", "Best selling",
        "Checkout", "Subtotal", "Sign in", "Register", "Search products",
        "All Gear", "What's in the Box", "Add to cart",
        "Price, high to low", "Price, low to high",
        "Your cart is empty", "Shop now", "Recently viewed", "1 sold",
        "Newest in", "Pageviews, high to low",
        "ShotStart — Your first shot starts here."]
missing = [k for k in must if k not in z]
print("missing must:", missing if missing else "none")

RESID = ["Mini Ball Head — $11.99", "Mini Ball Head ($11.99)",
         "Magnetic Mount — $9.99", "Microfiber 3-Pack — $8.99", "Shot List Cards — $6.99",
         "will reply by email", "within 2 business days"]
for b in RESID:
    hits = [k for k in z if b in k]
    if hits:
        print("RESIDUAL:", b, hits)
print("residual check done")

pp = d["_meta"]["plural_patterns"]
print("patterns:", list(pp.keys()))

# pages txt price/contact sanity
pages = list((ROOT/"pages").glob("*.txt"))
print("pages txt:", len(pages))
txt = "\n".join(p.read_text(encoding="utf-8") for p in pages)
for bad in ["Magnetic Mount — $9.99", "Microfiber 3-Pack — $8.99", "Shot List Cards — $6.99",
            "Mini Ball Head — $11.99", "our team will reply by email", "within 2 business days"]:
    print("pages residual", repr(bad), "->", bad in txt)
for good in ["Magnetic Mount — $11.99", "Microfiber 3-Pack — $6.99", "Shot List Cards — $8.99",
             "we read every message and reply as soon as we can"]:
    print("pages present", repr(good), "->", good in txt)
