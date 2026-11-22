# -*- coding: utf-8 -*-
import os
from docx import Document
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for name in ("ShotStart店铺文案包.docx", "ShotStart品牌定稿.docx", "评委速览卡.docx"):
    p = os.path.join(BASE, name)
    d = Document(p)
    print(f"{name}: paragraphs={len(d.paragraphs)} tables={len(d.tables)}")
