# -*- coding: utf-8 -*-
"""Render ShotStart copy package: pages/*.txt + ShotStart店铺文案包.docx."""
import os
import re
import sys
import io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shotstart_content import PAGES, SHIPPING_NOTES_ZH, CHECKLIST_ZH, READING_GUIDE_ZH

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE, "pages")
DOCX_PATH = os.path.join(BASE, "ShotStart店铺文案包.docx")

PAGE_ORDER = [
    "home.txt",
    "shop.txt",
    "product-tripod.txt",
    "product-stand.txt",
    "product-cleaning-kit.txt",
    "product-carry-case.txt",
    "product-reflector.txt",
    "product-backdrop.txt",
    "product-extension-pole.txt",
    "product-cleaning-refill.txt",
    "product-mini-ball-head.txt",
    "product-magnetic-mount.txt",
    "product-microfiber-3pack.txt",
    "product-shot-list-cards.txt",
    "cart-checkout.txt",
    "form-states.txt",
    "about.txt",
    "contact.txt",
    "shipping-policy.txt",
    "refund-policy.txt",
    "privacy-policy.txt",
    "terms.txt",
    "challenge.txt",
    "marketing.txt",
    "judge-guide-zh.txt",
    "glossary.txt",
    "placeholder-map.txt",
]

INTERNAL_KINDS = {"note", "price", "setup"}
INTERNAL_PAGES = {"glossary.txt", "placeholder-map.txt"}
PUBLISH_FALLBACK = "Details coming soon — contact us for specifics."

NAVY = RGBColor(0x0F, 0x1B, 0x2D)
ORANGE = RGBColor(0xFF, 0x5A, 0x2C)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x55, 0x55, 0x55)


# ---------------------------------------------------------------------------
# TXT rendering
# ---------------------------------------------------------------------------
def fallback_for(ph):
    """Standalone on-site sentence: used as its own line/block (R3-1)."""
    p = ph.lower()
    if any(k in p for k in ["address", "location", "entity", "hours", "mail"]):
        return "Contact us for the current mailing details."
    if any(k in p for k in ["window", "time", "schedule", "processing", "retention",
                             "dates", "validity", "cadence"]):
        return "Timing details will be confirmed before launch."
    if any(k in p for k in ["material", "weight", "dimensions", "width", "range",
                             "volume", "ingredient", "cloth", "liquid", "brush",
                             "cutout", "pad", "foot", "adapter", "bag", "accessory",
                             "surface", "contents"]):
        return "Full specifications are being finalized; ask us for details."
    if any(k in p for k in ["legal", "liability", "jurisdiction", "rights", "consent",
                             "intellectual", "dispute", "age"]):
        return "This section is being reviewed; contact us with any questions."
    if any(k in p for k in ["code", "offer", "refill", "incentive", "threshold",
                             "rate", "carrier", "region"]):
        return "Offer and shipping details are demo settings pending confirmation."
    return PUBLISH_FALLBACK


def inline_for(ph):
    """Short embedded clause: grammatically fits after a label, colon, or
    'is/are' slot. Never a full standalone sentence pasted mid-slot (R3-1)."""
    p = ph.lower()
    if any(k in p for k in ["window", "time", "schedule", "processing", "retention",
                             "dates", "validity", "cadence", "date", "hours"]):
        return "still being finalized before launch."
    if any(k in p for k in ["address", "location", "entity"]):
        return "available on request."
    if any(k in p for k in ["material", "weight", "dimensions", "width", "range",
                             "volume", "ingredient", "cloth", "liquid", "brush",
                             "cutout", "pad", "foot", "adapter", "bag", "accessory",
                             "surface", "contents", "mount", "length", "base"]):
        return "still being finalized; contact us for details."
    if any(k in p for k in ["legal", "liability", "jurisdiction", "rights", "consent",
                             "intellectual", "dispute", "age"]):
        return "under legal review; contact us with any questions."
    return "pending final confirmation."


def tag(kind, fname=None):
    if fname in INTERNAL_PAGES or kind in INTERNAL_KINDS:
        return "[INTERNAL] "
    return "[PUBLISH] "


PH_RE = re.compile(r"\[待确认:[^\]]*\]")


def publish_text(text, fname):
    """On PUBLISH-facing copy, swap unresolved placeholders for the neutral
    on-site fallback; placeholder keys stay listed in an internal note."""
    if not text or fname in INTERNAL_PAGES:
        return text
    out = PH_RE.sub(lambda m: inline_for(m.group(0)), text)
    out = re.sub(r"\.\s*\.", ".", out)
    out = re.sub(r"\.;", ";", out)
    out = re.sub(r"\s+([.,;])", r"\1", out)
    return out


def collect_publish_keys(blocks):
    """Placeholder keys that appeared on PUBLISH blocks (kept for the internal note)."""
    keys = []
    for blk in blocks:
        kind = blk[0]
        if kind in INTERNAL_KINDS:
            continue
        texts = []
        if kind in ("p", "h1", "h2", "faq_q", "faq_a"):
            texts = [blk[1]]
        elif kind == "bullets":
            texts = blk[1]
        elif kind == "table":
            texts = [cell for row in blk[2] for cell in row]
        for t in texts:
            for match in PH_RE.findall(t or ""):
                if match not in keys:
                    keys.append(match)
    return keys


def render_txt(blocks, fname):
    lines = ["[PUBLISH] 可粘贴到店铺前台 · [INTERNAL] 仅后台备注，禁止粘贴前台", ""]
    for blk in blocks:
        kind = blk[0]
        if kind == "h1":
            lines.append("# " + blk[1])
            lines.append("")
        elif kind == "h2":
            lines.append("## " + blk[1])
            lines.append("")
        elif kind == "p":
            lines.append(tag(kind, fname) + publish_text(blk[1], fname))
            lines.append("")
        elif kind == "faq_q":
            lines.append(tag(kind, fname) + "Q: " + publish_text(blk[1], fname))
            lines.append("")
        elif kind == "faq_a":
            lines.append(tag(kind, fname) + "A: " + publish_text(blk[1], fname))
            lines.append("")
        elif kind == "bullets":
            for item in blk[1]:
                lines.append("- " + tag(kind, fname) + publish_text(item, fname))
            lines.append("")
        elif kind == "setup":
            for item in blk[1]:
                lines.append("- [INTERNAL] " + item)
            lines.append("")
        elif kind == "table":
            headers, rows = list(blk[1]), list(blk[2])
            if fname == "placeholder-map.txt":
                headers = headers + ["Standalone on-site fallback", "Inline slot clause"]
            lines.append(" | ".join(headers))
            lines.append(" | ".join(["---"] * len(headers)))
            row_prefix = "[INTERNAL] " if fname in INTERNAL_PAGES else ""
            for row in rows:
                row = [publish_text(c, fname) for c in row]
                if fname == "placeholder-map.txt":
                    row = row + [fallback_for(row[0]), inline_for(row[0])]
                lines.append(row_prefix + " | ".join(row))
            lines.append("")
        elif kind == "note":
            lines.append("[INTERNAL] 【操作者说明】" + blk[1])
            lines.append("")
        elif kind == "price":
            lines.append("[INTERNAL] " + blk[1])
            lines.append("")
    if fname not in INTERNAL_PAGES:
        keys = collect_publish_keys(blocks)
        if keys:
            lines.append("")
            lines.append("[INTERNAL] 【待确认占位键】上线前在 placeholder-map.txt 查英文定稿与中性兜底句；前台不得残留方括号占位： "
                         + "; ".join(keys))
    return "\n".join(lines).rstrip() + "\n"


def write_txt_files():
    os.makedirs(PAGES_DIR, exist_ok=True)
    for fname in PAGE_ORDER:
        text = render_txt(PAGES[fname], fname)
        path = os.path.join(PAGES_DIR, fname)
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("Wrote", len(PAGE_ORDER), "txt files to", PAGES_DIR)


# ---------------------------------------------------------------------------
# DOCX rendering
# ---------------------------------------------------------------------------
def set_font(run, size=11, bold=False, color=BLACK, ascii_font="Times New Roman",
             ea_font="宋体", italic=False):
    run.font.name = ascii_font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), ascii_font)
    rfonts.set(qn("w:hAnsi"), ascii_font)
    rfonts.set(qn("w:eastAsia"), ea_font)


def add_body(doc, text, size=11, bold=False, color=BLACK, italic=False,
             align=None, indent=False, ea="宋体"):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(6)
    pf.line_spacing = 1.3
    if not indent:
        pf.first_line_indent = Pt(0)
    run = p.add_run(text)
    set_font(run, size=size, bold=bold, color=color, ea_font=ea, italic=italic)
    return p


def add_heading(doc, text, level=1):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    if level == 1:
        pf.space_before = Pt(14)
        pf.space_after = Pt(6)
        size, color, ea = 16, NAVY, "黑体"
    elif level == 2:
        pf.space_before = Pt(11)
        pf.space_after = Pt(5)
        size, color, ea = 13, NAVY, "黑体"
    else:
        pf.space_before = Pt(9)
        pf.space_after = Pt(4)
        size, color, ea = 12, NAVY, "黑体"
    pf.first_line_indent = Pt(0)
    run = p.add_run(text)
    set_font(run, size=size, bold=True, color=color, ea_font=ea)
    return p


def shade_cell(cell, fill="F2F2F2"):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcpr.append(shd)


def set_row_cant_split(row):
    trpr = row._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trpr.append(cant)


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.autofit = True
    hdr = table.rows[0]
    set_row_cant_split(hdr)
    for i, htext in enumerate(headers):
        cell = hdr.cells[i]
        shade_cell(cell)
        cell.paragraphs[0].paragraph_format.first_line_indent = Pt(0)
        run = cell.paragraphs[0].add_run(htext)
        set_font(run, size=10.5, bold=True, color=BLACK)
    for row_data in rows:
        row = table.add_row()
        set_row_cant_split(row)
        for i, val in enumerate(row_data):
            cell = row.cells[i]
            cell.paragraphs[0].paragraph_format.first_line_indent = Pt(0)
            run = cell.paragraphs[0].add_run(val)
            set_font(run, size=10.5, bold=False, color=BLACK)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def render_blocks(doc, blocks, fname=None, internal=False):
    for blk in blocks:
        kind = blk[0]
        if kind == "h1":
            add_heading(doc, blk[1], 1)
        elif kind == "h2":
            add_heading(doc, blk[1], 2)
        elif kind == "p":
            text = blk[1] if internal else publish_text(blk[1], fname)
            add_body(doc, ("[INTERNAL] " if internal else tag(kind, fname)) + text)
        elif kind == "faq_q":
            add_body(doc, tag(kind, fname) + "Q: " + publish_text(blk[1], fname), bold=True, color=NAVY)
        elif kind == "faq_a":
            add_body(doc, tag(kind, fname) + "A: " + publish_text(blk[1], fname))
        elif kind == "bullets":
            for item in blk[1]:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.first_line_indent = Pt(0)
                shown = item if internal else publish_text(item, fname)
                run = p.add_run(("[INTERNAL] " if internal else tag(kind, fname)) + shown)
                set_font(run, size=11)
        elif kind == "setup":
            for item in blk[1]:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.first_line_indent = Pt(0)
                run = p.add_run("[INTERNAL] " + item)
                set_font(run, size=10.5, color=GRAY)
        elif kind == "table":
            headers, rows = list(blk[1]), list(blk[2])
            if fname == "placeholder-map.txt":
                headers = headers + ["Standalone on-site fallback", "Inline slot clause"]
                rows = [list(r) + [fallback_for(r[0]), inline_for(r[0])] for r in rows]
            if fname not in INTERNAL_PAGES:
                rows = [[publish_text(c, fname) for c in r] for r in rows]
            if fname in INTERNAL_PAGES:
                rows = [["[INTERNAL] " + c for c in r] for r in rows]
            add_table(doc, headers, rows)
        elif kind == "note":
            add_body(doc, "[INTERNAL] 【操作者说明】" + blk[1], size=10, italic=True,
                     color=GRAY, ea="宋体")
        elif kind == "price":
            add_body(doc, "[INTERNAL] " + blk[1], size=10.5,
                     bold=True, color=ORANGE, ea="宋体")


def build_docx():
    doc = Document()
    # Page setup: A4, 2.5cm margins
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)
    sec.left_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)

    # Normal style defaults
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")

    # Cover / title
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.paragraph_format.space_after = Pt(6)
    trun = title_p.add_run("ShotStart 店铺文案包")
    set_font(trun, size=18, bold=True, color=NAVY, ea_font="黑体")

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_p.paragraph_format.space_after = Pt(4)
    srun = sub_p.add_run("Your first shot starts here.")
    set_font(srun, size=12, bold=False, color=ORANGE, ea_font="楷体")

    meta_p = doc.add_paragraph()
    meta_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta_p.paragraph_format.space_after = Pt(10)
    mrun = meta_p.add_run("Shoplazza 可粘贴英文文案 · 面向美国市场的新手短视频创作者与小商家")
    set_font(mrun, size=10.5, color=GRAY)

    intro = (
        "使用说明：本包内面向消费者的页面文案均为英文，可直接复制粘贴进 Shoplazza；"
        "灰色【操作者说明】与橙色 [Demo configuration] 标注仅为后台提示，不上前台。"
        "所有价格、运费、折扣均为演示配置，上线前必须核实；凡标 [待确认: ...] 的参数，"
        "未取得真实信息前不得填写具体数值。品牌视觉口径：主色珊瑚橙 #FF5A2C、"
        "深海军蓝 #0F1B2D、暖白 #FAF6F0；语气 energetic、直白、鼓励新手行动。"
    )
    add_body(doc, intro, size=10.5, color=GRAY)

    # Pages
    for fname in PAGE_ORDER:
        render_blocks(doc, PAGES[fname], fname)
        if fname not in INTERNAL_PAGES:
            keys = collect_publish_keys(PAGES[fname])
            if keys:
                add_body(doc, "[INTERNAL] 【待确认占位键】上线前在 placeholder-map.txt 查英文定稿与中性兜底句；前台不得残留方括号占位： "
                         + "; ".join(keys), size=10, italic=True, color=GRAY, ea="宋体")

    # Chinese operator sections
    render_blocks(doc, READING_GUIDE_ZH, internal=True)
    render_blocks(doc, SHIPPING_NOTES_ZH, internal=True)
    render_blocks(doc, CHECKLIST_ZH, internal=True)

    doc.save(DOCX_PATH)
    print("Saved docx:", DOCX_PATH)


if __name__ == "__main__":
    os.makedirs(BASE, exist_ok=True)
    write_txt_files()
    build_docx()
