# -*- coding: utf-8 -*-
"""Correct mini-ball-head price 11.99 -> 12.99 across source (mapping table + live)."""
import io, pathlib

p = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat\shotstart-copy\tools\shotstart_content.py")
src = p.read_text(encoding="utf-8")

REPL = [
    # bundle member sentences (3 occurrences: _pro_entry, home Pro card bullet, Pro SPU card p)
    ("Mini Ball Head ($11.99), Creator Carry Case ($12.99)",
     "Mini Ball Head ($12.99), Creator Carry Case ($12.99)"),
    # collection product-list bullet
    ("Mini Ball Head — $11.99. Level and lock the frame between shots with one twist.",
     "Mini Ball Head — $12.99. Level and lock the frame between shots with one twist."),
    # ball-head PDP pricing line (Pro kit member; magnetic mount line uses $9.99)
    ('("price", "Demo price: $11.99 — Demo configuration, confirm before launch. Bundle pricing available in the Pro Creator Kit.")',
     '("price", "Demo price: $12.99 — Demo configuration, confirm before launch. Bundle pricing available in the Pro Creator Kit.")'),
    # price table row
    ('["Mini Ball Head", "迷你云台", "$11.99"]',
     '["Mini Ball Head", "迷你云台", "$12.99"]'),
    # Chinese operator note
    ("演示价 $11.99，可加入 Pro Creator Kit。",
     "演示价 $12.99，可加入 Pro Creator Kit。"),
]

for old, new in REPL:
    n = src.count(old)
    src = src.replace(old, new)
    print(f"replaced {n}x: {old[:60]}")

# safety: no $11.99 should remain attached to ball head; list any residual 11.99
import re
for i, line in enumerate(src.splitlines(), 1):
    if "11.99" in line:
        print("RESIDUAL 11.99 L%d: %s" % (i, line.strip()[:120]))

p.write_text(src, encoding="utf-8")
print("saved")
