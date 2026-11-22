import os, shutil
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

base = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-playbook"
work = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\_arch_work\playbook"
edit = os.path.join(base, "_edit_work")
os.makedirs(work, exist_ok=True)

files = ["Athena建店指令包.docx", "运营配置与测试下单SOP.docx"]
backs = ["pkg-backup-arch.docx", "sop-backup-arch.docx"]

def iter_block_items(parent):
    from docx.document import Document as _Doc
    from docx.oxml.ns import qn
    parent_elm = parent.element.body if isinstance(parent, _Doc) else parent._element
    for child in parent_elm.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)

# 1. binary backup into _edit_work (kept out of delivery package)
for f, b in zip(files, backs):
    shutil.copy(os.path.join(base, f), os.path.join(edit, b))
    print("backup:", b)

# 2. extract paragraphs + tables in body order, with block index
def dump(doc, path):
    lines = []
    bi = 0
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            t = block.text
            if t.strip():
                lines.append(f"[P{bi}] {t}")
        else:
            ri = 0
            for row in block.rows:
                cells = [c.text.strip().replace("\n", " / ") for c in row.cells]
                lines.append(f"[T{bi}R{ri}] " + " | ".join(cells))
                ri += 1
        bi += 1
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(os.path.basename(path), len(lines), "lines")

for f in files:
    doc = Document(os.path.join(base, f))
    dump(doc, os.path.join(work, f.replace(".docx", ".txt")))
