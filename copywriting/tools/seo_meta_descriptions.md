# 集合 SEO Meta Description（交建站写入）

> 用途：建站在各集合后台填写 meta description（搜索引擎摘要，非前台可见 DOM）。
> 口径：以下英文为定稿写入文案；zh 为参考译，供中文后台对照。不虚构销量、评分、认证、库存、保修；不出现创立时间、所在地、法律主体名称。
> 这些是元信息字段，**不进 i18n 前台字典**；前台可见串以 `tools/i18n_zh.json` 为准。

## 五个集合

| 集合（EN） | 集合（zh 参考） | Meta description（EN 定稿，写入后台） | Meta description（zh 参考） |
| --- | --- | --- | --- |
| All Gear | 全部装备 | Every ShotStart single item in one collection. | ShotStart 全部单件装备，一站集齐。 |
| Stability & Height | 稳定与高度 | Raise and steady your camera position. | 抬高并稳住你的拍摄机位。 |
| Desk & Angle | 桌面与角度 | Desk shooting and fine angle adjustments. | 桌面拍摄与精细角度调节。 |
| Clean & Care | 清洁与养护 | Keep every lens and frame clear. | 保持每支镜头与画面洁净。 |
| Carry & Set Up | 携带与布场 | Pack, light and set the scene anywhere. | 打包轻便，随处布景开拍。 |

## About 页 meta description 口径

- 当前文案包内 About 前台三段（`pages/about.txt`）不含创立时间、所在地、法律主体名称等主体信息；相关占位仅存于内部注记 `[INTERNAL]`，不上前台。
- 若建站为 About 页补 meta description，使用中性品牌句，**不得**写入年份、城市/地区、公司主体名等未核实信息；待真实主体信息确认后再补。
- 参考中性句（EN）：ShotStart pairs simple filming gear with an AI content assistant to help new creators finish and publish their first short video.
- 参考中性句（zh）：ShotStart 以简单装备搭配 AI 内容助手，帮助新创作者完成并发布第一条短视频。

## 备注

- 包内现有集合页仅 `All Gear` 与 `Creator Kits`（见 `pages/shop.txt`）；Stability & Height / Desk & Angle / Clean & Care / Carry & Set Up 为建站侧用途分组集合，源文案包内无独立集合页。
- `Creator Kits` 集合名已入前台字典：`Creator Kits` → 创作者套装。
