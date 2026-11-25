# 007 First Light Localization

《007 初露锋芒》（IO Interactive，Glacier 2 引擎）简体中文本地化修正项目（字体替换仍在开发中）。

基于游戏版本 1.3.2（Steam BuildID 10870473，2026-11-24）。**游戏更新后密钥、偏移和 packagedefinition 都可能变化**，见文末“游戏更新后”。

**只想安装补丁**：到 [Releases](https://github.com/JackerGamer/007-FL-Localization/releases/latest) 下载压缩包，解压后按 `安装说明.txt` 操作，不需要下面的工具。

## 快速使用

只依赖 Python 3。游戏目录默认为 `D:\SteamLibrary\steamapps\common\007 First Light`，可用环境变量 `FL_GAME_DIR` 覆盖。以下命令都在项目根目录运行。仓库不含游戏原文，克隆后先运行 `export.py`，其他命令都要用到它导出的文件。

| 命令 | 作用 |
| --- | --- |
| `python -I tools\export.py` | 从游戏导出简中原文（附英文）到 `text\original\`，克隆后和游戏更新后运行 |
| `python -I tools\check.py` | 按规则检查译文，问题逐条打印，最后一行是各规则条数 |
| `python -I tools\fix.py ...` | 登记一条修改或确认到 `text\fixes.json` |
| `python -I tools\patch.py install` | 打包补丁并安装到游戏 |
| `python -I tools\patch.py uninstall` | 卸载补丁，还原游戏 |
| `python -I tools\patch.py package` | 打包给玩家的 `build\007FL-zhCN-Fix-<游戏版本>.zip`：补丁包、改好 patchlevel 的 `packagedefinition.txt` 和安装说明，解压复制即可安装，发到 Release |
| `python -I tools\report.py` | 生成勘误表 `Errata.md`（按类别列出全部更正） |

登记示例：

```powershell
python -I tools\fix.py dialogue 011BD9B549AE1B87 0 --cn "你根本就不该在这儿！" --note "原译与原文无关"
```

```powershell
python -I tools\fix.py ui 01FF8FD1D37DB622 6262E0D0 --ok --note "各语言都只有人名"
```

## 文件

| 路径 | 内容 |
| --- | --- |
| [`tools/`](tools/) | `glacier.py`（rpkg / XOR / LZ4 / XTEA）、`locr.py`、`dlge.py`，以及上表的各个命令 |
| `text/original/ui.json` | 界面原文 `{LOCR 资源: {字符串 hash: {en, cn}}}`，203 个资源、8,870 条 |
| `text/original/dialogue.json` | 对白原文 `{DLGE 资源: {元素序号: {en, cn, speaker, cat, unused?}}}`，17,913 个资源、27,891 条。分段字幕各段用换行连接；`unused` 表示只有英文有字幕（应是未使用的台词） |
| [`text/fixes.json`](text/fixes.json) | 逐条更正和确认 `{"ui"\|"dialogue": {资源: {序号: {cn?, was?, speaker?, was_speaker?, ok?, note}}}}` |
| [`Errata.md`](Errata.md) | 勘误表：按类别列出全部更正和建议译文，`report.py` 生成 |
| `build/` | 打包出的 patch rpkg 和玩家压缩包 |
| `backup/` | 安装前备份的 `packagedefinition.txt`（卸载时要用，别删） |

`text/original/`、`build/`、`backup/` 都在本机生成，不进仓库。`text/original/` 是从游戏导出的全部文本，版权归 IO Interactive，请勿上传。

`text/original/` 只读；改动只写在 `fixes.json`，`was` / `was_speaker` 自动记下原译和原说话人名，`ok` 表示确认原译无误、检查时跳过。省略号（`......` 等 → `……`）和问叹号（`！？` → `？！`）不逐条登记，由 `fix.py` 的 `BULK` 规则统一套用到全部文本；检查、打包、勘误表用的都是“原文 + 更正 + 批量规则”后的有效文本（`check.effective`）。分段字幕的 `cn` 也按行写，段数必须和原文一致（`fix.py` 会检查），打包时按原来的时间轴拆回各段。

`Errata.md` 每次运行 `report.py` 都会整个重写，手改会被覆盖，要改标题或说明文字请改 `report.py`，版本号和日期在 `glacier.py` 的 `GAME_VERSION` / `BUILD_ID` / `BUILD_DATE`。2026-11-24 已提交给官方，之后持续更新，以仓库中的版本为准。

## 判断原则与当前结果

check.py 的规则：原文已变（`was` 与当前原文不符，或原文里已没有这一条）、缺失（`unused` 的台词除外）、占位符（`{ES_xxx}`、`<br>` 等）、乱码、未翻译（含 `[sigh]` 等音效标注）、异体字、标点（含半角引号）、长度。省略号和问叹号由批量规则处理，不再检查。

判断是否要改，同时对照繁中、日、法、德：
- 简中和英文差别大、但繁中（以及日 / 法）意思相同的，多半是中文版依据了另一版台本（配音），**不改**。字幕切分方式各语言也常常不同。
- 只改简中独有的错误：错译、漏译、意思反了、性别错误、术语和人名不统一、错别字、标签损坏。
- 风格上“改了更好、原译也说得通”的不改。

当前结果：共 36,761 条，改译文 444 条、说话人名 129 条，确认无误 55 条（另有 614 条只有英文有字幕的未使用台词，导出时标为 `unused`）；另按国标 GB/T 15834-2011 由批量规则把 1,838 条的 `......` 统一成 `……`、108 条的 `！？` 统一成 `？！`（勘误表“标点”一节只汇总，不逐条列出）。全部检查项均为 0。主要类型（勘误表按类别逐条列出）：

- **一词多义译错**：armed（已激活，不是有枪）、handler（联络员 / 上线）、commander（中校）、Tank（重装兵）、recruit（学员）、Roger（人名）、门罗对邦德的称呼（机组成员，邦德是海军不是空军）、dump（泄露，不是清空）、No shit（还用你说，81 条）等。
- **标签与按键**：EULA 粗体标签不配对、按键占位符错误、显示内部字符串 ID。
- **漏译**：光敏癫痫警告漏句，以及少数只翻了半句的台词。
- **缺上下文**：邦德自言自语被译成对别人说（“建议你去找钱班霓”）、车内 Hold on 译成“等等”、菜单 Back 译成“后退”、Campaign 译成“活动”、界面标题串成别条说明（Keypads）等。
- **挑战**：任务挑战和战术模拟的条件说明（约 560 条）和挑战名逐条对过英文。条件说明主要是照抄上一条（庭院写成“安保室”）、“或”译成“和”、不开枪译成“不伤害任何人”、railing 译成“滑轨”、数量写错，以及任务名、装置名与其他地方不统一；挑战名主要是重名（如两个“寂静之夜”）、双关丢失（如 Gut feeling、Hayhem）和直译生硬。
- **统一**：Takedown（击倒，原译“处决”，44 条）、Agency（特工能力，原混用特工局能力 / 情报机构 / 专注）、说话人 “MI6 Handler” 由“军情六处指挥官”改为“军情六处联络员”（117 条）；人名加里、布莱特等。
- 其他：克蕾西达的“他”→“她”、练拳对手的“她”→“他”、未翻译的音效标注、错别字（畜力、帐号、曝露、電梯、“又”→“有”）、带质问语气的 Excuse me!? 被译成“请原谅”“借过”、行动代号 Knightfall 生造成“骑陨”（改为“骑士陨落”，与繁中一致）。
- **标点**（同样以国标为准）：半角引号和括号、多余空格、句末逗号、缺冒号等 17 处。界面标签末尾的冒号、型号里的连字符（祖科夫斯基-21）、EULA 的 (1) 属正常写法。

注意**分段字幕**（见“格式参考”）：判断是否漏译要看全部段落。简中常把英文的几段合成一段，或者分段位置不同，这都不是漏译。


## 补丁的安装方式

`tools\patch.py install` 做三件事，原版 `chunk0.rpkg` / `chunk1.rpkg` 不动：

1. 从原包读出被修改的 LOCR / DLGE，套用 `fixes.json` 和批量规则，写成 `chunk0patch1.rpkg`、`chunk1patch1.rpkg`（按资源原来所在的 chunk），保留原资源 hash 和引用表，并用读原包的同一套代码回读校验。
2. 复制到 `Runtime\`。
3. `packagedefinition.txt` 是原版（`patchlevel` 都为 0）时先备份到 `backup\`，然后把 `super`、`base` 两个分区的 `patchlevel` 改为 1。

Steam “验证文件完整性”或游戏更新可能会还原 `packagedefinition.txt`，届时补丁不再加载，重新 `install` 即可，备份会随之更新（游戏更新后先确认格式没变）。这时 `uninstall` 也只删补丁文件，不会用旧备份覆盖新版。

**状态：已在游戏中确认生效（2026-11-24）。** 最容易验证的是启动时的光敏癫痫警告：原版缺一句，补丁版多出一句安全提示。

## 格式参考

### RPKG v2

文件头 0x19 字节：magic `2KPR`、`u32` 1、`u8` chunk 编号、`u8` chunk 类型、`u8` patch 编号、`xx` 两字节、`u32` 资源数、`u32` hash 表大小、`u32` 信息表大小。**patch 包**在文件头后多一个删除列表（`u32` 数量 + 若干 `u64` hash）。

- hash 表每项 20 字节：`u64 hash`、`u64 offset`、`u32 size`。bit31 表示 XOR，低位是 LZ4 压缩后大小，0 表示未压缩。
- 信息表每项 20 字节 + 引用表：类型（四字符码反序）、引用表大小、解包后大小、`size_in_memory`、`size_in_video_memory`（LOCR / DLGE 后两项都是 `0xFFFFFFFF`）。
- XOR 密钥 `DC 45 A6 9C D3 72 4C AB`；压缩是 LZ4 block。补丁里的资源不压缩、只做 XOR，原包里也有这样存的 DLGE。

chunk0 约 27 GB，对应分区 `super`；chunk1 约 29.7 GB，对应 `base`。LOCR 170 + 34 个，DLGE 26,280 + 15,877 个。

### 文本加密

XTEA，32 轮，delta `0x9E3779B9`，按 8 字节分块，明文 UTF-8 末尾补 `\0`。

- 文本密钥（LOCR / DLGE / RTLV）：`61 33 ac 68 a0 4a 2b 56 1f 77 f2 b9 e7 3c eb 28`，exe 文件偏移 `0x2b9f1d0`。
- 配置密钥（`packagedefinition.txt` / `thumbs.dat`）：`f0 2c 48 71 9f 4b dc 5f 9d 56 ce 86 1e fc 09 05`。这两个文件的结构是 16 字节固定头 `B7E2EA00545B6B8711BD6FE84D6AD4BF` + 明文 CRC32 + 密文。

语言槽位共 16 个：1 英、2 法、4 德、**10 简中**、11 日、12 繁中（完整顺序：0 英文变体、1 en、2 fr、3 it、4 de、5 es、6 ru、7 mx、8 br、9 pl、10 cn、11 jp、12 tc、13 ko、14 tr、15 uk）。

### LOCR（界面文本）

版本字节（0 或 1）+ 16 个 `u32` 语言块偏移；每个语言块：`u32` 条目数，每条为 `u32 字符串 hash`、`u32 长度`、密文、`0x00`。

### DLGE（对白 / 字幕）

```
8 字节头，之后是元素序列，每个元素首字节为类型：
  1 = 台词：u8 multi；multi=1 时 u32 var_ref, nvar, extra；u32 soundtag, wavname, unk2
      16 种语言 × { i32 wav_ref（multi 且 ≠-1 时再跟 nvar-1 个 i32）, u8 flag, i32 ffx_ref, u32 len + 密文 }
  2 = Random：  u32 a, b, n；n × {u16 ref, u32 c, u32 weight}
  3 = Switch：  u32 key, default, n；n × {u16 ref, u32 m, m × u32}
  4 = Sequence：u32 a, b, n；n × {u16 ref, u32 c}
末尾 u16 根节点引用
```

字幕明文带元数据前缀，字段用 `\\` 分隔，之后是一个或多个 `//(起,止)\\正文`（时间单位为秒）：

```
//[CIVMRM04]\\//{Civilian}\\//##B3B3B3#\\//||\\//%DX_NPC_Story%\\//^1^\\//(0,30)\\Keep moving.
  说话人ID      说话人名        颜色          ?    类别              ?      时间轴    正文
```

**分段字幕**：一句台词可以按时间分几段显示，例如 `…//^1^\\//(0,4.5)\\第一段//(4.5,9)\\第二段`。英文 3,122 条（约 11%）、简中 1,577 条（约 6%）字幕是这样，多为 2～4 段，最多十几段。各语言分段方式不同，中文版有的还沿用了另一个剪辑版本的时间轴。`dlge.split_segments` / `join_segments` 负责拆分和还原，导出时各段正文用换行连接。也有只带元数据、没有时间轴和正文的字幕。

说话人名里可能嵌有 `{0}`（如 `{安保{0}}`），修改时要保留。全部 42,157 个 DLGE 都能逐字节往返，分段也能往返。

**视频字幕也在 DLGE 里**（类别 `DX_Cinematic_*`）。RTLV 只是视频的音频语言映射，GFXV 是不带字幕轨的 CRI USM 视频。

### 字体（GFXF）

BIN1 头包裹的 Scaleform GFX v15（未压缩，GFX 数据从偏移 0x54 开始）。简中字体资源 `01147D5803C66AF1`（32.9 MB，`fonts_chi_sim`）：3 个 DefineFont3（Noto Sans SC ExtraBold / SemiBold / Medium，各约 2.26 万字形），另有 Noto Sans KNT Global、Kimono（拉丁）；导出名 `$bold` `$medium` `$normal` `$global` `$numbers*`。

替换思路：TTF/OTF → DefineFont3（三次曲线需先用 fontTools `cu2qu` 转二次），替换 tag 后修正 GFX 头长度、BIN1 头和 rpkg 信息表大小。

## 游戏更新后

1. 先 `python -I tools\patch.py uninstall`，再更新游戏。
2. `python -I tools\export.py` 重新导出；如果报错，可能是密钥变了：
   - 在 exe 中搜索 XTEA 解密的初始 sum `0xC6EF3720`（字节 `20 37 EF C6`），定位解密函数（当前在文件偏移 `0x803b0`）。注意 `0x9E3779B9` 多数属于哈希函数。
   - 调用这个函数前的 `lea r8, [rip+X]` 指向 16 字节密钥。当前文本密钥在 `0x2b9f1d0`，`0x8026d` 处的调用指向配置密钥。
   - 填进 `tools\glacier.py` 的 `TEXT_KEY` / `CONFIG_KEY` 后重跑导出。
3. `fixes.json` 按资源 hash 和序号定位，导出后先跑 `check.py`：“原文已变”列出官方改过或删掉的条目，逐条重新确认（改好了就删掉那条修改，否则按新原文重新登记），再 `patch.py install`。
4. 改 `tools\glacier.py` 的 `GAME_VERSION` / `BUILD_ID` / `BUILD_DATE`（勘误表、玩家压缩包都用它），重新 `report.py`、`patch.py package`，发新的 Release。

## 进度

- [x] 解析 rpkg、LOCR、DLGE、配置文件，全部逐字节往返
- [x] 导出简中文本，查明视频字幕位置
- [x] 译文检查与修正，生成勘误表
- [x] 打包并安装补丁
- [x] 进游戏确认补丁生效（2026-11-24）
- [ ] 字体替换：TTF → DefineFont3

## 参考

- [glacier-modding/RPKG-Tool](https://github.com/glacier-modding/RPKG-Tool)：《杀手》系列的 rpkg 格式与 XTEA 做法
- [Nexus：《007 初露锋芒》乌克兰语本地化](https://www.nexusmods.com/007firstlight/mods/83)：致谢中提到 ZHMTools、TonyTools（DLGE 格式）
- [Nexus：《007 初露锋芒》希腊语翻译](https://www.nexusmods.com/007firstlight/mods/55)：说明替换自定义字体可行
