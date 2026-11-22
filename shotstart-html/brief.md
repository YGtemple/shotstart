# ShotStart Creator Kit — 商品页 Brief v1

## 任务与交付
- 交付一个可直接打开的响应式单文件 HTML，CSS 与 JavaScript 内联，图片使用同目录 `assets/` 相对路径。
- 页面语言为英文，延续原 ShotStarter 项目面向美国市场的内容语言；本次说明与交付使用中文。
- 不使用 Shoplazza，也不调用真实电商后端。购物袋仅在当前浏览器内演示，不包含支付、登录、库存或订单功能。
- 商品沿用用户原 HTML 的创作者配件类别：Adjustable Phone Tripod、Desktop Phone Stand、Lens Cleaning Kit，以及三者组成的 Creator Kit。
- 所有价格、配送、退货、评分和规格均作为界面演示数据，页面需明确标注“Demo storefront”，不得冒称真实销售承诺。

## 参考与采用边界
- 官方参考：https://store.google.com/product/pixel_9?hl=en-US 与 https://store.google.com/category/phones?hl=en-GB 。
- 继承：白底、低饱和浅灰产品画布、大圆角、蓝色行动按钮、清晰无衬线层级、顶部品牌导航、产品图库与购买配置并列、分区卖点、规格与 FAQ、宽页距和充足留白。
- 不复制：Google 标识、Pixel 产品、商标、官方文案、价格、评论、规格、页脚链接或任何“Google 官方”身份。
- 品牌使用 ShotStart，视觉只是 Google Store 风格的原创商品页。
- 模板库比较：已查询“详情页／主视觉＋图文分栏／极简商品”无命中；“选购＋信息列表／表格”有结果但均为长页、服饰或通用编辑风格，不适合本次交互式商店页面。故不采用模板，只按官方参考与当前功能自行实现。

## 页面结构与准确文案
1. 顶部导航：ShotStart；Shop / Creator kits / Accessories / Support；搜索、帮助、购物袋图标。
2. 公告条：Demo storefront — no real orders or payments.
3. 首屏商品区：
   - Eyebrow: SHOTSTART CREATOR SYSTEM
   - H1: Creator Kit
   - Subtitle: Your first shot starts with a steadier setup.
   - 支持 4 张图库切换；配置为 Creator Kit / Tripod Only / Desk Setup。
   - 演示价格分别为 $79 / $39 / $49；配置切换同步价格、包含内容与购物袋。
4. 信任说明：Free shipping demo / 30-day returns demo / 1-year warranty demo，明确为界面示例。
5. 卖点：
   - One desk. Three simple tools.
   - Set up. Frame up. Start talking.
   - A cleaner lens for a clearer first take.
   仅使用原 HTML 已有的一般性卖点，不新增性能、材质、兼容性或认证承诺。
6. 场景区：展示桌面拍摄场景，说明三脚架用于稳定构图、桌面支架用于解放双手、清洁套装用于日常镜头护理。
7. 套装内容：三件商品卡片及各自已有描述。
8. 比较与规格：以“What’s included / Best for / Setup”进行同口径比较；未确认的尺寸、重量、兼容范围写“Confirm before launch”。
9. FAQ：适合谁、包含什么、是否适配手机、是否为真实商店；回答不编造参数。
10. 页尾：ShotStart；演示声明与锚点导航。

## 视觉与图文关系
- 主体是产品，不使用紫色或大面积渐变。主色为白、冷灰和 Google Store 风格蓝；商品保持原图固有色。
- 首屏左侧为浅灰圆角图库，右侧为购买配置；产品图是第一焦点，H1 和价格次之。
- 后续使用大圆角图窗与开放文字分栏，卖点与对应图片就近组织；套装三件商品用同尺度卡片比较。
- 字体采用现代中性无衬线，优先 Arial / Helvetica Neue / 系统回退，避免未核实的外部字体依赖。
- 移动端改为单栏，购买配置跟在图库之后，购物袋为全宽底部抽屉。

## 素材计划
- 复用原 HTML 的 Tripod、Desktop Stand、Cleaning Kit 和干净桌面场景图片，下载到 `assets/`，已核验内容与尺寸。
- 原 Creator Kit 套装图仅作为身份与构图参考；使用图片编辑去除图内全部宣传文字，保留全部商品、配件数量、外观、颜色和结构，作为首屏干净主图。原带字套装图不进入正式页面。
- 现有 `desk-scene.png` 已可承担宽屏场景职责，不再生成额外场景图。
- 所有正式文本、按钮、规格、FAQ 和图标由 HTML/CSS/内嵌 SVG 实现，保持可编辑。

## 验收
- 图库、套装、数量、购物袋、FAQ、导航锚点和移动端菜单均可操作。
- 无外部 JS 框架，无真实支付或虚假订单成功提示。
- 图片无拉伸、关键产品不被文字遮挡；375px、768px、1440px 下无横向溢出。
