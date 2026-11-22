# -*- coding: utf-8 -*-
import os, re
from docx import Document

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ph = re.compile(r"\[待确认")
placeholder_words = re.compile(r"placeholder|to be confirmed|being confirmed", re.I)
demo_residue = re.compile(r"\bdemo\b|\bdrill\b|演练", re.I)
for name in ["ShotStart店铺文案包.docx", "ShotStart品牌定稿.docx", "评委速览卡.docx"]:
    doc = Document(os.path.join(BASE, name))
    leaks = []
    words = []
    demo = []
    def check(text, where):
        if not text.startswith("[PUBLISH]"):
            return
        if ph.search(text):
            leaks.append((where, text[:120]))
        if placeholder_words.search(text):
            words.append((where, text[:120]))
        if demo_residue.search(text):
            demo.append((where, text[:120]))
    for p in doc.paragraphs:
        check(p.text, "P")
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                check(c.text, "T")
    print(name, "PUBLISH leaks:", len(leaks), "| placeholder-word:", len(words), "| demo residue:", len(demo))
    for k, v in leaks:
        print("  leak", k, v)
    for k, v in words:
        print("  word", k, v)
    for k, v in demo:
        print("  demo", k, v)
