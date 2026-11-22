# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
TARGET = os.path.join(ROOT, "shotstart-playbook", "Athena建店指令包.docx")
doc = Document(TARGET)

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

fixed = 0
for block in iter_block_items(doc):
    if isinstance(block, Table):
        for row in block.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    if p.text.startswith("8. Email popup"):
                        new = "9." + p.text[2:]
                        if p.runs:
                            p.runs[0].text = new
                            for r in p.runs[1:]:
                                r.text = ""
                        fixed += 1
    else:
        p = block
        if p.text.startswith("8. Email popup"):
            new = "9." + p.text[2:]
            if p.runs:
                p.runs[0].text = new
                for r in p.runs[1:]:
                    r.text = ""
            fixed += 1

assert fixed == 1, f"弹窗编号修复数={fixed}"
doc.save(TARGET)
print("fixed popup numbering:", fixed)
