# 全球电商 UI/UX 标杆调研报告 · ShotStart 建站参考

> 用途：为 ShotStart 独立站（Shoplazza 免费主题 Reformia + Athena AI 建站）的现场优化提供可迁移的设计模式依据。
> 调研时间：2026-11-20；调研对象：创作者装备同类品牌 6 家 + 优秀 DTC/获奖电商 4 家 + 获奖公开案例 5 组与评审共性。
> 约束：只调研公开页面与公开案例分析，不深挖登录态内容；本报告不修改店铺配置、不操作 bu 浏览器。
> 配套交付：同目录《落地映射表.md》逐条给出免费可行性、Athena/主题装修落地方式、优先级与现场耗时。

## 0. 调研口径与红线

### 0.1 ShotStart 基线（本次借鉴必须对齐，不得改写）

- 市场：美国英语市场；人群：新手短视频创作者与小商家；语气平实、鼓励、无行话。
- 3 个 SPU：手机三脚架 $19.99、桌面支架 $14.99、镜头清洁套装 $9.99；三件套捆绑小计 $44.97，15% off 后 $38.22，券码 STARTERKIT；备选券 NEWCREATOR10 首单 10% off。
- 闭环：AI 助手 ShotStarter + 7 天拍摄挑战留资。
- 页面：Home / Shop / 7-Day Challenge / About / Contact + 四个政策页；主导航 Home、Shop、7-Day Challenge、About、Contact，政策链接仅放页尾。

### 0.2 信任元素红线（本报告与映射表共同遵守）

ShotStart 是演练店，无真实评价、销量、评分、奖项、资质认证与库存证据。**以下标杆做法一律不可迁移**：

- 任何评分星级、评价条数（如 Ridge 页面标注的数万评价、SmallRig 卡面 4.8 分、Elgato/Joby 评分位、Allbirds 自述双鞋销量等）；
- 销量数字、"已售 N 件"、用户数、社区规模；
- 未核实的认证徽章、奖项头衔、库存紧迫倒计时。

可使用的"信任元素"仅限**可兑现的中性文案**：免邮门槛（满 $35 美国标准免邮）、政策页链接、AI 草稿需创作者本人审核后再发布、邮件含退订入口。标杆品牌的终身保修、99 天试用、B Corp 等承诺，只有在 ShotStart 政策页具备对应条款时才可复用表述，否则只借鉴"承诺放哪里、怎么写清楚"的结构，不照搬承诺内容。

### 0.3 免费能力边界（映射可行性判定依据，帮助中心已核实）

- Reformia 免费主题区块：公告栏、页头/页尾、Hero 轮播、图文卡、商品网格、促销网格、画廊、视频 Hero、视频、图标文字、拆分轮播、图片轮播、博客文章；区块可增删、排序。
- 可新建/绑定自定义页面；主导航最多三级，页尾菜单一级；菜单可加热卖/新品角标；Page Builder 支持 FAQ 卡片。
- 嵌入应用块名单中，Popup、Reviews Flow、Trust Enhancement、Smart Recommendation 等属应用内嵌块——**本次免费约束下不得依赖**；评价类区块无免费实现；仅 3 个 SPU，无需筛选器；捆绑只能以"独立捆绑 SPU + 促销码"实现，无免费捆绑构建器。
- 来源：
  - https://helpcenter.shoplazza.com/hc/zh-cn/categories/4408574904729
  - https://helpcenter.shoplazza.com/hc/en-us/articles/22929902032153-A-Guide-to-the-Shoplazza-Theme-Editor
  - https://helpcenter.shoplazza.com/hc/en-us/articles/22929902032153-Customizing-your-store-theme
  - https://helpcenter.shoplazza.com/hc/zh-cn/articles/8888574212889-设置菜单导航
  - https://www.shoplazza.cn/athena-guide

---

## 一、创作者装备同类标杆

### 1. Peak Design（摄影/通勤装备 DTC）

来源：
- https://www.peakdesign.com/en-ch/products/everyday-sling?Size=3L&Color=Ash&Title=Default+Title&bvstate=pg%3A15%2Fct%3Ar
- https://www.peakdesign.com/products/everyday-messenger
- https://www.peakdesign.com/en-au/collections/straps

可迁移模式：

1. **捆绑/套装以变体选择呈现，而非强塞弹窗**：商品页把套装与单卖放在同一选择器内（单包 / 套装），用户在产品语境里比较两档，加价构成透明。ShotStart 可借鉴"三件套捆绑作为一个可比较选项"的呈现方式。
2. **变体选择器前置、选项文案具体**：颜色/容量等选项直接显示在主图下方，选择后价格与主图联动；不把变体藏进折叠菜单。
3. **缺货/不可用状态明示**：缺色或缺货选项置灰并标注，不保留可点但下不了单的入口。ShotStart 当前为演示库存，应保持商品可加购，不留失效变体。
4. **信息标签页组织长描述**：商详用 Materials / Fit & Details / Care 等标签页分段，避免首屏一屏到底堆参数文案。
5. **产品线分组陈列**：集合页按 strap / sling / messenger 等品类分组，先按用途再按型号浏览；首页棚拍与真人场景混排，产品图与使用环境交替出现。

取舍：其可持续材料、可维修等品牌承诺属企业事实，ShotStart 不可照抄；只借鉴标签页分组与场景图节奏。

### 2. Joby（三脚架/手机拍摄配件）

来源：
- https://joby.com/
- https://joby.com/cn-zh/tripods/
- https://joby.com/collections/all-products
- https://joby.com/collections/gorillapod
- https://joby.com/

可迁移模式：

1. **按设备/场景分卡，每卡一句定位**：脚架集合页按手机、运动相机、相机等场景分卡，每卡一句用途说明，新手能先判断"哪类是给我的"，再进型号。ShotStart 仅 3 个 SPU，可在商品卡描述行写清"说话头视频 / 桌面演示 / 镜头清洁"各自适用场景。
2. **产品卡功能标签角标**：卡片上用短标签（如 New、Best Seller）区分状态；标签必须真实可兑现。ShotStart 可只用"New"等无销量含义的角标，不打畅销榜。
3. **折扣价/原价并列展示**：促销时现价与划掉原价同卡显示，折扣一目了然；ShotStart 捆绑价 $38.22 与小计 $44.97 的并列写法与此一致。
4. **免邮门槛与退款承诺进公告栏/首屏信任行**：Joby 把满 $39 美国本土免邮、30 天全额退款放在靠前位置。ShotStart 对应可放"满 $35 美国标准免邮"，退款窗口只能在政策页占位后表述，不在公告栏承诺未确认天数。
5. **社群 UGC 区块与品牌故事区块**：首页后段用创作者社群内容与 20 年品牌故事建立认同。ShotStart 无 UGC 素材，替代方案是 7-Day Challenge 留资区块承担"社群感"，不放他人作品照。

### 3. Elgato（创作者设备生态）

来源：
- https://www.elgato.com/en-EU/eu/en/p/wave-3-black
- https://www.elgato.com/tw/en/p/key-light-bundle
- https://www.elgato.com/en/store

可迁移模式：

1. **策展式套装，开箱清单透明**：套装页列出"开箱包含哪些部件"，部件逐项配图；新手知道买到手有什么。ShotStart 三件套捆绑可在商品描述中列清三件单品，与捆绑页一致。
2. **配件加价、套装两档价格并列**：配件单卖与套装同页比较，套装优惠幅度直接标注；ShotStart 捆绑 SPU 可在描述中给出"三件单买 $44.97，套装 $38.22"的对照。
3. **部件拆解标注图**：产品图上用引线标注关键部位与用途，帮助理解功能；ShotStart 场景图条件有限，可用商品图 + 一句部位说明替代引线图。
4. **创作者导向标题与副标**：标题面向使用场景（直播、录音、补光）而非零件参数；ShotStart 现有三标题已是场景导向，保持。
5. **库存/状态明示**：可购、缺货、预售状态在卡片与商品页明确；演示店避免出现未确认的倒计时或紧迫话术。

### 4. Ulanzi（手机/相机配件，性价比 DTC）

来源：
- https://www.ulanzi.com/
- https://www.ulanzi.com/en-sg
- https://www.ulanzi.com/en-ca
- https://www.ulanzi.com/en-sg
- https://www.ulanzi.com/en-sg?variant=39871742214337
- https://www.ulanzi.com/

可迁移模式：

1. **每行产品一个 Hero 口号 + 场景四宫格**：首页按产品线成行，每行标题一句卖点，下方配四宫格功能/场景图，节奏轻快。ShotStart 首页商品卡区块可采用"一行一件商品 + 场景图"的轻量排版。
2. **Hot / New / Best Sellers 区块排序**：首页用独立区块突出新品与主推；ShotStart 3 件商品可直接排成推荐区块，不虚构销量排名。
3. **两件捆绑直标折扣**：套装直接标"两件 15% off"，不要求顾客先凑单找券；ShotStart 捆绑以 STARTERKIT 码实现，前台文案写清套装价即可。
4. **战役横幅叙事化套装**：大促页用横幅讲"为某类创作者配齐一套"，把商品组合成解决方案；ShotStart 的 7-Day Challenge 区块可承担叙事入口，而不是把三个商品孤立陈列。
5. **价格划掉原价 + 现价并列**：商品卡直接显示折后价与划掉原价，避免顾客自己算账。

### 5. SmallRig（相机/手机配件套件）

来源：
- https://www.smallrig.com/eu/smallrig-professional-phone-video-rig-kit-for-vlogging-live-streaming-3384.html
- https://www.smallrig.com/global/campaigns/winter-creator
- https://www.smallrig.com/list/Accessories.html
- https://www.amt.tv/smallrig-x-andyax-creator-tool-kit-4562.html
- http://www.shturl.cc/cc4231b23cce329af9fbd403fde0091a

可迁移模式：

1. **全能套件的模块化组件清单**：套件页按"包含组件"逐项列出，每件可单独对应单卖商品；ShotStart 捆绑描述照搬此结构：三脚架、桌面支架、清洁套装三件列明。
2. **兼容矩阵（For Brands / For Models / SKU）**：配件按兼容设备组织筛选；ShotStart 无多设备型号参数，兼容项保留占位，不编造适配机型清单。
3. **包装重量、说明书 PDF 等事实信息下沉**：规格区放重量、说明书等可核实资料；ShotStart 未核实的重量/材质一律占位，不仿造说明书下载链接。
4. **创作者人设分支战役页**：活动页按"哪类创作者"分流内容；ShotStart About / Challenge 页可按新手创作者与小商家两类人群写分流小标题。
5. **按品类→相机品牌的巨型导航**：集合导航层级清晰；ShotStart 商品仅 3 件，一级主导航已足够，不堆多级菜单。

### 6. DJI 官网商城

来源：
- https://store.dji.com/cn/selection/welcome
- https://www.shadcn.io/design/dji
- https://store.dji.com/mo#store-main-content
- https://www.dji.com/media-center/announcements/get-ready-to-up-your-creative-game-with-the-new-dji-mavic-air-2
- http://www.shturl.cc/12fff2ac65fe0b82baff23922b49a283

可迁移模式：

1. **按创作场景分组商品入口**：商城首页按航拍、稳定器、电源、配件、官翻、周边分组；ShotStart 可在 Shop 页或首页按"拍摄稳固 / 桌面演示 / 清洁维护"三类用途分组陈列。
2. **常驻白色顶栏 + 高对比 Hero**：顶栏轻量不抢焦点，首屏黑白高对比只让交互元素用单一品牌亮色；ShotStart 主色 #FF5A2C 作为唯一行动色，其余用深海军蓝与暖白，符合此节奏。
3. **产品卡列数随设备自适应**：桌面两列、移动一列，柔和底衬；卡片图下方居中文字。Reformia 商品网格可直接设置列数。
4. **编辑式氛围卡片 + 底部居中白字**：内容卡片用场景氛围图压暗后叠标题，区别于纯白底商品卡；ShotStart Challenge 海报区块可采用此处理。
5. **信任行"为什么在本店选购"**：首屏下方一行图标 + 短句，列出退换、免邮、选购支持等；ShotStart 只列可兑现项（满 $35 免邮、政策页），专家咨询等无服务不放。
6. **推荐场景块**：商品/首页后段按使用场景推荐搭配；ShotStart 仅三件，可在商详底部放"搭配成套"指向捆绑 SPU。

视觉细节参照（公开设计拆解）：64px 圆角幽灵按钮、轻阴影浮卡、按钮内边距竖 10px / 横 16px、单一字体家族；这些是 Reformia 主题设置可近似调整的方向，不写代码。

---

## 二、优秀 DTC 与获奖电商

### 7. Bellroy（皮具/包袋，克制留白型）

来源：
- https://www.goodcart.design/blog/best-travel-luggage-homepages-2026
- https://priceva.com/blog/best-product-pages
- https://es.bellroy.com/journal/bellroys-design-philosophy

可迁移模式：

1. **首页棚拍/实景分屏网格**：首屏左右或上下分屏，一边产品棚拍一边真人实景，信息层级先标题后图；ShotStart Hero 可左文右图（hero-banner.png）。
2. **分类菜单清晰：Featured / 品类 / 配件**：导航按购买意图分组，不按材料或内部编号；ShotStart 主导航 Shop 下不再拆复杂分类。
3. **产品卡悬停展示内衬/细节**：悬停切换第二张细节图；Reformia 商品卡支持多图轮播时可近似实现，不依赖悬停特效。
4. **色板选色紧贴主图**：颜色选项以小圆点色板呈现；ShotStart 商品无多色，省略该控件。
5. **sticky 加购条**：商品页滚动后底部/侧边保留加购按钮；需确认 Reformia 商品页模板是否自带 sticky CTA，免费主题不支持时用顶部醒目加购按钮替代（见映射表判定）。
6. **可核实徽章 + 图标化信任**：B Corp、可持续材料等徽章须有事实依据；ShotStart 不放任何未核实徽章，只做政策链接与免邮门槛两行。
7. **大留白、低饱和暖调、短视频讲解**：背景暖白、行距宽松，商品可用短视频讲用法；ShotStart 背景色 #FAF6F0 与此思路一致。

### 8. Ridge（钱包 DTC，套装与对比叙事强）

来源：
- https://ridgewallet.eu/pages/18-april-home
- https://ridge.com/products/heritage?variant=43261872537674
- https://ridgewallet.eu/products/tobacco-brown
- https://eu.ridge.com/products/gt?variant=55145073934712
- https://ridge-global.com/pages/how-it-works
- https://ridge.com/pages/how-it-works-old-2#leftMenu

可迁移模式：

1. **Bundle & Save 套装阶梯**：首页直接给套装折扣（最高 30% off），把凑单做成默认推荐；ShotStart 三件套捆绑 $38.22 即此结构，前台放在商品卡附近与首页主推位。
2. **PDP "Make It A Kit" 组件清单勾选**：商品页可选择加入套件，套件逐项列出；ShotStart 免费替代：捆绑作为独立 SPU 商品，描述列清单，PDP 内链到该捆绑商品。
3. **规格要点条目化**：容量、可换配件、功能点用短条目列出；ShotStart 未核实的规格保留占位，已确认的用途点写成短条目。
4. **拆解分层图 + 旧物 vs 新品对比**：用分层图展示结构，用对比叙事讲痛点改善；ShotStart 可写"新手常见困扰 → 本品怎么解决"的对照文案，不画未经核实的结构分解图。
5. **可兑现信任承诺集中呈现**：终身保修、99 天试用、免邮免退换等在服务页写清条件。ShotStart 只承诺政策页已确认项；试用天数、保修年限未确认前留占位，不在前台写死。

注意：Ridge 页面的评价数、用户规模等社交证明数字**不可迁移**。

### 9. Allbirds（鞋服 DTC，移动端购物流与叙事）

来源：
- https://www.allbirds.co.uk/pages/carbon-offset-projects
- https://www.designrocket.biz/case-studies/allbirds
- https://landingdoctors.com/teardowns/allbirds-com
- https://allbirds.com.ph/pages/allbirds-x-tiffany-bouelle
- https://www.limely.co.uk/inspiration/project/allbirds.co.uk

可迁移模式：

1. **品牌叙事逐节织入页面，而非堆 About 一页**：材料、生产故事分散在集合页与商品页相应位置；ShotStart 新手故事可在 Hero、三支柱、About 三处简短呼应，不把长文案压到商品入口前。
2. **真人上脚图保持一致灯光与场景**：场景图风格统一，避免棚拍与实景混用导致品牌感断裂；ShotStart 三张场景图需同光线、同场景基调（指令 5 已约束）。
3. **免邮 + 试用承诺放公告栏**：靠前位置讲配送与试用政策；ShotStart 公告栏只放满 $35 免邮，试用政策未确认不写。
4. **移动端两步结账、购物车预览可见支付方式**：移动端购物流步数少，车内能看到 Apple Pay/Shop Pay 等快捷入口。Reformia 免费模板结账步数以主题默认为准；ShotStart 保证车与结账页可达、优惠码入口可见即可（指令 8 复查项）。
5. **导航按购买意图（款式）分类，而非按材料**：卡片分类以顾客怎么找为准；ShotStart 按用途陈列，不按配件材质分类。
6. **移动/网页分别适配，移动端把决策拆成小步**：手机端信息块更短、按钮更大；指令 4 与指令 8 的移动端检查覆盖此点。

反面教训（公开拆解指出）：首页缺乏聚合信任信号，信任感分散在子页。ShotStart 应在首页保留一行可兑现的政策/免邮入口，不把信任内容全部埋进政策页。

注意：Allbirds 自述的销量、减排等经营数字不可迁移。

### 10. Gymshark（运动服饰，移动优先转化）

来源：
- https://hopatoo.com/blogs/news/gymshark-cro-audit-shopify-conversion-optimization
- https://releaselens.org/demos/gymshark/
- https://www.gymshark.com/

可迁移模式：

1. **移动优先拇指区布局**：关键按钮与筛选放在手机屏底部可达区；ShotStart 移动端 CTA 与加购按钮保持在底部易触达位置。
2. **移动端 sticky 加购**：滚动后底部常驻加购条；免费主题若不自带，替代方案是商品页主按钮字号加大、位置靠上（见映射表）。
3. **横向 chips 筛选而非侧栏**：分类筛选以横向滑动标签呈现；ShotStart 仅 3 个 SPU，无需筛选器，此条不适用，记录为边界。
4. **产品卡 Quick-Add**：卡片上直接加购，不强制进 PDP；Reformia 若支持卡片加购按钮则开启，否则保留卡片进 PDP 路径。
5. **性别 → 品类双层 mega 导航**：导航先人群后品类；ShotStart 人群单一（新手创作者/小商家），单层主导航即可。
6. **高对比产品摄影**：商品图主体清晰、背景干净；ShotStart 三张主图保持统一背景。

反面教训（公开 CRO 案例）：运动员长传记页压住商品网格，导致移动端跳出率偏高。ShotStart 的 About 与 Challenge 文案不可把商品入口挤出首屏；品牌故事区块长度受控，商品卡区块保持在首页可见位置。

---

## 三、获奖电商案例（Awwwards / CSS Design Awards）

### 11. Shopify Supply Performance Pack（Awwwards 案例）

来源：https://www.awwwards.com/sites/shopify-supply-performance-pack

- Hero 视频转场、滚动同步机位、产品区随滚动展开；双色 #1D1E1E / #000；WebGL/Three.js/Hydrogen 自定义。
- **可迁移**：首屏只留标题 + 单一主 CTA 的极简层级；主色与背景双色对比。
- **不可免费实现**：滚动 3D、WebGL 机位动画、headless Hydrogen 定制——Reformia + Athena 能力外，映射表标 P2 放弃。

### 12. iyO 音频电脑（Awwwards 配置器案例）

来源：https://www.awwwards.com/iyo-case-study-selling-the-worlds-first-audio-computer.html

- PDP 接近配置器：一侧玻璃拟态面板选连接方式/颜色/适配，无限渲染滑块，按住暂停帧，换色滑块同步；Webflow + TypeScript、Three.js 粒子、GSAP、Lenis 平滑滚动；Shopify 托管预售。
- **可迁移**：把可选选项（颜色/套装）放在主图旁同屏对照的布局思路。
- **不可免费实现**：无限渲染 3D 配置器、玻璃拟态自定义面板、自定义动效——P2 放弃。

### 13. Mother Root（食品 DTC，内容化 PDP）

来源：https://tribe.studio/our-work/mother-root

- 风味导向 PDP、食谱内容嵌入商品页、智能购物车机制；GSAP 动画。案例中的 "+49% 日单"等成果属品牌自有数据，不可挪用为 ShotStart 预期。
- **可迁移**：商品页嵌入"用法/场景内容"（ShotStart 对应 7-Day Challenge 任务与拍摄提示）；商品与内容互相导流。
- **不可免费实现**：智能购物车推荐机制、GSAP 滚动动画——P2 放弃。

### 14. Polaroid 官网旗舰（headless Shopify + Sanity 重建）

来源：https://www.frontrowgroup.com/en/cases/rebuilding-polaroid-digital-flagship-with-headless-shopify

- 生活方式摄影规范、弹性设计系统、会员区块；真实产品使用实景；I-2 获 Awwwards SOTD。
- **可迁移**：场景图统一规范（光线、构图、产品占比）；把品牌历史/故事独立成内容区块。
- **不可免费实现**：headless 架构、自定义内容中台、会员体系——P2 放弃。

### 15. Wook Water（转化导向 Shopify 案例）

来源：https://jbyer.com/work/case-studies/wook-water

- PDP、顺畅购物车/结账、移动端优化、易维护后台；趣味动效作为点缀而非主路径。
- **可迁移**：转化优先——PDP 信息完整、车与结账路径短、移动端不溢出；动效克制。与指令 8 全站复查口径一致。

### 16. CSS Design Awards / 公开评审共性

来源：
- https://www.cssdesignawards.com/website-gallery?feature=eCommerce&page=1
- https://www.cssdesignawards.com/website-gallery?feature=eCommerce&page=2
- https://www.cssdesignawards.com/website-gallery?feature=eCommerce&page=54
- https://www.webdesignawards.io/best-web-design-awards/for-ecommerce
- https://seahawkmedia.com/de/design/e-commerce-ui-design-themes-und-beispiele/
- https://www.awwwards.com/blog/figma/?page=3

评审与榜单分析的共性结论：

1. 评奖不只看首页：PDP、结账流程、商品陈列、导航与信息架构同样计入。
2. 好电商 UI = 简单、快、易用：清晰导航、快速加载、筛选可用、结账简短。
3. 高质量商品图、可用搜索、真实评价（不可伪造）、安全支付说明、快速下单入口是基础项。
4. 获奖站的实验性表达（非常规导航、横排编辑布局、3D 手势）通常依赖定制开发；模板店应先把基础转化项做扎实，再谈视觉亮点。

---

## 四、跨站共性归纳（按调研维度）

| 维度 | 标杆共识 | ShotStart 适配要点 |
| --- | --- | --- |
| 首屏信息层级 | 标题一句定位 + 单一主 CTA + 次要 CTA；首屏不堆多入口 | Hero 左文右图；主 CTA "Shop All Gear"，次 CTA "Join the 7-Day Challenge" |
| 产品卡设计 | 主图干净、价格与原价并列、短标签真实、场景图同风格 | 三卡场景图同光线；捆绑价与小计并列；不打销量标签 |
| 信任元素 | 承诺必须可兑现、条件写清；徽章/评价有据 | 只放满 $35 免邮、政策页链接、AI 草稿需本人审核；无评价/评分/认证 |
| 导航结构 | 按购买意图分组；层级扁平 | 单层主导航；政策链接仅页尾 |
| sticky 加购 | 滚动后加购入口常驻 | 视 Reformia 模板能力；不支持则加大顶部加购按钮 |
| 场景生活方式图 | 棚拍与实景交替、风格统一、产品不被改造 | 指令 5 生成三张同基调场景图 |
| 留白与字体节奏 | 暖白留白、单一字体家族、宽松行距 | #FAF6F0 背景；标题/正文一对字体 |
| 移动端拇指区 | 关键按钮底部可达、信息块短、按钮大 | 指令 4/8 移动端走查 |
| 捆绑/凑单交互 | 套装作为可比较选项、清单透明、优惠幅度直标 | 独立捆绑 SPU + STARTERKIT；描述列三件清单与对照价 |
| 弹窗时机 | 留资弹窗只出现一次、有退订说明 | 邮件弹窗含退订细则；不反复弹出 |

## 五、不可挪用证据清单（复核用）

以下数字/表述在标杆页面出现，但 ShotStart 前台不得出现：

- Ridge：评价条数、用户规模；SmallRig：卡面评分 4.8；Elgato/Joby：评分位与销量榜；Allbirds：双鞋销量、减排数量；任何奖项头衔、资质徽章、库存倒计时、"仅剩 N 件"。
- 案例成果数据（如 Mother Root +49% 日单）仅说明设计手段有效，不作为 ShotStart 承诺或预期写入页面。
- 未确认的参数：尺寸、材质、重量、兼容机型、退回窗口、保修年限、响应时效——一律占位，不上前台。

## 六、参考来源汇总

**Shoplazza 能力文档**
- https://helpcenter.shoplazza.com/hc/zh-cn/categories/4408574904729
- https://helpcenter.shoplazza.com/hc/en-us/articles/22929902032153-A-Guide-to-the-Shoplazza-Theme-Editor
- https://helpcenter.shoplazza.com/hc/en-us/articles/22929902032153-Customizing-your-store-theme
- https://helpcenter.shoplazza.com/hc/zh-cn/articles/8888574212889-设置菜单导航
- https://www.shoplazza.cn/athena-guide

**同类装备**：Peak Design、Joby、Elgato、Ulanzi、SmallRig、DJI 各条 URL 见对应小节。
**DTC/获奖**：Bellroy、Ridge、Allbirds、Gymshark、Shopify Supply Performance Pack、iyO、Mother Root、Polaroid、Wook Water、CSSDA 画廊各条 URL 见对应小节。
