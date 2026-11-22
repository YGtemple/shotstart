# round10 扣分闭环批 — 交付说明（字典 + ss-forms 成功句）

> **勘误（round11）**：本文件计数（711 键）、ball head $11.99、Pro $1.00 价差、联系正文未中性化、Sort 暂缓等口径已被 `round11_交付说明.md` 与 coverage 第十三节推翻；终版以 round11 为准（729 键，Pro 62.96 闭合）。本文件仅作历史留证。

- 交付时间口径：比赛日 08:00 签到批；演示重嵌随建站注入批一次执行，本批不重嵌主题包。
- 字典终版：`tools/i18n_zh.json`，**711 键**（`zh-CN` 节点）；`_meta.plural_patterns` 模式条目不计入前台键数。

## 一、终版计数链

| 阶段 | 键数 |
| --- | --- |
| 上一版终冻（第十一节） | 693 |
| 退役：12 条 specs 兜底整句 + 7 条旧承诺/旧文案键 | −19 |
| 新增：成功/refill 新句 7 + 集合 chrome 3 | +10 |
| 新增：PDP FAQ 兜底答案 | +27 |
| **终版** | **711** |

- 计数复核：693 − 19 + 10 + 27 = 711。
- 完整性校验（check_i18n3）：JSON 可解析；无重复键、无空值、无键内 CJK；evidence-only 0；matched nowhere 0；code-only 74（主题代码既有口径）。
- 基线复跑：占位方括号 0 / 占位词 0 / CJK 残留 0 / demo 语境外露 0 / Avoid 词 0；三件 docx 泄漏 0；Unmapped 0。

## 二、ss-forms 成功面板改动（交建站/演示替换）

> 旧句为线上旧承诺口径，新句已写入字典与源 `shotstart_content.py`；表单成功面板请按新英文串替换，zh 取字典值。

### 1. 挑战报名成功态（去收信箱承诺）
- 旧：`You're in! Check your inbox for Day 1. Remember: your first shot starts here.`
- 新：`You're in. Day 1 is below — start shooting. Remember: your first shot starts here.`
- zh：`你已加入。Day 1 见下方——开始拍摄吧。记住：你的第一个镜头，从这里开始。`
- 优惠码前缀孪生（报名面板整句）：
  - 旧：`Challenge sign-up: You're in! Check your inbox for Day 1. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.`
  - 新：`Challenge sign-up: You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — 10% off all single items in the Shop collection; bundle kits are excluded; it does not stack with STARTERKIT.`
  - zh：`挑战报名：你已加入。Day 1 见下方——开始拍摄吧。首单优惠码 NEWCREATOR10——Shop 集合全部单件 9 折；捆绑套装除外；不可与 STARTERKIT 叠加。`
  - 裸句孪生：`You're in. Day 1 is below — start shooting. Your first-order code: NEWCREATOR10 — …`（同上，无前缀）。

### 2. 联系表单成功态（去回复时限承诺）
- 旧：`Thanks for reaching out. We've received your message and will reply by email.`
- 新：`Thanks for reaching out. We read every message.`
- zh：`感谢留言，我们阅读每一条留言。`
- 前缀孪生：`Contact form: Thanks for reaching out. We read every message.` → `联系表单：感谢留言，我们阅读每一条留言。`
- 口径：新句不承诺回复时限、不承诺邮件回复；`You'll hear from us` 类收信句本轮未保留。

### 3. refill 提醒句（功效隐喻 sharp 去除）
- 旧：`when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit to keep every new clip sharp.`
- 新：`when your cleaning cloth or blower wears out, restock the Lens Cleaning Kit between shoots.`
- zh：`清洁布或气吹用旧时，在拍摄间隙补充镜头清洁套装。`
- 前缀孪生：`Refill reminder: …` → `补充提醒：…`。

## 三、集合 chrome 与计数模式

- 入键：`Filter` → 筛选；`Availability` → 库存状态；`Price` → 价格。
- 模式条目（`_meta.plural_patterns`，引擎复数/计数单独实现）：`{{count}} Products` → `{{count}} 件装备`。
- `Sort`：线上未捕获独立标题串，暂缓入键；待建站转发集合筛选/排序模板标题逐字串后统一补。

## 四、源侧其他改动（已同步 pages txt / 三件 docx / 发布快照）

- 12 单件 PDP specs 段兜底整句（`Exact … are being finalized; contact us for details.`）整段从源删除；对应 12 条字典键退役。FAQ 答案内联兜底从句保留不删。
- glossary / judge-guide 表 restocking 行：`演示默认无；正式营业前法务复核` → `补货手续费（退货条款以法务定稿为准）`。
- 挑战/联系成功句、refill 句按第二节更新；源 `shotstart_content.py` 导入校验 27 页通过。
- 重建产物：pages 27 txt；`ShotStart店铺文案包.docx`（1079 段 / 17 表，较基线减 12 条已删 specs 段）；`ShotStart品牌定稿.docx`（50 段 / 5 表）；`评委速览卡.docx`（24 段 / 4 表）；`vm-pages-publish.json`（challenge 页 DIFF，其余 5 页 SAME，cart 块保留）。

## 五、价格对账（源价未改，待上线前复核）

- Starter：Tripod $19.99 + Stand $14.99 + Lens Cleaning Kit $9.99 = **$44.97**；券后 $38.22，省 $6.75（44.97 − 38.22）✓。
- Pro：Tripod $19.99 + Extension Pole $16.99 + Mini Ball Head **$11.99** + Carry Case $12.99 = 组件单价加总 **$61.96**；捆绑 SPU 标价 **$62.96**；券后 $53.52，省 $9.44（62.96 − 53.52）。
- 说明：61.96 为组件单价加总，62.96 为捆绑标价，二者口径不同，差 **$1.00**；ball head 源价为 $11.99（非 $12.99）。价差属捆绑定价配置，待评审/建站上线前确认；本轮未擅改源价。

## 六、待建站转发 / 未决项

1. 集合 `Sort` 独立标题串；线上原生信任块、模板区块标题逐字串——到达后再入键，未提前臆造翻译。
2. Pro 捆绑标价与组件加总 $1.00 价差、ball head 单价口径，上线前复核定价。
3. 联系页**正文**仍含既有在册承诺句（`our team will reply by email` / `We reply to messages within 2 business days, by email.`），本轮仅改表单成功面板，正文未动；是否一并中性化待评审口径。
4. 主题包 `shotstart-theme-custom/assets/ss-i18n.js` 内嵌旧字典与旧计数注释不由本批维护；演示按终版 711 键重嵌后再建站注入。
