import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

base = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
doc = Document(os.path.join(base, "Athena建店指令包.docx"))

def iter_block_items(parent):
    parent_elm = parent.element.body
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

bi = 0
for block in iter_block_items(doc):
    if isinstance(block, Table):
        print(f"### T{bi} rows={len(block.rows)} cols={len(block.columns)}")
        if bi in (18, 265, 271):
            for ri, row in enumerate(block.rows):
                cells = [c.text.replace("\n"," / ")[:40] for c in row.cells]
                print(f"  R{ri}: {cells}")
    else:
        if bi == 63:
            print(f"### T63 paragraphs:")
            for pi, p in enumerate(block.rows[0].cells[0].paragraphs):
                print(f"  P{pi}: {p.text[:90]!r}")
    bi += 1
