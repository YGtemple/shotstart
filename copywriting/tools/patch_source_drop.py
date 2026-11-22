# -*- coding: utf-8 -*-
import io, pathlib, re
p = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy\tools\shotstart_content.py")
lines = io.open(p, encoding="utf-8").read().splitlines(keepends=True)
out, dropped = [], []
for ln in lines:
    # specs standalone fallback paragraph: ("p", "Exact ... are being finalized; contact us for details."),
    if re.match(r'\s*\("p", "Exact .* are being finalized; contact us for details\."\),\s*$', ln):
        dropped.append(ln.strip())
        continue
    out.append(ln)
p.write_text("".join(out), encoding="utf-8")
print("dropped:", len(dropped))
for d in dropped:
    print("  -", d)
