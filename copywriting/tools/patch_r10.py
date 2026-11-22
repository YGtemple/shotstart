# -*- coding: utf-8 -*-
import json, io, pathlib

p = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy\tools\i18n_zh.json")
d = json.load(io.open(p, encoding="utf-8"))
z = d["zh-CN"]

# ---- retire: 12 specs fallback paragraphs (source dropped) ----
DROP_SPECS = [
    "Exact specifications — compatible width range, height and tilt ranges, material, net weight, folded length, foot material, and included accessories — are being finalized; contact us for details.",
    "Exact specifications — compatible width range, angle range, material, base dimensions and non-slip pad, cable cutout details, and net weight — are being finalized; contact us for details.",
    "Exact contents, approved surface list, materials, fluid volume, and kit dimensions are being finalized; contact us for details.",
    "Exact dimensions, material, net weight, and included accessories are being finalized; contact us for details.",
    "Exact diameter, surface fabric, and net weight are being finalized; contact us for details.",
    "Exact dimensions, fabric, and color are being finalized; contact us for details.",
    "Exact extended/collapsed length, material, net weight, and holder compatibility are being finalized; contact us for details.",
    "Exact contents, cloth material, fluid volume, and ingredients are being finalized; contact us for details.",
    "Exact mount and thread details, material, net weight, and included adapter are being finalized; contact us for details.",
    "Exact case compatibility, material, base dimensions and non-slip pad, and net weight are being finalized; contact us for details.",
    "Exact cloth material, weave, size, and count are being finalized; contact us for details.",
    "Exact card count, size, material, and printed language list are being finalized; contact us for details.",
]

# ---- retire: old success / refill promise keys (source reworded) ----
DROP_OLD = [
    "Contact form: Thanks for reaching out. We've received your message and will reply by email.",
    "Thanks for reaching out. We've received your message and will reply by email.",
    "Challenge sign-up: You're in! Check your inbox for Day 1. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.",
    "You're in! Check your inbox for Day 1. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.",
    "You're in! Check your inbox for Day 1. Remember: your first shot starts here.",
    "when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit to keep every new clip sharp.",
    "Refill reminder: when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit to keep every new clip sharp.",
]

dropped = []
for k in DROP_SPECS + DROP_OLD:
    if k in z:
        del z[k]
        dropped.append(k)

ADD = {
    # success state (no reply-commitment)
    "Contact form: Thanks for reaching out. We read every message.": "联系表单：感谢留言，我们阅读每一条留言。",
    "Thanks for reaching out. We read every message.": "感谢留言，我们阅读每一条留言。",
    "Challenge sign-up: You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.": "挑战报名：你已加入。Day 1 见下方——开始拍摄吧。首单优惠码 NEWCREATOR10——Shop 集合全部单件 9 折；捆绑套装除外；不可与 STARTERKIT 叠加。",
    "You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.": "你已加入。Day 1 见下方——开始拍摄吧。首单优惠码 NEWCREATOR10——Shop 集合全部单件 9 折；捆绑套装除外；不可与 STARTERKIT 叠加。",
    "You're in. Day 1 is below — start shooting. Remember: your first shot starts here.": "你已加入。Day 1 见下方——开始拍摄吧。记住：你的第一个镜头，从这里开始。",
    "Refill reminder: when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots.": "补充提醒：清洁布或气吹用旧时，在拍摄间隙补充镜头清洁套装。",
    "when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots.": "清洁布或气吹用旧时，在拍摄间隙补充镜头清洁套装。",
    # collection filter chrome
    "Filter": "筛选",
    "Availability": "库存状态",
    "Price": "价格",
}

added = []
for k, v in ADD.items():
    if k not in z:
        z[k] = v
        added.append(k)

# plural pattern entry (engine pluralization, implemented separately)
d.setdefault("_meta", {}).setdefault("plural_patterns", {})
d["_meta"]["plural_patterns"]["{{count}} Products"] = "{{count}} 件装备"

p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("dropped:", len(dropped))
print("added:", len(added))
print("keys:", len(z))
