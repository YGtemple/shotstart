# -*- coding: utf-8 -*-
import re, os, io
WD = r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\_arch_work\playbook"
files = {"pkg":"verify_pkg.txt","sop":"verify_sop.txt","chk":"verify_chk.txt","jud":"verify_jud.txt"}
money = re.compile(r"\$\d+(?:\.\d{2})?")
for tag, fn in files.items():
    print(f"===== {tag} =====")
    for i, ln in enumerate(io.open(os.path.join(WD,fn),encoding="utf-8").read().splitlines(),1):
        if "$" in ln:
            m = money.findall(ln)
            print(f"  L{i} {m}: {ln[:150]}")
    print()
