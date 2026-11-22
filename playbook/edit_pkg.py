# -*- coding: utf-8 -*-
"""指令包 docx 同步终版商品口径（12 单品 + 2 套装）。断言通过后原地写回。"""
import os, copy, sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

BASE = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
TARGET = os.path.join(BASE, "Athena建店指令包.docx")

doc = Document(TARGET)

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

blocks = list(iter_block_items(doc))
log = []

def set_para_text(p, text, expect_old=None):
    if expect_old is not None:
        assert expect_old in p.text, f"锚点未命中: {expect_old!r} in {p.text!r}"
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)
    log.append(f"P: {text[:60]}")

def set_cell_text(cell, text):
    paras = cell.paragraphs
    set_para_text(paras[0], text)
    for p in paras[1:]:
        p._element.getparent().remove(p._element)

def find_table(idx):
    t = blocks[idx]
    assert isinstance(t, Table), f"block {idx} 不是表"
    return t

# ---------- T18 商品基线表 ----------
t18 = find_table(18)
set_cell_text(t18.rows[4].cells[2], "$12.99")
set_cell_text(t18.rows[5].cells[2], "$10.99")
set_cell_text(t18.rows[6].cells[2], "$13.99")
set_cell_text(t18.rows[7].cells[2], "$16.99")

new_rows = [
    ["9", "Mini Ball Head Mount（自拟工作名，待文案包回填）", "$12.99", "[待确认: 主图]", "[待回填]"],
    ["10", "Magnetic Phone Mount（自拟工作名，待文案包回填）", "$11.99", "[待确认: 主图]", "[待回填]"],
    ["11", "Microfiber Cloth 3-Pack（自拟工作名，待文案包回填）", "$6.99", "[待确认: 主图]", "[待回填]"],
    ["12", "Shot List Cards（自拟工作名，待文案包回填）", "$8.99", "[待确认: 主图]", "[待回填]"],
    ["13", "Creator Starter Kit（套装）", "$44.97 → $38.22（STARTERKIT 15%）", "—", "marketing.txt"],
    ["14", "Pro Creator Kit（套装）", "$62.96 → $53.52（STARTERKIT 15%）", "—", "marketing.txt"],
]
src_tr = t18.rows[8]._tr
for vals in new_rows:
    new_tr = copy.deepcopy(src_tr)
    src_tr.addnext(new_tr)
    src_tr = new_tr  # 保持顺序：逐行紧贴前一行后
# 重新取行写值
for ri, vals in enumerate(new_rows, start=9):
    row = t18.rows[ri]
    for ci, v in enumerate(vals):
        set_cell_text(row.cells[ci], v)
log.append(f"T18 rows -> {len(t18.rows)}")

# ---------- T32 指令 0 ----------
t32 = find_table(32)
c32 = t32.rows[0].cells[0].paragraphs
set_para_text(c32[9], "Twelve individual products (demo prices, confirm before launch):", "Eight")
set_para_text(c32[13], "4. Creator Carry Case - $12.99 - a portable case to keep gear and small accessories together.", "$16.99")
set_para_text(c32[14], "5. Folding Reflector - $10.99 - soften and fill light for face and product clips.", "$12.99")
set_para_text(c32[15], "6. Backdrop Cloth - $13.99 - a plain background for product and talking-head clips.", "$14.99")
set_para_text(c32[16], "7. Extension Pole - $16.99 - reach overhead and higher-angle shots for selfie and group clips.", "$13.99")
# 在 P17 后插入 4 条新品
src_p = c32[17]._p
extra = [
    "9. Mini Ball Head Mount - $12.99 - swivel head for angled phone shots (working title, copy pending).",
    "10. Magnetic Phone Mount - $11.99 - quick magnetic phone attachment for setups (working title, copy pending).",
    "11. Microfiber Cloth 3-Pack - $6.99 - spare cloths for lens and gear cleaning (working title, copy pending).",
    "12. Shot List Cards - $8.99 - shot-planning cards for beginner creators (working title, copy pending).",
]
prev = src_p
for txt in extra:
    new_p = copy.deepcopy(src_p)
    prev.addnext(new_p)
    prev = new_p
# 写入新段（新段落对象需重新取）
paras_now = t32.rows[0].cells[0].paragraphs
for offset, txt in enumerate(extra, start=18):
    set_para_text(paras_now[offset], txt)
set_para_text(paras_now[24], "- Home: hero with the tagline, product cards for all twelve items, brand value pillars, a section introducing the ShotStarter AI content assistant, a 7-Day Challenge signup block, and an email popup.", "all eight")
set_para_text(paras_now[25], "- Shop: listing of the twelve individual products, then the two bundle cards.", "eight")

# ---------- 段落数量词/口径 ----------
def P(idx):
    return blocks[idx]

set_para_text(P(34), "中文用途说明：一次性把品牌、口号、配色、人群、十二件单品与价格、页面清单、导航和合规边界交代给 Athena，作为整套店铺的生成基线。", "八件")
set_para_text(P(39), "十二件单品名称与价格 $19.99 / $14.99 / $9.99 / $12.99 / $10.99 / $13.99 / $16.99 / $7.99 / $12.99 / $11.99 / $6.99 / $8.99 一致；", "八件")
set_para_text(P(59), "素材映射：商品文案以 product-tripod.txt / product-stand.txt / product-cleaning-kit.txt / 其余九件 product-*.txt 为准（见第 6 节对照表）；主图 product-*.png。", "五件新品")

# ---------- T63 首页指令：顺序重排 + 文本 ----------
t63 = find_table(63)
cell63 = t63.rows[0].cells[0]
p63 = cell63.paragraphs
# 文本改写（先按原索引）
set_para_text(p63[8], "2. Trust signal row: a plain-text line reading \"Free standard shipping on US orders over $35.\" with links to the Shipping, Return & Refund, Privacy, and Terms policy pages; include the note that AI outputs are drafts creators review before posting.", "7. Trust")
set_para_text(p63[2], "3. Three scenario doorway cards: split beginner creators and small shop owners by use case; made for beginners; gear that works with your phone; AI that stays on your side.", "Three brand")
set_para_text(p63[4], "4. Creator Starter Kit banner card: above the individual product grid, show the three Starter Kit main images together, the list price $44.97 side by side with the after-code price $38.22 (no compare-at strike-through price field), the line \"Use code STARTERKIT at checkout\", and CTA \"View the kit\". If the free theme has no bundle card block, use an image + plain-text card with the same prices.", "4. Creator Starter")
set_para_text(p63[3], "5. Product grid cards for the twelve individual products with their approved prices, laid out in a 4-column grid across three rows.", "eight")
set_para_text(p63[5], "6. Pro Creator Kit bundle card: below the product grid, show the four Pro kit images together, the list price $62.96 side by side with the after-code price $53.52 (no compare-at strike-through price field), the line \"Use code STARTERKIT at checkout\", and CTA \"View the kit\". If the free theme has no bundle card block, use an image + plain-text card with the same prices.", "$58.96")
set_para_text(p63[6], "7. ShotStarter AI block: section title \"Meet ShotStarter, your AI content assistant.\"; describe the 15-second script draft, four-shot storyboard, and ready-to-review caption. Outputs are drafts creators review before posting.", "5. ShotStarter")
set_para_text(p63[7], "8. 7-Day Challenge block with email signup CTA \"Join the challenge\".", "6. 7-Day")
# 物理重排：Hero(0,1) → Trust(8) → Pillars(2) → Starter(4) → Grid(3) → Pro(5) → AI(6) → Challenge(7) → Popup(9) → palette(10)
order = [p63[1]._p, p63[8]._p, p63[2]._p, p63[4]._p, p63[3]._p, p63[5]._p, p63[6]._p, p63[7]._p, p63[9]._p, p63[10]._p]
holder = cell63._element
for el in holder.findall(qn('w:p')):
    holder.remove(el)
for el in order:
    holder.append(el)

set_para_text(P(66), "预期结果：首页区块齐全（Hero、信任行、场景门三列、Starter 横幅卡、商品网格、Pro 卡、ShotStarter、Challenge、弹窗），两个 CTA 分别指向 Shop 与 7-Day Challenge 页。", "三支柱")
set_para_text(P(70), "两张捆绑卡：Starter 三主图拼合、清单价 $44.97 与码后价 $38.22 同屏对照；Pro Creator Kit 四件清单、$62.96 与码后价 $53.52 同屏对照（均不用 compare-at 划线字段）、\"Use code STARTERKIT at checkout\" 与 CTA 可见；无原生卡片块时图文纯文本卡同等呈现；", "$58.96")

# ---------- T80 Shop 集合 ----------
t80 = find_table(80)
set_para_text(t80.rows[0].cells[0].paragraphs[1],
    "- Shop collection: list the twelve individual products first, then the Creator Starter Kit and Pro Creator Kit bundle cards. Each card shows the approved price and a one-line use-case summary from shop.txt; collections: \"All Gear\" holds the twelve individual products, with use-case collections \"Stability & Height\", \"Desk & Angle\", \"Clean & Care\", \"Carry & Set Up\"; the two bundles sit under the hidden \"Creator Kits\" collection if the theme supports collections, otherwise keep one single grid.",
    "eight")
set_para_text(P(87), "Shop 卡片短文案、十二件单品先于两张捆绑卡的排序符合 shop.txt；", "八件")

# ---------- T136 促销 ----------
t136 = find_table(136)
c136 = t136.rows[0].cells[0].paragraphs
set_para_text(c136[2], "   - 10% off the customer's first order; applies to all twelve individual products in the Shop collection; both bundle SPUs are excluded.", "eight")
set_para_text(c136[13], "   - Title: \"Pro Creator Kit - Tripod, Extension Pole, Mini Ball Head Mount, Carry Case\"", "Carry Case, Reflector")
set_para_text(c136[14], "   - List price on the bundle SPU: $62.96 ($19.99 + $16.99 + $12.99 + $12.99).", "$58.96")
set_para_text(c136[15], "   - What's in the kit: Adjustable Phone Tripod $19.99; Extension Pole $16.99; Mini Ball Head Mount $12.99; Creator Carry Case $12.99.", "$16.99")
set_para_text(c136[16], "   - Code STARTERKIT (15% off) applies to this bundle SPU only; at checkout the bundle becomes $53.52. The bundle page and its cards read \"Use code STARTERKIT at checkout\".", "$50.12")
set_para_text(P(142), "STARTERKIT 仅作用于两张捆绑独立 SPU：Starter Kit $44.97 → $38.22、Pro Creator Kit $62.96 → $53.52；不在十二件单品上生效；", "$58.96")

# ---------- T150 复查 ----------
t150 = find_table(150)
c150 = t150.rows[0].cells[0].paragraphs
set_para_text(c150[2], "- All twelve individual products and the two bundle products open, show the approved price and main image, and can be added to cart.", "eight")
set_para_text(c150[5], "- Both bundle product pages list their kit items and the price comparison: Starter $44.97 vs $38.22, Pro $62.96 vs $53.52, with \"Use code STARTERKIT at checkout\".", "$58.96")
set_para_text(P(155), "九个页面链接有效；十二件单品 + 两张捆绑 SPU 可加购；结账页有优惠码入口；", "八件")
set_para_text(P(156), "两张捆绑页各自清单、$44.97 / $38.22 与 $62.96 / $53.52 对照与 \"Use code STARTERKIT at checkout\" 前台可见；购物车凑单行按 cart-checkout.txt 口径；", "$58.96")

# ---------- P1 项 ----------
set_para_text(P(169), "预期结果：十二件商详各有一条指向捆绑商品的文本链接。", "八件")
set_para_text(P(178), "预期结果：十二件商详链到 Challenge，Challenge 页回链 Shop。", "八件")
t184 = find_table(184)
set_para_text(t184.rows[0].cells[0].paragraphs[0],
    "On the Shop collection page, group the twelve products under use-case collections: \"Stability & Height\" (tripod, extension pole, mini ball head), \"Desk & Angle\" (stand, magnetic mount, mini ball head), \"Clean & Care\" (cleaning kit, microfiber cloths, refill), \"Carry & Set Up\" (carry case, reflector, backdrop); the shot-list cards remain an All Gear hook item. A single product grid may stay unchanged if grouping blocks are not available in the free theme.",
    "eight")
set_para_text(P(186), "中文用途：集合页按 Stability & Height / Desk & Angle / Clean & Care / Carry & Set Up 四类用途集合分组，Shot List Cards 作为 All Gear Hook 单品。", "五类")
set_para_text(P(187), "预期结果：十二件商品归入对应集合；主题不支持分组区块时保留单一网格。", "八件")
set_para_text(P(189), "12 件单件，分组非必需。", "8 件")
t193 = find_table(193)
set_para_text(t193.rows[0].cells[0].paragraphs[0],
    "Add a second image to each of the twelve product cards or product galleries: the approved lifestyle scene image for that product. Keep the main product image first; the second image shows the product in a beginner creator's real setup. Preserve product color, shape, and details; no text, watermark, or fake logos.",
    "eight")
set_para_text(P(196), "预期结果：十二件商品各有两张图；主题卡片/商详多图轮播自动展示。", "八件")

# ---------- 5.10 扩品段 ----------
set_para_text(P(236), "5.10  扩品 SPU 创建：四件新增单品与 Pro Creator Kit 捆绑", "五件新品")
t238 = find_table(238)
c238 = t238.rows[0].cells[0].paragraphs
set_para_text(c238[0], "Create the four new individual products and the Pro Creator Kit bundle SPU in ShotStart. Match each product to the copy I provide; do not change the approved prices. The carry-case, reflector, backdrop, extension-pole, and refill products follow the prices in the 2.2 baseline table.", "five new")
set_para_text(c238[2], "1. Mini Ball Head Mount, $12.99: working title \"Mini Ball Head Mount\"; final title pending the copy pack. Main image: placeholder pending [待确认: 主图].", "Creator Carry Case")
set_para_text(c238[3], "2. Magnetic Phone Mount, $11.99: working title \"Magnetic Phone Mount\"; final title pending the copy pack. Main image: placeholder pending [待确认: 主图].", "Folding Reflector")
set_para_text(c238[4], "3. Microfiber Cloth 3-Pack, $6.99: working title \"Microfiber Cloth 3-Pack\"; final title pending the copy pack. Main image: placeholder pending [待确认: 主图].", "Backdrop Cloth")
set_para_text(c238[5], "4. Shot List Cards, $8.99: working title \"Shot List Cards\"; final title pending the copy pack. Main image: placeholder pending [待确认: 主图].", "Extension Pole")
# 删除旧 refill 段 P6
c238[6]._p.getparent().remove(c238[6]._p)
# 重新取段落
c238 = t238.rows[0].cells[0].paragraphs
# 旧 P7(description) -> 新索引 6；旧 P8 Pro 标题 -> 7；P9 ->8；P10->9；P11->10；P12->11；P13->12；P14->13
set_para_text(c238[8], "- Title: \"Pro Creator Kit - Tripod, Extension Pole, Mini Ball Head Mount, Carry Case\"", "Carry Case, Reflector")
set_para_text(c238[9], "- List price: $62.96 ($19.99 + $16.99 + $12.99 + $12.99).", "$58.96")
set_para_text(c238[10], "- What's in the kit: Adjustable Phone Tripod $19.99; Extension Pole $16.99; Mini Ball Head Mount $12.99; Creator Carry Case $12.99.", "$16.99")
set_para_text(c238[11], "- STARTERKIT (15% off) applies to this bundle SPU only; code price $53.52; the bundle page reads \"Use code STARTERKIT at checkout\".", "$50.12")
set_para_text(P(239), "中文用途说明：把四件新增单品与 Pro Creator Kit 捆绑 SPU 录入店内，标题、价格、主图与文案包对齐；新品缺图位保留占位，不补猜素材。", "五件新品")
set_para_text(P(240), "预期结果：四件新增单品预览卡与 Pro 捆绑卡列出标题、价格、主图（缺图占位）、清单与描述；人工核对后逐张应用。", "五件新品")
set_para_text(P(242), "四件新增单品标题与价格 $12.99 / $11.99 / $6.99 / $8.99 与 shop.txt、对应 product-*.txt 一致；", "五件新品")
set_para_text(P(243), "四件新增单品主图未备齐，占位 [待确认: 主图]，不得用无关图顶替；", "Extension Pole")
set_para_text(P(244), "Pro Creator Kit 四件清单、$62.96 / $53.52 对照与 \"Use code STARTERKIT at checkout\" 可见；", "$58.96")
set_para_text(P(247), "素材映射：product-mini-ball-head.txt / product-magnetic-mount.txt / product-microfiber-3pack.txt / product-shot-list-cards.txt（待回填）；shop.txt、marketing.txt、home.txt 捆绑卡口径。", "product-carry-case")
set_para_text(P(248), "预估耗时：22 分钟（P0：四件新增单品连同其余转正单品录入 + Pro 捆绑 SPU；映射表 #30、#31）。", "五件新品")

# ---------- T265 对照表 ----------
t265 = find_table(265)
# R9 后插 4 行
src9 = t265.rows[9]._tr
new_map_rows = [
    ["Mini Ball Head Mount 商详", "product-mini-ball-head.txt（待回填）", "[待确认: 主图]", "同上；标题待文案包回填"],
    ["Magnetic Phone Mount 商详", "product-magnetic-mount.txt（待回填）", "[待确认: 主图]", "同上；标题待文案包回填"],
    ["Microfiber Cloth 3-Pack 商详", "product-microfiber-3pack.txt（待回填）", "[待确认: 主图]", "同上；标题待文案包回填"],
    ["Shot List Cards 商详", "product-shot-list-cards.txt（待回填）", "[待确认: 主图]", "同上；标题待文案包回填"],
]
prev = src9
for vals in new_map_rows:
    new_tr = copy.deepcopy(src9)
    prev.addnext(new_tr)
    prev = new_tr
for ri, vals in enumerate(new_map_rows, start=10):
    row = t265.rows[ri]
    for ci, v in enumerate(vals):
        set_cell_text(row.cells[ci], v)
# 原 R19/R20 因插 4 行顺延为 R23/R24
set_cell_text(t265.rows[23].cells[3], "集合名 \"All Gear\"；十二件单品先于两张捆绑卡；用途集合 Stability & Height / Desk & Angle / Clean & Care / Carry & Set Up；Creator Kits 隐藏；卡片一句话短文案；Bundle Display Slot 文案")
set_cell_text(t265.rows[24].cells[3], "四件清单（tripod、extension-pole、mini-ball-head、carry-case）、$62.96 / $53.52 对照、\"View the kit\"；STARTERKIT 仅作用该捆绑 SPU")

# ---------- T271 Runbook ----------
t271 = find_table(271)
set_cell_text(t271.rows[4].cells[1], "指令 1b：其余九件单品 + Pro Creator Kit 捆绑录入")
set_cell_text(t271.rows[4].cells[3], "22 分钟")
set_cell_text(t271.rows[4].cells[5], "九件单品价格、标题、主图（缺图占位）正确；Pro 捆绑四件清单、$62.96 → $53.52 可见")
set_cell_text(t271.rows[17].cells[5], "十二件单品 + 两张捆绑页链接、加购、凑单行、移动端、前台文案无问题")
set_para_text(P(269), P(269).text.replace("八件单件", "十二件单品"), "八件")
set_para_text(P(270), P(270).text.replace("八件单件", "十二件单品"), "八件")
set_para_text(P(272), "Round 1 建议完成步骤 1–7 与 3a；Round 2 完成步骤 8–18。按总表复算：步骤 1–7 与 3a（R1）计 87 分钟，步骤 8–18（R2）计 75 分钟，合计 162 分钟；分层：设计配置 1–11 与 3a 计 124 分钟，测试单 12–15 计 13 分钟，复查留证 16–18 计 25 分钟；另留缓冲 10 分钟（门禁排队 5 + 故障恢复 5）。旧口径“P0 设计段约 70 分钟”为步骤 3–9 粗估，已被本总表分层取代，现场以总表步骤估时为准。", "152")

# ---------- T316R6 附录 ----------
t316 = find_table(316)
set_cell_text(t316.rows[6].cells[2], "12 件单件，无需筛选；侧栏筛选无免费必要")

# ---------- PDP 互补口径：P57 后插一段 ----------
p57 = P(57)
pdp_text = ("PDP 互补推荐：tripod → extension-pole / mini-ball-head / carry-case；desktop-stand → magnetic-mount / mini-ball-head；"
            "cleaning-kit → microfiber-3pack / cleaning-refill；carry-case → tripod / extension-pole；shot-list-cards → tripod / creator-starter-kit；"
            "其余互补位（extension-pole → tripod / mini-ball-head；mini-ball-head → tripod / desktop-stand；magnetic-mount → desktop-stand / mini-ball-head；"
            "reflector → backdrop / carry-case；backdrop → reflector / carry-case；microfiber-3pack → cleaning-kit / cleaning-refill；"
            "cleaning-refill → cleaning-kit / microfiber-3pack）为自拟口径，建品后随 PDP 回填。")
new_pdp = copy.deepcopy(p57._p)
p57._p.addnext(new_pdp)
# 写新段
from docx.text.paragraph import Paragraph as _P
np = _P(new_pdp, p57._parent)
set_para_text(np, pdp_text)

# ---------- 全局兜底数量词替换（逐 run） ----------
fallback = [
    ("八件单件", "十二件单品"),
    ("八件单品", "十二件单品"),
    ("八件商品", "十二件商品"),
    ("八件商详", "十二件商详"),
]
def replace_in_para(p, pairs):
    for r in p.runs:
        for a, b in pairs:
            if a in r.text:
                r.text = r.text.replace(a, b)

for block in blocks:
    if isinstance(block, Paragraph):
        replace_in_para(block, fallback)
    else:
        for row in block.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    replace_in_para(p, fallback)

doc.save(TARGET)
print("SAVED", TARGET)
print(f"edits logged: {len(log)}")
for l in log[:8]:
    print(" -", l)
