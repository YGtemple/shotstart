# -*- coding: utf-8 -*-
"""round11: price correction ($12.99 ball head), contact de-commit, v4 chrome/title keys."""
import json, io, pathlib

p = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy\tools\i18n_zh.json")
d = json.load(io.open(p, encoding="utf-8"))
z = d["zh-CN"]

# ---- retire old-price Pro strings still carrying $11.99 ball head ----
DROP_PRICE = [k for k in list(z) if "Mini Ball Head ($11.99)" in k]
# ---- retire old contact promise strings ----
DROP_CONTACT = [
    "Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note and our team will reply by email. For order questions, please include your order number so we can help faster.",
    "We reply to messages within 2 business days, by email. This store is email-only; no physical mailing address is published.",
]
dropped = []
for k in DROP_PRICE + DROP_CONTACT:
    if k in z:
        del z[k]
        dropped.append(k)

ADD = {
    # new-price Pro strings ($12.99 ball head)
    "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99).":
        "可调手机三脚架（$19.99）、延长杆（$16.99）、迷你云台（$12.99）、器材收纳包（$12.99）。",
    "Pair this with the other Pro Creator Kit items. What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.":
        "可与 Pro Creator Kit 其他商品搭配套装。套装内含：可调手机三脚架（$19.99）、延长杆（$16.99）、迷你云台（$12.99）、器材收纳包（$12.99）。套装价 $62.96——结账时使用优惠码 STARTERKIT：$53.52，省 $9.44。",
    "Bundle contents: Adjustable Phone Tripod ($19.99) + Extension Pole ($16.99) + Mini Ball Head ($12.99) + Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.":
        "可调手机三脚架（$19.99）+ 延长杆（$16.99）+ 迷你云台（$12.99）+ 器材收纳包（$12.99）。套装价 $62.96——结账时使用优惠码 STARTERKIT：$53.52，省 $9.44。",
    "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.":
        "可调手机三脚架（$19.99）、延长杆（$16.99）、迷你云台（$12.99）、器材收纳包（$12.99）。套装价 $62.96——结账时使用优惠码 STARTERKIT：$53.52，省 $9.44。",
    # contact de-commit (no reply-time/channel promise)
    "Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note — we read every message and reply as soon as we can. For order questions, please include your order number so we can help faster.":
        "对订单、商品或 7 天拍摄挑战有疑问？留言给我们——我们阅读每一条留言，并尽快回复。订单问题请附上订单号，以便更快协助。",
    "We read every message and reply as soon as we can. This store is email-only; no physical mailing address is published.":
        "我们阅读每一条留言，并尽快回复。本店仅以邮箱承接联系，不公布实体邮寄地址。",
    # home document.title / og:title
    "ShotStart — Your first shot starts here.":
        "ShotStart——你的第一个镜头，从这里开始。",
    # collection / cart chrome (new order overrides prior chrome non-translation)
    "Sort by": "排序方式",
    "Recommend": "推荐",
    "Your cart is empty": "购物车是空的",
    "Shop now": "立即选购",
    "Recently viewed": "最近浏览",
    "Quantity": "数量",
    "1 sold": "已售 1 件",
}
added = []
for k, v in ADD.items():
    if k not in z:
        z[k] = v
        added.append(k)

# value-only fix: Box heading wording
if "What's in the Box" in z:
    z["What's in the Box"] = "盒内清单"

# plural pattern: sold count
d.setdefault("_meta", {}).setdefault("plural_patterns", {})
d["_meta"]["plural_patterns"]["{{count}} sold"] = "已售 {{count}} 件"

p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("dropped:", len(dropped))
for k in dropped:
    print("  DROP:", k[:80])
print("added:", len(added))
print("keys:", len(z))
