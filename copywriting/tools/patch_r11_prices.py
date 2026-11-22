# -*- coding: utf-8 -*-
"""round11 三件单件价纠偏：源 12 处 + 字典 4 键 1:1 替换（键数不增）。
price 三句模板文字相同，按 1-based 行号定位，避免链式换价撞值。"""
import json, io, pathlib, sys

ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
SRC = ROOT / "tools" / "shotstart_content.py"
DICT = ROOT / "tools" / "i18n_zh.json"

# ---------- 1a. 商品名锚定的唯一串替换（bullet / 价格表行 / 中文自述） ----------
SRC_REPL = [
    # Magnetic Mount 9.99 -> 11.99
    ('"Magnetic Mount — $9.99. Snap your phone on and off for quick desk setups."',
     '"Magnetic Mount — $11.99. Snap your phone on and off for quick desk setups."'),
    ('["Magnetic Mount", "磁吸手机支架", "$9.99"]',
     '["Magnetic Mount", "磁吸手机支架", "$11.99"]'),
    ('磁吸手机支架，一键拆装，适合桌面演示与参考观看；手机壳与磁吸兼容性、底座材质为占位；仅作单件销售；演示价 $9.99。',
     '磁吸手机支架，一键拆装，适合桌面演示与参考观看；手机壳与磁吸兼容性、底座材质为占位；仅作单件销售；演示价 $11.99。'),
    # Microfiber 3-Pack 8.99 -> 6.99
    ('"Microfiber 3-Pack — $8.99. Three spare soft cloths for between-take lens and screen cleaning."',
     '"Microfiber 3-Pack — $6.99. Three spare soft cloths for between-take lens and screen cleaning."'),
    ('["Microfiber 3-Pack", "清洁布三片装", "$8.99"]',
     '["Microfiber 3-Pack", "清洁布三片装", "$6.99"]'),
    ('三片装超细纤维布，拍摄间隙擦拭手机镜头与屏幕；布材、尺寸与片数为占位；与镜头清洁套装搭配使用；仅作单件销售；演示价 $8.99。',
     '三片装超细纤维布，拍摄间隙擦拭手机镜头与屏幕；布材、尺寸与片数为占位；与镜头清洁套装搭配使用；仅作单件销售；演示价 $6.99。'),
    # Shot List Cards 6.99 -> 8.99
    ('"Shot List Cards — $6.99. Four-shot prompt cards paired with your ShotStarter script draft."',
     '"Shot List Cards — $8.99. Four-shot prompt cards paired with your ShotStarter script draft."'),
    ('["Shot List Cards", "分镜清单卡片（配套 AI 脚本草稿）", "$6.99"]',
     '["Shot List Cards", "分镜清单卡片（配套 AI 脚本草稿）", "$8.99"]'),
    ('配套 ShotStarter 脚本草稿的四镜提示卡（钩子 / 特写 / 演示 / 收尾）；卡片件数、材质与语种为占位；不替代创作者对 AI 草稿的自行审核；仅作单件销售；演示价 $6.99。',
     '配套 ShotStarter 脚本草稿的四镜提示卡（钩子 / 特写 / 演示 / 收尾）；卡片件数、材质与语种为占位；不替代创作者对 AI 草稿的自行审核；仅作单件销售；演示价 $8.99。'),
]

# ---------- 1b. price 行按行号（1-based）定位：(行号, 旧价, 新价) ----------
PRICE_ROWS = [
    (842, "$9.99", "$11.99"),  # magnetic-mount
    (900, "$8.99", "$6.99"),   # microfiber-3pack
    (959, "$6.99", "$8.99"),   # shot-list-cards
]

lines = io.open(SRC, encoding="utf-8").read().split("\n")

# 先做行级 price 替换
for ln, old_p, new_p in PRICE_ROWS:
    row = lines[ln - 1]
    if '("price", "Demo price:' not in row or old_p not in row:
        print(f"FAIL price row {ln}: {row[:80]}")
        sys.exit(1)
    lines[ln - 1] = row.replace(old_p, new_p)

text = "\n".join(lines)

for old, new in SRC_REPL:
    n = text.count(old)
    if n != 1:
        print(f"FAIL src count={n}: {old[:60]}")
        sys.exit(1)
    text = text.replace(old, new)
io.open(SRC, "w", encoding="utf-8").write(text)
print("src replaced: price rows", len(PRICE_ROWS), "+ anchor strings", len(SRC_REPL))

# ---------- 2. 字典 1:1 换价 ----------
DICT_REPL = [
    ("Mini Ball Head — $11.99. Level and lock the frame between shots with one twist.",
     "Mini Ball Head — $12.99. Level and lock the frame between shots with one twist.",
     "迷你云台 —— $11.99。一拧即可调平画面并在镜头间锁定。",
     "迷你云台 —— $12.99。一拧即可调平画面并在镜头间锁定。"),
    ("Magnetic Mount — $9.99. Snap your phone on and off for quick desk setups.",
     "Magnetic Mount — $11.99. Snap your phone on and off for quick desk setups.",
     "磁吸手机支架 —— $9.99。手机一吸即装、一取即下，快速完成桌面机位。",
     "磁吸手机支架 —— $11.99。手机一吸即装、一取即下，快速完成桌面机位。"),
    ("Microfiber 3-Pack — $8.99. Three spare soft cloths for between-take lens and screen cleaning.",
     "Microfiber 3-Pack — $6.99. Three spare soft cloths for between-take lens and screen cleaning.",
     "清洁布三片装 —— $8.99。三片备用软布，用于拍摄间隙擦拭镜头与屏幕。",
     "清洁布三片装 —— $6.99。三片备用软布，用于拍摄间隙擦拭镜头与屏幕。"),
    ("Shot List Cards — $6.99. Four-shot prompt cards paired with your ShotStarter script draft.",
     "Shot List Cards — $8.99. Four-shot prompt cards paired with your ShotStarter script draft.",
     "分镜清单卡片 —— $6.99。与你的 ShotStarter 脚本草稿配套的四镜提示卡片。",
     "分镜清单卡片 —— $8.99。与你的 ShotStarter 脚本草稿配套的四镜提示卡片。"),
]

d = json.load(io.open(DICT, encoding="utf-8"))
z = d["zh-CN"]
before = len(z)
for old_key, new_key, old_zh, new_zh in DICT_REPL:
    if old_key not in z:
        print(f"FAIL dict missing old key: {old_key[:60]}")
        sys.exit(1)
    if z[old_key] != old_zh:
        print(f"FAIL zh mismatch: {old_key[:50]}\n  got={z[old_key]}")
        sys.exit(1)
    items = list(z.items())
    for i, (k, _) in enumerate(items):
        if k == old_key:
            items[i] = (new_key, new_zh)
            break
    d["zh-CN"] = dict(items)
    z = d["zh-CN"]

after = len(z)
print("dict keys before:", before, "after:", after)
if before != after:
    print("FAIL key count drift")
    sys.exit(1)

json.dump(d, io.open(DICT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("dict written")

# ---------- 3. 残留复查 ----------
t2 = io.open(SRC, encoding="utf-8").read()
for bad in ["Magnetic Mount — $9.99", "Microfiber 3-Pack — $8.99", "Shot List Cards — $6.99",
            "Mini Ball Head — $11.99"]:
    assert bad not in t2, bad
d2 = json.load(io.open(DICT, encoding="utf-8"))
for bad in ["$11.99", "$9.99. Snap", "$8.99. Three spare", "$6.99. Four-shot"]:
    hits = [k for k in d2["zh-CN"] if bad in k]
    assert not hits, (bad, hits)
print("residual check ok; final keys:", len(d2["zh-CN"]))
