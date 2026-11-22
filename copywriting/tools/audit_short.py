# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
audit = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_diff.json", encoding="utf-8"))
live = audit["live"]
src = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"i18n_zh.json", encoding="utf-8"))["zh-CN"]

# short live values (chrome/button/heading candidates)
short = [(k,v) for k,v in live.items() if len(v) <= 18 and len(k) <= 40]
short.sort(key=lambda x: x[1])
out = []
for k,v in short:
    mark = "" if k in src else "  [STALE-ONLY]"
    out.append(f"{v}\t| {k}{mark}")
(ROOT/"shotstart-copy"/"tools"/"audit_short_live.txt").write_text("\n".join(out), encoding="utf-8")
print("short live:", len(short))

# source short for comparison
sshort = [(k,v) for k,v in src.items() if len(v) <= 18 and len(k) <= 40]
sshort.sort(key=lambda x: x[1])
out2 = [f"{v}\t| {k}" for k,v in sshort]
(ROOT/"shotstart-copy"/"tools"/"audit_short_src.txt").write_text("\n".join(out2), encoding="utf-8")
print("short src:", len(sshort))
