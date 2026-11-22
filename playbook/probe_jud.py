# -*- coding: utf-8 -*-
import os
from docx import Document
ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
JUD = os.path.join(ROOT, "shotstart-copy", "评委速览卡.docx")
doc = Document(JUD)
for ti, t in enumerate(doc.tables):
    for ri, row in enumerate(t.rows):
        c0 = row.cells[0].text.strip()
        if any(k in c0 for k in ["Extension Pole","Mini Ball","Magnetic","Microfiber","Shot List"]):
            for ci, cell in enumerate(row.cells):
                for pi, p in enumerate(cell.paragraphs):
                    runs = [r.text for r in p.runs]
                    print(f"T{ti}R{ri}C{ci}P{pi} runs={runs}")
            print("---")
