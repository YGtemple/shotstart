# -*- coding: utf-8 -*-
"""round11 线上实测缺键补批：仅入清单 confirmed 项，不扩未列变体。"""
import json, io, pathlib, sys

ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
DICT = ROOT / "tools" / "i18n_zh.json"

ADD = [
    ("Recommended", "推荐"),
    ("Best selling", "最畅销"),
    ("Checkout", "去结账"),
    ("Subtotal", "小计"),
    ("Sign in", "登录"),
    ("Register", "注册"),
]
# 既有键译文按线上清单口径校准
ZH_FIX = {
    "Sort by": "排序",
}

d = json.load(io.open(DICT, encoding="utf-8"))
z = d["zh-CN"]
before = len(z)

for k, v in ADD:
    if k in z:
        if z[k] != v:
            print(f"VALUE MISMATCH existing {k}: {z[k]} -> {v}")
            sys.exit(1)
        print(f"already present: {k}")
        continue
    if not v.strip():
        print(f"EMPTY value for {k}")
        sys.exit(1)
    z[k] = v
    print(f"added: {k} -> {v}")

for k, v in ZH_FIX.items():
    if k not in z:
        print(f"FIX target missing: {k}")
        sys.exit(1)
    print(f"zh fix: {k} | {z[k]} -> {v}")
    z[k] = v

json.dump(d, io.open(DICT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("keys before:", before, "after:", len(z), "added:", len(z) - before)

pp = d["_meta"]["plural_patterns"]
assert "{{count}} Products" in pp, "count Products pattern missing"
assert "{{count}} sold" in pp, "count sold pattern missing"
print("patterns ok:", list(pp.keys()))
