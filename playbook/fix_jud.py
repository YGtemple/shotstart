# -*- coding: utf-8 -*-
import os
from docx import Document
ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
JUD = os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx")
doc = Document(JUD)

def set_cell(cell, text):
    p = cell.paragraphs[0]
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)

# T0 价格表：名 + 价
price_fix = {
    "Extension Pole":      ("Extension Pole", "$16.99"),
    "Mini Ball Head":      ("Mini Ball Head Mount", "$12.99"),
    "Magnetic Mount":      ("Magnetic Phone Mount", "$11.99"),
    "Microfiber 3-Pack":   ("Microfiber Cloth 3-Pack", "$6.99"),
    "Shot List Cards":     ("Shot List Cards", "$8.99"),
}
# T1 卖点表：仅名
name_fix = {
    "Mini Ball Head": "Mini Ball Head Mount",
    "Magnetic Mount": "Magnetic Phone Mount",
    "Microfiber 3-Pack": "Microfiber Cloth 3-Pack",
}

hit0, hit1 = 0, 0
for ti, t in enumerate(doc.tables):
    for row in t.rows:
        c0 = row.cells[0].text.strip()
        if ti == 0 and c0 in price_fix:
            name, price = price_fix[c0]
            set_cell(row.cells[0], name)
            set_cell(row.cells[2], price)
            hit0 += 1
        elif ti == 1 and c0 in name_fix:
            set_cell(row.cells[0], name_fix[c0])
            hit1 += 1

assert hit0 == 5, f"T0 fixes={hit0}"
assert hit1 == 3, f"T1 fixes={hit1}"
doc.save(JUD)
print(f"judge card fixed: T0={hit0} T1={hit1}")
