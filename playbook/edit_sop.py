# -*- coding: utf-8 -*-
"""SOP docx 同步终版口径。断言通过后原地写回。"""
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

BASE = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
TARGET = os.path.join(BASE, "运营配置与测试下单SOP.docx")
doc = Document(TARGET)

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

def set_para_text(p, text, expect_old=None):
    if expect_old is not None:
        assert expect_old in p.text, f"锚点未命中: {expect_old!r} in {p.text!r}"
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)

def repl_para(p, old, new):
    assert old in p.text, f"未命中 {old!r} in {p.text!r}"
    set_para_text(p, p.text.replace(old, new))

blocks = list(iter_block_items(doc))

# 逐段/单元格按锚点处理
for block in blocks:
    if isinstance(block, Paragraph):
        t = block.text
        if "仅八件单件" in t:
            repl_para(block, "仅八件单件", "仅十二件单品")
        elif t.startswith("4. 适用范围：八件单件商品"):
            repl_para(block, "八件单件商品", "十二件单品商品")
        elif t.startswith("落地形式（与指令包 5.7 一致）"):
            repl_para(block, "该码不在八件单件上生效", "该码不在十二件单品上生效")
        elif t.startswith("Pro Creator Kit 捆绑核算"):
            set_para_text(block, "Pro Creator Kit 捆绑核算：$19.99 + $16.99 + $12.99 + $12.99 = $62.96；$62.96 × (1 − 15%) = $53.516，取 $53.52；较单品合计省 $9.44。", "$16.99")
        elif t.startswith("捆绑商品页：Starter"):
            set_para_text(block, "捆绑商品页：Starter 三件清单 $44.97 / $38.22、Pro 四件清单 $62.96 / $53.52 对照与 \"Use code STARTERKIT at checkout\" 前台可见；捆绑为独立 SPU，不依赖免费捆绑构建器；STARTERKIT 仅作用于捆绑 SPU。", "$58.96")
        elif t.startswith("新品凑单门槛用例"):
            set_para_text(block, "新品凑单门槛用例（折后基数默认、实机待验）：Folding Reflector $10.99 + Backdrop Cloth $13.99 + Extension Pole $16.99 = $41.97，达到免邮档；Lens Cleaning Refill $7.99 单件为付费档。", "$12.99")
    else:
        for row in block.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    t = p.text
                    if t.startswith("Shop 集合内全部八件单件"):
                        set_para_text(p, "Shop 集合内全部十二件单品商品（演示）；两张捆绑独立 SPU 不适用 NEWCREATOR10", "八件")
                    elif "不在八件单件上生效" in t and "Starter" in t:
                        repl_para(p, "不在八件单件上生效", "不在十二件单品上生效")
                    elif t.startswith("独立捆绑 SPU：标题 \"Pro Creator Kit"):
                        set_para_text(p, "独立捆绑 SPU：标题 \"Pro Creator Kit - Tripod, Extension Pole, Mini Ball Head Mount, Carry Case\"；标价 $62.96（$19.99 + $16.99 + $12.99 + $12.99）；STARTERKIT（15% off）仅作用于该捆绑 SPU，用码后 $53.52；不在十二件单品上生效；每单仅一码，不与 NEWCREATOR10 叠加；商品页逐项列四件单品及单价、$62.96 / $53.52 对照与 \"Use code STARTERKIT at checkout\"；图库用四件主图（Mini Ball Head Mount 主图待补占位），描述内链回四件单品；日期、库存与资格占位待确认。", "$58.96")
                    elif t.startswith("捆绑页四件清单"):
                        set_para_text(p, "捆绑页四件清单与 $62.96 / $53.52 对照可见；STARTERKIT 仅在捆绑 SPU 生效；两码不叠加。", "$58.96")

doc.save(TARGET)
print("SAVED", TARGET)
