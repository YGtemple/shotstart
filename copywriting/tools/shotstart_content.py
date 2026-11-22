# -*- coding: utf-8 -*-
"""ShotStart copy package: shared content data source.
Consumer-facing copy is English; operator notes are Chinese and prefixed as notes.
"""

PAGES = {}

CONTACT_EMAIL = "1744059451@qq.com"


def cta_blocks(kit_button="Add to Creator Starter Kit"):
    return [
        ("h2", "Add to Cart"),
        ("bullets", [
            "Primary button: Add to Cart",
            "Secondary button: " + kit_button,
        ]),
    ]


def trust_blocks():
    return [
        ("h2", "Shopping Trust (generic; no certification claims)"),
        ("bullets", [
            "Secure checkout: Payments are processed on the store's secure checkout page.",
            "Return terms: see the Return & Refund Policy for the confirmed return window.",
            "ShotStarter outputs are drafts you review and approve before posting.",
            "No hidden fees: the price shown at checkout is what you pay, before any applicable shipping.",
            "Questions? Reach us at " + CONTACT_EMAIL + ".",
        ]),
        ("note", "Platform fact (INTERNAL only): the drill store is hosted on Shoplazza; the public checkout line does not name the platform. Strip any platform mention from the live store per the launch cleanup checklist."),
    ]


def _starter_entry():
    return [
        ("h2", "Bundle Entry"),
        ("p", "Pair this with the other Creator Starter Kit items. What's in the kit: Adjustable Phone Tripod ($19.99), "
              "Desktop Phone Stand ($14.99), Lens Cleaning Kit ($9.99). Kit price $44.97 — use code STARTERKIT at checkout: $38.22. You save $6.75."),
        ("bullets", [
            "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        ]),
        ("setup", ["Demo configuration: the kit is a standalone SPU listed at $44.97; STARTERKIT (15% off) applies to that SPU only; "
                   "code price $38.22; savings $6.75 (44.97 − 38.22), rounded to the cent. "
                   "Confirm bundle discount, inventory, and eligibility before launch. No compare-at reference price or strike-through field is used."]),
    ]


def _pro_entry():
    return [
        ("h2", "Bundle Entry"),
        ("p", "Pair this with the other Pro Creator Kit items. What's in the kit: Adjustable Phone Tripod ($19.99), "
              "Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — "
              "use code STARTERKIT at checkout: $53.52. You save $9.44."),
        ("bullets", [
            "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        ]),
        ("setup", ["Demo configuration: the Pro Creator Kit is a standalone SPU listed at $62.96; STARTERKIT (15% off) applies to that SPU only; "
                   "code price $53.52; savings $9.44 (62.96 − 53.52), rounded to the cent. "
                   "Confirm bundle discount, inventory, and eligibility before launch. No compare-at reference price or strike-through field is used."]),
    ]


def bundle_blocks(kit="starter"):
    if kit == "starter":
        return _starter_entry()
    if kit == "pro":
        return _pro_entry()
    if kit == "refill":
        return [
            ("h2", "Bundle Entry"),
            ("p", "This refill is sold as a single item. Bundle sets are listed in the Creator Kits collection."),
        ]
    return [
        ("h2", "Bundle Entry"),
        ("p", "This item is sold as a single item. Bundle sets are listed in the Creator Kits collection."),
    ]


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
PAGES["home.txt"] = [
    ("h1", "Home Page Copy"),
    ("note", "本页为 Shoplazza 首页各区块文案；面向消费者的英文内容可直接复制，括号内中文为操作者备注，不上架。"),

    ("h2", "Announcement Bar (Top Banner)"),
    ("p", "Free standard shipping on US orders over $35."),
    ("price", "Demo configuration: free-shipping threshold $35; standard flat rate $4.99. Confirm before launch."),
    ("p", "Alternate announcement: New creators get 10% off their first order with code NEWCREATOR10."),
    ("price", "Demo configuration: 10% off welcome code NEWCREATOR10 for first orders; applies to all single items in the Shop collection; both bundle SPUs (Creator Starter Kit and Pro Creator Kit) are excluded. Confirm discount terms before launch."),
    ("p", "评委导览：商品价格、挑战闭环与参观路线一览。Judge Guide"),
    ("note", "例外说明：本行为店内唯一面向中文评委的入口链接，指向独立中文导览页 Judge Guide；除该页外，其余前台页面均为英文。Judge Guide 仅供评审使用，正式店上线前可移除该条。"),

    ("h2", "Hero Section"),
    ("setup", ["Layout: split hero — copy on the left, hero image on the right. Hero image slot: hero-banner.png (see shotstart-visuals)."]),
    ("p", "Headline: Your first shot starts here."),
    ("p", "Subhead: ShotStart helps beginner creators and small shop owners film cleaner videos, write smarter captions, and stay consistent — with simple phone gear and the ShotStarter AI content assistant."),
    ("bullets", [
        "Primary CTA button: Shop All Gear",
        "Secondary CTA button: Join the 7-Day Shooting Challenge",
    ]),

    ("h2", "Trust Row"),
    ("bullets", [
        "Policy links: Shipping Policy · Return & Refund Policy · Privacy Policy · Terms of Service",
    ]),

    ("h2", "Home Trust Signals"),
    ("p", "ShotStarter AI outputs are drafts you review before posting · Beginner-friendly plain-language guidance · Responsive support by email."),

    ("h2", "Brand Value Proposition (3 pillars)"),
    ("bullets", [
        "Made for beginners: No jargon, no complicated setup. Simple gear and plain-language AI prompts help you publish your first video faster.",
        "Gear that works with your phone: Designed around common smartphone sizes and everyday short-video setups; confirmed compatibility details are listed on each product page.",
        "AI that stays on your side: ShotStarter turns your platform, product, and main selling point into a 15-second script, a four-shot storyboard, and publish-ready caption copy.",
    ]),
    ("setup", [
        "Pending before launch: exact phone compatibility range (confirmed on each product page). [待确认: exact phone compatibility range]",
    ]),

    ("h2", "Product Showcase (short cards)"),
    ("p", "Adjustable Phone Tripod: Steady shots, hands free. Adjustable framing for talking-head videos, product demos, and on-location clips."),
    ("p", "Desktop Phone Stand: A clean home for your phone on the desk. Keeps your device upright and within reach for demos, streams, and live clips."),
    ("p", "Lens Cleaning Kit: Keep smudges and dust off your lenses. A compact cleaning set for phones, cameras, and accessory lenses."),
    ("p", "Creator Carry Case: A portable case to keep your tripod, stand, and small accessories together."),
    ("p", "Folding Reflector: Soften and fill light for face and product clips."),
    ("p", "Backdrop Cloth: A plain background for product and talking-head clips."),
    ("p", "Extension Pole: Reach overhead and higher-angle shots for selfie and group clips."),
    ("p", "Lens Cleaning Refill: Restock fluid, cloths, and the brush pen for your cleaning kit."),
    ("p", "Mini Ball Head: Level and lock the frame between shots with one twist."),
    ("p", "Magnetic Mount: Snap your phone on and off for quick desk setups."),
    ("p", "Microfiber 3-Pack: Three spare soft cloths for between-take lens and screen cleaning."),
    ("p", "Shot List Cards: Four-shot prompt cards paired with your ShotStarter script draft."),

    ("h2", "Creator Starter Kit Bundle Card"),
    ("p", "Section title: The Starter Kit: your first filming setup in one kit."),
    ("bullets", [
        "What's in the kit: Adjustable Phone Tripod ($19.99), Desktop Phone Stand ($14.99), Lens Cleaning Kit ($9.99).",
        "Kit price $44.97 — use code STARTERKIT at checkout: $38.22. You save $6.75.",
        "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        "Card CTA button: View the kit",
    ]),
    ("setup", ["Demo configuration: the kit is a standalone SPU listed at $44.97; STARTERKIT (15% off) applies to that SPU only; code price $38.22, savings $6.75 (44.97 − 38.22). No compare-at reference price or strike-through field is shown."]),

    ("h2", "Pro Creator Kit Bundle Card"),
    ("p", "Section title: The Pro Kit: stable framing, height, angle control, and a carry case for the next level."),
    ("bullets", [
        "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99).",
        "Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44.",
        "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        "Card CTA button: View the kit",
    ]),
    ("setup", ["Demo configuration: Pro Creator Kit standalone SPU listed at $62.96; STARTERKIT (15% off) applies to that SPU only; code price $53.52, savings $9.44 (62.96 − 53.52). No compare-at reference price or strike-through field is shown."]),

    ("h2", "ShotStarter AI Block"),
    ("p", "Section title: Meet ShotStarter, your AI content assistant."),
    ("p", "Body: Tell ShotStarter your platform (TikTok, Instagram Reels, YouTube Shorts, or another), your product type, and the one selling point you want to lead with. It drafts a 15-second script, lays out a four-shot storyboard, and suggests a caption and publish-ready text you can edit before posting."),
    ("bullets", [
        "15-second script draft tailored to your platform and product",
        "Four-shot storyboard: hook, close-up, demonstration, closing line",
        "Caption and publish-ready copy to review and personalize",
    ]),
    ("note", "合规提示：ShotStarter 输出为草稿，发布前由创作者自行审核修改；页面不得暗示 AI 生成内容可直接免责或保证效果。"),

    ("h2", "7-Day Shooting Challenge Block"),
    ("p", "Section title: Join the 7-Day Shooting Challenge."),
    ("p", "Body: One small filming task each day for seven days. Sign up with your email to receive the day-by-day tasks, prompts, and ShotStarter template suggestions."),
    ("bullets", ["CTA button: Join the challenge"]),
    ("setup", ["Lead form: email signup (see challenge.txt for fields and thank-you message)"]),

    ("h2", "Email Popup"),
    ("p", "Popup headline: Your first discount is one click away."),
    ("p", "Popup body: Submit to get your welcome code NEWCREATOR10."),
    ("bullets", ["Button: Save my spot"]),
    ("setup", ["Form field: Email"]),
    ("bullets", [
        "Fine print: By subscribing, you agree to receive marketing emails from ShotStart. You can unsubscribe at any time.",
    ]),
    ("price", "Demo configuration: first-order discount applied after signup; confirm rate, minimum order, and expiry before launch."),

    ("h2", "Footer Brand Blurb"),
    ("p", "ShotStart builds simple filming gear and the ShotStarter AI content assistant for beginner short-video creators and small shop owners in the US market. Your first shot starts here."),
    ("bullets", [
        "Footer links: Shop, About, Contact, Shipping Policy, Return & Refund Policy, Privacy Policy, Terms of Service",
    ]),
    ("setup", [
        "Footer note: Prices and offers on this store are demo configurations pending final confirmation.",
    ]),
]

# ---------------------------------------------------------------------------
# SHOP / COLLECTION PAGE (new)
# ---------------------------------------------------------------------------
PAGES["shop.txt"] = [
    ("h1", "Shop / Collection Page Copy"),

    ("h2", "Collections"),
    ("bullets", [
        "All Gear: Every creator item in one collection.",
        "Creator Kits: Bundled gear sets — the Creator Starter Kit and the Pro Creator Kit.",
    ]),

    ("h2", "Sorting"),
    ("bullets", [
        "Sort options: Featured, Price: Low to High, Price: High to Low, Newest.",
    ]),
    ("setup", [
        "Default collection sort and product order to be configured in the store admin. [待确认: default sorting rule]",
    ]),

    ("h2", "Product Cards"),
    ("bullets", [
        "Adjustable Phone Tripod — $19.99. Steady, hands-free framing for talking-head clips and product demos.",
        "Desktop Phone Stand — $14.99. Keep your phone upright on the desk for demos and live clips.",
        "Lens Cleaning Kit — $9.99. A compact cleaning set to keep lenses clear.",
        "Creator Carry Case — $12.99. A portable case to keep gear and small accessories together.",
        "Folding Reflector — $10.99. Soften and fill light for face and product clips.",
        "Backdrop Cloth — $13.99. A plain background for product and talking-head clips.",
        "Extension Pole — $16.99. Reach overhead and higher-angle shots for selfie and group clips.",
        "Lens Cleaning Refill — $7.99. Restock fluid, cloths, and the brush pen for your cleaning kit.",
        "Mini Ball Head — $12.99. Level and lock the frame between shots with one twist.",
        "Magnetic Mount — $11.99. Snap your phone on and off for quick desk setups.",
        "Microfiber 3-Pack — $6.99. Three spare soft cloths for between-take lens and screen cleaning.",
        "Shot List Cards — $8.99. Four-shot prompt cards paired with your ShotStarter script draft.",
    ]),
    ("setup", [
        "Cleaning kit demonstrated composition is a demo configuration; confirm contents before launch.",
    ]),

    ("h2", "Bundle SPU Card (Creator Starter Kit)"),
    ("p", "Card description: Creator Starter Kit — steady framing, a desk stand, and a compact lens cleaning set together."),
    ("p", "What's in the kit: Adjustable Phone Tripod ($19.99), Desktop Phone Stand ($14.99), Lens Cleaning Kit ($9.99). Kit price $44.97 — use code STARTERKIT at checkout: $38.22. You save $6.75."),
    ("bullets", [
        "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        "Card CTA: View the kit",
    ]),
    ("setup", ["Demo configuration: standalone bundle SPU listed at $44.97; STARTERKIT (15% off) applies to that SPU only; code price $38.22, savings $6.75 (44.97 − 38.22). Confirm discount, inventory, and eligibility before launch. No compare-at reference price or strike-through field is used."]),

    ("h2", "Bundle SPU Card (Pro Creator Kit)"),
    ("p", "Card description: Pro Creator Kit — a tripod, extension pole, mini ball head, and carry case for the next level of setup."),
    ("p", "What's in the kit: Adjustable Phone Tripod ($19.99), Extension Pole ($16.99), Mini Ball Head ($12.99), Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44."),
    ("bullets", [
        "STARTERKIT applies to this kit only; it cannot be combined with other codes.",
        "Card CTA: View the kit",
    ]),
    ("setup", ["Demo configuration: standalone bundle SPU listed at $62.96; STARTERKIT (15% off) applies to that SPU only; code price $53.52, savings $9.44 (62.96 − 53.52). Confirm discount, inventory, and eligibility before launch. No compare-at reference price or strike-through field is used."]),
]

# ---------------------------------------------------------------------------
# PRODUCT 1: TRIPOD
# ---------------------------------------------------------------------------
PAGES["product-tripod.txt"] = [
    ("h1", "Product Detail: Adjustable Phone Tripod"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Adjustable Phone Tripod — Steady, Hands-Free Framing for Short Videos"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Adjustable height and angle for varied shooting setups.",
        "Phone clamp fits common smartphone sizes.",
        "Hands-free shooting for talking-head clips, product demos, and outdoor clips.",
        "Foldable, portable design for indoor and on-location use.",
        "Feet designed for placement on flat surfaces.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: compatible phone width range]; [待确认: height range / tilt range]; [待确认: main material, e.g., aluminum alloy / ABS plastic]; [待确认: foot material]; [待确认: folded length]; [待确认: net weight]; [待确认: any included mount adapter or carry bag]; [待确认: any accessory such as a carry bag or adapter].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Adjustable Phone Tripod is built for creators who want steady framing without a complicated rig. Set your phone in the clamp, adjust the height and angle to your shot, and film hands-free. It suits short talking-head videos, product close-ups, and casual on-location clips. Exact dimensions, materials, and compatibility details will be updated after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Adjustable phone tripod"],
        ["Clamp compatibility", "Common smartphone sizes"],
        ["Adjustability", "Height and angle adjustable"],
        ["Placement surface", "Flat, stable surfaces"],
        ["Carry design", "Portable, foldable design"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Adjustable phone tripod",
    ]),
    ("p", "The phone clamp/mount details are [待确认: included mount details]. Any additional accessory, such as a carry bag or adapter, is listed once the box contents are confirmed."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Talking-head introductions and talking points filmed at home",
        "Product demos and unboxing clips on a tabletop or floor",
        "On-location clips outdoors or at an event, placed on flat ground",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "Will it fit my phone?"),
    ("faq_a", "The clamp fits common smartphone sizes. The exact compatible width range is [待确认: compatible phone width range]."),
    ("faq_q", "Can I take it outdoors?"),
    ("faq_a", "The tripod is designed for portable, on-location use on flat, stable surfaces; avoid unstable or sloped ground."),
    ("faq_q", "Does it come with a carry bag?"),
    ("faq_a", "Whether a carry bag is included is [待确认: carry bag inclusion]. Check the What's in the Box section for the confirmed contents."),

    ("h2", "Pricing"),
    ("price", "Demo price: $19.99 — Demo configuration, confirm before launch. Bundle pricing available in the Creator Starter Kit."),
] + cta_blocks() + trust_blocks() + bundle_blocks()

# ---------------------------------------------------------------------------
# PRODUCT 2: DESKTOP STAND
# ---------------------------------------------------------------------------
PAGES["product-stand.txt"] = [
    ("h1", "Product Detail: Desktop Phone Stand"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位。"),

    ("h2", "Product Title"),
    ("p", "Desktop Phone Stand — Keep Your Phone Upright on Your Desk"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Holds your phone upright at a usable desk angle.",
        "Compact footprint for desks, countertops, and small workspaces.",
        "Designed for steady desk placement during demos, live clips, and reference viewing.",
        "Holder compatible with common smartphone sizes.",
        "Cable-friendly open design.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: compatible phone width range]; [待确认: angle range]; [待确认: main material, e.g., ABS plastic / metal]; [待确认: base material / non-slip pad]; [待确认: charging cutout]; [待确认: net weight].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Desktop Phone Stand gives your phone a steady home right on the desk. Keep your device upright while you film product demos, follow along with a recipe or tutorial, or prepare for a live short clip. Its compact footprint suits small workspaces, and the open design leaves room for everyday use. Exact dimensions, materials, and compatibility will be confirmed after final verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Desktop phone stand"],
        ["Holder compatibility", "Common smartphone sizes"],
        ["Angle adjustability", "Adjustable viewing/tilt angle"],
        ["Base", "Desk base"],
        ["Cable access", "Open design for charging cable"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Desktop phone stand",
    ]),
    ("p", "A non-slip pad or any additional accessory is [待确认: any non-slip pad or accessory]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Product demos shot from a desk or countertop",
        "Live streams and Q&A clips with the phone held steady",
        "Keeping reference videos, scripts, or captions within view while filming",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "Will it fit my phone?"),
    ("faq_a", "It holds common smartphone sizes. The exact width range is [待确认: compatible phone width range]."),
    ("faq_q", "Can I charge my phone while it's on the stand?"),
    ("faq_a", "The open design allows cable access. The cutout position is [待确认: charging cutout details]."),
    ("faq_q", "Is the base stable?"),
    ("faq_a", "The base is designed for desk-level stability. Its net weight and material are [待确认: net weight / base material]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $14.99 — Demo configuration, confirm before launch. Bundle pricing available in the Creator Starter Kit."),
] + cta_blocks() + trust_blocks() + bundle_blocks()

# ---------------------------------------------------------------------------
# PRODUCT 3: CLEANING KIT
# ---------------------------------------------------------------------------
PAGES["product-cleaning-kit.txt"] = [
    ("h1", "Product Detail: Lens Cleaning Kit"),
    ("note", "清洁液成分、容量、适用表面属于需核实信息；未确认前一律占位，不得写认证或功效承诺。四件组成为演示配置，上线前与实物核对。"),

    ("h2", "Product Title"),
    ("p", "Lens Cleaning Kit — Keep Phone and Camera Lenses Clear"),
    ("p", "Contents are listed in What's in the Box."),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "A compact cleaning set for phone and camera lenses; contents listed in What's in the Box.",
        "For dust, smudges, and fingerprints on phone lenses, compact camera lenses, and accessory lenses.",
    ]),
    ("setup", [
        "Demo composition, pending physical confirmation: cleaning fluid bottle, air blower, cleaning cloth, lens pen. Do not publish fixed contents or material names until the physical product is verified.",
        "Pending before launch: [待确认: approved surface list]; [待确认: included contents list]; [待确认: blower/pen material, cloth material]; [待确认: liquid volume, kit dimensions].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "A clear lens makes your clips look cleaner. The Lens Cleaning Kit gathers the basics for dusting and wiping phone, camera, and accessory lenses. It is compact enough to keep in your filming bag. Final contents, materials, and any liquid ingredients will be confirmed after final verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Lens cleaning kit"],
        ["Compatible surfaces", "Phone lenses, compact camera lenses, accessory lenses"],
     ]),

    ("h2", "What's in the Box"),
    ("p", "A compact cleaning set for phone and camera lenses. Contents will be listed here after final confirmation."),
    ("setup", [
        "Demo composition (confirm against the physical product before launch): cleaning fluid bottle, air blower, cleaning cloth, lens pen.",
        "Final included items, cloth material, and fluid volume/ingredients: [待确认: included contents, cloth material, liquid volume and ingredients].",
    ]),
    ("note", "图注口径：商品图注只写商品与用途，不标注生成方式或演示性质；上线前替换为真实在售商品图。"),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Wiping fingerprints off a phone lens before filming",
        "Dusting a compact camera or accessory lens between takes",
        "Traveling with a small cleaning set in a creator bag",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "Is it safe for my phone camera?"),
    ("faq_a", "The kit is designed for lens surfaces; avoid pressing or rubbing hard. The approved surface list is [待确认: compatible surface types]."),
    ("faq_q", "What is included in the set?"),
    ("faq_a", "The set is a compact cleaning set; contents are listed in What's in the Box. Contents, cloth material, and fluid volume are [待确认: included contents, cloth material, liquid volume and ingredients]."),
    ("faq_q", "Does it include cleaning liquid?"),
    ("faq_a", "Whether cleaning liquid is included, along with its volume and ingredients, is [待确认: liquid inclusion, volume, and ingredients]; check the contents list before ordering."),

    ("h2", "Pricing"),
    ("price", "Demo price: $9.99 — Demo configuration, confirm before launch. Bundle pricing available in the Creator Starter Kit."),
] + cta_blocks() + trust_blocks() + bundle_blocks()

# ---------------------------------------------------------------------------
# PRODUCT 4: CREATOR CARRY CASE
# ---------------------------------------------------------------------------
PAGES["product-carry-case.txt"] = [
    ("h1", "Product Detail: Creator Carry Case"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Creator Carry Case — Keep Your Gear Together on the Go"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "A carry case for the tripod, stand, and small filming accessories.",
        "Compact, portable design for home storage and on-location shoots.",
        "Internal organization is listed in What's in the Box.",
        "Built around common creator gear setups.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: carry case dimensions and material]; [待确认: net weight]; [待确认: any accessory such as a carry bag or adapter].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Creator Carry Case keeps your phone gear and small accessories in one place between shoots. Pack the tripod, stand, cleaning supplies, and clips for a session, then stow the case at home or take it to a location. Exact dimensions, material, and fit details will be updated after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Gear carry case"],
        ["Carry design", "Portable case"],
        ["Organization", "Internal pockets/compartments listed in What's in the Box"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Creator carry case",
    ]),
    ("p", "The included pockets, dividers, and any accessory strap are [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Packing gear for a home or outdoor shoot",
        "Storing tripod, stand, and small accessories between sessions",
        "Moving gear between locations without loose pieces",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "Will it fit the tripod and stand?"),
    ("faq_a", "The case is built around common creator gear setups. Exact fitted dimensions are [待确认: carry case dimensions and material]."),
    ("faq_q", "What accessories fit inside?"),
    ("faq_a", "Internal pockets and compartments are listed in What's in the Box. Any additional accessory is [待确认: included contents list]."),
    ("faq_q", "Is the case water resistant?"),
    ("faq_a", "Water resistance and fabric coating are [待确认: main material, e.g., aluminum alloy / ABS plastic]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $12.99 — Demo configuration, confirm before launch. Bundle pricing available in the Pro Creator Kit."),
] + cta_blocks("Add to Pro Creator Kit") + trust_blocks() + bundle_blocks("pro")

# ---------------------------------------------------------------------------
# PRODUCT 5: FOLDING REFLECTOR
# ---------------------------------------------------------------------------
PAGES["product-reflector.txt"] = [
    ("h1", "Product Detail: Folding Reflector"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Folding Reflector — Soften and Fill Light for Clips"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Fills harsh shadows and softens light on a face or product.",
        "Folds down for storage in a gear bag.",
        "Handheld or held by a second person during a shot.",
        "Suited to talking-head and product close-up clips.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: reflector diameter and fabric]; [待确认: main material, e.g., aluminum alloy / ABS plastic]; [待确认: net weight].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Folding Reflector helps bounce light back onto your subject when the room light is flat or one-sided. Hold it near the product or face to open up shadows, then fold it flat for storage between takes. Exact diameter, fabric, and weight will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Folding light reflector"],
        ["Use", "Fill light for face and product clips"],
        ["Storage", "Folds flat for a gear bag"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Folding reflector",
    ]),
    ("p", "Any storage pouch or carry strap is [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Filling shadow on a talking-head clip at home",
        "Softening product close-up lighting near a window",
        "On-location shots where natural light is uneven",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What size and surface does it have?"),
    ("faq_a", "Diameter and surface fabric are [待确认: reflector diameter and fabric]."),
    ("faq_q", "How do I store it?"),
    ("faq_a", "The reflector folds flat for bag storage. The included storage pouch, if any, is listed in What's in the Box."),
    ("faq_q", "Does it come with a stand?"),
    ("faq_a", "A stand or mounting clip is not listed in the basic contents; any included accessory is [待确认: included contents list]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $10.99 — Demo configuration, confirm before launch. Sold as a single item; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("single")

# ---------------------------------------------------------------------------
# PRODUCT 6: BACKDROP CLOTH
# ---------------------------------------------------------------------------
PAGES["product-backdrop.txt"] = [
    ("h1", "Product Detail: Backdrop Cloth"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Backdrop Cloth — A Simple Background for Product and Talking-Head Clips"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "A plain background for product and talking-head clips.",
        "Hangs on common stands, clamps, or a wall-mounted setup.",
        "Easy to hang and fold for storage between sessions.",
        "One neutral surface behind the subject.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: backdrop dimensions and fabric]; [待确认: main material, e.g., aluminum alloy / ABS plastic].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Backdrop Cloth gives your clip a clean, uncluttered background instead of a busy room. Hang it behind the product or yourself, frame the shot, and film. Exact size, fabric, and color will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Backdrop cloth"],
        ["Use", "Background for product and talking-head clips"],
        ["Mounting", "Common stands, clamps, or wall setup"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Backdrop cloth",
    ]),
    ("p", "Any included clip, rod, or storage bag is [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Product shots with a plain background",
        "Talking-head clips filmed at a desk",
        "Recurring setup reused across daily challenge videos",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What size is the cloth?"),
    ("faq_a", "Dimensions and fabric are [待确认: backdrop dimensions and fabric]."),
    ("faq_q", "What color is it?"),
    ("faq_a", "The available color is listed after final product verification; exact dimensions, fabric, and finish are being finalized."),
    ("faq_q", "How do I hang it?"),
    ("faq_a", "The cloth works with common stands or clamps. Any included mounting accessory is [待确认: included contents list]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $13.99 — Demo configuration, confirm before launch. Sold as a single item; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("single")

# ---------------------------------------------------------------------------
# PRODUCT 7: EXTENSION POLE
# ---------------------------------------------------------------------------
PAGES["product-extension-pole.txt"] = [
    ("h1", "Product Detail: Extension Pole"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Extension Pole — Reach Higher Angles for Selfie and Group Clips"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Extends your reach for overhead or higher-angle shots.",
        "Handheld for selfie-style clips or mounted on a stand.",
        "Collapses for transport in a gear bag.",
        "Phone holder fits common smartphone sizes.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: pole extended and collapsed length]; [待确认: main material, e.g., aluminum alloy / ABS plastic]; [待确认: net weight].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Extension Pole lifts your phone above eye level for top-down, overhead, or wider group clips. Extend the length to your shot, hold it or fix it to a stand, and collapse it afterward. Exact extended and collapsed length, material, and weight will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Extension pole with phone holder"],
        ["Use", "Overhead, higher-angle, and selfie-style clips"],
        ["Storage", "Collapses for a gear bag"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Extension pole",
    ]),
    ("p", "Any included mount adapter or carry strap is [待确认: any included mount adapter or carry bag]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Overhead product arrangement shots",
        "Group clips where one phone must reach the whole frame",
        "Higher-angle talking-head setup on a stand",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "How long does it extend?"),
    ("faq_a", "Extended and collapsed lengths are [待确认: pole extended and collapsed length]."),
    ("faq_q", "Does it fit my phone?"),
    ("faq_a", "The holder fits common smartphone sizes. The exact compatible width range is [待确认: compatible phone width range]."),
    ("faq_q", "What is the pole made of?"),
    ("faq_a", "Material and net weight are [待确认: main material, e.g., aluminum alloy / ABS plastic]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $16.99 — Demo configuration, confirm before launch. Bundle pricing available in the Pro Creator Kit."),
] + cta_blocks("Add to Pro Creator Kit") + trust_blocks() + bundle_blocks("pro")

# ---------------------------------------------------------------------------
# PRODUCT 8: LENS CLEANING REFILL
# ---------------------------------------------------------------------------
PAGES["product-cleaning-refill.txt"] = [
    ("h1", "Product Detail: Lens Cleaning Refill"),
    ("note", "清洁液成分、容量、布材、笔刷与件数属于需核实信息；未确认前一律占位，不得写认证或功效承诺。"),

    ("h2", "Product Title"),
    ("p", "Lens Cleaning Refill — Restock Fluid, Cloths, and the Brush Pen for Your Kit"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Refills the cleaning fluid, cloth, and brush pen for your Lens Cleaning Kit.",
        "For phone lenses, compact camera lenses, and accessory lenses.",
        "Contents and pack count are listed in What's in the Box.",
    ]),
    ("setup", [
        "Pending before launch: [待确认: included contents list]; [待确认: cloth material and count]; [待确认: liquid inclusion, volume, and ingredients].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Lens Cleaning Refill restocks the cleaning fluid, cloth, and brush pen you use between shoots, so your kit stays ready for the next clip. Exact counts, cloth material, and any fluid volume or ingredients will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Cleaning kit refill"],
        ["Compatible surfaces", "Phone lenses, compact camera lenses, accessory lenses"],
     ]),

    ("h2", "What's in the Box"),
    ("p", "The depicted refill includes a cleaning fluid bottle, a cloth, and a brush pen; final counts, materials, and fluid details are listed here after final confirmation."),
    ("setup", [
        "Final included items, cloth material, and fluid volume/ingredients: [待确认: included contents, cloth material, liquid volume and ingredients].",
    ]),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Replenishing the cloth and brush pen after repeated lens cleaning",
        "Refilling fluid for the existing Lens Cleaning Kit",
        "Keeping cleaning supplies on hand for on-location shoots",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What is included in the refill?"),
    ("faq_a", "The depicted refill includes a cleaning fluid bottle, a cloth, and a brush pen; exact count, cloth material, and fluid volume or ingredients are [待确认: included contents, cloth material, liquid volume and ingredients]."),
    ("faq_q", "Does it include cleaning fluid?"),
    ("faq_a", "The refill includes a cleaning fluid bottle; the fluid volume and ingredients are [待确认: liquid inclusion, volume, and ingredients]; check the contents list before ordering."),
    ("faq_q", "Does it work with the Lens Cleaning Kit?"),
    ("faq_a", "The refill is made for use with the Lens Cleaning Kit on phone, compact camera, and accessory lenses."),

    ("h2", "Pricing"),
    ("price", "Demo price: $7.99 — Demo configuration, confirm before launch. Sold as a single refill; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("refill")

# ---------------------------------------------------------------------------
# PRODUCT 9: MINI BALL HEAD
# ---------------------------------------------------------------------------
PAGES["product-mini-ball-head.txt"] = [
    ("h1", "Product Detail: Mini Ball Head"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Mini Ball Head — Level Your Frame in One Twist"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Tilt and rotate to level the frame, then lock it in for the take.",
        "Mounts between the tripod and phone clamp for steadier angle adjustments.",
        "Compact add-on that stays on the tripod between shoots.",
        "Mount size and compatibility details are listed in What's in the Box.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: ball head mount and thread details]; [待确认: main material, e.g., aluminum alloy / ABS plastic]; [待确认: net weight]; [待确认: included mount adapter].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Mini Ball Head sits between your tripod and phone clamp, so you can tilt, rotate, and level the frame with one twist instead of moving the whole tripod. It suits talking-head setups, product demos, and quick re-framing between takes. Exact mount size, materials, and hold details will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Mini ball head"],
        ["Use", "Angle adjustment on a tripod"],
        ["Mount", "Details confirmed in What's in the Box"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Mini ball head",
    ]),
    ("p", "Any included mount adapter or accessory is [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Re-leveling the frame between talking-head takes",
        "Adjusting the angle for product demos on a flat surface",
        "Moving between a desk setup and an outdoor flat-ground spot",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What tripod does it fit?"),
    ("faq_a", "The mount and thread details are [待确认: ball head mount and thread details]; check What's in the Box before ordering."),
    ("faq_q", "Does it replace the tripod?"),
    ("faq_a", "No. The ball head is an add-on that mounts to a tripod or stand; it does not replace the support itself."),
    ("faq_q", "What is it made of?"),
    ("faq_a", "Material and net weight are [待确认: main material, e.g., aluminum alloy / ABS plastic]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $12.99 — Demo configuration, confirm before launch. Bundle pricing available in the Pro Creator Kit."),
] + cta_blocks("Add to Pro Creator Kit") + trust_blocks() + bundle_blocks("pro")

# ---------------------------------------------------------------------------
# PRODUCT 10: MAGNETIC MOUNT
# ---------------------------------------------------------------------------
PAGES["product-magnetic-mount.txt"] = [
    ("h1", "Product Detail: Magnetic Mount"),
    ("note", "规格表仅写品类通用、可诚实描述的属性；凡需真实参数处一律用 [待确认: ...] 占位，上线前由运营替换，不得编造数值。"),

    ("h2", "Product Title"),
    ("p", "Magnetic Mount — Snap Your Phone On and Off in Seconds"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Attach and remove the phone in one motion for quick setup between clips.",
        "Holds the phone at a usable angle for desk demos and reference viewing.",
        "Compact footprint for desks, countertops, and small workspaces.",
        "Case and magnet compatibility are listed in What's in the Box.",
    ]),
    ("setup", [
        "Pending before launch (specification keys only; no values published until verified): [待确认: magnetic mount compatibility and case thickness]; [待确认: main material, e.g., ABS plastic / metal]; [待确认: base material / non-slip pad]; [待确认: net weight].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Magnetic Mount lets you attach and remove your phone without fumbling with clamps each time. It suits desk demos, recipe or tutorial follow-alongs, and quick reference checks between shoots. Exact compatibility, base material, and hold details will be confirmed after final verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Magnetic phone mount"],
        ["Use", "Desk-side phone holding for demos and reference viewing"],
        ["Compatibility", "Case and magnet details confirmed in What's in the Box"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Magnetic mount",
    ]),
    ("p", "Any included magnet plate or accessory is [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Product demos shot from a desk or countertop",
        "Keeping a reference video or script within view while filming",
        "Quick phone removal and remount between takes",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "Will it hold my phone with a case?"),
    ("faq_a", "Case thickness and magnet compatibility are [待确认: magnetic mount compatibility and case thickness]."),
    ("faq_q", "Does it work without a clamp?"),
    ("faq_a", "The mount uses a magnetic attachment; the included plates or pads are listed in What's in the Box."),
    ("faq_q", "What is the base made of?"),
    ("faq_a", "Base material and non-slip pad are [待确认: base material / non-slip pad]."),

    ("h2", "Pricing"),
    ("price", "Demo price: $11.99 — Demo configuration, confirm before launch. Sold as a single item; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("single")

# ---------------------------------------------------------------------------
# PRODUCT 11: MICROFIBER 3-PACK
# ---------------------------------------------------------------------------
PAGES["product-microfiber-3pack.txt"] = [
    ("h1", "Product Detail: Microfiber 3-Pack"),
    ("note", "清洁布材质、片数与适用表面属于需核实信息；未确认前一律占位，不得写认证或功效承诺。"),

    ("h2", "Product Title"),
    ("p", "Microfiber 3-Pack — Soft Cloths for Between-Take Cleaning"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Three spare cloths so one can stay in the cleaning kit while another handles touch-ups.",
        "For dust, smudges, and fingerprints on phone lenses and screens.",
        "Soft surface; approved use list is listed in What's in the Box.",
        "Pairs with the Lens Cleaning Kit for between-take lens care.",
    ]),
    ("setup", [
        "Pending before launch: [待确认: approved surfaces and cloth material]; [待确认: cloth size and count]; [待确认: cloth material and weave].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Microfiber 3-Pack gives you spare cloths so one can remain in the cleaning kit while another handles on-location touch-ups. Use it on phone lenses and screens between takes; exact cloth material, size, and pack count will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Cleaning cloth 3-pack"],
        ["Compatible surfaces", "Phone lenses and screens; approved list confirmed in What's in the Box"],
     ]),

    ("h2", "What's in the Box"),
    ("p", "Three soft cleaning cloths for between-take lens and screen care. Final material and size are listed here after final confirmation."),
    ("setup", [
        "Final cloth material, weave, size, and count: [待确认: cloth material and count].",
    ]),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Wiping smudges off a phone lens before a take",
        "Cleaning a phone screen between clips",
        "Keeping a spare cloth in the creator bag for on-location shoots",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What surfaces are the cloths for?"),
    ("faq_a", "Approved surfaces are [待确认: approved surfaces and cloth material]; check What's in the Box before use."),
    ("faq_q", "How many cloths are included?"),
    ("faq_a", "The pack count and cloth size are [待确认: cloth size and count]."),
    ("faq_q", "Does this replace the Lens Cleaning Kit?"),
    ("faq_a", "No. The cloths pair with the Lens Cleaning Kit; fluid and brush pen are sold separately in the kit and refill."),

    ("h2", "Pricing"),
    ("price", "Demo price: $6.99 — Demo configuration, confirm before launch. Sold as a single item; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("single")

# ---------------------------------------------------------------------------
# PRODUCT 12: SHOT LIST CARDS
# ---------------------------------------------------------------------------
PAGES["product-shot-list-cards.txt"] = [
    ("h1", "Product Detail: Shot List Cards"),
    ("note", "卡片件数、材质与语种清单属于需核实信息；未确认前一律占位。卡片为 ShotStarter AI 草稿的配套提示工具，不替代创作者自行审核。"),

    ("h2", "Product Title"),
    ("p", "Shot List Cards — Plan Your Four Shots Before You Press Record"),

    ("h2", "Selling Points (bullets)"),
    ("bullets", [
        "Four-shot prompt sequence: hook, close-up, demonstration, closing line.",
        "Each card pairs with the ShotStarter AI script and storyboard draft.",
        "Pocket-sized set to keep beside the setup during filming.",
        "Card count, material, and language list are listed in What's in the Box.",
    ]),
    ("setup", [
        "Pending before launch: [待确认: shot list cards contents and material]; [待确认: card size and count]; [待确认: printed language list].",
    ]),

    ("h2", "Description Paragraph"),
    ("p", "The Shot List Cards turn the ShotStarter draft into a physical check you can follow on set. Match each card to the script line and the four-shot storyboard, then tick off the hook, close-up, demonstration, and closing line before you publish. The cards are a companion to the ShotStarter AI assistant; they do not replace your own review of the draft. Exact card count, size, and material will be confirmed after final product verification."),

    ("h2", "Specifications"),
    ("table",
     ["Attribute", "Detail"],
     [
        ["Product type", "Shot list prompt card set"],
        ["Use", "On-set four-shot planning paired with the ShotStarter draft"],
        ["Contents", "Card count and material confirmed in What's in the Box"],
     ]),

    ("h2", "What's in the Box"),
    ("bullets", [
        "1 x Shot List card set",
    ]),
    ("p", "Card count, material, and any included ring or pocket case are [待确认: included contents list]."),

    ("h2", "Use Scenarios"),
    ("bullets", [
        "Planning the hook, close-up, demonstration, and closing line before filming",
        "Matching each shot to the ShotStarter script draft on set",
        "Keeping the shot order visible beside a desk or flat-ground setup",
    ]),

    ("h2", "FAQ"),
    ("setup", ["FAQ layout: question line as a bold standalone heading; answer paragraph below; collapsed by default on mobile; on desktop, open the first question and collapse the rest."]),
    ("faq_q", "What cards are included?"),
    ("faq_a", "The set follows the four-shot sequence — hook, close-up, demonstration, closing line; card count and material are [待确认: shot list cards contents and material]."),
    ("faq_q", "Do the cards replace the ShotStarter AI draft?"),
    ("faq_a", "No. The cards pair with the script and storyboard draft from ShotStarter; you still review and edit the draft before posting."),
    ("faq_q", "What languages are the cards printed in?"),
    ("faq_a", "The printed language list is [待确认: printed language list]; check What's in the Box before ordering."),

    ("h2", "Pricing"),
    ("price", "Demo price: $8.99 — Demo configuration, confirm before launch. Sold as a single item; bundle sets are listed in the Creator Kits collection."),
] + cta_blocks("Browse Creator Kits") + trust_blocks() + bundle_blocks("single")

# ---------------------------------------------------------------------------
# CART & CHECKOUT (new)
# ---------------------------------------------------------------------------
PAGES["cart-checkout.txt"] = [
    ("h1", "Cart & Checkout Microcopy"),

    ("h2", "Cart Page"),
    ("bullets", [
        "Add-to-cart confirmation: Added to cart.",
        "Quantity control: Qty minus / plus; each line shows product name, unit price, and line total.",
        "Continue shopping link: Continue browsing gear",
        "Checkout button: Secure Checkout",
        "Total recalculation: Your order total, taxes, and shipping are recalculated at checkout.",
    ]),

    ("h2", "Free Shipping Nudge"),
    ("p", "Nudge line: You're $X away from free US standard shipping."),
    ("p", "Example in-cart scenario: Tripod $19.99 + Stand $14.99 = $34.98 before any discount, $0.02 away. Add the Lens Cleaning Kit ($9.99) to reach the $35 free-shipping threshold."),
    ("setup", ["Insert the live gap ($X) at checkout; keep the tone neutral, no pressure wording."]),
    ("bullets", [
        "Suggestion card: Add the Lens Cleaning Kit — keep your lenses clear and unlock free standard shipping.",
    ]),
    ("setup", [
        "Threshold basis: the free-shipping threshold defaults to the post-discount subtotal; verify this basis against the live store backend before launch.",
    ]),

    ("h2", "Promo Code"),
    ("bullets", [
        "Input label: Promo code",
        "Apply button: Apply",
        "Applied message: Code applied.",
        "Invalid code message: This code isn't valid. Check the code and try again.",
        "Code rule: one code per order; STARTERKIT and NEWCREATOR10 cannot be combined.",
    ]),

    ("h2", "Stock and Address States"),
    ("bullets", [
        "Out of stock: This item is out of stock. Remove it from your cart or check back later.",
        "Address validation: Please review your address — one or more fields look incomplete. Check the highlighted field and try again.",
    ]),
    ("setup", [
        "Demo checkout notice (demo store only, do not publish on the live store): Demo checkout — no real payment is processed.",
    ]),

    ("h2", "Checkout Trust Copy (generic; no fabricated certifications)"),
    ("bullets", [
        "Secure checkout: Payments are processed on the store's secure checkout page.",
        "No hidden fees: The order total shown at checkout includes item price and any applicable shipping; taxes (if any) are shown before you pay.",
        "Support: Questions before ordering? Email " + CONTACT_EMAIL + ".",
    ]),

    ("h2", "Order Confirmation Page"),
    ("bullets", [
        "Heading: Thank you — your order is confirmed.",
        "Body: A confirmation and order number have been sent to your email. Please save your order number for support questions.",
        "Order number: your order number is shown on the confirmation page and sent to your email.",
        "Next steps: We'll send tracking details once your order ships.",
        "CTA: Continue shopping",
        "Support link: Contact us at " + CONTACT_EMAIL,
    ]),
]

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
PAGES["about.txt"] = [
    ("h1", "About ShotStart"),
    ("p", "ShotStart was built around a simple observation: the hardest part of starting short-video creation isn't talent — it's taking the first shot."),
    ("p", "New creators and small shop owners often have a real product and a real message, but they don't know how to set up a phone, frame a shot, or turn an idea into a caption. ShotStart pairs straightforward filming gear with the ShotStarter AI assistant to lower that barrier. We keep instructions plain, setups simple, and decisions in your hands."),
    ("p", "We don't promise overnight growth. We help you finish and publish that first video, then the next one — seven days at a time."),
    ("setup", [
        "Audience: beginner short-video creators and small shop owners in the US English-speaking market.",
        "Brand line: Your first shot starts here.",
    ]),
    ("note", "上线前补充：品牌创立时间、所在地、法律主体名称等 [待确认: founding date, location, legal entity name]。"),
]

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
PAGES["contact.txt"] = [
    ("h1", "Contact Us"),
    ("p", "Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note — we read every message and reply as soon as we can. For order questions, please include your order number so we can help faster."),

    ("h2", "Contact Form"),
    ("setup", [
        "Field: First name",
        "Field: Email",
        "Field: Order number (optional)",
        "Field: Subject",
        "Field: Message",
    ]),
    ("bullets", [
        "Checkbox: I agree to be contacted about my question.",
        "Submit button: Send message",
    ]),

    ("h2", "Other Contact"),
    ("p", "Email " + CONTACT_EMAIL + " — include your name, order number (if any), and a short description of the issue. Reference your order number in the subject line for a faster reply."),
    ("p", "We read every message and reply as soon as we can. This store is email-only; no physical mailing address is published."),
    ("note", "Demo configuration，正式营业前复核：回复渠道与时效按真实客服能力核实，不承诺固定回复时限；不公布实体地址。"),
]

# ---------------------------------------------------------------------------
# SHIPPING POLICY
# ---------------------------------------------------------------------------
PAGES["shipping-policy.txt"] = [
    ("h1", "Shipping Policy"),
    ("note", "Demo configuration，正式营业前复核：地区、费率、时效以正式营业前运营核实为准；前台行不出现演示/演练字样。"),
    ("p", "Last updated: 2026-11-20."),
    ("p", "This policy describes how orders are handled after checkout. Actual carrier times depend on destination and order availability; estimated delivery times are provided at checkout."),

    ("h2", "Order Processing"),
    ("p", "We process orders within 2 business days after payment. Orders placed on weekends or holidays are processed the next business day."),

    ("h2", "Shipping Destinations"),
    ("p", "We currently ship to the United States only. Cross-border shipping is not available from this store."),
    ("setup", ["Demo configuration，正式营业前复核：supported regions and cross-border availability to verify before launch."]),

    ("h2", "Shipping Rates"),
    ("p", "Standard shipping: US flat rate $4.99; free standard shipping on orders over $35."),
    ("setup", ["Demo configuration，正式营业前复核：rates, threshold, and excluded products to confirm before launch."]),

    ("h2", "Estimated Delivery"),
    ("p", "US standard delivery typically arrives in 5–8 business days after processing. Carrier timing may vary; the estimated delivery window is shown at checkout."),

    ("h2", "Order Tracking"),
    ("p", "A tracking number is emailed to you once your order ships."),

    ("h2", "Address Issues"),
    ("p", "It is the customer's responsibility to provide a correct shipping address. Re-routing or address correction after dispatch may incur additional carrier charges."),

    ("h2", "Customs and Duties"),
    ("p", "Because this store ships to the United States only, cross-border customs and duties do not apply to current orders."),

    ("h2", "Contact"),
    ("p", "Shipping questions: " + CONTACT_EMAIL),
]

# ---------------------------------------------------------------------------
# REFUND POLICY
# ---------------------------------------------------------------------------
PAGES["refund-policy.txt"] = [
    ("h1", "Return & Refund Policy"),
    ("note", "Demo configuration，正式营业前复核：退回窗口、费用与换货规则须对照适用消费者保护规则与法务意见核实；前台行不出现演示/演练字样。"),
    ("p", "Last updated: 2026-11-20."),

    ("h2", "Return Eligibility"),
    ("p", "You may request a return within 30 days of delivery. Items must be unused and in their original packaging."),
    ("setup", ["Demo configuration，正式营业前复核：return window and restocking fee to confirm with legal review."]),

    ("h2", "Non-Returnable Items"),
    ("p", "Opened hygiene-related items cannot be returned."),

    ("h2", "How to Request a Return"),
    ("p", "Contact " + CONTACT_EMAIL + " with your order number. We will send return instructions by email."),
    ("setup", ["Demo configuration，正式营业前复核：return warehouse address is withheld from public copy; arranged by email after the return request."]),

    ("h2", "Return Shipping Costs"),
    ("p", "Unless the item arrives damaged or defective, return shipping costs are paid by the customer."),

    ("h2", "Refunds"),
    ("p", "Approved refunds are issued to the original payment method within 5 business days after we receive the returned item. Original shipping charges are not refundable."),

    ("h2", "Exchanges"),
    ("p", "Exchanges are handled case by case. Contact " + CONTACT_EMAIL + " with your order number to check availability, any price difference, and return-shipping responsibility before a replacement is arranged."),

    ("h2", "Damaged or Defective Items"),
    ("p", "If an item arrives damaged or defective, contact us with photos within 30 days of delivery. We will arrange a replacement or refund according to eligibility."),

    ("note", "模板免责（INTERNAL，不上前台）：本政策为演示配置，正式营业前复核；退货窗口、费用、退货运费责任须对照适用消费者保护规则核实。"),
]

# ---------------------------------------------------------------------------
# PRIVACY POLICY
# ---------------------------------------------------------------------------
PAGES["privacy-policy.txt"] = [
    ("h1", "Privacy Policy"),
    ("note", "Demo configuration，正式营业前复核：采集范围、服务商、适用地区权利条款须经法务与技术配置核实；前台行不出现演示/演练字样。"),
    ("p", "Last updated: 2026-11-20."),

    ("h2", "What We Collect"),
    ("bullets", [
        "Contact and order information: name, email address, shipping address, and order details",
        "Challenge participation: email signup, chosen platform, and daily task interaction",
        "Usage data: email opens and store browsing behavior",
    ]),

    ("h2", "How We Use Information"),
    ("bullets", [
        "Process orders and provide customer support",
        "Send the 7-Day Shooting Challenge sequence and marketing emails, where you have consented",
        "Improve the store experience and product assortment",
    ]),

    ("h2", "Data Retention"),
    ("p", "Order records are kept for 24 months. Marketing consent remains active until 30 days after you unsubscribe; after that, the associated email is removed from marketing lists."),

    ("h2", "Email Marketing"),
    ("p", "Marketing emails are sent only with your consent. Each email includes an unsubscribe option."),
    ("setup", ["Demo configuration，正式营业前复核：email service provider and send schedule to confirm before launch."]),

    ("h2", "Sharing Information"),
    ("p", "We do not sell personal data. Information is shared with service providers (payment, shipping, email) only as needed to operate the store."),
    ("setup", ["Demo configuration，正式营业前复核：service provider list to confirm before launch."]),

    ("h2", "Cookies and Pixels"),
    ("p", "The store uses necessary cookies to operate checkout and remember your preferences. Non-essential cookies can be declined through your browser or store consent settings where available."),
    ("setup", ["Demo configuration，正式营业前复核：cookie list and any third-party pixel or advertising tools to confirm before launch."]),

    ("h2", "Security"),
    ("p", "We apply reasonable measures to protect personal data; no method of transmission over the internet is fully secure."),

    ("h2", "Your Rights"),
    ("p", "You may request access to, correction of, or deletion of your personal data, and may withdraw consent at any time. To exercise these rights, email " + CONTACT_EMAIL + "."),
    ("setup", ["Demo configuration，正式营业前复核：region-specific privacy rights text (e.g., US state privacy law) to confirm with legal review."]),

    ("h2", "Children"),
    ("p", "The store is not directed to children under 13. If you are under 13, do not place an order or submit personal data."),

    ("h2", "Contact"),
    ("p", "Privacy questions: " + CONTACT_EMAIL),
]

# ---------------------------------------------------------------------------
# TERMS OF SERVICE
# ---------------------------------------------------------------------------
PAGES["terms.txt"] = [
    ("h1", "Terms of Service"),
    ("note", "Demo configuration，正式营业前复核：法律主体、责任限制、AI 输出权属、管辖法律条款须法务确认后定稿；前台行不出现演示/演练字样。"),
    ("p", "Effective: 2026-11-20."),

    ("h2", "Use of the Store"),
    ("p", "You agree to use the store lawfully and not to engage in fraud, abuse, unauthorized scraping, or interference with store operations."),

    ("h2", "Eligibility"),
    ("p", "The store is intended for customers 13 or older. Minors require a parent or guardian's account where permitted. If you are under 13, do not place an order without adult involvement."),

    ("h2", "Products, Pricing, and Availability"),
    ("p", "Listings, prices, and discounts may change. Availability and bundle terms are noted on each product page."),
    ("setup", ["Demo configuration，正式营业前复核."]),

    ("h2", "Orders"),
    ("p", "Placing an order is an offer to purchase; acceptance and order confirmation occur when the order is processed, and a confirmation email is sent."),

    ("h2", "Intellectual Property"),
    ("p", "The ShotStart name, store copy, and creative materials belong to the brand."),
    ("setup", ["Demo configuration，正式营业前复核：IP ownership of AI-generated drafts and product photos pending legal review; omitted from public terms until confirmed."]),

    ("h2", "ShotStarter AI Assistant"),
    ("p", "ShotStarter outputs are drafts. You are responsible for reviewing, editing, and any claims made in content you publish."),

    ("h2", "Challenge Participation"),
    ("p", "Joining the 7-Day Shooting Challenge is optional. Participation does not guarantee followers, sales, or any platform result."),

    ("h2", "Promo Codes"),
    ("p", "Discount codes such as NEWCREATOR10 and STARTERKIT follow the rules listed at checkout: eligibility, one-use limits, stacking restrictions, excluded items, and validity dates. A code cannot be applied after an order is placed."),

    ("h2", "Dispute Resolution"),
    ("p", "If you have an issue with an order or product, contact us at " + CONTACT_EMAIL + " first. We will work with you by email to try to resolve the matter directly."),

    ("h2", "Contact"),
    ("p", "Questions about these terms: " + CONTACT_EMAIL),

    ("setup", [
        "Demo configuration，正式营业前复核：legal entity name, limitation-of-liability wording, AI-draft/photo IP, and jurisdiction/governing-law clause were not published; they are omitted until legal review confirms the wording.",
    ]),
]

# ---------------------------------------------------------------------------
# CHALLENGE
# ---------------------------------------------------------------------------
PAGES["challenge.txt"] = [
    ("h1", "7-Day Shooting Challenge"),
    ("p", "Seven short daily tasks. One small step each day to plan, film, and publish your first short video. Sign up with your email to receive daily prompts and ShotStarter template suggestions."),

    ("h2", "Rules"),
    ("bullets", [
        "Sign up with a valid email; one short challenge email arrives each day for seven days.",
        "Complete one task per day. You may adapt tasks to your product and style.",
        "Use ShotStarter drafts as starting points — review and edit before posting.",
        "The challenge is free to join; no purchase is required.",
        "Participation does not guarantee followers, sales, or any platform result.",
    ]),

    ("h2", "Daily Tasks"),
    ("p", "Day 1 — Pick your topic and selling point. Write down your product or topic and the one point you want viewers to remember. Use ShotStarter to set your platform and product type."),
    ("p", "Day 2 — Plan your 15-second script. Generate a draft script with ShotStarter; edit the opening line so it sounds like you."),
    ("p", "Day 3 — Set up your shot. Choose a flat surface or tripod/stand position; clean your lens; frame your first shot."),
    ("p", "Day 4 — Shoot four storyboard clips. Follow the four-shot storyboard: opening hook, product/topic close-up, middle demonstration, closing line. Record each clip."),
    ("p", "Day 5 — Assemble your cut. Trim clips to a 15-second pace; add simple captions; check lighting and focus."),
    ("p", "Day 6 — Write the publish caption. Use the ShotStarter caption draft; add your own voice, relevant hashtags, and a clear call to action."),
    ("p", "Day 7 — Publish and review. Post your first short video, note what worked, and plan your next clip."),

    ("h2", "Sign-Up Form Fields"),
    ("setup", [
        "First name",
        "Email",
        "Platform (select: TikTok / Instagram Reels / YouTube Shorts / Other)",
        "Product or topic you want to film (optional)",
    ]),
    ("bullets", [
        "Button: Join the challenge",
    ]),

    ("h2", "Thank-You Message"),
    ("p", "You're in. Day 1 is below — start shooting. Remember: your first shot starts here."),
    ("p", "First-order offer: 10% off your first order with code NEWCREATOR10, valid on all single items in the Shop collection; bundle kits are excluded; the code does not stack with STARTERKIT."),

    ("h2", "Day 8+ Nurture Email Sequence"),
    ("p", "Email 1 (Day 8 — Review & next shot)"),
    ("p", "Subject: Which shot worked best?"),
    ("p", "Preheader: Your next topic gets a 15-second script draft."),
    ("p", "Body: Hi [first name], Day 7 is done. Which shot worked best? Reply and tell us your next topic; ShotStarter can draft your next 15-second script."),
    ("p", "Email 2 (Day 10 — Keep your gear ready)"),
    ("p", "Subject: A quick lens check before your next clip"),
    ("p", "Preheader: Keep phone and camera lenses clear between shoots."),
    ("p", "Body: Quick lens check: smudges show up on camera. The Lens Cleaning Kit keeps phone and camera lenses clear between shoots."),
    ("p", "Email 3 (Day 14 — Second video prompt)"),
    ("p", "Subject: One video down — what's next?"),
    ("p", "Preheader: Pick a new selling point and run the four-shot storyboard again."),
    ("p", "Body: Hi [first name], one video down, the next one is easier. Pick a new selling point and run the four-shot storyboard again."),
    ("setup", [
        "Merge field: [first name] inserts the sign-up first name; in emails that do not use a name greeting, keep the Body plain (e.g., the Win-Back Email below).",
        "ESP and send times: [待确认: email service provider, send schedule]; sequence copy is a draft for review.",
    ]),

    ("h2", "Cleaning Kit Refill Repurchase Hook"),
    ("p", "Refill reminder: when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots."),
    ("setup", ["Demo configuration，正式营业前复核：refill availability and any repeat-purchase offer to confirm before launch."]),

    ("h2", "Win-Back Email"),
    ("p", "Subject: Your first shot is still waiting"),
    ("p", "Preheader: No pressure — pick up where you left off."),
    ("p", "Body: We noticed you haven't finished the challenge. Reply here or open Day 1 again."),

    ("h2", "Participant Exclusive Incentive"),
    ("bullets", [
        "Participants may receive a thank-you offer; offer terms are finalized before launch.",
        "Participation does not guarantee followers, sales, or any platform result.",
    ]),
    ("setup", [
        "Demo incentive; demo default code CHALLENGE7; code name and limits: [待确认: incentive code, usage window, one-time use] — Demo configuration, confirm before launch. The public line must not promise a code, free shipping, or any reward until the offer is configured and confirmed.",
    ]),

    ("h2", "Growth Metrics (Funnel Definitions)"),
    ("bullets", [
        "Signups: number of valid emails collected through the challenge form.",
        "Participants: signups who open at least one challenge email or complete Day 1.",
        "Engagement: participants who complete three or more daily tasks.",
        "Purchase: participants who place an order during or after the challenge.",
        "Tools: metrics tracked via the connected analytics or email tool; fields are set up in the store admin.",
    ]),
]

# ---------------------------------------------------------------------------
# MARKETING COMPONENTS
# ---------------------------------------------------------------------------
PAGES["marketing.txt"] = [
    ("h1", "Marketing Components"),
    ("note", "以下折扣、门槛、码均为演示配置，上线前必须与运营/财务确认生效期限、叠加规则与库存范围。"),

    ("h2", "1. Announcement Bar — Free Shipping Threshold"),
    ("p", "Consumer copy: Free standard shipping on US orders over $35."),
    ("setup", [
        "Demo configuration: threshold $35; standard flat rate $4.99",
        "Applies to: US standard shipping only",
        "Threshold basis: defaults to the post-discount subtotal; verify against the live store backend before launch.",
        "Confirm: final threshold, excluded products, and messaging before launch",
    ]),

    ("h2", "2. Creator Starter Kit Bundle (three items)"),
    ("p", "Bundle contents: Adjustable Phone Tripod ($19.99) + Desktop Phone Stand ($14.99) + Lens Cleaning Kit ($9.99). Kit price $44.97 — use code STARTERKIT at checkout: $38.22. You save $6.75."),
    ("p", "Consumer copy: The Creator Starter Kit pairs steady gear with a clean lens — the basics a first-time creator needs to set up and shoot."),
    ("setup", [
        "Mechanism (decided): there is no free native bundle builder; the kit is a standalone SPU listed at $44.97. STARTERKIT = 15% off and applies to that SPU only; code price $38.22; savings $6.75 (44.97 − 38.22), rounded to the cent.",
        "Demo defaults: code valid during the drill period; no usage cap; no minimum order; one code per order; STARTERKIT and NEWCREATOR10 cannot be combined. No compare-at reference price or strike-through field is shown.",
        "Confirm: final validity, limits, inventory, and eligibility before launch.",
    ]),

    ("h2", "2b. Pro Creator Kit Bundle (four items)"),
    ("p", "Bundle contents: Adjustable Phone Tripod ($19.99) + Extension Pole ($16.99) + Mini Ball Head ($12.99) + Creator Carry Case ($12.99). Kit price $62.96 — use code STARTERKIT at checkout: $53.52. You save $9.44."),
    ("p", "Consumer copy: The Pro Creator Kit adds steady framing, height and angle control, and a carry case for creators moving beyond the basics."),
    ("setup", [
        "Mechanism (decided): like the Starter Kit, this is a standalone SPU listed at $62.96. STARTERKIT = 15% off and applies to that SPU only; code price $53.52; savings $9.44 (62.96 − 53.52), rounded to the cent.",
        "Demo defaults: code valid during the drill period; no usage cap; no minimum order; one code per order; STARTERKIT and NEWCREATOR10 cannot be combined. No compare-at reference price or strike-through field is shown.",
        "Confirm: final validity, limits, inventory, and eligibility before launch.",
    ]),

    ("h2", "3. Welcome Discount Code (First-Order Offer)"),
    ("p", "Consumer copy: New here? Take 10% off your first order with code NEWCREATOR10."),
    ("setup", [
        "Demo configuration: NEWCREATOR10 = 10% off the customer's first order",
        "Note (internal): 原拟 WELCOME10 因后台已结束记录锁定不可复用，演练改用 NEWCREATOR10；正式店可重新启用 WELCOME10 或沿用新码，上线前定稿。",
        "Validity: demo valid during the drill period; final expiry to confirm before launch",
        "Usage: one redemption per customer; one code per order; does not stack with STARTERKIT",
        "Eligibility: applies to all single items in the Shop collection; both bundle SPUs (Creator Starter Kit and Pro Creator Kit) are excluded",
        "Pricing: no minimum order in the demo; discount applied before shipping; totals rounded to the cent",
        "Confirm: minimum order, excluded items, and consent wording before launch",
    ]),

    ("h2", "4. Email Popup — First-Order Offer"),
    ("p", "Consumer copy: Subscribe for a first-order discount and the 7-Day Shooting Challenge checklist."),
    ("p", "Button: Save my spot"),
    ("setup", [
        "Demo configuration: 10% off first order after email signup",
        "Mechanism: NEWCREATOR10 code shown immediately after the email is submitted",
        "Frequency: shown once per browser; a localStorage flag prevents it from showing again in the same browser",
        "Fallback: if the native email popup is not available, show the NEWCREATOR10 code on the challenge sign-up success state (see challenge.txt thank-you message) and the form-states challenge success copy; keep eligibility wording aligned with section 3.",
        "Confirm: expiry, consent wording, and unsubscribe flow before launch",
    ]),

    ("h2", "5. Challenge UGC Hashtag Wall — Retention / Community Component"),
    ("p", "Concept: a UGC hashtag wall collecting public posts tagged #ShotStartChallenge."),
    ("bullets", [
        "Display copy: Made something this week? Tag #ShotStartChallenge — your clip could be featured.",
    ]),
    ("setup", [
        "Moderation: featured content is reviewed before display; creators retain ownership of their posts. [待确认: UGC repost consent wording]",
        "Demo configuration: community concept only; wall tool and permissions to confirm before launch",
    ]),
]

# ---------------------------------------------------------------------------
# JUDGE GUIDE (Chinese reviewer custom page — sole Chinese storefront exception)
# ---------------------------------------------------------------------------
PAGES["judge-guide-zh.txt"] = [
    ("h1", "评委导览 / Judge Guide"),
    ("note", "本页为面向中文评委的独立 Custom Page，是英文前台口径的唯一中文例外；中英对照，供评审使用，正式店上线前可移除。页内价格与折扣均为演示配置。"),

    ("h2", "顶部提示句（首页顶部条复用，≤40 字）"),
    ("p", "评委导览：商品价格、挑战闭环与参观路线一览。"),

    ("h2", "品牌一句话 / Brand in one line"),
    ("p", "ShotStart 面向美国市场的新手短视频创作者与小商家，用简洁手机装备加 ShotStarter AI 助手，帮创作者把第一条视频做完发出去。"),
    ("p", "ShotStart pairs simple phone gear with the ShotStarter AI assistant for beginner creators and small shop owners in the US market, helping them finish and publish that first video."),

    ("h2", "锁定色与字体 / Locked Colors and Fonts"),
    ("table",
     ["角色 / Role", "色值 / Hex", "字体 / Font"],
     [
        ["主强调色 Coral Orange", "#FF5A2C", "标题：Montserrat / Poppins（Bold, SemiBold）"],
        ["品牌深色 Deep Navy", "#0F1B2D", "正文：Inter / 系统无衬线常规字重"],
        ["界面底色 Warm White", "#FAF6F0", "回落栈见品牌定稿文档"],
     ]),
    ("p", "橙色仅用于 ≥24px 粗体标题、按钮与符号；小字号正文用海军蓝或暖灰，不承载正文。"),

    ("h2", "商品与捆绑价格 / Products and Bundle Pricing"),
    ("table",
     ["商品 / Item", "中文", "价格 / Listed price"],
     [
        ["Adjustable Phone Tripod", "可调手机三脚架", "$19.99"],
        ["Desktop Phone Stand", "桌面手机支架", "$14.99"],
        ["Lens Cleaning Kit", "镜头清洁套装", "$9.99"],
        ["Creator Carry Case", "器材收纳包", "$12.99"],
        ["Folding Reflector", "折叠反光板", "$10.99"],
        ["Backdrop Cloth", "背景布", "$13.99"],
        ["Extension Pole", "延长杆", "$16.99"],
        ["Lens Cleaning Refill", "清洁补充装（单件，不进捆绑）", "$7.99"],
        ["Mini Ball Head", "迷你云台", "$12.99"],
        ["Magnetic Mount", "磁吸手机支架", "$11.99"],
        ["Microfiber 3-Pack", "清洁布三片装", "$6.99"],
        ["Shot List Cards", "分镜清单卡片（配套 AI 脚本草稿）", "$8.99"],
        ["Creator Starter Kit (bundle)", "三件套捆绑（独立 SPU）", "$44.97 → $38.22（STARTERKIT 15%，省 $6.75）"],
        ["Pro Creator Kit (bundle)", "四件套捆绑（独立 SPU）", "$62.96 → $53.52（STARTERKIT 15%，省 $9.44）"],
     ]),
    ("bullets", [
        "STARTERKIT：15% 优惠码，仅作用两个捆绑 SPU；每单一码，不与 NEWCREATOR10 叠加。",
        "NEWCREATOR10：新客首单 10%，作用 Shop 集合全部单件；两个捆绑 SPU 排除；每客一次、每单一码。",
        "以上价格、折扣与有效期以店铺后台最终配置为准，上线前须核实。",
    ]),

    ("h2", "7 日挑战闭环 / 7-Day Challenge Loop"),
    ("bullets", [
        "Day 1–7：选题 → 脚本 → 布机 → 拍摄 → 剪辑 → 文案 → 发布；每日一任务、每日一封短邮件，共 7 天。",
        "留资入口：首页挑战区块与邮件弹窗；提交后即时展示 NEWCREATOR10。",
        "Day 8+：三封 nurture 邮件、清洁套装复购钩子、流失唤醒邮件（均为草稿文案）；漏斗指标口径见 challenge.txt。",
    ]),

    ("h2", "参观路线 / Walkthrough"),
    ("bullets", [
        "首页 Home → Shop 集合页 → 单件商详（三脚架 / 支架 / 清洁套装 / 收纳包 / 反光板 / 背景布 / 延长杆 / 补充装 / 迷你云台 / 磁吸支架 / 清洁布三片装 / 分镜清单卡片）→ 捆绑 SPU（Starter / Pro）→ Challenge 挑战页 → 购物车与结账测试单。",
        "结账核对：价格、免邮门槛（满 $35）、折扣码适用范围与不叠加规则、运费与免邮条件。",
    ]),

    ("h2", "AI 能力映射 / ShotStarter AI Capabilities"),
    ("bullets", [
        "输入：平台（TikTok / Instagram Reels / YouTube Shorts 等）、商品类型、核心卖点。",
        "输出：15 秒脚本草案、四镜分镜（钩子 / 特写 / 演示 / 收尾）、可编辑文案与发布稿。",
        "所有 AI 输出为草稿，发布前由创作者自行审核修改；页面链接以店内相对页面说明为准，不引用内部路径。",
    ]),

    ("h2", "举证索引 / Evidence Index"),
    ("bullets", [
        "评审轮次：R2–R9 文案评审，另含一轮占位清零批；最新评审报告见留证目录 round9/expert-copy.md 专家复核稿。",
        "测试断言：tools 目录扫描脚本输出七项基线（未映射占位、方括号泄漏、占位词、中文残留、演示语境外露、废弃词、docx 泄漏）均为 0；FAQ 问答加粗 24/24。",
        "留证目录：评审报告与脚本快照随文案包保存；本页不记录账号 ID、登录口令或内部服务器路径。",
    ]),
]

# ---------------------------------------------------------------------------
# FORM STATES (shared microcopy for contact / challenge / popup)
# ---------------------------------------------------------------------------
PAGES["form-states.txt"] = [
    ("h1", "Form States Copy (Contact / Challenge / Popup)"),
    ("note", "三套表单共用同一套状态文案；字段命名全店统一为 First name / Email / Platform。状态句为英文消费者文案；字段定义为后台配置。"),

    ("h2", "Canonical Field Labels"),
    ("setup", [
        "First name",
        "Email",
        "Platform (challenge sign-up form only)",
        "Message (contact form only)",
    ]),

    ("h2", "Success State"),
    ("bullets", [
        "Contact form: Thanks for reaching out. We read every message.",
        "Challenge sign-up: You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.",
        "Email popup: Thanks — your welcome code is shown below. Save it before you leave.",
    ]),

    ("h2", "Required Field Message"),
    ("bullets", [
        "Please enter your first name.",
        "Please enter your email address.",
        "Please enter your message.",
    ]),

    ("h2", "Invalid Email Format"),
    ("p", "Please enter a valid email address, e.g., name@example.com."),

    ("h2", "Submission Failure"),
    ("p", "Something went wrong and your message wasn't sent. Please try again, or email us directly at " + CONTACT_EMAIL + "."),

    ("h2", "Consent Checkbox"),
    ("bullets", [
        "Contact: I agree to be contacted about my question.",
        "Challenge / popup: By signing up, I agree to receive challenge and marketing emails. I can unsubscribe at any time.",
        "Unselected state: Please agree to be contacted before submitting.",
    ]),

    ("h2", "Field Labeling Note"),
    ("note", "每个输入框必须有可见标签；不能只靠 placeholder 提示文字充当标签，上线前在表单组件中核对。"),
]

# ---------------------------------------------------------------------------
# GLOSSARY (canonical terms)
# ---------------------------------------------------------------------------
PAGES["glossary.txt"] = [
    ("h1", "Copy Glossary (Canonical Terms)"),
    ("note", "全店英文文案统一用词；右列为避免混用或已废弃的写法。"),
    ("table",
     ["Topic", "Use this", "Avoid"],
     [
        ["Audience", "small shop owners", "small merchants, sellers"],
        ["Content readiness", "publish-ready", "ready-to-publish, ready-to-post"],
        ["Program name", "7-Day Shooting Challenge", "lowercase “7-day challenge” as a title, Shooting Challenge 7 Days"],
        ["Privacy term", "personal data", "user data, customer info (in privacy context)"],
        ["AI assistant", "ShotStarter", "Shot Starter, AI helper"],
        ["Bundle", "Creator Starter Kit, Pro Creator Kit", "Starter bundle, Creator Pack, Pro Pack"],
        ["Welcome code", "NEWCREATOR10", "FIRSTSHOT, generic “welcome code” when the code is referenced"],
        ["Bundle code", "STARTERKIT", "STARTER KIT written as two words in code context"],
        ["Collections", "All Gear / Creator Kits", "Shop All, Creator Bundle as collection names"],
        ["Cleaning claim", "Designed for lens surfaces", "lens-safe, scratch-free guarantee wording"],
     ]),

    ("h2", "Policy Terms (English → 中文对照)"),
    ("note", "政策页英文术语与中文释义对照；条款定稿以法务确认为准。"),
    ("table",
     ["English term", "中文含义"],
     [
        ["Return window", "可退货期限（自签收起算）"],
        ["Restocking fee", "补货手续费（退货条款以法务定稿为准）"],
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
     ]),
]

# ---------------------------------------------------------------------------
# PLACEHOLDER MAP (new)
# ---------------------------------------------------------------------------
PAGES["placeholder-map.txt"] = [
    ("h1", "Placeholder → English Final-Wording Replacement Map"),
    ("note", "上线前逐条把 [待确认: ...] 占位替换为下表英文定稿措辞；未取得真实信息前不得填写数值、认证或承诺。发布前检查项：前台扫描不得出现任何 [待确认 方括号；未替换的占位改用本表中性兜底句，不得把中文备注留在店铺页面。"),
    ("table",
     ["Placeholder", "English final-wording template", "Applies to"],
     [
        ["[待确认: compatible phone width range] / [待确认: compatible width range] / [待确认: exact phone compatibility range]",
         "Fits phones from [min width] to [max width] mm ([example models]).",
         "Tripod, Stand"],
        ["[待确认: height range and tilt range] / [待确认: height range / tilt range]",
         "Height adjusts from [min] to [max] cm; tilt range [x]°–[y]°.",
         "Tripod"],
        ["[待确认: net weight and folded length] / [待确认: net weight]",
         "Net weight [x] g; folded length [x] cm.",
         "Tripod, Stand"],
        ["[待确认: net weight / base material]",
         "Net weight [x] g; base material: [material]; non-slip [pad material] pad.",
         "Stand FAQ"],
        ["[待确认: foot material]",
         "Non-slip [material, e.g., rubber] feet.",
         "Tripod"],
        ["[待确认: main material, e.g., aluminum alloy / ABS plastic] / [待确认: main material, e.g., ABS plastic / metal]",
         "Body material: [material, e.g., aluminum alloy / ABS plastic].",
         "Tripod, Stand"],
        ["[待确认: folded length]",
         "Folded length [x] cm.",
         "Tripod"],
        ["[待确认: any included mount adapter or carry bag] / [待确认: included mount details] / [待确认: any accessory such as a carry bag or adapter]",
         "Included: [accessory list, e.g., phone clamp, carry bag].",
         "Tripod box"],
        ["[待确认: carry bag inclusion]",
         "Carry bag: included / not included.",
         "Tripod FAQ"],
        ["[待确认: angle range]",
         "Tilt/viewing angle adjusts [x]°–[y]°.",
         "Stand"],
        ["[待确认: base dimensions]",
         "Base measures [width] × [depth] cm.",
         "Stand"],
        ["[待确认: base material / non-slip pad]",
         "Base material: [material]; non-slip [pad material] pad.",
         "Stand"],
        ["[待确认: charging cutout details] / [待确认: charging cutout]",
         "Open cable cutout fits [cable type/width]; charging cable not included.",
         "Stand"],
        ["[待确认: any non-slip pad or accessory]",
         "Included: [pad/accessory list].",
         "Stand box"],
        ["[待确认: compatible surface types] / [待确认: approved surface list]",
         "Approved surfaces: [list, e.g., smartphone cameras, compact camera lenses, accessory lenses].",
         "Cleaning Kit"],
        ["[待确认: cloth material and count] / [待确认: cloth material/count] / [待确认: material and quantity] / [待确认: cloth quantity] / [待确认: cloth material]",
         "Cleaning cloth: [material], [count] piece(s), [size] cm.",
         "Cleaning Kit"],
        ["[待确认: liquid inclusion, volume, and ingredients] / [待确认: liquid inclusion and volume] / [待确认: inclusion, volume, ingredients] / [待确认: volume, ingredients] / [待确认: cloth material, liquid volume and ingredients] / [待确认: cloth material, liquid volume, ingredients] / [待确认: included contents, cloth material, liquid volume and ingredients]",
         "Cleaning fluid: [volume] ml, [ingredient list]; [included / refillable bottle]. Cleaning cloth: [material], [count] piece(s).",
         "Cleaning Kit"],
        ["[待确认: included contents list]",
         "Included items: [confirmed item list, e.g., fluid bottle, air blower, cleaning cloth, lens pen].",
         "Cleaning Kit"],
        ["[待确认: brush/blower material, cloth material] / [待确认: brush bristle material, cloth material] / [待确认: blower/pen material] / [待确认: blower/pen material, cloth material]",
         "Blower/pen material: [material]; cloth: [material].",
         "Cleaning Kit specs"],
        ["[待确认: liquid volume, kit dimensions]",
         "Fluid volume [x] ml; kit dimensions [x] × [x] × [x] cm.",
         "Cleaning Kit"],
        ["[待确认: founding date, location, legal entity name]",
         "ShotStart was founded in [year] in [location]; operating entity: [legal entity name].",
         "About"],
        ["[待确认: business hours / support address] / [待确认: business hours]",
         "Support hours: [days, hours, time zone]. Support address: [address or 'email only'].",
         "Contact"],
        ["[待确认: response time window]",
         "We aim to reply within [e.g., 1–2 business days].",
         "Contact"],
        ["[待确认: processing time window]",
         "Orders are processed within [e.g., 1–2 business days] after payment.",
         "Shipping"],
        ["[待确认: supported countries/regions]",
         "We currently ship to [country/region list].",
         "Shipping"],
        ["[待确认: shipping rate table by destination]",
         "Rates by destination: [zone/rate table].",
         "Shipping"],
        ["[待确认: carrier and estimated transit window]",
         "Carrier: [carrier name]; estimated transit [window], not guaranteed.",
         "Shipping"],
        ["[待确认: tracking email details]",
         "Tracking details are emailed to the address on your order.",
         "Shipping"],
        ["[待确认: cross-border shipping availability]",
         "International shipping: [available/not available].",
         "Shipping"],
        ["[待确认: return window, e.g., 30 days]",
         "Return window: [e.g., 30 days] from delivery.",
         "Refund"],
        ["[待确认: restocking fee policy]",
         "Restocking fee: [none / x%], applies to [conditions].",
         "Refund"],
        ["[待确认: non-returnable categories]",
         "Non-returnable: [category list].",
         "Refund"],
        ["[待确认: return warehouse address]",
         "Return address: [warehouse address].",
         "Refund"],
        ["[待确认: refund processing window]",
         "Refunds are issued within [e.g., 5–10 business days] after inspection.",
         "Refund"],
        ["[待确认: refundable / non-refundable]",
         "Shipping charges are [refundable / non-refundable].",
         "Refund"],
        ["[待确认: exchange availability and process]",
         "Exchanges: [available/not available]; process: [steps].",
         "Refund"],
        ["[待确认: damage claim window]",
         "Damaged/defective claims must be reported within [window] of delivery.",
         "Refund"],
        ["[待确认: effective date]",
         "Last updated: [YYYY-MM-DD].",
         "Privacy, Terms"],
        ["[待确认: analytics tools used]",
         "Analytics tools: [tool list, e.g., store native analytics].",
         "Privacy"],
        ["[待确认: email service provider] / [待确认: email service provider, send schedule]",
         "Marketing emails are sent via [ESP name]; send schedule: [time/cadence].",
         "Privacy, Challenge"],
        ["[待确认: code active dates and usage limits]",
         "Discount code active [start]–[end]; usage: [one per customer / per item / per order]; excluded items: [list].",
         "Marketing codes"],
        ["[待确认: processor list]",
         "Service providers: [payment, shipping, ESP names].",
         "Privacy"],
        ["[待确认: cookie policy and any third-party pixel or advertising tools]",
         "Cookies and pixels: [list and purpose].",
         "Privacy"],
        ["[待确认: regional rights text, e.g., US state privacy law, to confirm with legal review]",
         "Applicable rights: [region-specific privacy rights text, reviewed by legal].",
         "Privacy"],
        ["[待确认: age threshold]",
         "The store is not directed to children under [age].",
         "Privacy"],
        ["[待确认: order confirmation process]",
         "Order confirmation is sent [method, e.g., email] once payment is verified.",
         "Terms"],
        ["[待确认: intellectual-property ownership of AI-generated drafts and product photos]",
         "IP ownership: [clause covering AI drafts and product photos, reviewed by legal].",
         "Terms"],
        ["[待确认: legal liability wording to review]",
         "Liability clause: [legal-reviewed wording].",
         "Terms"],
        ["[待确认: jurisdiction and governing law]",
         "Governing law: [jurisdiction].",
         "Terms"],
        ["[待确认: delivery time and cadence]",
         "Challenge emails are delivered [time/cadence, e.g., each morning at 9:00 AM ET].",
         "Challenge"],
        ["[待确认: whether challenge access is bundled with gear]",
         "Challenge access: [free with any gear purchase / free for all signups].",
         "Challenge"],
        ["[待确认: free-shipping threshold basis (pre/post discount)]",
         "Free-shipping threshold defaults to the post-discount subtotal; verify the basis against the store backend.",
         "Cart"],
        ["[待确认: order number placeholder format]",
         "Order number: [#XXXXXX].",
         "Confirmation"],
        ["[待确认: default sorting rule]",
         "Default collection sort: [rule].",
         "Shop"],
        ["[待确认: incentive code, usage window, one-time use]",
         "Incentive code: [code]; valid [window]; one-time use per completer.",
         "Challenge incentive"],
        ["[待确认: refill option and repeat-purchase offer]",
         "Refill: [available/not available]; repeat-purchase offer: [offer details].",
         "Challenge refill hook"],
        ["[待确认: analytics/ESP tool]",
         "Funnel metrics tracked in [analytics/ESP tool].",
         "Challenge metrics"],
        ["[待确认: UGC repost consent wording]",
         "Featured posts: [consent and attribution wording, reviewed by legal].",
         "UGC wall"],
        ["[待确认: physical mailing/return address]",
         "Mail-in address: [street address, city, state, ZIP]; used for correspondence and returns.",
         "Contact, Shipping, Refund"],
        ["[待确认: data retention period]",
         "Personal data is retained for [retention period by data type], then deleted or anonymized.",
         "Privacy"],
        ["[待确认: return shipping cost responsibility]",
         "Return shipping is paid by [customer / store / store for defective items], per the confirmed policy.",
         "Refund"],
        ["[待确认: dispute resolution process]",
         "Issues are first handled by email; unresolved disputes follow [mediation / arbitration / court process], reviewed by legal.",
         "Terms"],
        ["[待确认: minimum age eligibility]",
         "Customers must be [age] or older; minors require a parent or guardian's account.",
         "Terms, Privacy"],
        ["[待确认: promo code terms to align with marketing.txt]",
         "Code [name] applies to [eligibility], one use per [customer/order], excludes [items], valid [dates]; does not stack with [other code].",
         "Terms, Marketing"],
        ["[待确认: carry case dimensions and material]",
         "Case measures [width] × [depth] × [height] cm; material: [material].",
         "Carry Case"],
        ["[待确认: reflector diameter and fabric]",
         "Reflector diameter [x] cm; surface fabric: [fabric].",
         "Reflector"],
        ["[待确认: backdrop dimensions and fabric]",
         "Backdrop measures [width] × [height] cm; fabric: [fabric].",
         "Backdrop"],
        ["[待确认: pole extended and collapsed length]",
         "Pole extends to [x] cm; collapses to [y] cm.",
         "Extension Pole"],
        ["[待确认: ball head mount and thread details] / [待确认: included mount adapter]",
         "Mount: [thread/interface details]; included adapter: [adapter list].",
         "Mini Ball Head"],
        ["[待确认: magnetic mount compatibility and case thickness]",
         "Compatible with phone cases up to [thickness] mm; magnet plate: [included/not included].",
         "Magnetic Mount"],
        ["[待确认: approved surfaces and cloth material] / [待确认: cloth material and weave]",
         "Approved surfaces: [list]; cloth: [material], [weave].",
         "Microfiber 3-Pack"],
        ["[待确认: cloth size and count]",
         "Cloths: [count] piece(s), [size] cm each.",
         "Microfiber 3-Pack"],
        ["[待确认: shot list cards contents and material] / [待确认: card size and count]",
         "Cards: [count] [size] mm; material: [material]; ring/pocket case: [included/not included].",
         "Shot List Cards"],
        ["[待确认: printed language list]",
         "Printed languages: [language list].",
         "Shot List Cards"],
     ]),
]

# ---------------------------------------------------------------------------
# Chinese reviewer reading guide (rendered into the docx only)
# ---------------------------------------------------------------------------
READING_GUIDE_ZH = [
    ("h1", "附录：评委阅读指南（中文，逐页摘要）"),
    ("note", "本附录帮助不熟悉英文的评委快速理解全店内容；店铺前台消费者文案仍为英文。"),

    ("h2", "首页 home.txt"),
    ("p", "公告栏给出免邮门槛与欢迎码两条备选；Hero 口号 “Your first shot starts here.”，副题说明面向新手与小商家，配 Shop 与 Join the 7-Day Shooting Challenge 双 CTA。三条价值主张为新手友好、手机适配、AI 辅助；下方十二张单件商品卡片、两张捆绑卡片（Creator Starter Kit 与 Pro Creator Kit）、ShotStarter AI 功能区块、7 天挑战入口、邮件弹窗与页脚简介。"),

    ("h2", "集合页 shop.txt"),
    ("p", "两个集合：All Gear 与 Creator Kits；排序选项含价格与上新。十二张单件卡片分别给出演示价与一句话卖点；两个捆绑均为独立 SPU：Starter Kit 标价 $44.97，用码 STARTERKIT 后 $38.22，省 $6.75；Pro Creator Kit 标价 $62.96，用码后 $53.52，省 $9.44（均为演示配置，无虚构划线原价）。"),

    ("h2", "三脚架 product-tripod.txt"),
    ("p", "面向口播、产品演示与外景的可调三脚架；卖点围绕高度角度可调、手机夹适配、免手持与折叠便携。所有宽度、尺寸、重量、材质、配件均为占位；FAQ 回答适配、户外使用与收纳包问题；演示价 $19.99。"),

    ("h2", "桌面支架 product-stand.txt"),
    ("p", "把手机直立放在桌面，适合演示、直播与参考观看；卖点为角度、紧凑占地、底座与线材开口。参数全部占位；演示价 $14.99。"),

    ("h2", "清洁套装 product-cleaning-kit.txt"),
    ("p", "图中构成待实物确认：清洁液瓶、气吹、清洁布、镜头笔；前台文案只写 compact cleaning set，不写死件数与材质。适用表面、布材、液体容量与成分为占位。图注只写商品与用途，不标注生成方式；演示价 $9.99。"),

    ("h2", "收纳包 product-carry-case.txt"),
    ("p", "便携收纳包，用于收纳三脚架、支架与小配件；尺寸、材质、隔层与兼容物件清单为中性兜底占位；演示价 $12.99，可加入 Pro Creator Kit。"),

    ("h2", "反光板 product-reflector.txt"),
    ("p", "折叠反光板，为面部与产品特写补光、柔化光线；直径、面料与折叠方式为占位；演示价 $10.99，仅作单件销售，不进入捆绑。"),

    ("h2", "背景布 product-backdrop.txt"),
    ("p", "纯色背景布，用于产品与口播镜头的干净背景；尺寸、布料、颜色与悬挂配件为占位；演示价 $13.99，仅作单件销售，不进入捆绑。"),

    ("h2", "延长杆 product-extension-pole.txt"),
    ("p", "延长杆，用于 overhead 与高角度自拍、群拍；材质、展开与收拢长度、夹持方式为占位；演示价 $16.99，可加入 Pro Creator Kit。"),

    ("h2", "清洁补充装 product-cleaning-refill.txt"),
    ("p", "清洁套装的补充装：替换清洁布与清洁液；布材、液体容量与成分为占位；仅作单件销售，不进入任何捆绑；演示价 $7.99。"),

    ("h2", "迷你云台 product-mini-ball-head.txt"),
    ("p", "装在三脚架与手机夹之间的迷你云台，一拧即可倾斜、旋转并调平画面；安装接口、材质与净重为占位；演示价 $12.99，可加入 Pro Creator Kit。"),

    ("h2", "磁吸支架 product-magnetic-mount.txt"),
    ("p", "磁吸手机支架，一键拆装，适合桌面演示与参考观看；手机壳与磁吸兼容性、底座材质为占位；仅作单件销售；演示价 $11.99。"),

    ("h2", "清洁布三片装 product-microfiber-3pack.txt"),
    ("p", "三片装超细纤维布，拍摄间隙擦拭手机镜头与屏幕；布材、尺寸与片数为占位；与镜头清洁套装搭配使用；仅作单件销售；演示价 $6.99。"),

    ("h2", "分镜清单卡片 product-shot-list-cards.txt"),
    ("p", "配套 ShotStarter 脚本草稿的四镜提示卡（钩子 / 特写 / 演示 / 收尾）；卡片件数、材质与语种为占位；不替代创作者对 AI 草稿的自行审核；仅作单件销售；演示价 $8.99。"),

    ("h2", "购物车与结账 cart-checkout.txt"),
    ("p", "加购确认、数量增减、继续浏览与 Secure Checkout 按钮；免邮凑单提示（三脚架+支架 $34.98，差 $0.02，引导加清洁套装）；优惠码入口与无效码提示、缺货与地址校验状态、演示结账提示；结账信任文案仅用 secure checkout / no hidden fees 等通用表述；订单确认页含订单号占位与支持邮箱。"),

    ("h2", "表单状态 form-states.txt"),
    ("p", "联系、挑战、弹窗三套表单共用的状态文案：成功态、必填提示、邮箱格式错误、提交失败、同意勾选；字段命名统一 First name / Email / Platform。"),

    ("h2", "About about.txt"),
    ("p", "品牌故事：开始做短视频最难的是迈出第一个镜头；ShotStart 用直白装备加 AI 助手降低门槛，不承诺一夜涨粉，陪创作者一条一条发出去。"),

    ("h2", "Contact contact.txt"),
    ("p", "联系表单字段、客服邮箱；2 个工作日内邮件回复，邮箱唯一承接，不公布实体地址；订单问题请附订单号。"),

    ("h2", "运输政策 shipping-policy.txt"),
    ("p", "仅美国地区；标准运费 $4.99、满 $35 免邮；2 个工作日内处理，美区 5–8 个工作日送达；邮件追踪；不支持跨境；邮箱承接。"),

    ("h2", "退换政策 refund-policy.txt"),
    ("p", "送达后 30 天内、未使用原包装；重新上架费演示默认无、正式营业前法务复核；非质量退货运费顾客承担；收货后 5 个工作日原路退款；换货个案处理；破损凭照片 30 天内申诉。"),

    ("h2", "隐私政策 privacy-policy.txt"),
    ("p", "采集 name/email/订单/platform preference；用途为履约与经同意的挑战邮件；订单记录保留 24 个月、营销同意至退订后 30 天；不出售 personal data；13+；行权邮箱；服务商清单与 Cookie/州权利仍待核实。"),

    ("h2", "服务条款 terms.txt"),
    ("p", "使用规则、13+ 资格、订单确认、品牌名与文案权属、AI 草稿责任、挑战参与、促销码规则；争议先邮件协商；法律主体、责任上限、AI 草稿与产品图片权属、管辖法律未发布，待法务确认。"),

    ("h2", "挑战页 challenge.txt"),
    ("p", "规则与 Day1–Day7 任务（选题→脚本→布机→拍摄→剪辑→文案→发布）；每日一任务、每日一封短邮件共 7 天；留资表单与感谢语，成功态展示 NEWCREATOR10；Day8+ 三封 nurture 邮件、清洁套装复购钩子、流失唤醒邮件、完成挑战激励（演示配置）与留资→参与→购买漏斗指标。"),

    ("h2", "营销组件 marketing.txt"),
    ("p", "免邮门槛、两个捆绑 SPU（Starter Kit 标价 $44.97 用码后 $38.22 省 $6.75；Pro Creator Kit 标价 $62.96 用码后 $53.52 省 $9.44；STARTERKIT 15% off 分别作用对应捆绑 SPU）、NEWCREATOR10 首单 10% 规则（作用 Shop 集合全部单件，两个捆绑 SPU 排除）、弹窗机制（提交后即时显码、同浏览器 localStorage 标记只弹一次）、#ShotStartChallenge UGC 话题墙；全部为演示配置。"),

    ("h2", "评委导览页 judge-guide-zh.txt"),
    ("p", "面向中文评委的独立 Custom Page，是英文前台口径的唯一中文例外；含品牌一句话、锁定色/字体、12 单件与 2 捆绑价格表及两码机制、7 日挑战闭环与 nurture 节奏、演示路线、AI 能力映射、举证索引；不写账号 ID、口令或内部路径。"),

    ("h2", "术语表 glossary.txt 与占位对照表 placeholder-map.txt"),
    ("p", "术语表统一全店用词与避免写法；占位对照表逐条给出英文定稿模板、适用位置与上线前可展示的中性兜底句。"),
]

SHIPPING_NOTES_ZH = [
    ("h1", "附：运费与结账建议（中文说明，仅后台可见）"),
    ("p", "演示用统一运费：美国标准运费 $4.99；订单满 $35 免标准运费。以上均为演示配置，待与物流渠道和履约方案确认后再定稿。"),
    ("bullets", [
        "政策页面不得承诺具体到货天数；送达时效以 carrier 在结账时提供的预估为准。",
        "十二件单件的售价均为演示定价，页面标注 “Demo price, confirm before launch”，上线前替换为真实价格；两个捆绑的标价与用码价同为演示配置。",
        "免邮门槛折前/折后口径以后台实测为准；退回物流成本、偏远地区附加费需在上线前与履约方核对。",
        "结账流程需测试：浏览商品 → 加购 → 输入折扣码 → 核对运费与免邮条件 → 提交测试订单。",
    ]),
]

CHECKLIST_ZH = [
    ("h1", "附录：现场粘贴清单（中文，操作者使用）"),
    ("note", "顺序：商品 → 页面 → 运费 → 营销 → 测试下单。对照 pages\\ 目录下同名 txt 文件逐页粘贴。"),

    ("h2", "一、商品录入"),
    ("bullets", [
        "在 Shoplazza 后台创建 12 个单件 SPU：Adjustable Phone Tripod、Desktop Phone Stand、Lens Cleaning Kit、Creator Carry Case、Folding Reflector、Backdrop Cloth、Extension Pole、Lens Cleaning Refill、Mini Ball Head、Magnetic Mount、Microfiber 3-Pack、Shot List Cards；另创建 2 个捆绑 SPU：Creator Starter Kit、Pro Creator Kit（归入 Creator Kits 集合）。",
        "逐个对照 placeholder-map.txt 替换规格表中的 [待确认: ...] 占位项；未核实前不要填写具体数值、材质、兼容宽度、重量或尺寸。",
        "不得虚构销量、评价、认证、库存数量或“爆款”类表述。",
        "十二件单件与两个捆绑的演示定价上线前确认；页面价格统一标注演示配置。",
    ]),

    ("h2", "二、页面粘贴（对照 pages\\ 下全部 txt）"),
    ("bullets", [
        "home.txt：公告栏（含 Judge Guide 中文评委入口条，店内唯一中文例外）、Hero 标题/副标题/双 CTA、3 条价值主张、十二张单件卡片与两张捆绑卡片短文案、ShotStarter AI 区块、7 天挑战区块、邮件弹窗、页脚简介。",
        "shop.txt：集合命名（All Gear / Creator Kits）、排序口径、十二张单件卡片、Starter Kit $38.22 与 Pro Creator Kit $53.52 两个捆绑展示位。",
        "product-tripod.txt / product-stand.txt / product-cleaning-kit.txt / product-carry-case.txt / product-reflector.txt / product-backdrop.txt / product-extension-pole.txt / product-cleaning-refill.txt / product-mini-ball-head.txt / product-magnetic-mount.txt / product-microfiber-3pack.txt / product-shot-list-cards.txt：标题、卖点、描述、规格表、包装清单、场景、FAQ、演示定价、加购引导、信任文案、套装入口。",
        "cart-checkout.txt：购物车微文案、免邮凑单提示（Tripod+Stand=$34.98，差 $0.02）、优惠码入口/无效码、缺货与地址校验状态、演示结账提示、结账信任文案、订单确认页。",
        "发布前扫描：前台页面不得残留任何 [待确认 方括号占位或 [INTERNAL] 备注；未替换的占位改用 placeholder-map 中的中性英文兜底句。",
        "form-states.txt：联系/挑战/弹窗三套表单的成功、必填、邮箱格式、失败、同意勾选状态文案；字段命名统一。",
        "about.txt：品牌故事页；联系我们使用 contact.txt。",
        "shipping-policy.txt / refund-policy.txt / privacy-policy.txt / terms.txt：对应政策页面。",
        "challenge.txt：7 天挑战规则、Day1–Day7、Day8+  nurture 三封邮件、复购钩子、唤醒邮件、参与者激励、漏斗指标。",
        "marketing.txt：免邮门槛、两个捆绑 SPU（独立 SPU + STARTERKIT 15%，分别作用对应捆绑）、NEWCREATOR10（仅作用全部单件，捆绑 SPU 排除）、弹窗机制（localStorage 只弹一次）、UGC 话题墙。",
        "judge-guide-zh.txt：中文评委导览 Custom Page（中英对照例外页）；品牌一句话、色/字体、价格表与码机制、挑战闭环、演示路线、AI 映射、举证索引；不放账号 ID、口令或内部路径。",
        "glossary.txt：全店统一用词表，避免 merchants/sellers、ready-to-post 等混用写法。",
        "placeholder-map.txt：占位 → 英文定稿措辞与中性兜底句对照表，上线前逐条落实。",
    ]),

    ("h2", "三、运费与政策核对"),
    ("bullets", [
        "运费演示配置：US 标准 $4.99，满 $35 免邮；门槛折前/折后口径以后台实测为准，上线前确认最终费率表与地区范围。",
        "政策页演练值（30 天退货、5 个工作日退款、2 个工作日处理/回复、5–8 天送达、订单记录 24 个月、13+）为 Demo configuration，正式营业前复核；法律主体、管辖法律、责任上限、AI 草稿与产品图片权属仍待法务确认，前台未发布。",
        "客服邮箱已填 " + CONTACT_EMAIL + "；隐私政策的服务商清单与 Cookie/像素工具待确认。",
    ]),

    ("h2", "四、营销组件核对"),
    ("bullets", [
        "免邮门槛、两个捆绑独立 SPU（Creator Starter Kit 标价 $44.97，STARTERKIT 15% off 用码后 $38.22；Pro Creator Kit 标价 $62.96，用码后 $53.52）、NEWCREATOR10 欢迎码 10%（作用全部单件，捆绑排除）、邮件弹窗首单 10% 均为演示配置。",
        "每单仅一码，STARTERKIT 与 NEWCREATOR10 不叠加；演示有效期为演练期间、无起订额、金额四舍五入到分；上线前确认有效期、次数与排除商品。",
        "弹窗：提交邮箱即显示码、每访客一次、7 天冷却；邮件订阅需有勾选同意与退订入口。",
        "UGC 话题墙 #ShotStartChallenge 为概念组件；展示前需审核并确认转授权措辞。",
    ]),

    ("h2", "五、测试下单与全站检查"),
    ("bullets", [
        "用测试订单走完：浏览 → 加购 → 结账 → 折扣码 → 运费计算 → 提交；核对价格、免邮门槛、折扣计算正确。",
        "测试邮件订阅与挑战留资：确认表单提交成功、感谢语显示、确认邮件触发。",
        "全站复查：消费者可见语言为英文；中文备注与 [待确认] 占位不得出现在前台页面。",
        "复查无虚构参数、销量、评价、认证、库存或到货承诺；政策表述经法务/运营确认后再发布。",
    ]),

    ("h2", "六、发布洁净度扫描（四步）"),
    ("bullets", [
        "第一步：扫描所有 PUBLISH 前台行，确认无中文残留（中文备注仅允许出现在 INTERNAL/note/setup 块）。",
        "第二步：扫描无方括号占位残留（[待确认: ...] 及任何方括号标签）；未落实项按 placeholder-map 中性英文兜底句替换。",
        "第三步：扫描无 demo 内部标签或演示语境外露（INTERNAL、Demo price、demo configuration、演示店域名/密码等）；演示声明只留在页尾 INTERNAL 公告条，上线定稿全部删除。",
        "第四步：扫描越界词清单零命中（small merchants、sellers、ready-to-publish、ready-to-post、lens-safe 等，以 glossary 废弃词表为准）。",
        "自动化复跑：脚本实体随包放在 tools\\ 目录（见 tools\\README.md）——check_placeholders.py（未映射占位前向检查，兜底句从 placeholder-map 动态读取）、scan_publish.py（PUBLISH 方括号泄漏、占位词 placeholder/to be confirmed/being confirmed 残留、中文残留、demo/drill/演练语境外露、glossary Avoid 废弃词自动比对）、scan_docx.py（三 docx 泄漏、占位词残留、demo 语境外露），重建入口为 build_shotstart.py、build_brand_and_card.py；在 tools\\ 目录依次运行重建与三个扫描脚本，基线要求 unmapped=0、方括号泄漏 0、占位词残留 0、中文残留 0、demo 外露 0、废弃词命中 0、docx 泄漏 0。",
    ]),

    ("h2", "七、上线定稿剥离清单（正式店删除 / 替换项）"),
    ("bullets", [
        "所有 INTERNAL / setup / note 行：操作者说明、演示配置说明、占位键清单、页头图例行均不粘贴前台；正式店页面只保留 PUBLISH 行。",
        "Demo price / Demo configuration 行：上线前替换为真实价格、真实折扣与条款；未核实前不得发布对应前台承诺。",
        "演示店域名与密码：仅用于演练与速览卡举证，正式提交版从店铺页面与任何对外物料中剥离。",
        "政策页 INTERNAL 模板免责注记：上线定稿删除；演示版如需声明，统一放页尾公告条，不留在政策前台句。",
        "清洁套装图注与 Box 中性句：实物清单核实后，替换为真实构成、材质与容量说明；未核实前保持中性占位口径。",
        "邮件草案标注：Preheader 与 [first name] merge 槽位在 ESP 模板中落实；Win-back 不使用称呼字段，按统一说明处理。",
    ]),
]
