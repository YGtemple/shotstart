# -*- coding: utf-8 -*-
import re, os, io

WD = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\_arch_work\playbook"
files = {
    "pkg": "verify_pkg.txt",
    "sop": "verify_sop.txt",
    "chk": "verify_chk.txt",
    "jud": "verify_jud.txt",
}
# 明确旧口径关键词（数量 / 旧套装价 / 旧工时）
hard = [
    "八件单件", "八件单品", "八件商品", "八件商详", "八件",
    "五件新品", "five new", "all eight", "eight individual", "eight product",
    "$58.96", "$50.12", "$8.84", "$50.116", "58.96", "50.12", "8.84",
]
# 旧价上下文词（数字本身合法保留，需人工判读语境）
price_ctx = ["13.99", "14.99", "16.99", "12.99"]

for tag, fn in files.items():
    path = os.path.join(WD, fn)
    text = io.open(path, encoding="utf-8").read()
    lines = text.splitlines()
    print(f"===== {tag} ({fn}) =====")
    hit_any = False
    for kw in hard:
        for i, ln in enumerate(lines, 1):
            if kw.lower() in ln.lower():
                print(f"  [HARD][{kw}] L{i}: {ln}")
                hit_any = True
    if not hit_any:
        print("  hard keywords: 0 hits")
    # 旧价语境：13.99 旧 pole 价（新口径 pole=16.99）；14.99 旧 backdrop（新 backdrop=13.99）
    for i, ln in enumerate(lines, 1):
        if "13.99" in ln and "pole" not in ln.lower() and "extension" not in ln.lower():
            # 13.99 合法=backdrop；若上下文是 pole/extension 则异常
            pass
    print()
