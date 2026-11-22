# -*- coding: utf-8 -*-
import os, shutil
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
WORK = os.path.join(ROOT, "_arch_work", "playbook")
EDIT = os.path.join(ROOT, "shotstart-playbook", "_edit_work")

targets = [
    (os.path.join(ROOT, "shotstart-playbook", "运营配置与测试下单SOP.docx"), "sop"),
    (os.path.join(ROOT, "现场执行清单.docx"), "checklist"),
    (os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx"), "judge"),
]

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

for path, tag in targets:
    if not os.path.exists(path):
        print("MISSING", path); continue
    # 备份（未备份过的）
    bak = os.path.join(EDIT, f"{tag}-backup-arch.docx")
    if not os.path.exists(bak):
        shutil.copy(path, bak)
    doc = Document(path)
    out = []
    bi = 0
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            for ri, row in enumerate(block.rows):
                for ci, cell in enumerate(row.cells):
                    for pi, p in enumerate(cell.paragraphs):
                        out.append(f"[T{bi}R{ri}C{ci}P{pi}] {p.text}")
        else:
            out.append(f"[P{bi}] {block.text}")
        bi += 1
    txt = os.path.join(WORK, f"{tag}_now.txt")
    with open(txt, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"{tag}: blocks={bi} paras+rows lines={len(out)} -> {txt}")
