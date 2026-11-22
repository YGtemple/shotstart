# -*- coding: utf-8 -*-
import json, io, pathlib, sys
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy")
sys.path.insert(0, str(ROOT / "tools"))
from shotstart_content import PAGES
from build_shotstart import publish_text

p = ROOT / "tools" / "i18n_zh.json"
d = json.load(io.open(p, encoding="utf-8"))
z = d["zh-CN"]

# zh aligned to source meaning; fallback clause uses the established neutral wording.
ZH = {
    "The clamp fits common smartphone sizes. The exact compatible width range is still being finalized; contact us for details.": "夹具适配常见智能手机尺寸。确切适配宽度范围正在定稿；详情请联系我们。",
    "Whether a carry bag is included is still being finalized; contact us for details. Check the What's in the Box section for the confirmed contents.": "是否包含收纳包正在定稿；详情请联系我们。已确认的箱单见“箱单”部分。",
    "It holds common smartphone sizes. The exact width range is still being finalized; contact us for details.": "可容纳常见智能手机尺寸。确切宽度范围正在定稿；详情请联系我们。",
    "The open design allows cable access. The cutout position is still being finalized; contact us for details.": "开放式设计可走线充电。开孔位置正在定稿；详情请联系我们。",
    "The base is designed for desk-level stability. Its net weight and material are still being finalized; contact us for details.": "底座按桌面稳定放置设计。净重与材质正在定稿；详情请联系我们。",
    "The kit is designed for lens surfaces; avoid pressing or rubbing hard. The approved surface list is still being finalized; contact us for details.": "本套装面向镜头表面使用；避免用力按压或擦拭。适用表面清单正在定稿；详情请联系我们。",
    "The set is a compact cleaning set; contents are listed in What's in the Box. Contents, cloth material, and fluid volume are still being finalized; contact us for details.": "本套装为紧凑清洁套装；构成见“箱单”。构成、布料材质与清洁液容量正在定稿；详情请联系我们。",
    "Whether cleaning liquid is included, along with its volume and ingredients, is still being finalized; contact us for details; check the contents list before ordering.": "是否含清洁液及其容量、成分正在定稿；详情请联系我们；下单前请核对构成清单。",
    "The case is built around common creator gear setups. Exact fitted dimensions are still being finalized; contact us for details.": "收纳包围绕常见创作者装备配置设计。确切适配尺寸正在定稿；详情请联系我们。",
    "Internal pockets and compartments are listed in What's in the Box. Any additional accessory is still being finalized; contact us for details.": "内部口袋与隔层见“箱单”。其他附带配件正在定稿；详情请联系我们。",
    "Water resistance and fabric coating are still being finalized; contact us for details.": "防水性与面料涂层正在定稿；详情请联系我们。",
    "Diameter and surface fabric are pending final confirmation.": "直径与表面面料待最终确认。",
    "A stand or mounting clip is not listed in the basic contents; any included accessory is still being finalized; contact us for details.": "基础构成不含支架或固定夹；是否附带配件正在定稿；详情请联系我们。",
    "Dimensions and fabric are still being finalized; contact us for details.": "尺寸与面料正在定稿；详情请联系我们。",
    "The cloth works with common stands or clamps. Any included mounting accessory is still being finalized; contact us for details.": "背景布可搭配常见支架或夹具。是否附带安装配件正在定稿；详情请联系我们。",
    "Extended and collapsed lengths are still being finalized; contact us for details.": "伸展与收拢长度正在定稿；详情请联系我们。",
    "The holder fits common smartphone sizes. The exact compatible width range is still being finalized; contact us for details.": "夹具适配常见智能手机尺寸。确切适配宽度范围正在定稿；详情请联系我们。",
    "Material and net weight are still being finalized; contact us for details.": "材质与净重正在定稿；详情请联系我们。",
    "The depicted refill includes a cleaning fluid bottle, a cloth, and a brush pen; exact count, cloth material, and fluid volume or ingredients are still being finalized; contact us for details.": "所示补充装含一瓶清洁液、一块布与一支笔刷；确切件数、布料材质及清洁液容量或成分正在定稿；详情请联系我们。",
    "The refill includes a cleaning fluid bottle; the fluid volume and ingredients are still being finalized; contact us for details; check the contents list before ordering.": "补充装含一瓶清洁液；清洁液容量与成分正在定稿；详情请联系我们；下单前请核对构成清单。",
    "The mount and thread details are still being finalized; contact us for details; check What's in the Box before ordering.": "安装与螺纹细节正在定稿；详情请联系我们；下单前请核对“箱单”。",
    "Material and net weight are still being finalized; contact us for details.": "材质与净重正在定稿；详情请联系我们。",
    "Case thickness and magnet compatibility are still being finalized; contact us for details.": "手机壳厚度与磁吸适配正在定稿；详情请联系我们。",
    "Base material and non-slip pad are still being finalized; contact us for details.": "底座材质与防滑垫正在定稿；详情请联系我们。",
    "Approved surfaces are still being finalized; contact us for details; check What's in the Box before use.": "适用表面正在定稿；详情请联系我们；使用前请核对“箱单”。",
    "The pack count and cloth size are still being finalized; contact us for details.": "片数与布面尺寸正在定稿；详情请联系我们。",
    "The set follows the four-shot sequence — hook, close-up, demonstration, closing line; card count and material are still being finalized; contact us for details.": "本套卡片按四镜顺序排列——钩子、特写、演示、收尾；卡片数量与材质正在定稿；详情请联系我们。",
    "The printed language list is under legal review; contact us with any questions; check What's in the Box before ordering.": "印刷语言清单正在法务复核；有疑问请联系我们；下单前请核对“箱单”。",
}

# render source FAQ answers to online (fallback) strings, match dict ZH
rendered = []
for fname, blocks in PAGES.items():
    if not fname.startswith("product-"):
        continue
    for blk in blocks:
        if blk[0] == "faq_a":
            rendered.append(publish_text(blk[1], fname))

missing_zh = [r for r in rendered if r not in ZH]
unmatched_rendered = [r for r in rendered if r not in z and r not in ZH]
print("rendered faq_a:", len(rendered))
print("ZH missing for rendered:", len(missing_zh))
for r in missing_zh:
    print("  NO ZH:", r)

added = []
for k, v in ZH.items():
    if k not in z:
        z[k] = v
        added.append(k)

p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("added faq keys:", len(added))
print("keys:", len(z))
