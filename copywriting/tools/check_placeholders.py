# -*- coding: utf-8 -*-
"""Unmapped-placeholder forward check + fallback-coverage report.

Fallback phrases are read dynamically from placeholder-map.txt
(Standalone on-site fallback column); no hardcoded fallback list here.
"""
import os, re, glob

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages")
map_path = os.path.join(BASE, "placeholder-map.txt")
map_text = open(map_path, encoding="utf-8").read().lower()

# Dynamic standalone fallback phrases: map column 4 (index 3)
fallbacks = set()
for line in open(map_path, encoding="utf-8"):
    if not line.startswith("[INTERNAL]"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) >= 4 and cells[3] and cells[3] != "Standalone on-site fallback":
        fallbacks.add(cells[3].lower())

ph_re = re.compile(r"\[待确认:[^\]]*\]")
unmapped = []
all_ph = set()
for f in sorted(glob.glob(os.path.join(BASE, "*.txt"))):
    if os.path.basename(f) == "placeholder-map.txt":
        continue
    text = open(f, encoding="utf-8").read()
    for ph in ph_re.findall(text):
        all_ph.add(ph)
        if ph.lower() not in map_text:
            unmapped.append((os.path.basename(f), ph))

print("Distinct placeholders in pages:", len(all_ph))
for ph in sorted(all_ph):
    print(" ", ph)
print("Unmapped:", len(unmapped))
for f, ph in unmapped:
    print("  MISSING", f, ph)

# TBD / Chinese bracket leak outside internal pages
for f in sorted(glob.glob(os.path.join(BASE, "*.txt"))):
    base = os.path.basename(f)
    text = open(f, encoding="utf-8").read()
    for i, line in enumerate(text.splitlines(), 1):
        if "TBD" in line and base not in ("glossary.txt", "placeholder-map.txt"):
            print("TBD", base, i, line)

# Standalone fallback phrases defined in the map (dynamic source of truth).
# Rendered PUBLISH lines mostly use the inline slot clause; these standalone
# sentences apply to own-line fallback blocks.
print("Dynamic standalone fallback phrases in map:", len(fallbacks))
for fb in sorted(fallbacks):
    print("  ", fb)
