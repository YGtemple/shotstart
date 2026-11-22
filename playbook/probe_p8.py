# -*- coding: utf-8 -*-
import os
from docx import Document
ROOT = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat"
doc = Document(os.path.join(ROOT, "现场执行清单.docx"))
for pi, p in enumerate(doc.paragraphs):
    if pi in (1, 8):
        print(f"P{pi} runs={len(p.runs)}")
        for ri, r in enumerate(p.runs):
            print(f"  r{ri}: {r.text!r}")
