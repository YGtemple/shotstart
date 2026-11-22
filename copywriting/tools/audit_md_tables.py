# -*- coding: utf-8 -*-
import json, io, pathlib
ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
c = json.load(io.open(ROOT/"shotstart-copy"/"tools"/"audit_classified.json", encoding="utf-8"))

def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")

def table(rows, prio, block_col=True):
    head = "| 键名（EN 逐字） | 中文值 | 区块 | 类型 | 优先级 | 阻塞 |\n| --- | --- | --- | --- | --- | --- |"
    out = [head]
    for r in rows:
        out.append(f"| `{esc(r['key'])}` | {esc(r['zh'])} | {r['block']} | {r['type']} | {prio} | {'是' if prio=='P0' else '否'} |")
    return "\n".join(out)

p0 = table(c["P0"], "P0 必须上线")
p1 = table(c["P1"], "P1 可延后")
p2 = table(c["P2"], "P2 可延后")

# stale list
stale = ["| `%s` | %s |" % (esc(r["key"]), esc(r["zh"])) for r in c["stale_live"]]
stale = "| 线上残留旧键（EN 逐字） | 线上现值 |\n| --- | --- |\n" + "\n".join(stale)

(ROOT/"shotstart-copy"/"tools"/"audit_tables.md").write_text(
    "## P0\n\n"+p0+"\n\n## P1\n\n"+p1+"\n\n## P2\n\n"+p2+"\n\n## STALE\n\n"+stale,
    encoding="utf-8")
print("P0", len(c["P0"]), "P1", len(c["P1"]), "P2", len(c["P2"]), "stale", len(c["stale_live"]))
