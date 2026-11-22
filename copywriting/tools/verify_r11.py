# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
p = ROOT / "tools" / "i18n_zh.json"
d = json.load(io.open(p, encoding="utf-8"))
z = d["zh-CN"]
print("keys:", len(z))
print("$11.99 in keys:", sum("$11.99" in k for k in z))

OLD_CONTACT = [
    "Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note and our team will reply by email. For order questions, please include your order number so we can help faster.",
    "We reply to messages within 2 business days, by email. This store is email-only; no physical mailing address is published.",
]
for k in OLD_CONTACT:
    print("OLD contact retired:", k[:40], "->", k not in z)

NEW = [
    "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99).",
    "Pair this with the other Pro Creator Kit items. What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.",
    "Bundle contents: Adjustable Phone Tripod ($19.99) + Extension Pole ($16.99) + Mini Ball Head ($12.99) + Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.",
    "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.",
    "Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note — we read every message and reply as soon as we can. For order questions, please include your order number so we can help faster.",
    "We read every message and reply as soon as we can. This store is email-only; no physical mailing address is published.",
    "ShotStart — Your first shot starts here.",
    "Sort by", "Recommend", "Your cart is empty", "Shop now",
    "Recently viewed", "Quantity", "1 sold",
]
missing = [k for k in NEW if k not in z]
print("new keys total:", len(NEW), "missing:", len(missing))
for k in missing:
    print("  MISS:", k)

print("Box heading value:", z.get("What's in the Box"))
print("sold pattern:", d.get("_meta", {}).get("plural_patterns", {}).get("{{count}} sold"))
# old ball-head price keys still present?
for k in list(z):
    if "Mini Ball Head ($11.99)" in k:
        print("RESIDUAL OLD PRICE KEY:", k[:90])
