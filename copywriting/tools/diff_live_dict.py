# -*- coding: utf-8 -*-
"""Read-only audit: diff source dict (729) vs live injected dict (693)."""
import json, io, re, pathlib, ast

ROOT = pathlib.Path(r"C:\Users\temple\Doubao\chats\2026-11-20\new-chat")
SRC = ROOT / "shotstart-copy" / "tools" / "i18n_zh.json"
LIVE = ROOT / "shotstart-store-evidence" / "scratch" / "live-i18n-30384df7882911c341f09ce8a21edd05.js"

live_text = LIVE.read_text(encoding="utf-8")
# slice object between SS_I18N_ZH = { and };;
start = live_text.index("var SS_I18N_ZH = {")
brace = live_text.index("{", start)
end = live_text.index("};;", brace)
obj = live_text[brace:end+1]

pair_re = re.compile(r'"((?:[^"\\]|\\.)*)"\s*:\s*"((?:[^"\\]|\\.)*)"')
def unesc(s):
    try:
        return ast.literal_eval('"' + s + '"')
    except Exception:
        return s

live = {}
for m in pair_re.finditer(obj):
    k = unesc(m.group(1)); v = unesc(m.group(2))
    live[k] = v

src = json.load(io.open(SRC, encoding="utf-8"))["zh-CN"]

only_src = {k: src[k] for k in src if k not in live}
only_live = {k: live[k] for k in live if k not in src}

print("source keys:", len(src))
print("live keys:", len(live))
print("only in source (missing on live):", len(only_src))
print("only in live (not in source):", len(only_live))

out = {"only_source": only_src, "only_live": only_live, "live": live}
(ROOT / "shotstart-copy" / "tools" / "audit_diff.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

print("\n=== ONLY SOURCE (need to inject) ===")
for k, v in only_src.items():
    print(f"  {k!r}  =>  {v}")
print("\n=== ONLY LIVE (residual / stale) ===")
for k, v in only_live.items():
    print(f"  {k!r}  =>  {v}")
