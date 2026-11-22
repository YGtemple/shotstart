# i18n 简中字典覆盖清单（EN → zh-CN）

- 字典文件：`tools/i18n_zh.json`（UTF-8；扁平字典置于 `zh-CN` 节点；`_meta` 为口径说明，不参与翻译）
- 语种范围：仅 EN + 简中两语种。键 = 前台 PUBLISH 英文原文逐字串（含大小写、标点、空格），值 = 简中译文。
- 原则：只覆盖关键部分，**不译全文**；字典为独立辅助文件，未回写 `pages/*.txt`，未重建任何 docx。
- 术语口径：与 `judge-guide-zh.txt` 及 glossary 一致——personal data=个人数据、publish-ready=可直接发布、small shop owners=小商家、7-Day Shooting Challenge=7 天拍摄挑战；品牌名 ShotStart / ShotStarter 不译。

## 一、已覆盖元素（按页面）

### 首页 home.txt
- 公告免邮句：满 $35 免标准运费。
- Hero：主标题、副标题；主/次 CTA 按钮（Shop All Gear、Join the 7-Day Shooting Challenge）。
- 政策链接行；信任行（三句短评）。
- 三支柱：区块标题 + 每支柱首句。
- 双捆绑卡：两卡区块标题、价格/优惠码句（STARTERKIT 机制与省额）、卡片 CTA（View the kit）。
- AI 区块：ShotStarter 助手介绍句；挑战区块按钮（Join the challenge）。
- 页脚链接集合。
- 顶部中文条：本就是中文例外条，**不进字典、不重复翻译**。

### 集合页 shop.txt
- 两集合标题 + 描述首句（All Gear、Creator Kits）。
- 两 SPU 卡片描述句（Creator Starter Kit、Pro Creator Kit）。

### 商品页 PDP（8 单件 + 2 捆绑入口）
- 8 单件完整标题（含副标题）；2 捆绑入口标题随首页/集合卡覆盖。
- 每个 PDP：Highlights 首句；CTA 三变体（Add to Cart、加入对应套装、Browse Creator Kits）。
- 共享 Trust 五条短句（安全结账、退货条款、AI 草稿、无隐藏费用、联系邮箱）。
- 全部 FAQ 问句（单件 18 组 + 套装相关 5 组），仅译问句，答案解释段不逐句译。

### About 页
- 首段（创办观察）、第二段（不承诺涨粉、逐天完成）首句口径句。

### Contact 页
- 首段联系说明句；2 工作日邮件回复、仅邮箱不公布地址句。
- 表单：同意勾选句、提交按钮。

### 四政策页
- Shipping：首段说明、2 工作日处理、仅美国、标准运费/免邮门槛、5–8 工作日送达句。
- Refund：30 天退货窗口、未使用原包装；已开封卫生类不退；非质量退货运费顾客承担；5 工作日原路退款、原运费不退；破损缺陷 30 天内带照片联系。
- Privacy：收集的联系/订单信息类别；订单记录保留 24 个月、营销同意退订后 30 天；营销邮件同意与退订；不出售个人数据、服务商共享边界；安全措施与非绝对安全；查阅/更正/删除/撤回同意与联系邮箱；13+ 限制句。
- Terms：13 岁及以上、未成年人账户要求；AI 草稿责任归属；挑战自愿、不保证结果；优惠码规则（NEWCREATOR10 / STARTERKIT 适用范围、次数、叠加限制、排除商品、有效期、下单后不可用）。

### 导航与全局
- 导航/页脚菜单项：Shop、About、Contact、Shipping Policy、Return & Refund Policy、Privacy Policy、Terms of Service。
- 购物车：凑单免邮提示句、凑单建议卡片句；无效码提示、缺货状态句。
- 表单：标签（First name、Email、Platform、Message）；联系/挑战两类同意句；成功态（联系感谢、挑战报名成功 + NEWCREATOR10 展示句、邮件弹窗欢迎码句）；校验报错句（名字/邮箱/留言/格式/发送失败）；未勾选提示。

### 挑战 / 优惠说明
- 首单优惠 NEWCREATOR10 展示句：10%、单件范围、捆绑除外、不叠加 STARTERKIT。

## 二、未覆盖范围（显式声明）

1. **结账托管深层不覆盖**：checkout 托管页 DOM、支付表单字段、第三方支付流程、运费/税费实时计算展示、订单确认托管页文案，均不在字典内；由店铺托管结账界面按其默认语言呈现。
2. **INTERNAL / 备注行不译**：`note`、`price`（演示配置价）、`setup`、`glossary`、`placeholder-map` 等内部操作者行与占位说明，不进入字典。
3. **规格表占位参数**：PDP 规格表中待店铺实配确认的参数（尺寸、重量、材质、颜色、兼容机型清单等）占位行，不译。
4. **挑战逐日与邮件正文**：7 天挑战 Day 1–7 逐日任务全文、Day 8+ 培育邮件正文、AI 生成脚本/分镜/草稿全文，不逐句进入字典。
5. **法律待核条款**：法律主体名称、管辖法律/地、责任上限、知识产权、免责声明等尚未定稿条款，不译。
6. **例外页本身**：`judge-guide-zh.txt` 为面向中文评委的整页中文例外，已是中文，不在字典内重复翻译；首页顶部中文条同此处理。

## 三、校验记录

- JSON 可被 `json.load` 解析；无重复键；键总数以 `i18n_zh.json` 内 `zh-CN` 条目为准。
- 每个英文键作为子串在 23 个 `pages/*.txt` 中匹配存在（逐字核对，大小写敏感）。
- 本轮未改动 23 个 txt 正文，未重建主文案包 / 品牌定稿 / 速览卡 docx。

## 四、主题组件区块新增键（代码包来源，仅登记本批新增）

来源：`sections/ss-trust-row.liquid`、`sections/ss-scene-trio.liquid`、`sections/ss-ai-band.liquid`、`sections/ss-challenge-band.liquid`、`assets/ss-popup.js`、`snippets/ss-bundle-slot.liquid`、`mock-preview.html`。schema 内编辑器标签（区块名、设置项名、block 名）不进入字典；键为顾客可见的英文串逐字。

- **ss-trust-row.liquid（信任条短句）**：Free US shipping over $35；30-day returns；ShotStarter AI script assistant；Secure checkout（已在册，复核一致）。
- **ss-scene-trio.liquid（场景三列）**：标题 Steady shooting / Desktop demos / Clean & care；定位句 Stable framing for talking-head and product clips. / Compact stands for desk-side setup. / Keep lenses and phones clear between takes.
- **ss-ai-band.liquid（AI 三步 + 按钮）**：区块标题 Turn one product into a ready-to-shoot set；步骤 Choose your platform / Pick your product and point / Get script, storyboard and copy；按钮 Try the AI assistant。
- **ss-challenge-band.liquid（挑战表单）**：副标 One short video a day. Templates and prompts included.；邮箱字段 Email address；退订小字 You can unsubscribe at any time. We never share your email.；同意句、提交按钮（Join the challenge）已在册，复核一致。
- **ss-popup.js（留资弹窗）**：关闭 Close；标题 Get your first-order code；正文 Join the challenge list and we'll email you the code.；提交 Get the code；成功态标签 Your code；优惠码说明 Single items only; bundle kits are excluded and the code does not stack with STARTERKIT. You can unsubscribe at any time.
- **捆绑裸标题**：Creator Starter Kit；Pro Creator Kit（套装专有名，译文保留原英文）。

> 本批仅追加上述组件键；第一至三节旧口径未改。组件键命中范围为主题代码包（liquid/js/html），不要求在 `pages/*.txt` 中出现。

## 五、语言走查残留补键（探针/DOM 实际串）

来源：`shotstart-store-evidence/走查报告_1120_阶段二前半_合并.json` 的 `f_language_switch.residualDefects`，以及 `语言切换探针_1120_desktop.json` / `语言切换探针_1120_mobile.json` 的 `bodyHead` DOM 文本。键为线上 DOM 逐字串。

- **页头导航**：Home；7-Day Challenge；More links。Shop、About、Contact 已在册，复核一致。
- **Hero 引导小字（eyebrow）**：For beginner creators and small shop owners。
- **图片占位**：Scene image（首屏/三列图未选图时的占位文案）。
- **两捆绑卡标题**：Creator Starter Kit、Pro Creator Kit 已在册；套装为专有名，译文保留原英文。

**本批未纳入**
- 平台托管组件默认串（如购物车抽屉 "Taxes and shipping calculated at checkout"）：属结账/抽屉托管 DOM，按第二节排除口径不进字典。
- `mock-preview.html` 中未上线的页脚草稿链文本（All gear / Starter kit / Pro kit / Support / Newsletter / Subscribe 等）：本地镜像草稿，未在线上 DOM 检出，不入字典。
- schema 编辑器标签（区块名、设置项名）仍不进入字典。

## 六、页头/抽屉/PDP 按钮与排印升级补键（批 3 + 批 4）

来源：线上主题配置转储 `scripts/theme-dump-1120/config__settings_data.json`、走查报告 DOM 样本、语言切换探针；批 4 排印拆 span 配套短词。仅登记本批新增键，前几节旧口径不动。

### 批 3：页头图标 / 购物车抽屉 / PDP 按钮（12 键）
- **页头图标标签（配置 icon_text，图标态 aria/提示串）**：Search；Account；Cart。
- **加购成功提示与抽屉按钮**：View cart。
- **抽屉推荐位**：You may also like；View all。
- **PDP / 快速加购弹窗按钮（按 DOM 与配置逐字，保留大小写变体）**：Buy Now；Buy now；Add to cart。
- **抽屉免邮进度条与倒计时（保留占位符）**：Buy {amount} more to enjoy Free Shipping；Your cart is reserved for {countdown}!。
- **抽屉小计行**：Taxes and shipping calculated at checkout。

### 批 4：hero 拆 span 与短编号标题（4 键）
- **hero 主标题混合字重拆分段**：Your first shot；starts here.（整句键 "Your first shot starts here." 仍在册）。
- **区块短编号标题（后台改名为短词时命中）**：GEAR；AI ASSISTANT。

### 本批未纳入（线上未检出 / 排除口径）
- 抽屉结账按钮裸串 "Checkout"：探针未捕获其逐字 DOM 文案；结账托管深层 DOM 仍按第二节排除，待实捕后再补。
- 公告栏整句 "Free US shipping over $35 · 30-day returns · Weekly creator tips"：线上公告 app 已禁用、双端均无公告栏，未检出逐字串，不臆造入键。
- 页脚列标题 Shop / Support / Policies / About、Newsletter、Subscribe、退订句、mock 版权行：线上页脚仅版权 + 辅助菜单 + 政策链，无订阅模块与列标题；mock 草稿文本不入字典。
- PDP 默认徽章 "Free worldwide shipping" / "Enjoy free shipping on every order,"：与 US-only、$35 门槛口径冲突，属待修缺陷，不译入字典。
- "See detail"：快速加购弹窗查看详情按钮在配置中关闭（enable_view_more_details_button=false），不可见，不入。
- 库存紧张 "🔥Only {n} left!" / "Only N item(s) left in stock!"、"N people are viewing this right now"：动态计数串且为待修虚假社交证明/库存缺陷项，不入。
- Judge Guide：中文例外页入口，白名单不译。

## 七、扩品/分类/页脚公告补键（批 5 + 价格修正批 + 扩品批遗留）

来源：`shotstart-theme-custom/mock-preview.html` 逐字串、线上主题配置转储、主文案包新 PDP 标题。仅登记本批新增与改名键；前几节旧口径不动。

### 7.1 集合/分区标题与分类短词
- All Gear；Gear；Kits；KITS；GEAR（大小写逐字双份保留，按源码实际大小写命中）。
- Stability & Height；Desk & Angle；Clean & Care；Carry & Set Up（用途分组短标题，后台启用分组时命中）。
- Pairs well with（PDP 推荐位标题）。

### 7.2 页脚列标题 / 链接 / 订阅 / 版权（mock 草稿口径，逐字）
- Support；Policies；FAQ；Newsletter；Subscribe；All gear；Starter kit；Pro kit；Starter Kit；Pro Kit。
- 版权行整句：© 2026 ShotStart. All rights reserved.
- 公告栏整句：Free US shipping over $35 · 30-day returns · Weekly creator tips（译文：美国满 $35 免邮 · 30 天退货 · 每周创作者技巧；weekly tips 为演示配置）。
- Shop / About / Contact / 四条政策链已在册，本批复核未重复入键；退订句 "You can unsubscribe at any time. We never share your email." 已在册。

### 7.3 四个新单件 SPU（卡名 + PDP 整句标题）
- Mini Ball Head；Mini Ball Head — Level Your Frame in One Twist。
- Magnetic Mount；Magnetic Mount — Snap Your Phone On and Off in Seconds。
- Microfiber 3-Pack；Microfiber 3-Pack — Soft Cloths for Between-Take Cleaning。
- Shot List Cards；Shot List Cards — Plan Your Four Shots Before You Press Record。

### 7.4 Pro 捆绑键随新组合改名（旧英文键移除，新英文键入册）
- 组合改为：三脚架 + 延长杆 + 迷你云台 + 收纳包；标价 $62.96，用码 $53.52，省 $9.44。
- 改名键：Pro 区块标题、Pro 卡片描述、Pro 整句卡片描述、Pro 套装价句、Pro Section title 前缀句，共 5 条；旧 58.96 / 50.12 / 8.84 英文键不再在册。

**批 5 收尾复核（终冻前）**：逐条检索旧 Pro 英文串，终版字典 0 残留，以下 5 条旧键已退役、不再在册：
1. `Section title: The Pro Kit: lighting, background, and reach for the next level.`
2. `The Pro Kit: lighting, background, and reach for the next level.`
3. `Card description: Pro Creator Kit — a carry case, reflector, backdrop cloth, and extension pole for the next level of setup.`
4. `Pro Creator Kit — a carry case, reflector, backdrop cloth, and extension pole for the next level of setup.`
5. `Kit price $58.96 — use code STARTERKIT at checkout: $50.12. You save $8.84.`

退役原因：旧 Pro 成员为收纳包 + 反光板 + 背景布 + 延长杆，现组合与定价已变更，上述英文源节点在 `shotstart_content.py` 与 `pages/*.txt` 全库均不存在；字典内不含 58.96 / 50.12 / 8.84，也不含 reflector/backdrop 作为 Pro 成员的描述串。反光板、背景布仅保留单件卡名与单件整句标题键（退出 Pro 后的单件口径）。注：收纳包旧价 16.99 已改为 12.99；延长杆终版零售为 16.99（合法新价，非旧价泄漏）。

## 八、延长杆改价 + AI 区块补键 + 译文润色 + 删标注批

### 8.1 价格纠错
- Extension Pole 零售 $13.99 → **$16.99**（Core 层口径；后台旧 13.99 正由建站改价）。页面 PDP 价格行、Pro 捆绑组件清单、Shop 卡片、judge-guide 价格表、速览卡价格表同步。
- Backdrop Cloth 维持 $13.99；Creator Carry Case 维持 $12.99；二者与延长杆新价不冲突。`16.99` 不再属旧价泄漏黑名单，命中语境仅限延长杆单件与 Pro 组件清单。

### 8.2 AI 区块补键（首页 AI Band 可见串，源 `shotstart_content.py`）
- `Tell ShotStarter your platform (TikTok, Instagram Reels, YouTube Shorts, or another), your product type, and the one selling point you want to lead with. It drafts a 15-second script, lays out a four-shot storyboard, and suggests a caption and publish-ready text you can edit before posting.` → 把你的平台（TikTok、Instagram Reels、YouTube Shorts 或其他）、商品类型和想主推的一个卖点告诉 ShotStarter。它会起草 15 秒脚本，排出四镜分镜，并给出可供发布前自行编辑的文案与成稿。
- `15-second script draft tailored to your platform and product` → 按你的平台和商品定制的 15 秒脚本草稿。
- `Four-shot storyboard: hook, close-up, demonstration, closing line` → 四镜分镜：钩子、特写、演示、收尾。
- `Caption and publish-ready copy to review and personalize` → 可供审阅与调整的文案与成稿。

### 8.3 译文润色（英文键逐字未动，仅改 zh）
- `I agree to be contacted about my question.` → 我同意接收与我的咨询相关的回复邮件。（联系表单与挑战框共用同串；前缀目录孪生键 `Contact: I agree...` 同步润色。）
- `Responsive support by email` → 邮件响应支持。

### 8.4 删标注批（前台自我说明移除）
- 移除 PUBLISH 中的 illustration/demonstrated/demo configuration/示例/AI 生成示意等自述；12 个 PDP 区块标题 `Demo Pricing` → `Pricing`；营销页标题去掉 `(Demo Configurations)`；judge-guide 去掉演示配置/演示路线措辞（保留码、路径、验收点）。逐句删前→删后见 `shotstart-copy/已删除标注清单.md`。
- 本轮删除的前台英文串未在册，无英文源键退役；字典内 INTERNAL/setup/note 注记保留不上前台。
- 未命中候选（mock/线上/源码均无逐字串，未入键）：Three steps from a blank page…；Tell it what you sell and who buys.；Describe your product and audience in one line.；Get a script and a shot list.；Hooks, scenes and camera notes in seconds.；Generate your first frames.；Prompts you can paste into any image tool.；Open ShotStarter AI；Shop the gear；Regular price；USD；`7-DAY CHALLENGE` 大写字面（DOM 实际为 `7-Day Challenge`）。hero/挑战/AI 区块截图中的烘焙道具文案（Simple gear. Real videos. 等）为图片内光栅文字，非可选 DOM，不入键。

### 8.5 终版键数
- 终版 **249 键**（上一版 245 + 本节 AI 区块 4 键；无退役键）。JSON 可解析、无重复/空值/键内 CJK；matched nowhere 仍为 4 个前瞻分组标题键。

### 本批仍未纳入
- 抽屉结账按钮裸串 "Checkout"：探针未捕获逐字 DOM 文案，托管结账深层仍排除。
- PDP 默认徽章 "Free worldwide shipping" 等与 US-only 口径冲突的待修缺陷串；动态库存/浏览人数串；See detail（按钮关闭）；Judge Guide 例外页。
- 支付方式 aria-label（Visa / Mastercard / American Express / PayPal / Payment methods）：第三方支付标识，未入键。

## 九、批 6：前台中文全覆盖补译（PDP 整串 + 政策 + About + 集合 + 弹窗 + 挑战 + 营销）

### 9.1 范围与口径
- 源：`pages 27 txt`（唯一内容数据源 `shotstart_content.py`）。键 = 英文逐字整串（段落级），角色前缀取冒号后裸句，前缀目录孪生键同步保留；zh 保持真实在售口吻，不虚构销量/评分/认证/库存/保修，参数中性兜底。
- 本批按 PUBLISH 块类型提取；`note / price / setup` 内部注记、含 `[待确认: …]` 子句的串、编辑器脚手架标题、占位键、法律待核条款不入字典。

### 9.2 新增覆盖分组
- **14 个 PDP**：副标 Highlights 每条、描述每段、规格表标签与中性值、箱单每条、场景句、FAQ 每 Q 每 A、单件/套装搭配句；12 单件 + 4 新 SPU（Mini Ball Head / Magnetic Mount / Microfiber 3-Pack / Shot List Cards）全覆盖。
- **政策四页**：标题 + 每段（Shipping / Refund / Privacy / Terms），含章节标题（Order Processing、Return Eligibility、What We Collect、Use of the Store 等）。
- **About**：页面标题 + 正文整段。
- **集合副标题**：源内仅 2 条（All Gear、Creator Kits），已在册；无第 3–5 条副标题可补。
- **弹窗**：headline `Your first discount is one click away.`、body `Submit to get your welcome code NEWCREATOR10.`、按钮 `Save my spot`、退订 Fine print、联系页入口 `Or leave your email on the Contact page`。
- **挑战页**：H1、引言、规则 bullets、Day 1–Day 7 任务段、成功态、Day 8+ 三封培育邮件（Subject / Preheader / Body）、复购钩子句、流失唤醒邮件、参与者优惠口径句。
- **购物车/结账块**：加购确认、数量控件、总额重算、凑单示例、优惠码输入/应用/已应用、码规则、地址校验、无隐藏费用、售前咨询、订单确认页标题/正文/订单号/物流/继续购物/联系链接。
- **营销页**：两捆绑组件清单句、两条 Consumer copy、新客码句、订阅句、UGC 话题墙概念句与展示句。
- **追加批短串**：`SCENES` 分区标题；烤字 10 条（Hero / 挑战 / AI 区块图片内文字，供 zh 态 HTML 头组改用）：`Simple gear. Real videos.`、`One small task a day. Publish your first video.`、`Scripts, storyboards and captions — drafted for you.`、`Gear + AI content assistant for new creators.`、`Join the 7-Day Challenge`、`Your AI content assistant.`、`SHOTSTART · FOR BEGINNER CREATORS`、`MEET SHOTSTARTER`、`FREE · 7 DAYS · YOUR FIRST VIDEO`、`SHOTSTART`（品牌保留不译）。

### 9.3 退役与口径修正
- 退役旧邮件投递承诺键 `Join the challenge list and we'll email you the code.`（旧 zh「优惠码将邮件发送给你」同步移除）；弹窗 body 口径改为提交后即时显码 `Submit to get your welcome code NEWCREATOR10.` → 提交后即可获取欢迎码 NEWCREATOR10。源 `shotstart_content.py` L174 已同步改写。
- 合规保留：挑战成功态 `Check your inbox for Day 1`（同意订阅挑战邮件序列）、营销订阅文案（同意口径）、即时显码成功句，均不属邮件承诺违规。

### 9.4 排除项（未入键）
- Judge Guide 中文例外条 1 条；form-states 编辑器脚手架标题 1 条；Growth Metrics 漏斗定义 5 条（Signups / Participants / Engagement / Purchase / Tools，内部 admin 指标）。
- 沿用 8.4 未命中口径：`Three steps…`、`Tell it what you sell…`、`Describe your product…`、`Get a script and a shot list.`、`Hooks, scenes…`、`Generate your first frames.`、`Prompts you can paste…`、`Open ShotStarter AI`、`Shop the gear`、`Regular price`、`USD`、`7-DAY CHALLENGE` 大写字面——mock、线上转储与源码均无逐字 DOM，未入键。
- 抽屉结账裸串 `Checkout`、动态库存/浏览人数、平台托管深层 DOM、第三方支付标识、冲突徽章串仍排除。

### 9.5 终版键数与校验
- 终版 **661 键**（上一版 249；退役 1；本批新增 413：裸句 350 + 前缀孪生 63）。
- JSON 可解析；无重复键、无空值、无键内 CJK；evidence-only 0；matched nowhere 1 条（`Gear + AI content assistant for new creators.`，Hero 烤字前瞻键，待 zh 态 HTML 头组落地后命中）。
- 基线复跑：check_placeholders Unmapped 0；scan_publish 占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0；scan_docx 三 docx 泄漏 0；final_check forbidden 0。三 docx 统计：主包 1091 段 / 17 表、品牌 50 / 5、速览卡 24 / 4；pages 27 个 txt；发布快照 6 页 SAME、cart 块保留。

## 十、复扫 v2 残留小批补键（省额 chip / 联系页 h2 / 搜索框）

### 10.1 新增键（6 条，无退役）
- `Save $6.75` → 省 $6.75（Starter 套装价格角标独立串；源内整句 `You save $6.75.` 已在册）。
- `Save $9.44` → 省 $9.44（Pro 套装价格角标独立串；源内整句 `You save $9.44.` 已在册）。
- `Other Contact` → 其他联系方式（联系页 h2，源 `shotstart_content.py` L1071）。
- `Search products` → 搜索商品（站内搜索框占位/标签，线上 DOM）。
- `Thanks — here is your welcome code: NEWCREATOR10` → 感谢提交——你的欢迎码：NEWCREATOR10（表单成功面板即时显码态，不承诺邮件投递）。
- `Thanks — you're subscribed.` → 感谢订阅。（表单订阅成功面板）

### 10.2 复扫 v2 候选定性（去重清单 113 条）
机械三档比对（audit_v2.py：字典 + pages 27 txt 拼接 + 候选 JSON；跳过 CJK / hex / noscript / token）：pages 内逐字存在但未在册 14 条，已在册 7 条，不在 pages 102 条。
- **入键 1**：`Other Contact`（前台联系页区块标题）。
- **不补 13**：
  - `Bundle Entry` / `Specification` / `Rule`：编辑器/模板分区标题，沿用 9.1 脚手架标题排除口径，待建站转发模板标题逐字串后统一处理；`Rule` / `Specification` 与源内 `Rules` / `Specifications` 非逐字一致，不补。
  - `Confirm` / `Send` / `Show` / `Quantity` / `Creator Kit`：平台表单、数量控件、导航/模板碎片 chrome，非源内独立整串（多为子串命中）。
  - `Q: How do I hang it?` / `Q: Will it fit my phone?`：裸问句 `How do I hang it?` / `Will it fit my phone?` 已在册，`Q:` 为模板前缀，非源串。
  - `Creator Starter Kit (bundle)` / `Pro Creator Kit (bundle)`：Judge Guide 例外页表内条目，内部页排除。
  - `EN`：语言切换按钮 chrome。
- **不在 pages 102 条归因**：OCR/编码掉字母的 FAQ / 箱单 / Day 1–7 / Rules 乱序串（源内整句批 6 已入键）；托管结账与注册 chrome；judge-guide 中文例外条；hex 色值 / noscript / token；线上环保与支付承诺信任块（源 `trust_blocks()` 五条已在册，线上模板信任行与源非逐字一致，归建站回写根因）。

### 10.3 终版键数与校验
- 终版 **674 键**（批 6 终冻 661 + 本批 13：省额 chip 2 + 联系页 h2 1 + 搜索框 1 + 表单成功面板 2 + 分区标题 7；无退役）。
- check_i18n3：JSON 可解析；无重复键、无空值、无键内 CJK；matched nowhere 0；evidence-only 1（`Highlights`，线上模板标题，后台脚手架标签为 `Selling Points (bullets)`）；code-only 72。
- 基线复跑：check_placeholders Unmapped 0；scan_publish 占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0；scan_docx 三 docx 泄漏 0。
- 演示重嵌随建站注入批一次执行，本批不重嵌；主题包 `ss-i18n.js` 内嵌旧字典与旧计数注释不由本批维护。

### 10.4 PDP / 信任区分区标题（建站逐字回报，7 条）
线上模板渲染的裸标题字面（后台脚手架别名见括号），建站回报后入键：
- `Description` → 商品描述（后台标签 `Description Paragraph`）。
- `Highlights` → 亮点（后台标签 `Selling Points (bullets)`；源内无逐字串，evidence-only）。
- `Specifications` → 规格（源 h2 逐字一致）。
- `What's in the Box` → 箱单（源 h2 逐字一致）。
- `Use Scenarios` → 使用场景（源 h2 逐字一致）。
- `Shopping Trust` → 购物保障（后台标签 `Shopping Trust (generic; no certification claims)`，裸标题入键；不含认证/奖项承诺）。
- `Bundle Entry` → 套装入口（原 10.2 脚手架排除项，建站回报线上标题后补入；规则句已在册）。
- 口径备注：`Description` / `Highlights` / `Shopping Trust` 裸标题与后台脚手架标签非逐字同名，差异归建站后台回写；译文保持中性，不补材质/尺寸/认证。

## 十一、复扫 v3 变体键批 + SEO 元信息批

### 11.1 复扫 v3 候选定性（去重清单 113 条，audit_v3.py 三档）
机械比对：字典 + `shotstart_content.py` + pages 27 txt 拼接 + 候选 JSON；跳过 CJK / hex / noscript；`Q:` / `A:` 前缀剥离后再匹配。结果：源内逐字且缺键 19、已在册 60、不在源 27、skip 34。
- **入键**：套装前缀 1、Day 标题 7、Day 正文 7、挑战分区标题 3、集合名 1（清单见 11.2）。
- **不补（平台 chrome / 动态 / 例外页）**：`Availability` / `Price` / `Show` / `Out of stock`（集合排序筛选与库存状态 chrome，动态库存口径排除）；`EN`（语言切换按钮）；`Creator Starter Kit (bundle)` / `Pro Creator Kit (bundle)`（judge-guide 例外页表内条目）；`1 sold`（动态计数）；`In stock` / `Newest in` / 各排序选项 / `Pageviews, high to low` / `Purchases, high to low` / `Total sales, high to low`（集合排序 chrome）；`Clear all` / `Close preview` / `Hide bar` / `You're previewing:` / `Recently viewed` / `Your cart is empty` / `Your cart is reserved for` / `Verification code` / `Re-send again` / `Have not get verification code?`（平台表单/预览/购物车 chrome）；`404 | Page Not Found` / `The page you are looking for cannot be found.`（平台 404）；`Reformia`（平台残留名，非源）。
- **不补（源非逐字，归建站回写）**：两条 Pro 套装线上旧文句；线上环保/支付/承诺信任块四句（`Designed with the planet in mind…` / `Shop with confidence…` / `Your payment information…` / `Secure payments`，源 `trust_blocks()` 五条已在册，模板信任行与源非逐字一致）；两条 FAQ 兜底截断变体（reflector `pending final confirmation`、refill `still being finalized; contact u`，源占位句在册对应兜底键，线上变体截断/混编不补）。

### 11.2 本批新增键（19 条，无退役）
**套装前缀**
- `What's in the kit:` → 套装内含：

**挑战页 Day 1–7 半键（strong 标题 7 + 独立 p 正文 7，共 14；按 `pages/challenge.txt` 逐字拆分）**
- 标题：
  - `Day 1 — Pick your topic and selling point.` → Day 1 — 选定选题与卖点。
  - `Day 2 — Plan your 15-second script.` → Day 2 — 规划 15 秒脚本。
  - `Day 3 — Set up your shot.` → Day 3 — 布置机位。
  - `Day 4 — Shoot four storyboard clips.` → Day 4 — 拍摄四个分镜片段。
  - `Day 5 — Assemble your cut.` → Day 5 — 剪辑成片。
  - `Day 6 — Write the publish caption.` → Day 6 — 撰写发布文案。
  - `Day 7 — Publish and review.` → Day 7 — 发布与复盘。
- 正文：
  - `Write down your product or topic and the one point you want viewers to remember. Use ShotStarter to set your platform and product type.` → 写下你的商品或选题，以及想让观众记住的一个要点。用 ShotStarter 设置平台与商品类型。
  - `Generate a draft script with ShotStarter; edit the opening line so it sounds like you.` → 用 ShotStarter 生成脚本草稿；修改开场台词，让它听起来像你自己。
  - `Choose a flat surface or tripod/stand position; clean your lens; frame your first shot.` → 选择平整表面或三脚架/支架位置；清洁镜头；构图拍下第一个镜头。
  - `Follow the four-shot storyboard: opening hook, product/topic close-up, middle demonstration, closing line. Record each clip.` → 按四镜分镜执行：开场钩子、商品/选题特写、中段演示、收尾台词。逐段录制。
  - `Trim clips to a 15-second pace; add simple captions; check lighting and focus.` → 把片段剪成 15 秒节奏；添加简单字幕；检查光线与对焦。
  - `Use the ShotStarter caption draft; add your own voice, relevant hashtags, and a clear call to action.` → 使用 ShotStarter 文案草稿；加入你自己的表达、相关话题标签与明确的行动号召。
  - `Post your first short video, note what worked, and plan your next clip.` → 发出第一条短视频，记录效果好的地方，并规划下一条片段。

**挑战分区标题 / 集合名**
- `Rules` → 规则
- `Daily Tasks` → 每日任务
- `Thank-You Message` → 致谢信
- `Creator Kits` → 创作者套装

### 11.3 Pro 套装第二段核查（以当前 pages txt 源为准）
- 源两条逐字句均已在册：`Pro Creator Kit — a tripod, extension pole, mini ball head, and carry case for the next level of setup.`；`The Pro Creator Kit adds steady framing, height and angle control, and a carry case for creators moving beyond the basics.`（裸句 + 前缀孪生键均在册）。
- 线上候选两条旧文混编句（`…stable framing, height, angle control…` / `…steady support, reach, one-twist angle control…`）与源非逐字一致，归建站后台回写；字典键不改、不补变体。

### 11.4 SEO 元信息与 About 核查
- 五个集合 meta description 定稿交建站写入，清单见 `tools/seo_meta_descriptions.md`（All Gear / Stability & Height / Desk & Angle / Clean & Care / Carry & Set Up）；元信息字段不入前台字典。
- About 页：`pages/about.txt` 三段 PUBLISH 正文不含创立时间、所在地、法律主体名称；主体占位仅存于 `[INTERNAL]` 注记、`placeholder-map.txt` 映射行与 judge-guide 例外表，构建脚本以 INTERNAL 斜体写入内部备注区，前台无泄漏（scan_docx 泄漏 0）。包内无 About meta description 字段；建站补写时用中性品牌句，不虚构主体/日期/地点（参考句见清单）。
- judge-guide 保持公开（评委入口既定口径），本轮未改。

### 11.5 终版键数与校验
- 终版 **693 键**（上一版 674 + 本批 19：套装前缀 1 + Day 半键 14 + 挑战分区标题 3 + 集合名 1；无退役）。
- check_i18n3：JSON 可解析；无重复键、无空值、无键内 CJK；evidence-only 0；matched nowhere 0；code-only 73。
- 基线复跑：check_placeholders Unmapped 0；scan_publish 占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0；scan_docx 三 docx 泄漏 0。
- 演示重嵌随建站注入批一次执行；主题包 `ss-i18n.js` 内嵌旧字典与旧计数注释不由本批维护。

## 十二、round10 扣分闭环批（比赛日 08:00 签到口径）

### 12.1 集合筛选 / 计数 chrome 补键
- `Filter` → 筛选；`Availability` → 库存状态；`Price` → 价格。
- 模式条目（引擎复数/计数实现，字典 `_meta.plural_patterns`，不计入前台键数）：`{{count}} Products` → `{{count}} 件装备`。
- `Sort`：线上未捕获独立标题串，暂缓入键；待建站转发集合筛选/排序模板标题逐字串后统一补。

### 12.2 PDP FAQ 答案与箱单审计（12 单件）
- 方法：源 `faq_a` 先经 `publish_text` 把 `[待确认: …]` 占位替换为线上兜底串，再逐条比对字典键；`Q:` / `A:` 前缀由引擎剥离不入键。
- 36 条 FAQ 答案全部在册：27 条兜底答案本轮补入（含 1 条英文键在两个 PDP 复用，按唯一键入一次）；8 条无占位纯答案此前已在册；1 条重复英文键未重复加。
- 182 条箱单 / 卖点 bullets 全部在册，missing 0。
- FAQ 答案内联兜底从句（`still being finalized; contact us for details.` 等）保留；仅删除 specs 段整句兜底（见 12.3）。

### 12.3 退役键 19 条（源已改写 / 整句删除）
**退役 12 条 specs 段兜底整句**（12 单件 PDP specs 段整句从源删除，FAQ 内联从句不在此列）：
- 12 条 `Exact … are being finalized; contact us for details.` 整段，清单见 `tools/patch_r10.py` 的 `DROP_SPECS`。

**退役 7 条旧承诺 / 旧文案键**（源去收信承诺、隐喻中性化后被新句替换）：
- 联系表单旧承诺句（裸句 + `Contact form:` 前缀孪生）：`Thanks for reaching out. We've received your message and will reply by email.`
- 挑战报名旧收信箱句（裸句 + `Challenge sign-up:` 前缀孪生）：`You're in! Check your inbox for Day 1. …NEWCREATOR10…`
- 挑战成功旧句：`You're in! Check your inbox for Day 1. Remember: your first shot starts here.`
- refill 旧隐喻句（裸句 + `Refill reminder:` 前缀孪生）：`…restock the Lens Cleaning Kit to keep every new clip sharp.`

### 12.4 新增键 37 条（成功 / refill 新句 7 + chrome 3 + FAQ 27）
**表单 / 挑战成功态（去收信与回复时限承诺）**
- `Contact form: Thanks for reaching out. We read every message.` → 联系表单：感谢留言，我们阅读每一条留言。
- `Thanks for reaching out. We read every message.` → 感谢留言，我们阅读每一条留言。
- `Challenge sign-up: You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — …` → 挑战报名：你已加入。Day 1 见下方——开始拍摄吧。首单优惠码 NEWCREATOR10——…
- `You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — …` → 你已加入。Day 1 见下方——开始拍摄吧。…
- `You're in. Day 1 is below — start shooting. Remember: your first shot starts here.` → 你已加入。Day 1 见下方——开始拍摄吧。记住：你的第一个镜头，从这里开始。

**refill 中性句（隐喻 sharp 去除）**
- `Refill reminder: when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots.` → 补充提醒：清洁布或气吹用旧时，在拍摄间隙补充镜头清洁套装。
- `when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots.` → 清洁布或气吹用旧时，在拍摄间隙补充镜头清洁套装。

**集合 chrome**：`Filter` / `Availability` / `Price`（见 12.1）。

**FAQ 兜底答案 27 条**：映射清单见 `tools/patch_faq28.py` 的 `ZH`；译文沿用既定中性口径（“正在定稿；详情请联系我们”），不补材质/尺寸/认证。

### 12.5 隐喻与断言清理（源侧，同步 txt / docx）
- refill 钩子句结尾 `keep every new clip sharp` → `between shoots`（功效隐喻改中性，不承诺成片质量）。
- glossary / judge-guide 表 restocking 行：`演示默认无；正式营业前法务复核` → `补货手续费（退货条款以法务定稿为准）`。
- 12 单件 specs 段兜底整句源侧整段删除；FAQ 答案内联兜底从句保留。
- judge-guide 保持公开（评委入口既定口径），本轮未改。

### 12.6 价格对账（未擅改价，待上线前复核）
- Starter 套装：Tripod $19.99 + Stand $14.99 + Lens Cleaning Kit $9.99 = $44.97，券后 $38.22，省 $6.75（44.97−38.22）✓。
- Pro 套装组件单价实加总：Tripod $19.99 + Extension Pole $16.99 + Mini Ball Head **$11.99** + Carry Case $12.99 = **$61.96**；捆绑 SPU 标价 **$62.96**，用码 STARTERKIT 后 $53.52，省 $9.44（62.96−53.52）。标价与组件加总差 **$1.00**。
- 复核结论：61.96 为组件单价加总，62.96 为捆绑标价，两者口径不同；指令预设 ball head $12.99 系笔误，源实为 $11.99。$1.00 价差属捆绑定价配置，源价未改，待评审 / 建站上线前确认。
- **勘误（round11，见第十三节）**：本条 61.96 / $1.00 价差结论已推翻。映射表 L4/L18/L63 与线上实测一致，Mini Ball Head 单价为 **$12.99**；源内 $11.99 系陈旧笔误，已纠正。Pro 组件加总 19.99+16.99+12.99+12.99=**62.96**，与捆绑标价闭合，**不存在 $1.00 价差**。

### 12.7 终版键数与校验
- 终版 **711 键**（上一版 693 − 退役 19 + 新增 10 + FAQ 27；模式条目置于 `_meta` 不计键）。
- check_i18n3：JSON 可解析；无重复键、无空值、无键内 CJK；evidence-only 0；matched nowhere 0；code-only 74（主题代码既有口径）。
- 基线复跑：check_placeholders Unmapped 0；scan_publish 占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0；scan_docx 三 docx 泄漏 0。
- pages 27 txt 与三件 docx 已按改后源重建：主包 1079 段 / 17 表（较基线 1091 段减 12 条已删 specs 段）、品牌定稿 50 段 / 5 表、速览卡 24 段 / 4 表。
- 演示重嵌随建站注入批一次执行；主题包 `ss-i18n.js` 内嵌旧字典与旧计数注释不由本批维护。

### 12.8 交演示 / 建站改动说明
- 字典终版 711 键随本批交付；成功态新英文串以 12.4 为准，ss-forms 两成功面板需同步替换：
  - 挑战报名成功态：`You're in. Day 1 is below — start shooting.`（不承诺收件箱，Day 1 在页面下方）。
  - 联系表单成功态：`Thanks for reaching out. We read every message.`（不承诺回复时限；原 `will reply by email` 已去除）。
- 待建站转发：集合 `Sort` 独立标题串；线上原生信任块 / 模板区块标题逐字串；到达后再入键，未提前臆造翻译。
- ~~Pro 捆绑标价与组件加总 $1.00 价差、ball head 单价口径，上线前复核定价。~~（round11 已闭合，见第十三节；ball head $12.99，Pro 加总 62.96 与标价一致。）

## 十三、round11 价格纠偏 + 联系中性化 + 面板 chrome 补键批（回连续跑封板）

### 13.1 套装价格对账闭合（计算器复核，推翻 12.6 旧结论）
- Starter：Tripod $19.99 + Stand $14.99 + Lens Cleaning Kit $9.99 = **$44.97**；STARTERKIT 15%：44.97×0.85=38.2245 → **$38.22**；省 44.97−38.22 = **$6.75**。
- Pro：Tripod $19.99 + Extension Pole $16.99 + Mini Ball Head **$12.99** + Carry Case $12.99 = **$62.96**；62.96×0.85=53.516 → **$53.52**；省 62.96−53.52 = **$9.44**。
- 结论：Pro 组件加总 62.96 与捆绑标价 62.96 闭合，**不存在 $1.00 价差**；12.6 条 61.96 / $1.00 系 ball head 价误判所致，已销。cleaning-kit $9.99、cleaning-refill $7.99 等其余单件价不变。

### 13.2 四件单件价纠偏（映射表 L4 + 线上实测为准；源内列表 bullet / PDP price 行 / 价格表 / 中文自述全改）
| 商品 | handle | 旧（源笔误） | 新（映射表 + 实测） |
| --- | --- | --- | --- |
| Mini Ball Head Mount | mini-ball-head | $11.99 | $12.99 |
| Magnetic Phone Mount | magnetic-mount | $9.99 | $11.99 |
| Microfiber Cloth 3-Pack | microfiber-3pack | $8.99 | $6.99 |
| Shot List Cards | shot-list-cards | $6.99 | $8.99 |
- 字典受影响列表 bullet 键 1:1 退役旧价、补新价，键数不增；PDP price 行、价格表价列、中文自述段属内部 / 表格口径，不入英文字典。
- cleaning-kit 9 条 $9.99 键保留未动。

### 13.3 联系页正文两句中性化（去收信渠道与回复时限承诺；无 ESP 不承诺）
- 首段：`Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note — we read every message and reply as soon as we can. For order questions, please include your order number so we can help faster.`
- 末段：`We read every message and reply as soon as we can. This store is email-only; no physical mailing address is published.`
- 旧承诺键 `…will reply by email…`、`We reply to messages within 2 business days, by email.…` 已退役；发布快照 contact 页同步刷新。

### 13.4 本轮新增字典键（线上 DOM 实测，不臆造未检出选项）
**v4 增补（patch_r11 已入册）**
- `ShotStart — Your first shot starts here.` → 首页标题整串。
- `Sort by` → 排序；`Recommend` → 推荐；`Recommended` → 推荐。
- `Your cart is empty` → 购物车空模板；`Shop now`；`Recently viewed`；`Quantity`；`1 sold`。
- 模式条目保留：`{{count}} Products` → `{{count}} 件装备`；`{{count}} sold` → 已售 {{count}} 件（置于 `_meta.plural_patterns`，不计前台键数）。

**集合筛选 / 排序面板本轮补 7 条**（证据：复扫 v3 候选去重 + r10-brand-probe DOM）
- `Products` → 件装备（计数被拆成 "12" + "Products" 两相邻叶节点，单串键与模式条目并存；引擎跨节点逻辑由演示实现）。
- `In stock` → 有货；`Out of stock` → 缺货。
- `Newest in` → 最新上架。
- `Pageviews, high to low` → 浏览量从高到低。
- `Price, high to low` → 价格从高到低；`Price, low to high` → 价格从低到高。
- 已在册沿用：`Filter`→筛选、`Availability`→库存状态、`Price`→价格、`Search products`→搜索商品。
- 未检出不入键：Featured / Relevance 等仅见于主题 demo 预设配置与浏览器本地化串，非集合面板线上实测选项；VISA / Mastercard / PayPal 等卡组织品牌名不译不入键。

**线上 js 清单实测补 6 条**（用户直接解析线上 `ss-i18n` 脚本，quoted 命中=0 确认缺键；本地 pages/theme/evidence 快照未含，按线上实测入键）
- `Best selling` → 最畅销（排序选项；本地快照未命中，nowhere 1 属线上运行时渲染串，豁免）。
- `Checkout` → 去结账；`Subtotal` → 小计。
- `Sign in` → 登录；`Register` → 注册。
- `Recommended` → 推荐（与 `Recommend` 同译）。
- 已在册勿重复：`Search products`→搜索商品、`All Gear`→全部装备、`What's in the Box`→盒内清单、`Add to cart`→加入购物车；`Judge Guide` 既定例外页不译。

### 13.5 终版键数与四扫描（实测封板）
- 终版 **729 键**（zh-CN 节点；`_meta` 不计键）。
- check_i18n3：JSON 可解析；无重复键、无空值、无键内 CJK；evidence-only 4（Recommended / Subtotal / Sign in / Register，证据 JSON 命中）；matched nowhere 1（`Best selling`，线上运行时渲染串，按线上 js 清单实测入键豁免）；code-only 86（主题代码既有口径）。
- check_placeholders：Unmapped 0；45 个占位均有映射；动态兜底从句 6 条在册。
- scan_publish：占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0。
- scan_docx：主包 / 品牌定稿 / 速览卡三件 PUBLISH 泄漏 0、占位词 0、demo 残留 0。
- 产物重建：pages 27 txt；主包 1079 段 / 17 表，品牌定稿 50 段 / 5 表，速览卡 24 段 / 4 表；发布快照 `vm-pages-publish.json` 六页 + cart 块从当前 PAGES 重建，contact 段已切中性句，其余五页 SAME。

### 13.6 交演示 / 建站说明
- 终版 729 键随本批交付；线上当前内嵌字典解析为 693 键（旧 510 口径作废），仍缺本批 confirmed 项，建站注入时须以本终版 `tools/i18n_zh.json` 整体重嵌，勿沿用旧内嵌 `ss-i18n.js` 计数。
- 联系页两句中性化与挑战 / 联系表单成功态新串（见 12.4）同一口径：不承诺收信渠道、不承诺回复时限。
- 待建站转发：集合独立 `Sort` 标题串、线上原生信任块 / 模板区块标题逐字串；到达后再入键，未提前臆造。
- 价格以映射表 L4 口径为准；三件新单件 PDP 回链随建品回填。
