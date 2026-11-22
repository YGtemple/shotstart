import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

base = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
files = ["Athena建店指令包.docx", "运营配置与测试下单SOP.docx"]

def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.oxml.ns import qn
    parent_elm = parent.element.body if isinstance(parent, _Doc) else parent._element
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

for f in files:
    doc = Document(os.path.join(base, f))
    print("="*100)
    print(f)
    bi = 0
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            for ri, row in enumerate(block.rows):
                for ci, cell in enumerate(row.cells):
                    for pi, p in enumerate(cell.paragraphs):
                        if p.text.strip():
                            runs = [(i, r.text) for i, r in enumerate(p.runs)]
                            flag = "MULTI" if len(runs) > 1 else "single"
                            if any(k in p.text for k in ["$16.99","$12.99","$14.99","$13.99","$58.96","$50.12","八件","五件","四件","三件","$44.97","$38.22","$62.96","$53.52"]):
                                print(f"  T{bi}R{ri}C{ci}P{pi} [{flag}] runs={len(runs)}")
                                for i, t in runs:
                                    print(f"     r{i}: {t!r}")
        else:
            if block.text.strip():
                runs = [(i, r.text) for i, r in enumerate(block.runs)]
                flag = "MULTI" if len(runs) > 1 else "single"
                if any(k in block.text for k in ["$16.99","$12.99","$14.99","$13.99","$58.96","$50.12","八件","五件","四件","三件","$44.97","$38.22","$62.96","$53.52","152","77","75","114"]):
                    print(f"  P{bi} [{flag}] runs={len(runs)}")
                    for i, t in runs:
                        print(f"     r{i}: {t!r}")
        bi += 1
