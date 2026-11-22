# -*- coding: utf-8 -*-
"""Rebuild bilingual brand guideline docx and one-page reviewer quick card."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = os.path.join(BASE, "ShotStart品牌定稿.docx")
CARD = os.path.join(BASE, "评委速览卡.docx")
VISUALS_REL = r"shotstart-visuals"

NAVY = RGBColor(0x0F, 0x1B, 0x2D)
ORANGE = RGBColor(0xFF, 0x5A, 0x2C)
BLACK = RGBColor(0x00, 0x00, 0x00)
GRAY = RGBColor(0x55, 0x55, 0x55)


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


def body(doc, text, size=11, bold=False, color=BLACK, italic=False, ea="宋体"):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(5)
    pf.line_spacing = 1.25
    pf.first_line_indent = Pt(0)
    run = p.add_run(text)
    set_font(run, size=size, bold=bold, color=color, ea_font=ea, italic=italic)
    return p


def heading(doc, text, size=15, color=NAVY):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(11)
    pf.space_after = Pt(4)
    pf.first_line_indent = Pt(0)
    run = p.add_run(text)
    set_font(run, size=size, bold=True, color=color, ea_font="黑体")
    return p


def shade(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcpr.append(shd)


def cant_split(row):
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def make_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    hdr = table.rows[0]
    cant_split(hdr)
    for i, h in enumerate(headers):
        shade(hdr.cells[i], "F2F2F2")
        hdr.cells[i].paragraphs[0].paragraph_format.first_line_indent = Pt(0)
        r = hdr.cells[i].paragraphs[0].add_run(h)
        set_font(r, size=10, bold=True)
    for row_data in rows:
        row = table.add_row()
        cant_split(row)
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.paragraphs[0].paragraph_format.first_line_indent = Pt(0)
            r = c.paragraphs[0].add_run(val)
            set_font(r, size=10)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def bullets(doc, items, size=11):
    for item in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.first_line_indent = Pt(0)
        r = p.add_run(item)
        set_font(r, size=size)


def setup_doc():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(2.2)
    sec.left_margin = Cm(2.3)
    sec.right_margin = Cm(2.3)
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
    return doc


# ---------------------------------------------------------------------------
# Brand guideline (bilingual, CN first, EN after)
# ---------------------------------------------------------------------------
def build_brand():
    doc = setup_doc()

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_after = Pt(4)
    r = t.add_run("ShotStart 品牌定稿 / Brand Guidelines")
    set_font(r, size=18, bold=True, color=NAVY, ea_font="黑体")

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s.paragraph_format.space_after = Pt(10)
    r = s.add_run("Your first shot starts here. · 你的第一个镜头，从这里开始。")
    set_font(r, size=12, color=ORANGE, ea_font="楷体")

    heading(doc, "品牌名 / Brand Name")
    body(doc, "ShotStart")

    heading(doc, "品牌定位 / Positioning")
    body(doc, "ShotStart 面向美国英语市场的新手短视频创作者与小商家，提供简洁拍摄装备与 ShotStarter AI 内容助手。")
    body(doc, "ShotStart builds simple filming gear and the ShotStarter AI content assistant for beginner short-video creators and small shop owners in the US English-speaking market.")

    heading(doc, "品牌口号 / Slogan")
    body(doc, "Your first shot starts here.")
    body(doc, "你的第一个镜头，从这里开始。")

    heading(doc, "品牌故事 / Brand Story")
    body(doc, "我们从一个朴素的观察出发：开始做短视频最难的不是天赋，而是迈出第一个镜头。")
    body(doc, "新手创作者和小商家往往有真实的产品和真实的想法，却不知道怎么架手机、构图、把点子写成文案。ShotStart 用直白易用的拍摄装备搭配 ShotStarter AI 助手，降低这道门槛：说明清楚、设置简单，决定权在你手里。")
    body(doc, "我们不承诺一夜涨粉。我们帮你把第一条视频做完、发出去，然后一条一条继续——用七天挑战的节奏。")
    body(doc, "ShotStart was built around a simple observation: the hardest part of starting short-video creation isn't talent — it's taking the first shot.")
    body(doc, "New creators and small shop owners often have a real product and a real message, but they don't know how to set up a phone, frame a shot, or turn an idea into a caption. ShotStart pairs straightforward filming gear with the ShotStarter AI assistant to lower that barrier. We keep instructions plain, setups simple, and decisions in your hands.")
    body(doc, "We don't promise overnight growth. We help you finish and publish that first video, then the next one — seven days at a time.")

    heading(doc, "配色规范 / Color Palette")
    make_table(doc,
        ["角色 / Role", "Color", "Hex", "使用建议 / Usage"],
        [
            ["主强调色 / Primary accent", "Coral Orange", "#FF5A2C",
             "主 CTA、折扣徽章、重点高亮与激活状态，少量用于行动引导。Primary CTA buttons, discount badges, key highlights, active states; use sparingly."],
            ["品牌深色 / Brand dark", "Deep Navy Blue", "#0F1B2D",
             "品牌文字、标题、页脚与深色 Hero 背景；浅色页面正文。Brand text, headings, footer, dark hero backgrounds, and body text on light surfaces."],
            ["界面底色 / Surface", "Warm White", "#FAF6F0",
             "页面背景、卡片表面、深色面板上的文字底色。Page background, card surfaces, text background on navy panels."],
            ["次要派生色 / Muted secondary", "Muted Warm Gray", "#6B6259",
             "次要说明文字、弱化标签，用于暖白底。Secondary captions and muted labels on warm white."],
            ["备注色 / Note gray", "Neutral Note Gray", "#555555",
             "仅后台操作者备注文字，不上前台。Operator note text only; not for storefront."],
            ["实物成色 / Product finish", "Matte Black", "#1B1B1B",
             "实物商品主体哑光黑，属产品成色，不是品牌界面色；不得与海军蓝文字/页脚混用。Physical product matte black finish; a product color, not a brand UI color — do not mix with navy text or footer."],
        ])
    body(doc, "保持对比度可达：深蓝文字配暖白底，白字配深蓝底，橙色留给行动点。Keep contrast accessible: navy text on warm white, white on navy, orange for action points.",
         size=10, italic=True, color=GRAY)
    body(doc, "界定：#0F1B2D 海军蓝只用于品牌文字与页脚等界面结构；商品实拍中的哑光黑是实物颜色，两者不互相替代。The navy #0F1B2D is reserved for brand text and footer UI structure; product matte black is a physical finish and is not substituted for it.",
         size=10, italic=True, color=GRAY)
    body(doc, "橙色使用约束：#FF5A2C 珊瑚橙仅用于大字号展示标题（≥24px 粗体）、行动按钮与图形符号；不用于小字号正文——实测橙/暖白对比度 2.89:1，低于大文本 AA 3:1 边际。小字号文字统一使用海军蓝 #0F1B2D 或 muted #6B6259。如未来需让橙色承载正文，必须改用加深派生色并重新通过对比度测试。",
         size=10, italic=True, color=GRAY)
    body(doc, "Orange usage constraint: #FF5A2C is reserved for large display headings (≥24px bold), action buttons, and graphic symbols only; it is not used for small-size body text — measured contrast on warm white is 2.89:1, below the large-text AA 3:1 margin. Small text stays navy #0F1B2D or muted #6B6259. If orange ever carries body copy in future, a darkened derivative must be adopted and its contrast retested.",
         size=10, italic=True, color=GRAY)
    body(doc, "派生色附录：muted 暖灰 #6B6259（次要说明/弱化标签）、备注灰 #555555（仅后台备注）已入表；加深橙色派生色（若日后用于正文）待定，须在选定后补登 Hex 并附对比度实测值。Derived-color appendix: muted warm gray #6B6259 (secondary captions/muted labels) and note gray #555555 (operator notes only) are listed above; a darkened orange derivative (if used for body copy later) is pending — record its Hex and measured contrast once selected.",
         size=10, italic=True, color=GRAY)
    make_table(doc,
        ["浅底派生色 / Light tint", "Color", "Hex", "拟定用途 / Proposed usage"],
        [
            ["卡片浅底 / Card surface", "Warm light gray", "#E8DED2",
             "卡片底色，拟定用于商品卡/信息卡。Proposed card background for product or info cards."],
            ["分区浅底 / Section surface", "Off-white beige", "#F3ECE3",
             "分区底色，拟定用于页面分区或浅色面板。Proposed section background for page zones or light panels."],
            ["橙晕浅底 / Orange tint", "Light coral tint", "#FFE9E1",
             "橙色晕染底，拟定用于挑战/活动区块的浅底色。Proposed tinted background for challenge or promo zones."],
        ])
    body(doc, "三条浅底用途均为拟定方向；实际采用须在视觉稿核实后定稿，未核实前不得作为固定配色承诺。These three tints are proposed directions; final usage is confirmed against the visual design before launch.",
         size=10, italic=True, color=GRAY)

    heading(doc, "Logo 素材 / Logo Assets")
    body(doc, "素材位于店铺根目录 shotstart-visuals\\ 文件夹。Assets live in the store-root shotstart-visuals\\ folder.")
    make_table(doc,
        ["File", "Path (root-relative)", "用途 / Primary use"],
        [
            ["logo-square.png", VISUALS_REL + r"\logo-square.png",
             "暖白底横版锁合大尺寸场景母版（图标+字标，方形画布）；不用于 favicon 或头像。Horizontal-lockup master on warm-white background (icon + wordmark, square canvas) for large-format scenes; not used for favicon or avatar."],
            ["logo-transparent.png", VISUALS_REL + r"\logo-transparent.png",
             "透明底横版锁合大尺寸场景母版；不承担页眉锁合位，头像源归口图标-only 母版。Transparent horizontal-lockup master for large-format scenes; not the header lockup slot, and avatar source uses the icon-only masters."],
            ["logo-white.png", VISUALS_REL + r"\logo-white.png",
             "深底反白变体，用于页脚、深色横幅与海军蓝面板。White reverse variant for footer, dark banners, and navy panels."],
            ["logo-lockup-navy.png", VISUALS_REL + r"\logo-lockup-navy.png",
             "横版锁合（字标组合，navy 版），417×144 透明底；页眉浅底使用 DPI 锐利版。Horizontal lockup with wordmark, navy version, 417×144 transparent; crisp-DPI edition for the light-background header."],
            ["logo-lockup-white.png", VISUALS_REL + r"\logo-lockup-white.png",
             "横版锁合（反白组合），417×144 透明底；页脚深底使用 DPI 锐利版。Horizontal lockup, white reverse version, 417×144 transparent; crisp-DPI edition for the dark-background footer."],
            ["logo-icon-square.png", VISUALS_REL + r"\logo-icon-square.png",
             "图标-only 方形母版（不透明底），1024×1024；favicon、社交头像、商品卡片角标统一归口此母版。Icon-only square master, opaque background, 1024×1024; favicon, social profile picture, and small product-card corner mark all use this master."],
            ["logo-icon-transparent.png", VISUALS_REL + r"\logo-icon-transparent.png",
             "图标-only 透明底方形母版，1024×1024 ARGB；favicon/头像透明底场景。Icon-only transparent square master, 1024×1024 ARGB; favicon/avatar on transparent surfaces."],
        ])
    body(doc, "路由规则：页眉浅底统一使用 logo-lockup-navy，页脚深底使用 logo-lockup-white；logo-square 为暖白底横版锁合大尺寸场景母版，logo-transparent 为透明底横版锁合大尺寸场景母版；favicon、头像、卡片角标统一归口图标-only 母版 logo-icon-square / logo-icon-transparent；深底（深色横幅、海军蓝面板）使用反白变体 logo-white。Routing: the light header uses logo-lockup-navy and the dark footer uses logo-lockup-white; logo-square is the warm-white horizontal-lockup master for large-format scenes, and logo-transparent is the transparent horizontal-lockup master for large-format scenes; favicon, avatar, and corner marks all use the icon-only masters logo-icon-square / logo-icon-transparent; on dark backgrounds (dark banners, navy panels) use the white reverse variant logo-white.",
         size=10, italic=True, color=GRAY)

    heading(doc, "字体规范 / Typography")
    bullets(doc, [
        "标题：粗几何无衬线，推荐 Montserrat 或 Poppins（Bold / SemiBold），字距收紧。Headings: bold geometric sans-serif; Montserrat or Poppins (Bold/SemiBold), tight tracking.",
        "正文：易读常规无衬线，如 Inter 或系统无衬线常规字重。Body: clean readable sans-serif, e.g., Inter or system sans regular weight.",
        "标题回落栈 / Heading stack: Montserrat, Poppins, 'Helvetica Neue', Arial, sans-serif",
        "正文回落栈 / Body stack: Inter, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif",
        "避免装饰性或手写字体。Avoid decorative or script typefaces.",
    ])

    heading(doc, "语气规范 / Tone of Voice")
    bullets(doc, [
        "有活力：语气积极，推动创作者迈出下一步。Energetic: motivated, ready to help creators take the next step.",
        "直白：短句、平实语言，不堆术语和空话。Direct: short sentences, plain language, no jargon or filler.",
        "鼓励新手行动：聚焦把第一条视频做完发出去，站在新手角度说话。Encouraging beginner action: finish and publish that first shot; meet new creators where they are.",
        "诚实：不使用夸大、保证增长或施压话术；AI 草稿仅作起点，需本人审核。Stay honest: no hype, guaranteed-growth claims, or pressure tactics; AI drafts are starting points to review.",
    ])

    heading(doc, "CTA 组件矩阵 / Button Matrix")
    make_table(doc,
        ["位置 / Placement", "按钮文案 / Button label", "说明 / Note"],
        [
            ["Hero — 主按钮 / Primary", "Shop All Gear", "首页 Hero 主行动入口。Hero primary action."],
            ["Hero — 次按钮 / Secondary", "Join the 7-Day Shooting Challenge", "首页 Hero 次级行动入口。Hero secondary action."],
            ["挑战区块 / Challenge block", "Join the challenge", "首页挑战区块入口。Challenge section entry."],
            ["挑战留资表单提交 / Challenge sign-up submit", "Join the challenge", "挑战报名表提交按钮。Challenge form submit."],
            ["邮件弹窗 / Email popup", "Save my spot", "邮件弹窗订阅按钮。Popup subscribe button."],
            ["海报 / Poster", "Join the challenge", "宣传海报 CTA。Poster call to action."],
            ["联系表单 / Contact form submit", "Send message", "联系页表单提交按钮。Contact form submit."],
        ])
    body(doc, "口径说明：Hero 次按钮使用全称 “Join the 7-Day Shooting Challenge”，属入口级完整表述；挑战区块、表单提交、海报使用短 CTA “Join the challenge”。二者为同一动作的入口级/组件级两级口径，并非文案不一致。Note: the Hero secondary button uses the full name “Join the 7-Day Shooting Challenge” as an entry-level complete expression; the challenge block, form submit, and poster use the short CTA “Join the challenge”. These are entry-level and component-level phrasings of the same action, not a copy inconsistency.",
         size=10, italic=True, color=GRAY)

    heading(doc, "海报与图面使用规范 / Poster Usage")
    bullets(doc, [
        "白字压图：白色文字叠加实拍/场景图时，须加半透明深色遮罩（或预先加深图面），保证文字对比度可读；遮罩不可用时，优先回退到纯色卡片排版，不要直接把白字压在亮图上。White text over a photo or scene image must sit on a semi-transparent dark overlay (or a pre-darkened image) for readable contrast; when an overlay is not feasible, fall back to a solid-color card layout instead of placing white text directly on a bright image.",
        "海报主标题使用 7-Day Shooting Challenge；按钮 CTA 使用 Join the challenge（见 CTA 矩阵）。Poster headline uses 7-Day Shooting Challenge; the button CTA uses Join the challenge (see the Button Matrix).",
    ])

    heading(doc, "图面英文对照 / On-Image Copy Reference")
    body(doc, "供中文评委对照图面文案；图面以英文为准，中文仅释义。For Chinese reviewers only; on-image text stays English.")
    make_table(doc,
        ["图面位置 / Placement", "图面英文 / On-image EN copy", "中文释义"],
        [
            ["海报主标题 / Poster headline", "7-Day Shooting Challenge", "7 天拍摄挑战（海报主标题）"],
            ["海报按钮 / Poster button", "Join the challenge", "加入挑战"],
            ["七日标签 / Day labels", "Day 1 – Day 7", "第 1 天 – 第 7 天（每日任务标签）"],
            ["Hero 横幅 / Hero banner", "No on-image text; no wordmark (pure scene image)", "横幅为纯场景图，无文字、无字标"],
            ["Logo 字标 / Wordmark", "ShotStart", "品牌名，不翻译"],
        ])

    doc.save(BRAND)
    print("saved brand:", BRAND)


# ---------------------------------------------------------------------------
# Reviewer quick card (one page, bilingual)
# ---------------------------------------------------------------------------
def build_card():
    doc = setup_doc()
    sec = doc.sections[0]
    sec.top_margin = Cm(1.6)
    sec.bottom_margin = Cm(1.6)

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_after = Pt(4)
    r = t.add_run("ShotStart 评委速览卡 / Reviewer Quick Card")
    set_font(r, size=16, bold=True, color=NAVY, ea_font="黑体")

    body(doc, "品牌定位 / Positioning", size=11, bold=True, color=NAVY)
    body(doc, "面向美国市场新手短视频创作者与小商家的拍摄装备 + AI 内容助手。Simple filming gear plus the ShotStarter AI assistant for beginner creators and small shop owners in the US market.", size=10)

    body(doc, "商品与演示价 / Products & Demo Prices", size=11, bold=True, color=NAVY)
    make_table(doc,
        ["Product", "中文", "Demo price"],
        [
            ["Adjustable Phone Tripod", "可调手机三脚架", "$19.99"],
            ["Desktop Phone Stand", "桌面手机支架", "$14.99"],
            ["Lens Cleaning Kit", "镜头清洁套装（演示配置，构成待实物确认）", "$9.99"],
            ["Creator Carry Case", "器材收纳包", "$12.99"],
            ["Folding Reflector", "折叠反光板", "$10.99"],
            ["Backdrop Cloth", "背景布", "$13.99"],
            ["Extension Pole", "延长杆", "$16.99"],
            ["Lens Cleaning Refill", "清洁补充装（单件，不进捆绑）", "$7.99"],
            ["Mini Ball Head", "迷你云台", "$12.99"],
            ["Magnetic Mount", "磁吸手机支架", "$11.99"],
            ["Microfiber 3-Pack", "清洁布三片装", "$6.99"],
            ["Shot List Cards", "分镜清单卡片（配套 AI 脚本草稿）", "$8.99"],
            ["Creator Starter Kit (bundle)", "三件套捆绑（独立 SPU）", "Kit $44.97 → $38.22 with code STARTERKIT, save $6.75 (demo)"],
            ["Pro Creator Kit (bundle)", "四件套捆绑（独立 SPU）", "Kit $62.96 → $53.52 with code STARTERKIT, save $9.44 (demo)"],
        ])

    body(doc, "商品卖点 / PDP Selling Points", size=11, bold=True, color=NAVY)
    make_table(doc,
        ["Product", "EN selling point", "中文释义"],
        [
            ["Adjustable Phone Tripod", "Adjustable height and angle for varied shooting setups.", "高度与角度可调，适配不同拍摄机位（具体范围待核实）。"],
            ["Adjustable Phone Tripod", "Hands-free shooting for talking-head clips, product demos, and outdoor clips.", "免手持拍摄口播、产品演示与户外片段。"],
            ["Desktop Phone Stand", "Holds your phone upright at a usable desk angle.", "把手机直立固定在适合桌面拍摄/观看的角度。"],
            ["Desktop Phone Stand", "Compact footprint for desks, countertops, and small workspaces.", "占地紧凑，适合书桌、台面与狭小工作空间。"],
            ["Lens Cleaning Kit", "A compact cleaning set for phone and camera lenses; contents listed in What's in the Box.", "小巧的手机/相机镜头清洁套装；以包装内清单为准。"],
            ["Lens Cleaning Kit", "For dust, smudges, and fingerprints on phone, compact camera, and accessory lenses.", "清除手机、便携相机与附加镜头上的灰尘、污迹与指纹。"],
            ["Creator Carry Case", "A portable case to keep tripod, stand, and small accessories together.", "便携收纳包，集中收纳器材与小配件。"],
            ["Folding Reflector", "Soften and fill light for face and product clips.", "柔化并补光，适合面部与产品片段。"],
            ["Backdrop Cloth", "A plain background for product and talking-head clips.", "干净纯色背景，适合产品与口播片段。"],
            ["Extension Pole", "Reach overhead and higher-angle shots for selfie and group clips.", "抬高机位，适合高角度自拍与群拍。"],
            ["Lens Cleaning Refill", "Restock fluid, cloths, and the brush pen for your cleaning kit.", "补充清洁液、清洁布与笔刷。"],
            ["Mini Ball Head", "Tilt and rotate to level the frame, then lock it in for the take.", "倾斜旋转调平画面后锁定，可加装在三脚架与手机夹之间。"],
            ["Magnetic Mount", "Attach and remove the phone in one motion for quick setup.", "磁吸一键拆装手机，适合桌面演示与参考观看。"],
            ["Microfiber 3-Pack", "Three spare cloths for dust, smudges, and fingerprints on lenses and screens.", "三片备用软布，用于镜头与屏幕的灰尘、污迹与指纹擦拭。"],
            ["Shot List Cards", "Four-shot prompt sequence paired with the ShotStarter AI script draft.", "四镜提示卡，配套 ShotStarter AI 脚本草稿使用。"],
        ])

    body(doc, "FAQ 问答对照 / Product FAQ (EN → 中文)", size=11, bold=True, color=NAVY)
    make_table(doc,
        ["Product", "Question (EN)", "中文释义"],
        [
            ["Tripod", "Will it fit my phone?", "能否适配我的手机？（具体宽度范围待核实）"],
            ["Tripod", "Can I take it outdoors?", "能否带到户外使用？（需放置在平整稳定表面）"],
            ["Tripod", "Does it come with a carry bag?", "是否附带收纳包？（以包装清单为准）"],
            ["Stand", "Will the stand fit my phone?", "支架能否适配我的手机？（常见机型，宽度范围待核实）"],
            ["Stand", "Can I charge my phone while it's on the stand?", "手机放在支架上时能否充电？"],
            ["Stand", "Is the base stable?", "底座是否稳固？（重量与材质待核实）"],
            ["Cleaning Kit", "Is it safe for my phone camera?", "对手机摄像头是否适用？（适用表面清单待核实）"],
            ["Cleaning Kit", "What is included in the set?", "套装内包含什么？（构成待实物确认）"],
            ["Cleaning Kit", "Does it include cleaning liquid?", "是否包含清洁液？（是否包含、容量与成分待核实）"],
        ])

    body(doc, "政策术语对照 / Policy Terms (EN → 中文)", size=11, bold=True, color=NAVY)
    make_table(doc,
        ["English term", "中文含义"],
        [
            ["Return window", "可退货期限（自签收起算）"],
            ["Restocking fee", "演示默认无；正式营业前法务复核"],
            ["Original payment method", "原路退回的支付方式"],
            ["Refund", "退款"],
            ["Exchange", "换货"],
            ["Consent", "同意（订阅邮件或数据处理）"],
            ["Unsubscribe", "退订"],
            ["Personal data", "个人数据"],
            ["Service provider", "服务商（支付、物流、邮件等）"],
            ["Promo code", "优惠码"],
            ["Free standard shipping", "标准配送免邮"],
            ["Out of stock", "缺货"],
            ["Secure checkout", "安全结账（通用表述，不代表某项认证）"],
        ])

    body(doc, "折扣码 / Codes", size=11, bold=True, color=NAVY)
    bullets(doc, [
        "NEWCREATOR10：新客首单 10% off；演示有效期为演练期间；每客一次；每单一码，不与捆绑码叠加；作用 Shop 集合全部单件，两个捆绑 SPU 排除。First order 10% off; valid during the drill period; once per customer; one code per order, no stack with the bundle code; applies to all single items in the Shop collection; both bundle SPUs excluded.",
        "STARTERKIT：15% 优惠码，分别作用两个独立捆绑 SPU：Starter Kit $44.97 → $38.22（省 $6.75）；Pro Creator Kit $62.96 → $53.52（省 $9.44）。15% code applied to each standalone bundle SPU only: Starter Kit $44.97 → $38.22 (save $6.75); Pro Creator Kit $62.96 → $53.52 (save $9.44).",
    ], size=10)

    body(doc, "免邮 / Free Shipping", size=11, bold=True, color=NAVY)
    body(doc, "美国标准运费 $4.99；满 $35 免标准运费（演示配置；门槛默认按折后小计计算，以后台实测为准）。US standard $4.99; free standard shipping over $35 (demo; threshold defaults to post-discount subtotal, verify against backend).", size=10)

    body(doc, "ShotStarter 玩法 / AI Content Assistant", size=11, bold=True, color=NAVY)
    body(doc, "按平台、商品类型、卖点生成 15 秒脚本、四镜分镜与发布文案；草稿由创作者自行审核。15-second script, four-shot storyboard, and caption drafts by platform/product/selling point; drafts are reviewed by the creator.", size=10)

    body(doc, "7 天挑战 / 7-Day Shooting Challenge", size=11, bold=True, color=NAVY)
    body(doc, "Day1–7：选题 → 脚本 → 布机 → 拍摄 → 剪辑 → 文案 → 发布；邮箱留资参与；另有 Day8+ nurture 邮件草案、清洁套装复购钩子草案与流失唤醒邮件草案。Signup by email; the Day8+ nurture sequence, refill hook, and win-back email are draft copy for review.", size=10)

    body(doc, "演练店 / Demo Store Access", size=11, bold=True, color=NAVY)
    body(doc, "地址 / URL: ygtokenstemple.myshoplaza.com　　密码 / Password: 【口令已脱敏】", size=10)

    body(doc, "诚实边界 / Honesty Boundary", size=11, bold=True, color=NAVY)
    body(doc, "价格与折扣均为演示配置；未虚构参数、销量、评价、认证、库存或到货承诺；AI 输出为草稿；所有占位项以上线前核实为准。Prices and offers are demo configs; no fabricated specs, reviews, certifications, stock, or delivery promises; AI outputs are drafts; placeholders pending verification.", size=10)

    doc.save(CARD)
    print("saved card:", CARD)


if __name__ == "__main__":
    os.makedirs(BASE, exist_ok=True)
    build_brand()
    build_card()
