# -*- coding: utf-8 -*-
"""round11 集合筛选/排序面板 chrome 补键：仅入线上 DOM 实测项，不臆造选项。"""
import json, io, pathlib, sys

ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
DICT = ROOT / "tools" / "i18n_zh.json"

ADD = [
    ("Products", "件装备"),                        # 计数被拆成 "12" + "Products" 两叶节点
    ("In stock", "有货"),
    ("Out of stock", "缺货"),
    ("Newest in", "最新上架"),
    ("Pageviews, high to low", "浏览量从高到低"),
    ("Price, high to low", "价格从高到低"),
    ("Price, low to high", "价格从低到高"),
]

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

json.dump(d, io.open(DICT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("keys before:", before, "after:", len(z), "added:", len(z) - before)

# 模式条目仍在
pp = d["_meta"]["plural_patterns"]
assert "{{count}} Products" in pp, "count Products pattern missing"
assert "{{count}} sold" in pp, "count sold pattern missing"
print("patterns ok:", list(pp.keys()))
