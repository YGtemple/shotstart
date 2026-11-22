# -*- coding: utf-8 -*-
"""PUBLISH-line hygiene scan.

Checks on consumer-facing [PUBLISH] lines:
1. Placeholder bracket leak ([待确认 ...]).
2. Placeholder-word residue: placeholder / to be confirmed / being confirmed.
3. CJK residue outside the page legend line.
4. Demo-context residue: demo / drill / 演练 must not appear on PUBLISH lines.
5. Forbidden-word match against the glossary.txt Avoid column
   (read dynamically; no hardcoded word list).
"""
import os, glob, re

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages")
INTERNAL_PAGES = {"glossary.txt", "placeholder-map.txt"}
# Explicit CJK exemption: judge-guide-zh.txt is the sole Chinese reviewer
# custom page; Chinese is allowed there by approved exception.
CJK_EXEMPT_PAGES = {"judge-guide-zh.txt"}
# Line-level CJK exemption marker: the home top-bar link to the Judge Guide
# is the only Chinese line on otherwise English storefront pages.
JUDGE_GUIDE_LINK_MARKER = "judge guide"

ph = re.compile(r"\[待确认")
placeholder_words = re.compile(r"placeholder|to be confirmed|being confirmed", re.I)
cjk = re.compile(r"[一-鿿]")
demo_residue = re.compile(r"\bdemo\b|\bdrill\b|演练", re.I)

# --- Glossary Avoid terms, dynamic from glossary.txt column 3 ---
# Canonical compounds that must not trigger an Avoid substring match.
CANONICAL_COMPOUNDS = ["shop all gear"]
avoid = {}
glossary = os.path.join(BASE, "glossary.txt")
if os.path.exists(glossary):
    for line in open(glossary, encoding="utf-8"):
        if not line.startswith("[INTERNAL]"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[2]:
            for part in cells[2].split(","):
                part = part.strip().strip('"“”').strip()
                if part:
                    avoid[part.lower()] = re.compile(r"\b" + re.escape(part.lower()) + r"\b")

bracket_issues = []
word_issues = []
cjk_issues = []
demo_issues = []
avoid_hits = []

for f in sorted(glob.glob(os.path.join(BASE, "*.txt"))):
    base = os.path.basename(f)
    if base in INTERNAL_PAGES:
        continue
    for i, line in enumerate(open(f, encoding="utf-8").read().splitlines(), 1):
        if "[PUBLISH]" not in line:
            continue
        if ph.search(line):
            bracket_issues.append((base, i, line.strip()))
        if placeholder_words.search(line):
            word_issues.append((base, i, line.strip()))
        # legend line 1 carries the Chinese marker legend; skip it.
        # Whole-page CJK exemption: judge-guide-zh.txt (approved Chinese page).
        # Line-level exemption: home top-bar Judge Guide link line.
        if (i > 1 and base not in CJK_EXEMPT_PAGES and cjk.search(line)
                and JUDGE_GUIDE_LINK_MARKER not in line.lower()):
            cjk_issues.append((base, i, line.strip()))
        if demo_residue.search(line):
            demo_issues.append((base, i, line.strip()))
        low = line.lower()
        if any(comp in low for comp in CANONICAL_COMPOUNDS):
            continue
        for term, rx in avoid.items():
            if rx.search(low):
                avoid_hits.append((base, i, term, line.strip()))

print("PUBLISH lines with placeholder brackets:", len(bracket_issues))
for b, i, l in bracket_issues:
    print(" ", b, i, l)

print("PUBLISH lines with placeholder-word residue:", len(word_issues))
for b, i, l in word_issues:
    print(" ", b, i, l)

print("PUBLISH lines with CJK residue:", len(cjk_issues))
for b, i, l in cjk_issues:
    print(" ", b, i, l)

print("PUBLISH lines with demo-context residue:", len(demo_issues))
for b, i, l in demo_issues:
    print(" ", b, i, l)

print("Avoid-word hits on PUBLISH lines:", len(avoid_hits))
for b, i, term, l in avoid_hits:
    print(" ", b, i, "[" + term + "]", l)
