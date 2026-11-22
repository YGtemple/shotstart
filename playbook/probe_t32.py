import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

base = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
doc = Document(os.path.join(base, "Athena建店指令包.docx"))

def iter_block_items(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

bi = 0
for block in iter_block_items(doc):
    if isinstance(block, Table) and bi == 32:
        for pi, p in enumerate(block.rows[0].cells[0].paragraphs):
            print(f"P{pi} runs={len(p.runs)}: {p.text!r}")
    if isinstance(block, Table):
        bi += 1
    else:
        bi += 1
