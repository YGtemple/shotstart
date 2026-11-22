# 物料数量/组合/价格同步批 — 回读核验与旧表述清零留证

- 复核时间：2026-11-20（本地，UTC+8）
- 事实依据：`商品架构映射表.md`（终版锁定，价格不得再动）、`商品架构图.png`
- 提取依据：本目录 `verify_pkg.txt` / `verify_sop.txt` / `verify_chk.txt` / `verify_jud.txt`（python-docx 回读，带 `[P]`/`[T]` 块索引）

## 1. 改动范围与边界

解冻范围仅限下列四份 docx 的商品数量 / 组合 / 价格 / 集合 / PDP 互补 / 工时表述：

| 文档 | 物理路径 | 段落数 | 表格数 | 提取行数 |
| --- | --- | ---: | ---: | ---: |
| Athena 建店指令包 | `shotstart-playbook\Athena建店指令包.docx` | 292 | 26 | 886 |
| 运营配置与测试下单 SOP | `shotstart-playbook\运营配置与测试下单SOP.docx` | 132 | 4 | 195 |
| 现场执行清单 | `现场执行清单.docx`（项目根） | 7 | 2 | 66 |
| 评委速览卡 | `shotstart-copy\评委速览卡.docx` | 24 | 4 | 175 |

未改动：`pages/*.txt` 文案原文、主题、后台配置；`_edit_work\` 备份不进交付包；未解冻的文案包 / 品牌定稿 / 举证材料 docx 未触碰。

## 2. 终版口径（已锁定）

### 2.1 商品总数：12 单品 + 2 套装 = 14 商品

| # | handle（工作 handle，全 slug 待建站回报） | 演示价 | 备注 |
| ---: | --- | ---: | --- |
| 1 | tripod | $19.99 | 不变 |
| 2 | desktop-stand | $14.99 | 不变 |
| 3 | cleaning-kit | $9.99 | 不变 |
| 4 | carry-case | $12.99 | 调价（旧 $16.99） |
| 5 | reflector | $10.99 | 调价（旧 $12.99） |
| 6 | backdrop | $13.99 | 调价（旧 $14.99） |
| 7 | extension-pole | $16.99 | 单件价即套装计入价；不存在双价（旧 $13.99） |
| 8 | cleaning-refill | $7.99 | 不变 |
| 9 | mini-ball-head | $12.99 | 新四件；标题待文案包回填 |
| 10 | magnetic-mount | $11.99 | 新四件；标题待文案包回填 |
| 11 | microfiber-3pack | $6.99 | 新四件；标题待文案包回填 |
| 12 | shot-list-cards | $8.99 | 新四件；标题待文案包回填 |
| 13 | creator-starter-kit（套装） | $44.97 → $38.22 | 省 $6.75 |
| 14 | pro-creator-kit（套装） | $62.96 → $53.52 | 省 $9.44 |

### 2.2 套装成员

- Starter（creator-starter-kit）= tripod + desktop-stand + cleaning-kit，三件。
- Pro（pro-creator-kit）= tripod + extension-pole + mini-ball-head + carry-case，四件。

### 2.3 集合：5 前台 + 1 隐藏

- 前台：`all-gear` All Gear（12 全量）；`stability-height` Stability & Height（tripod, extension-pole, mini-ball-head）；`desk-angle` Desk & Angle（desktop-stand, magnetic-mount, mini-ball-head）；`clean-care` Clean & Care（cleaning-kit, microfiber-3pack, cleaning-refill）；`carry-set-up` Carry & Set Up（carry-case, reflector, backdrop）。
- 隐藏：`creator-kits` Creator Kits（两张套装 SPU）。

### 2.4 促销码

- STARTERKIT 15%：仅两张套装 SPU；不与 NEWCREATOR10 叠加。
- NEWCREATOR10 10%：仅十二件单品；两套装排除；每单一码、两码不叠加；无 compare-at 划线字段。

## 3. 算术复核（calculator 实算，非估算）

| 项 | 算式 | 结果 | 文档取值 |
| --- | --- | --- | --- |
| Starter 合计 | 19.99 + 14.99 + 9.99 | $44.97 | $44.97 ✅ |
| Starter 用码 | 44.97 × 0.85 | 38.2245 | $38.22 ✅ |
| Starter 省 | 44.97 − 38.22 | $6.75 | $6.75 ✅ |
| Pro 合计 | 19.99 + 16.99 + 12.99 + 12.99 | $62.96 | $62.96 ✅ |
| Pro 用码 | 62.96 × 0.85 | 53.516 | $53.52 ✅ |
| Pro 省 | 62.96 − 53.52 | $9.44 | $9.44 ✅ |
| 凑单用例 | reflector 10.99 + backdrop 13.99 + pole 16.99 | $41.97 | $41.97（达免邮档）✅ |
| refill 单件 | $7.99 | — | 付费档 ✅ |

## 4. 旧表述清零核对

扫描范围：四份 `verify_*.txt` 全量段落与表格单元格。

### 4.1 硬关键词（数量 / 旧套装价 / 旧工时）— 命中 0

| 旧口径关键词 | pkg | sop | chk | jud |
| --- | ---: | ---: | ---: | ---: |
| 八件单件 / 八件单品 / 八件商品 / 八件商详 / 八件 | 0 | 0 | 0 | 0 |
| 五件新品 / five new / all eight / eight individual / eight product | 0 | 0 | 0 | 0 |
| $58.96 / 58.96 | 0 | 0 | 0 | 0 |
| $50.12 / 50.12 | 0 | 0 | 0 | 0 |
| $8.84 / 8.84 | 0 | 0 | 0 | 0 |
| $50.116 | 0 | 0 | 0 | 0 |
| 旧工时 152 / 77 / 114 分钟、双价表述 | 0 | 0 | 0 | 0 |

### 4.2 价格语境逐条判读（数字合法保留项已甄别）

- `$16.99`：仅出现在 extension-pole 单件与 Pro 套装内的 extension-pole 计价；无旧 carry-case 双价语境。
- `$12.99`：仅出现在 carry-case 与 mini-ball-head；无旧 reflector 语境。
- `$13.99`：仅出现在 backdrop；无 pole 旧价语境（pole 一律 $16.99）。
- `$14.99`：仅出现在 desktop-stand；无旧 backdrop 语境。
- `$9.99`：仅出现在 cleaning-kit；速览卡磁性支架行已纠正为 $11.99（修复前错位，见 §6）。

### 4.3 数量与集合表述落点

- 指令包基线表：14 行（12 单品 R1–R12 + 两套装 R13/R14）。
- 指令包 T32 建品清单：编号 1–12 十二件；新四件为 9–12。
- SOP / 清单 / 速览卡：统一“十二件单品 + 两张捆绑（套装）SPU”。
- 集合：All Gear + 四用途集合前台；Creator Kits 隐藏；成员归属与 §2.3 一致。
- PDP 互补：指令包 P53 落 5 对实线推荐 + 7 对标注“自拟”的互补位；SOP 仅保留加购核查口径，不重复推荐表。

### 4.4 工时口径（指令包 Runbook 总表）

- 3a 行：其余九件单品 + Pro 套装录入，22 分钟（含四件新品建品）。
- R1（步骤 1–7 + 3a）= 87 分钟；R2（步骤 8–18）= 75 分钟；合计 162 分钟。
- 分层：设计配置 1–11 + 3a = 124 分钟；测试单 12–15 = 13 分钟；复查留证 16–18 = 25 分钟；缓冲 10 分钟（门禁排队 5 + 故障恢复 5）。
- 清单分钟盒：R3 单件录入 17 分钟；各步合计 115 分钟，缓冲 10 分钟。
- 清单页数：Word COM `ComputeStatistics(wdStatisticPages=2)` = **Pages 1**（Words 1288），保持 1 页。

## 5. 有意保留的占位（非遗漏）

- 新四件（mini-ball-head / magnetic-mount / microfiber-3pack / shot-list-cards）标题：工作名 + “自拟工作名，待文案包回填”；主图 `[待确认: 主图]`；文案列 `[待回填]`。
- extension-pole、cleaning-refill 主图占位为既有状态，本轮未补猜素材。
- 套装行图列 `—`，文案来源 `marketing.txt`。
- 各规格（尺寸 / 材质 / 重量 / 兼容性 / 库存）保留未核实占位；日期、资格、库存占位待上线前确认。
- WELCOME10 更名注记、锁定 CTA（Save my spot / Join the challenge / Send message / View the kit / Shop All Gear）、运费 $4.99 / 满 $35 免邮、表单字段、品牌色 #FF5A2C / #0F1B2D / #FAF6F0 均未改动。

## 6. 本轮修复的两处瑕疵

1. 指令包首页指令表：弹窗段编号原为“8. Email popup”，与 Challenge 段“8. 7-Day Challenge”重复；已改为“9. Email popup”，顺序 1–9 连续（Hero / Trust / Pillars / Starter / Grid / Pro / AI / Challenge / Popup）。
2. 速览卡价格表与卖点表：修复前 R7/R9–R12 价格列错位、三件新品英文名被截断；已纠正为——Mini Ball Head Mount $12.99、Magnetic Phone Mount $11.99、Microfiber Cloth 3-Pack $6.99、Shot List Cards $8.99、Extension Pole $16.99；卖点表三名同步补全全称。

## 7. 备份隔离

回滚备份位于 `shotstart-playbook\_edit_work\`（仅本批：`pkg-backup-arch.docx`、`sop-backup-arch.docx`、`checklist-backup-arch.docx`、`judge-backup-arch.docx`），目录内另有历史轮次备份；全部不复制进交付包。交付目录内 docx 仅四份解冻目标 + 未解冻的文案包 / 品牌定稿 / 举证材料。

## 8. 未决项（待下游回报）

- 新四件最终标题：待文案包回报后终版回填。
- 全 slug / handle：待建站后台回报；表内当前为工作 handle。
- 新四件主图与对应 `product-*.txt` 文案：待素材与文案包回填。
- 凑单门槛基数（折后小计）实机待验；STARTERKIT 限定单 SPU 能力以后台实测为准。
