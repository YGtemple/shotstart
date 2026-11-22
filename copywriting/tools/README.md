# ShotStart 文案包 · 重建与核验工具

脚本随文案包放在 `tools\` 目录，自动定位上一级项目目录（`shotstart-copy\`），无需修改路径。

## 依赖

- Python 3.13
- python-docx 1.2.0

## 重建产物（改数据源 `shotstart_content.py` 后执行）

```
python build_shotstart.py
python build_brand_and_card.py
```

## 基线核验（三项应全绿）

```
python check_placeholders.py
python scan_publish.py
python scan_docx.py
```

- `check_placeholders.py`：未映射占位前向检查（Unmapped: 0）；兜底句清单从 `placeholder-map.txt` 第四列动态读取，无硬编码兜底表。
- `scan_publish.py`：PUBLISH 行方括号占位泄漏（0）、占位词残留 placeholder / to be confirmed / being confirmed（0）、中文残留（0）、demo/drill/演练语境外露（0）、glossary Avoid 列废弃词自动比对（命中 0；词表从 `glossary.txt` 第三列动态读取）。
- `scan_docx.py`：三 docx 的 PUBLISH 泄漏（0）、占位词残留（0）、demo 语境外露（0）。

## 一键顺序执行（重建后核验）

PowerShell：

```
python build_shotstart.py; python build_brand_and_card.py; python check_placeholders.py; python scan_publish.py; python scan_docx.py
```

## 数据源与维护口径（双脚本）

- `shotstart_content.py`：27 个 `pages\*.txt`（12 单件 PDP + 2 捆绑口径 + 中文评委导览例外页 + 政策/营销/表单等页面）与主文案包 docx 的**唯一内容数据源**；`build_shotstart.py` 从该源渲染，禁止直接改产物。
- 品牌定稿与评委速览卡的文案**内联在** `build_brand_and_card.py` 中（不回写 `shotstart_content.py`）；需要修改品牌稿/速览卡文案时，必须改该脚本。
- 维护风险注记：内容分两处维护——改前台页面文案看 `shotstart_content.py`，改品牌稿/速览卡文案看 `build_brand_and_card.py`；两处术语与 CTA 口径需保持一致。
- 扫描脚本读取重建后的 `pages\*.txt` 与三份 docx，复核占位映射、方括号泄漏、中文残留、废弃词与 PUBLISH 外露。
