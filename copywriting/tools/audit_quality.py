# -*- coding: utf-8 -*-
"""Read-only quality scan: live 693 values vs source 729."""
import json, io, pathlib, re

ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
audit = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_diff.json", encoding="utf-8"))
live = audit["live"]
src = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"i18n_zh.json", encoding="utf-8"))["zh-CN"]

# 1) same key but value differs (live stale wording still served)
print("=== SAME KEY, LIVE VALUE DIFFERS FROM SOURCE ===")
diff = []
for k in live:
    if k in src and live[k] != src[k]:
        diff.append((k, live[k], src[k]))
        print(f"KEY: {k}\n  live : {live[k]}\n  src  : {src[k]}\n")
print("count:", len(diff))

# 2) tone / machine-translation risk words in live values
risk = ["亲", "宝贝", "购买", "下单", "包邮", "客户", "亲们", "店铺", "超值", "抢购", "限时", "赶紧", "快去"]
print("\n=== RISK TONE WORDS IN LIVE ===")
for w in risk:
    hits = [(k,v) for k,v in live.items() if w in v]
    if hits:
        print(f"[{w}]")
        for k,v in hits:
            print(f"  {k!r} => {v}")

# 3) terminology drift in live values
terms = {"个人数据": ["个人信息", "私人数据"], "可直接发布": ["可发布", "直接发布"], "小商家": ["小店主", "小店铺"]}
print("\n=== TERMINOLOGY DRIFT (LIVE) ===")
for canon, wrongs in terms.items():
    for w in wrongs:
        for k,v in live.items():
            if w in v:
                print(f"  {w!r} instead of {canon}: {k!r} => {v}")

# save diff list
(ROOT/"shotstart-copy"/"tools"/"audit_diff_values.json").write_text(
    json.dumps([{"key":k,"live":l,"src":s} for k,l,s in diff], ensure_ascii=False, indent=2), encoding="utf-8")
