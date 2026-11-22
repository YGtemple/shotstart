# round11 收尾批 — 交付说明（价格纠偏 + 联系中性化 + 面板/线上实测补键）

> 本说明取代 `round10_交付说明.md` 中的计数、价格与联系承诺口径；旧结论已在本批推翻，详见 `tools/i18n_zh_coverage.md` 第十三节。

- 字典终版：`tools/i18n_zh.json`，**729 键**（`zh-CN` 节点）；`_meta.plural_patterns` 模式条目不计入前台键数。
- 源文案：`tools/shotstart_content.py`；产物：pages 27 txt、三件 docx、`vm-pages-publish.json` 已按改后源重建。

## 一、终版计数（实测封板，不预设）

| 阶段 | 键数 |
| --- | --- |
| round10 终版 | 711 |
| round11 退役旧承诺 / 旧价串；新价 / 中性句 / v4 / 面板 / 线上实测补键（净增） | +18 |
| **终版** | **729** |

- 完整性校验（check_i18n3）：JSON 可解析；无重复键、无空值、无键内 CJK；code-only 86（主题代码既有口径）；evidence-only 4（Recommended / Subtotal / Sign in / Register）；matched nowhere 1（`Best selling`，线上运行时渲染串，按线上 js 清单实测入键豁免）。
- 基线复跑：check_placeholders Unmapped 0（45 占位均有映射，动态兜底从句 6 条在册）；scan_publish 占位方括号 0 / 占位词 0 / CJK 0 / demo 语境外露 0 / Avoid 0；scan_docx 三件泄漏 0 / 占位词 0 / demo 残留 0。

## 二、价格对账闭合（计算器复核；推翻 round10 的 $1.00 价差结论）

- Starter：Tripod $19.99 + Stand $14.99 + Lens Cleaning Kit $9.99 = **$44.97**；STARTERKIT 15% → **$38.22**；省 **$6.75**。
- Pro：Tripod $19.99 + Extension Pole $16.99 + Mini Ball Head **$12.99** + Carry Case $12.99 = **$62.96**；→ **$53.52**；省 **$9.44**。
- 结论：Pro 组件加总 62.96 与捆绑标价 62.96 闭合，**不存在 $1.00 价差**；round10 的 61.96 / $1.00 系 ball head 价误判，已销。

### 四件单件价纠偏（映射表 L4 + 线上实测为准）

| 商品 | handle | 旧（源笔误） | 新 |
| --- | --- | --- | --- |
| Mini Ball Head Mount | mini-ball-head | $11.99 | $12.99 |
| Magnetic Phone Mount | magnetic-mount | $9.99 | $11.99 |
| Microfiber Cloth 3-Pack | microfiber-3pack | $8.99 | $6.99 |
| Shot List Cards | shot-list-cards | $6.99 | $8.99 |

- 源内列表 bullet / PDP price 行 / 价格表 / 中文自述全改；字典列表 bullet 键 1:1 换价，键数不增；cleaning-kit $9.99 九键保留未动。

## 三、联系页正文两句中性化（去收信渠道与回复时限承诺；无 ESP 不承诺）

- 首段：`Have a question about an order, a product, or the 7-Day Shooting Challenge? Send us a note — we read every message and reply as soon as we can. For order questions, please include your order number so we can help faster.`
- 末段：`We read every message and reply as soon as we can. This store is email-only; no physical mailing address is published.`
- 旧承诺键（`…will reply by email…`、`We reply to messages within 2 business days, by email.…`）已退役；快照 contact 页同步刷新。挑战 / 联系表单成功态新串口径见 round10 说明第二节，本批未再改。

## 四、本轮补键清单（线上 DOM / js 实测，不臆造未检出选项）

### 集合筛选 / 排序面板
- `Products` → 件装备（计数被拆成 "12" + "Products" 两相邻文本节点，单串键与 `{{count}} Products` 模式条目并存；跨节点逻辑由演示实现）。
- `In stock` → 有货；`Out of stock` → 缺货。
- `Newest in` → 最新上架；`Pageviews, high to low` → 浏览量从高到低。
- `Price, high to low` → 价格从高到低；`Price, low to high` → 价格从低到高。
- 已在册沿用：`Filter`→筛选、`Availability`→库存状态、`Price`→价格、`Search products`→搜索商品。

### 线上 js 清单实测缺键（quoted 命中=0 确认）
- `Best selling` → 最畅销；`Checkout` → 去结账；`Subtotal` → 小计；`Sign in` → 登录；`Register` → 注册；`Recommended` → 推荐。
- `Sort by` → 排序；`Recommend` → 推荐；`Quantity` → 数量。

### 已有键勿重复（已核译文）
- `Search products`→搜索商品、`All Gear`→全部装备、`What's in the Box`→盒内清单、`Add to cart`→加入购物车。
- 不译：`Judge Guide`（既定例外页）；VISA / Mastercard / PayPal 等卡组织品牌名。

### 模式条目（`_meta.plural_patterns`，引擎复数单独实现，不计前台键数）
- `{{count}} Products` → `{{count}} 件装备`；`{{count}} sold` → 已售 {{count}} 件。线上 SS_I18N_PLURAL 当前为 null，未上线。

## 五、产物与同步

- pages 27 txt；`ShotStart店铺文案包.docx`（1079 段 / 17 表）；`ShotStart品牌定稿.docx`（50 段 / 5 表）；`评委速览卡.docx`（24 段 / 4 表）；`vm-pages-publish.json` 六页 + cart 块从当前 PAGES 重建（contact DIFF，其余五页 SAME）。
- 主题包 `shotstart-theme-custom/assets/ss-i18n.js` 内嵌旧字典不由本批维护；建站注入时以本终版 `tools/i18n_zh.json` 整体重嵌。

## 六、待建站转发 / 未决项

1. 集合独立 `Sort` 标题串；线上原生信任块 / 模板区块标题逐字串——到达后再入键，未提前臆造。
2. 三件新单件 PDP 回链随建品回填；价格以映射表 L4 口径为准。
