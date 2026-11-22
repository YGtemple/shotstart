# -*- coding: utf-8 -*-
import json, io, pathlib, re
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
audit = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_diff.json", encoding="utf-8"))
only = audit["only_source"]

CONTROL = {
 "Filter","Availability","Price","Sort by","Recommend","Recommended","Products",
 "In stock","Out of stock","Newest in","Pageviews, high to low","Price, high to low",
 "Price, low to high","Best selling","Checkout","Subtotal","Sign in","Register",
 "Quantity","Your cart is empty","Shop now","Recently viewed","1 sold",
 "ShotStart — Your first shot starts here."
}

P0, P1, P2 = [], [], []
for k, v in only.items():
    if k in CONTROL:
        P0.append((k,v,"A 功能控件")); continue
    if k.startswith(("Contact form:","Challenge sign-up:","Refill reminder:")):
        P2.append((k,v,"分段兜底前缀")); continue
    if ("still being finalized" in k or "pending final confirmation" in k
        or "under legal review" in k):
        P1.append((k,v,"PDP 定稿中规格句")); continue
    if re.search(r"\$(12\.99|11\.99|6\.99|8\.99|62\.96|53\.52|9\.44|38\.22|6\.75)", k):
        P0.append((k,v,"价格纠偏/套装正文")); continue
    P0.append((k,v,"承诺/成功态/正文"))

print("P0 必须上线:", len(P0))
for k,v,t in P0: print(f"  [{t}] {k[:60]} => {v[:40]}")
print("\nP1 可延后(规格待定):", len(P1))
for k,v,t in P1: print(f"  {k[:60]}")
print("\nP2 可延后(分段冗余):", len(P2))
for k,v,t in P2: print(f"  [{t}] {k[:60]}")
print("\n合计:", len(P0)+len(P1)+len(P2), "= 源有线上无", len(only))
print("线上残留旧键:", len(audit["only_live"]))

# block assignment heuristics
def block(k):
    if re.search(r"tripod|stand|cleaning kit|carry case|reflector|backdrop|extension pole|refill|mini ball|magnetic|microfiber|shot list cards|cloth", k, re.I): return "PDP 商品页"
    if re.search(r"starter kit|pro creator kit|creator starter kit|bundle contents|what's in the kit", k, re.I): return "捆绑入口/套装"
    if re.search(r"challenge|day [1-7]|you're in|signup|sign-up", k, re.I): return "挑战/报名回执"
    if re.search(r"contact|message|reach out|question", k, re.I): return "联系页/表单"
    if re.search(r"cart|checkout|subtotal|stock|quantity|shop now|recently", k, re.I): return "购物车/集合 chrome"
    if re.search(r"filter|sort|price|availability|recommend|best selling|products|gear", k, re.I): return "集合筛选/排序"
    return "其他/全局"

out = {"P0":[{"key":k,"zh":v,"type":t,"block":block(k)} for k,v,t in P0],
       "P1":[{"key":k,"zh":v,"type":t,"block":block(k)} for k,v,t in P1],
       "P2":[{"key":k,"zh":v,"type":t,"block":block(k)} for k,v,t in P2],
       "stale_live":[{"key":k,"zh":v} for k,v in audit["only_live"].items()]}
(ROOT/"shotstart-copy"/"tools"/"audit_classified.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
