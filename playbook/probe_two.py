# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
files = [
    (os.path.join(ROOT, "现场执行清单.docx"), "checklist"),
    (os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx"), "judge"),
]

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

for path, tag in files:
    doc = Document(path)
    print("="*80, tag)
    bi = 0
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            for ri, row in enumerate(block.rows):
                for ci, cell in enumerate(row.cells):
                    for p in cell.paragraphs:
                        if p.text.strip():
                            flag = "M" if len(p.runs) > 1 else "s"
                            print(f"  T{bi}R{ri}C{ci} [{flag}] {p.text[:70]!r}")
        else:
            if block.text.strip():
                flag = "M" if len(block.runs) > 1 else "s"
                print(f"  P{bi} [{flag}] {block.text[:80]!r}")
        bi += 1
