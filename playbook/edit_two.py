# -*- coding: utf-8 -*-
"""现场执行清单 + 评委速览卡 同步终版口径。断言通过后原地写回。"""
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

def replace_para(p, old, new):
    full = p.text
    assert old in full, f"未命中 {old!r} in {full!r}"
    new_text = full.replace(old, new)
    if p.runs:
        p.runs[0].text = new_text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(new_text)

def set_cell(cell, text):
    paras = cell.paragraphs
    p = paras[0]
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)
    for extra in paras[1:]:
        extra._element.getparent().remove(extra._element)

# ============ 现场执行清单 ============
chk = os.path.join(ROOT, "现场执行清单.docx")
doc = Document(chk)
blocks = list(iter_block_items(doc))
for b in blocks:
    if isinstance(b, Paragraph):
        if "合计 110 分钟" in b.text:
            replace_para(b, "合计 110 分钟", "合计 115 分钟")
        elif "Pro $58.96→$50.12" in b.text:
            replace_para(b, "Pro $58.96→$50.12", "Pro $62.96→$53.52")
    else:
        for row in b.rows:
            cells = row.cells
            for c in cells:
                for p in c.paragraphs:
                    t = p.text
                    if "八件单件 + 两捆绑" in t:
                        replace_para(p, "八件单件 + 两捆绑", "十二件单品 + 两捆绑")
                    elif t.startswith("录入八件单件"):
                        replace_para(p, "录入八件单件", "录入十二件单品")
                    elif "Pro $58.96→$50.12" in t:
                        replace_para(p, "Pro $58.96→$50.12（省 $8.84）", "Pro $62.96→$53.52（省 $9.44）")
                    elif "八件单件，两捆绑排除" in t:
                        replace_para(p, "八件单件", "十二件单品")
                    elif "8 单件 + 2 捆绑" in t:
                        replace_para(p, "8 单件 + 2 捆绑", "12 单件 + 2 捆绑")
# R3 分钟 12→17（表 T3 第 3 行，分钟列）
t3 = blocks[3]
set_cell(t3.rows[3].cells[2], "17")
doc.save(chk)
print("SAVED", chk)

# ============ 评委速览卡 ============
jud = os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx")
doc2 = Document(jud)
blocks2 = list(iter_block_items(doc2))
# T4 价格表：blocks2[4]
t4 = blocks2[4]
set_cell(t4.rows[7].cells[2], "$16.99")
set_cell(t4.rows[9].cells[0], "Mini Ball Head Mount")
set_cell(t4.rows[9].cells[2], "$12.99")
set_cell(t4.rows[10].cells[0], "Magnetic Phone Mount")
set_cell(t4.rows[10].cells[2], "$11.99")
set_cell(t4.rows[11].cells[0], "Microfiber Cloth 3-Pack")
set_cell(t4.rows[11].cells[2], "$6.99")
set_cell(t4.rows[12].cells[2], "$8.99")
# T7 卖点表：blocks2[7] 产品名对齐
t7 = blocks2[7]
set_cell(t7.rows[12].cells[0], "Mini Ball Head Mount")
set_cell(t7.rows[13].cells[0], "Magnetic Phone Mount")
set_cell(t7.rows[14].cells[0], "Microfiber Cloth 3-Pack")
doc2.save(jud)
print("SAVED", jud)
