# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
WORK = os.path.join(ROOT, "_arch_work", "playbook")
files = [
    ("pkg", os.path.join(ROOT, "shotstart-playbook", "Athena建店指令包.docx")),
    ("sop", os.path.join(ROOT, "shotstart-playbook", "运营配置与测试下单SOP.docx")),
    ("chk", os.path.join(ROOT, "现场执行清单.docx")),
    ("jud", os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx")),
]

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

for tag, path in files:
    doc = Document(path)
    paras, tables, lines = 0, 0, []
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            tables += 1
            for ri, row in enumerate(block.rows):
                for ci, cell in enumerate(row.cells):
                    for p in cell.paragraphs:
                        lines.append(f"[T{tables-1}R{ri}C{ci}] {p.text}")
        else:
            paras += 1
            lines.append(f"[P{paras-1}] {block.text}")
    out = os.path.join(WORK, f"verify_{tag}.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"{tag}: paragraphs={paras} tables={tables} lines={len(lines)} -> {out}")
