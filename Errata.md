# 《007 初露锋芒》简体中文勘误表

> 适用版本：1.3.2（Steam BuildID 10870473，2026-11-24）

本表列出游戏简体中文文本中需要更正的 2,380 条字符串，每条附建议译文。其中 1,930 条只是省略号或问叹号的写法，批量替换即可，见文末“标点”一节；其余 450 条按类别逐条列出。

**范围**：每条都对照了英文，必要时也对照了繁中、日、法、德版本。只收简中独有的错误；与英文不一致、但与繁中意思相同的（多半依据了配音台本）不在此列。

**表格说明**

- **ID**：`LOCR` 为界面文本，`DLGE` 为对白字幕，后接资源 hash 和字符串 hash 或元素序号；同一句出现在多个资源中时合并为一行。
- 长文本（如 EULA）只摘出改动处。
- 分段显示的字幕各段之间换行，建议译文的分段与现有译文相同。
- 建议译文里的省略号、问叹号已按文末“标点”一节统一。

## 分类统计

| 类别 | 条数 | 说明 |
| --- | --- | --- |
| 标签或按键提示错误 | 7 | 格式标签或按键占位符与英文不一致，导致显示异常或提示了错误的按键。 |
| 错译 | 186 | 意思与英文不符，多因缺少上下文：多义词（armed、handler、commander、tank、Roger、recruit、No shit 等）、邦德自言自语被译成对别人说、车内台词、菜单短词（Back、Campaign、Buy），以及生造难懂的译名（Knightfall 译作“骑陨”）。 |
| 漏译或残留旧稿 | 12 | 英文的一部分没有译出、残留旧版台本的文字，或显示成了另一条字符串的内容。 |
| 人称性别错误 | 3 | 人称代词“他”“她”用错。 |
| 人名、术语不统一 | 65 | 同一人名或术语有多种译法，或译名会造成误解（如 Takedown 译作“处决”，教程说明却是击晕敌人）。 |
| 音效标注未翻译 | 24 | 方括号里的音效描述保留了英文。 |
| 错别字与繁体字 | 7 | 错别字和混入的繁体字。 |
| 字幕说话人名 | 129 | 说话人名译错或不统一，如 MI6 Handler 应为“军情六处联络员”，不是“指挥官”。 |
| 标点 | 1,947 | 省略号和问叹号的写法（1,930 条，批量替换即可，见文末），以及半角标点、引号方向、多余空格等。都以 GB/T 15834-2011 为准。 |

## 标签或按键提示错误（7）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `LOCR 01179467BC0E9F2F / 0B4C5557` |  | &lt;b&gt;6. Liability&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;SUMMARY:&lt;/u&gt; there are some situations where we may be legally responsible to each other. These positions differ depen… | &lt;b&gt;6.责任&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要… …保证或声明。&lt;br/&gt;&lt;br/&gt;&lt;b&gt;6.4.责任限制（美国及非英… …/&gt;&lt;br/&gt;&lt;b&gt;7.终止&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… | &lt;b&gt;6.责任&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要… …保证或声明。&lt;br/&gt;&lt;br/&gt;6.4.责任限制（美国及非英… …/&gt;&lt;br/&gt;&lt;b&gt;7.终止&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… | 章节标题缺 &lt;/b&gt;；6.4 多余的 &lt;b&gt;（英文无粗体）。另有一处 &lt;br/&gt; 差异不影响显示 |
| `LOCR 01179467BC0E9F2F / 7C4B65C1` |  | &lt;b&gt;3. Rules for the 007 First Light Services&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;SUMMARY:&lt;/u&gt; this section sets out the rules you must follow for using the 007 First Ligh… | …07 初露锋芒》服务的所有权&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… …&lt;br/&gt;&lt;b&gt;5.虚拟物品&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… | …07 初露锋芒》服务的所有权&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… …&lt;br/&gt;&lt;b&gt;5.虚拟物品&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;&lt;u&gt;摘要：… | 章节标题缺 &lt;/b&gt;，后文会整段变粗体 |
| `LOCR 013C9CB95EEBC692 / 79143A6B` |  | Use {ES_Move/NoGesture} and {ES_CloseCombat_Sidestep} to sidestep a grab. | {ES_MoveRight}和{ES_CloseCombat_Sidestep}侧闪躲避擒拿。 | 使用{ES_Move/NoGesture}和{ES_CloseCombat_Sidestep}侧闪躲避擒拿。 | 应为移动键 {ES_Move}，原译只显示“右移”键 |
| `LOCR 01679BA07B61C09F / 1FB7A10E` |  | Q-04: Impetus cube test #5 - Pending<br> <br>&lt;br&gt;Stress Test Chamber: Q-Watch - Certified - Operational | Q-04：Impetus立方体测试#5——待定<br><br>&lt;br&gt;压力测试室：Q博士腕表——已认证，运行中&lt;/br&gt; | Q-04：Impetus立方体测试#5——待定<br><br>&lt;br&gt;压力测试室：Q博士腕表——已认证，运行中 | 多余的无效标签 &lt;/br&gt; |
| `LOCR 019ACD7BF6EEE5FD / EBD3BCE0` |  | {ES_QuickMeleeAttack} twice, then hold {ES_ChargedMeleeAttack/NoGesture}, to perform a late guard break with a gut punch, then press {ES_QuickMeleeAtt… | 按两次{ES_QuickMeleeAttack/NoGesture}，然后{ES_ChargedMeleeAttack}，用一记击腹拳执行延迟破防，然后再次{ES_ChargedMeleeAttack}将敌人踢开。 | 按两次{ES_QuickMeleeAttack/NoGesture}，然后按住{ES_ChargedMeleeAttack/NoGesture}，用一记击腹拳执行延迟破防，然后再按一次{ES_QuickMeleeAttack/NoGesture}将敌人踢开。 | 踢开应按轻击键而非蓄力键；补“按住” |
| `LOCR 01C60F7F0A636F7D / 86D50E2C` |  | Gadgets Online | ['Ivy_Setpieces_ExoDamien_GadgetsOnline_D'] | 装置已上线 | 译文是内部字符串 ID |
| `LOCR 01F66B96654B7259 / 8DC570D6` |  | Authority | 官方 | 官员 | Authority 是 NPC 身份标签，指当权人员，不是“官方” |

## 错译（186）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 01002E3BD8CE1EE8 / 0` | 敌人{0} | Yeah.<br>This one's armed. | 是啊，这个人居然有枪 | 是啊，这个已经激活了 | armed 指炸弹已激活（日“作動してる”、德“scharf”），不是“有枪” |
| `DLGE 01016D39A402D224 / 0`<br>`DLGE 01043A525DA3BFC1 / 0`<br>`DLGE 0108DD3DD4436878 / 0`<br>`DLGE 011841ABB4BA07BF / 0`<br>`DLGE 0118EBFB923400BD / 0`<br>`DLGE 011B957C49410D84 / 0`<br>`DLGE 01233308C37A17CF / 0`<br>`DLGE 01281A87D2A81376 / 0`<br>`DLGE 012975FF3E3ACB76 / 0`<br>`DLGE 012BBED9F5F80030 / 0`<br>`DLGE 012E1A7F5B8BA261 / 0`<br>`DLGE 012F05CE65D6787D / 0`<br>`DLGE 0133919A552E8B40 / 0`<br>`DLGE 01366C101A8D8BBF / 0`<br>`DLGE 0144D25B13468EC9 / 0`<br>`DLGE 014BB77E9284B36E / 0`<br>`DLGE 01710F8B2E561EEC / 0`<br>`DLGE 01727D559256BCE2 / 0`<br>`DLGE 0178A4CDA3D463AB / 0`<br>`DLGE 0179AC26D4A21E46 / 0`<br>`DLGE 017C4CA73EF5C632 / 0`<br>`DLGE 017E6883405F3F95 / 0`<br>`DLGE 0180A6810A550944 / 0`<br>`DLGE 01870F106EE23CC8 / 0`<br>`DLGE 0196CE7BDA69AE90 / 0`<br>`DLGE 019D0B295723ACA2 / 0`<br>`DLGE 01A19D216550DCE9 / 0`<br>`DLGE 01B9C618DB06EACB / 0`<br>`DLGE 01BA0C93DAA37930 / 0`<br>`DLGE 01BA8238E4FCB071 / 0`<br>`DLGE 01C6BE460376D7E0 / 0`<br>`DLGE 01CBC2FEB1CCE0A1 / 0`<br>`DLGE 01D6042123B9BB84 / 0`<br>`DLGE 01E781FB34DA6EBA / 0`<br>`DLGE 01EB40CC98787E64 / 0`<br>`DLGE 01EDDA5A1307BBC5 / 0`<br>`DLGE 01FB9E92C6BCD152 / 0` | 安保、平民、雇佣兵 | No shit. You need some extra muscle? | 我服了。你需要帮手吗？ | 还用你说。你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 0107D662BEF6484C / 0`<br>`DLGE 0119C15ADA3F0C94 / 0`<br>`DLGE 0133AF40241A3CFC / 0`<br>`DLGE 014DF7485EC888B1 / 0`<br>`DLGE 015E720954026AB4 / 0`<br>`DLGE 01628B35435CFBFE / 0`<br>`DLGE 0174E2E453F4B2DA / 0`<br>`DLGE 01771DB9EE4FA890 / 0`<br>`DLGE 017E918AF6A50EBA / 0`<br>`DLGE 01817477ABDEB1B9 / 0`<br>`DLGE 01A780D0222EDA29 / 0`<br>`DLGE 01B67EC685218B22 / 0`<br>`DLGE 01D74D8F8AFC3646 / 0`<br>`DLGE 01E422B42597C618 / 0`<br>`DLGE 01E61D2D8AFF325D / 0`<br>`DLGE 01F17ADD324DA309 / 0`<br>`DLGE 01F18E7A952AF2D1 / 0`<br>`DLGE 01FA07307517149E / 0` | 安保、平民 | No shit. Have a look around. | 别瞎说，四下看看吧 | 还用你说，四下看看吧 | No shit 意为“这还用说”，原译“别瞎说”意思不对（繁中作“還用說”） |
| `DLGE 0109EC69DDC890AE / 0`<br>`DLGE 011271BCB7F2A68E / 0`<br>`DLGE 012089750CE0F5E9 / 0`<br>`DLGE 014911CEAF472828 / 0`<br>`DLGE 015375B36503A3CF / 0`<br>`DLGE 0163371FFA030919 / 0`<br>`DLGE 0163E589E68C2AAB / 0`<br>`DLGE 01BD8757B7235257 / 0`<br>`DLGE 01BFB8254D3E12C4 / 0`<br>`DLGE 01CB1EE064F60E13 / 0`<br>`DLGE 01EB535A6863E660 / 0`<br>`DLGE 01F5D9DEA3B6E611 / 0`<br>`DLGE 01F7E244BBB95F80 / 0`<br>`DLGE 01FC3A8CC49711A3 / 0` | 平民、雇佣兵 | No shit. Have a look around. | 别瞎说。四下看看吧 | 还用你说。四下看看吧 | No shit 意为“这还用说”，原译“别瞎说”意思不对（繁中作“還用說”） |
| `DLGE 010B04836E3ED263 / 0` | Valhalla | Arming missiles. Twelve per cent complete. Stand by. | 导弹武装中。完成12%。待命 | 导弹激活中。已完成12%。请待命 | arming 指武器激活 |
| `DLGE 010ECAC45B3AED08 / 0` | 海盗{0} | Hey, you wouldn't happen to have spare engine block kicking around?<br>Something that won't blow up if we breathe on it would be nice. | 嘿，你们这儿有没有多余的发动机组？最好是那种不会一碰就炸的 | 嘿，你们这儿有没有多余的发动机缸体？最好是那种不会一碰就炸的 | engine block 是发动机缸体，不是“发动机组” |
| `DLGE 010FBF8BA3DA6CC2 / 0` | 军情六处员工{0} | Good. But put that on slow burn for now and await the results from the diplomacy. | 好，我们在斯洛伐克的常驻人员用得上吗？ | 好。不过这事先缓一缓，等外交那边的结果吧 | 原译“我们在斯洛伐克的常驻人员用得上吗？”与原文无关 |
| `DLGE 01113020711155AC / 0` | 加里 | That drone nearly gave our new recruit a free haircut. Keep your test flights tighter. | 那架无人机差点给新兵免费理发，试飞范围控制得更严格些 | 那架无人机差点给我们的新学员免费理发，试飞范围控制得更严格些 | recruit 指 00 计划学员，不是军队新兵 |
| `DLGE 011526C71F5BE19C / 0` | 军情六处员工 | Ah, recruit Bond. Check out the latest styles. Whatever you fancy. | 啊，新兵邦德，看看最新的款式，喜欢什么随便挑 | 啊，学员邦德，看看最新的款式，喜欢什么随便挑 | recruit 指 00 计划学员，不是军队新兵 |
| `DLGE 011AE605800900F6 / 2` | 格林威 | Serious? Serious? Serious? Serious? Serious? No wait... Serious? | 当然？ | 认真的？认真的？认真的？认真的？认真的？不对，等等……认真的？ | 误译：Serious? 不是“当然” |
| `DLGE 011BD9B549AE1B87 / 0` | 门罗 | You shouldn't even be here! | 你傲慢又自私 | 你根本就不该在这儿！ | 原译“你傲慢又自私”与原文无关；繁中/日/法均为“你根本不该在这里” |
| `DLGE 011DEC168B8E9E63 / 0` | 邦德 | Better get that mission briefing from Moneypenny. | 建议你去找钱班霓拿任务简报 | 我最好去找钱班霓拿任务简报 | 邦德自言自语（同组“我应该去找钱班霓”），原译“建议你去”变成了对别人说 |
| `DLGE 012192CEB51AEB25 / 0` | 客人 | Oh... they did? What do you think I should do? | 哦......她们真这么问？<br>你觉得我该去吗？ | 哦……她们真这么问？<br>你觉得我该怎么办？ | 后半句是“我该怎么办”，不是“我该去吗”（繁中/日文均如此） |
| `DLGE 0123C8684A19B2F9 / 0` | 军情六处员工 | Commander Bond. The bridge is yours. | 邦德指挥官，舰桥由您指挥 | 邦德中校，舰桥交给您了 | Commander 是海军军衔“中校” |
| `DLGE 0125B27F2DCCA9B7 / 0` | 邦德 | Alright? Ali said I could take a look around operations. We just bought at the auction. | 好了！阿里说我可以参观参观你们的运营，我们刚在拍卖会上买下了 | 你好啊！阿里说我可以参观参观你们的运营，我们刚在拍卖会上买下了 | 句首 Alright? 是英式打招呼，不是“好了！” |
| `DLGE 012713ED38987CFA / 0`<br>`DLGE 012C1A33D08DE722 / 0`<br>`DLGE 0180C15F95E1FBB0 / 0`<br>`DLGE 018C816F95128BA9 / 0`<br>`DLGE 0197FBDC2015A063 / 0`<br>`DLGE 01CE00E9FA714A93 / 2`<br>`DLGE 01D177A8D2D07C65 / 0`<br>`DLGE 01D8FC4FE3210D83 / 2` | 平民 | Excuse me!? I think you should leave. | 请原谅！？我想你应该离开了 | 喂？！我想你应该离开了 | “Excuse me!?”在这里是不满地质问，不是“请原谅” |
| `DLGE 01280168F66D493C / 0` | 门罗 | Okay, Aircrew, you're up.<br>If you're serious about earning your place, let's go. | 行了，空军来的家伙，到你了。如果你真想证明自己，跟我来 | 行了，机组成员先生，到你了。如果你真想证明自己，跟我来 | 邦德是皇家海军机组人员，不是空军；门罗别处称他“机组成员先生”（Mr Aircrewman） |
| `DLGE 012C9595BE409D5B / 0` | 邦德 | Enjoyed that. | 尝尝这个！ | 真过瘾 | 车内台词 Enjoyed that（刚才真好玩），原译“尝尝这个！” |
| `DLGE 0131192032EB8E0D / 0` | 安保 | No shit. Do you need some extra muscle? | 我服了。你需要帮手吗？ | 还用你说。你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 013136123F6A239C / 0` | 韦伯员工 | Look, hey, if you can't cut the mustard,<br>don't get on a helicopter in the middle of the Southern Ocean, am I right? | 听着，要是受不了噪音，就别在暴风雪天坐直升机，我说得对不对？ | 听着，要是受不了噪音，就别跑到南大洋中间去坐直升机，我说得对不对？ | Southern Ocean 是南大洋，原译“暴风雪天” |
| `DLGE 01320A042883DF8A / 1` | 邦德 | Right, Q's waiting. | 去吧，Q在等你 | 对，Q还在等着呢 | 邦德自言自语（Q 在等他），原译“去吧，Q在等你”像是叫别人去 |
| `DLGE 01399BF07C42E9D1 / 0` | 雇佣兵 | No shit. Yeah, have a look around. | 别瞎说。好啊，四下看看吧 | 还用你说。好啊，四下看看吧 | No shit 意为“这还用说”，原译“别瞎说”意思不对（繁中作“還用說”） |
| `DLGE 013AE83D63FA7F7C / 0` | 尼古拉斯爵士 | Health monitoring device.<br>Like all tech, its purpose can be redirected,<br>such as dumping every last bit of MI6 data the moment that my heart stops beat… | 健康监测装置，和所有科技产品一样，它的功能可以被重设<br>——比如在我心跳停止的瞬间，清空军情六处的所有数据 | 健康监测装置，和所有科技产品一样，它的功能可以被重设<br>——比如在我心跳停止的瞬间，把军情六处的所有数据全部泄露出去 | 意思反了：dump 指（死后自动）公开泄露，不是“清空”；繁中“洩漏出去”、法语 diffusées |
| `DLGE 013DAE3CF0B19261 / 0` | 平民 | Excuse me!? | 借过！？ | 喂？！ | “Excuse me!?”是表示不满的“喂/搞什么”，不是“借过”（日文作“失礼します！？”带质问语气） |
| `DLGE 013E77BC9DA0AEEE / 0` | 钱班霓 | Whoa. That's... beautiful. | 哇哦<br>挺......帅啊 | 哇哦<br>真是……太美了 | beautiful 是“美”，原译“帅”不对 |
| `DLGE 01439DE225FD1A55 / 0` | 辛格 | Give her hell, okay?<br>We need her to call her handler. | 给她点颜色瞧瞧，明白吗？我们得逼她联系指挥官 | 给她点颜色瞧瞧，明白吗？我们得逼她联系上线 | handler 指派克的上线，不是指挥官 |
| `DLGE 0143BB0C466E1E9E / 0`<br>`DLGE 016A424A6F942FAD / 0`<br>`DLGE 0170F66917DE99DB / 0`<br>`DLGE 01B031464B228378 / 0` | 平民 | No shit. You need some extra muscle? | 我服了，你需要帮手吗？ | 还用你说，你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 01450F0B1B3250CC / 0` | 邦德 | I would've handled it my way. | 你本可以用我的方式处理 | 我本可以用自己的方式解决 | 人称错：邦德说的是自己 |
| `DLGE 014CF05779861820 / 0` | 敌人{0} | They are all armed. | 他们全都有枪 | 它们全都已经激活了 | armed 指炸弹已激活（日“作動中”、德“scharf”），不是“有枪” |
| `DLGE 0150D81E466EBE90 / 0` | 军情六处员工 | Nine hours engaged, 30 to handover. I need an extension. Let me check. I'll get back to you. | 已经开始9小时，30小时后交接。我需要延期。我先确认一下，稍后回复你 | 已经工作9小时，还有30分钟交接。我需要延期。我先确认一下，稍后回复你 | 30 to handover 是 30 分钟后交接（繁中同），原译“30小时” |
| `DLGE 01576220911527CA / 0` | 安保 | No shit. You need extra muscle? | 我服了。你需要帮手吗？ | 还用你说。你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 0157F76188239140 / 0` | 邦德 | Reception. Good man. | 大厅啊，你真是个好人 | 前台是吧，多谢 | Reception 是前台；Good man 在此是道谢，原译“你真是个好人” |
| `DLGE 015FD179379AF5CE / 0` | 邦德 | Just keeping you on your toes. | 只管保持警觉 | 我只是想让你保持警觉 | 车内对白 Just keeping you on your toes，原译“只管保持警觉”变成了祈使句 |
| `DLGE 01611BB2396B4AB3 / 0` | 邦德 | Back into character. | 集中精神 | 该入戏了 | 邦德在执行伪装身份，get back in character 指回到角色，不是“集中精神” |
| `DLGE 01611BB2396B4AB3 / 1` | 邦德 | Let's get back in character. | 让我们集中精神 | 继续演戏吧 | 邦德在执行伪装身份，get back in character 指回到角色，不是“集中精神” |
| `DLGE 01611BB2396B4AB3 / 2` | 邦德 | Time to get back in character. | 该集中精神了 | 是时候重新入戏了 | 邦德在执行伪装身份，get back in character 指回到角色，不是“集中精神” |
| `DLGE 0166D1ADE67A641E / 0` | Valhalla | Machine guns armed and ready to fire. | 机枪已武装，准备开火 | 机枪已激活，准备开火 | armed 指武器已激活 |
| `DLGE 0168E5FB5420C7AD / 0` | 特种空勤团 | Damn it, recruit. If you're gonna stand and stare like that,<br>you might as well join in! | 还愣着干什么，新兵！再发呆就给我滚去训练场和他们一起！ | 还愣着干什么，学员！再发呆就给我滚去训练场和他们一起！ | recruit 指 00 计划学员，不是军队新兵 |
| `DLGE 01718E6F7D9563E7 / 0` | 格林威 | Operation Knightfall. | 骑陨行动 | 骑士陨落行动 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `DLGE 01798AE2BD32D1A9 / 0` | 门罗 | They knew each other though. That much is clear.<br>Something to do with an operation called Knightfall. | 不过，他们认识彼此，这点我是知道的。他们在一场名为骑陨的行动中有过交集 | 不过，他们认识彼此，这点我是知道的。他们在一场名为骑士陨落的行动中有过交集 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `DLGE 0180D9543A5056D0 / 0` | 邦德 | Excuse you. | 借过一下 | 真没礼貌 | Excuse you 是回敬对方无礼（日 失敬だね、法 On dit « pardon »），不是“借过一下” |
| `DLGE 018BE74914C92E44 / 0` | 邦德 | Still looking? | 好，我马上就搞定 | 还在找吗？ | 原文是问句（繁中、日、法均同），原译与原文无关 |
| `DLGE 0195076CF56C15E4 / 0` | 安保 | No shit. You need some backup? | 我服了。你需要帮手吗？ | 还用你说。你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 0199A45F872B15DF / 0` | 门罗 | Don't let him beat you up this time. | 这次别让他揍趴下 | 这次别被他揍趴下 | 原译“别让他揍趴下”有语病（像是让对手倒下）；对手为男性 |
| `DLGE 01A8F5CC340EE338 / 0` | 军情六处员工{0} | Ah... so it wasn't a terrorist strike. It was a heist. The plot thickens. | 啊......所以是恐怖袭击,是场抢劫案。剧情变复杂了 | 啊……所以不是恐怖袭击，是场抢劫案。剧情变复杂了 | 误译：wasn't 译成了“是”，意思反了；半角逗号 |
| `DLGE 01B1F2C4D54EA242 / 0` | 邦德 | Hello, gorgeous. | 你好啊，美人 | 你好啊，帅哥 | Hello, gorgeous 的对象为男性（繁中帅哥、日 イケメン君、德 Hübscher），原译“美人” |
| `DLGE 01B366B770E014A4 / 0` | 特种空勤团 | Report to your superior officer, recruit. | 去向你的上级军官报到，新兵 | 去向你的上级报到，学员 | recruit 指 00 计划学员，不是军队新兵；邦德的上级是军情六处的人，不是军官（繁中“上級”、日文“上官”也不限定军官） |
| `DLGE 01B3823EE0DEA704 / 0` | 海盗{0} | Next time I'm staying on dry land.<br>[Sighs] I'll go see what I can do about that engine block. | 下次我要留在陆地上<br>我去看看发动机组还能不能修 | 下次我要留在陆地上<br>我去看看发动机缸体还能不能修 | engine block 是发动机缸体，不是“发动机组” |
| `DLGE 01BB85D9A88894F5 / 0` | 安保 | No shit. You need some extra muscle. | 我服了。你需要帮手吗？ | 还用你说。你需要几个帮手 | No shit 意为“这还用说”，原译“我服了”意思不对；后半句是陈述“你得多带几个人”，不是问句（繁中“你應該多帶點人”） |
| `DLGE 01BEDF85C0A98A99 / 0` | 钱班霓 | They served together as 00's.<br>Right up until Operation Knightfall. | 他们曾经是00计划的同僚，直到骑陨行动 | 他们曾经是00计划的同僚，直到骑士陨落行动 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `DLGE 01C27CA0516665DD / 0` | 邦德 | Hold on. | 等等 | 抓稳 | 车内台词 Hold on 是“抓稳”（繁中、日、法、德同），不是“等等” |
| `DLGE 01C2C895DB3F6ED0 / 0` | 特种空勤团{0} | Luck like that just isn't natural. | 我自认倒霉 | 那种运气根本不正常 | 原译“我自认倒霉”意思不对；繁中/日/法均为“运气好得不正常” |
| `DLGE 01C6B723AE1A3230 / 0` | 特种空勤团 | Go find your squad, recruit. | 去找你的小队，新兵 | 去找你的小队，学员 | recruit 指 00 计划学员，不是军队新兵 |
| `DLGE 01D7CD3A74EF867B / 0` | 雇佣兵 | No shit. You need some extra muscle. | 我服了。你需要几个帮手 | 还用你说。你需要几个帮手 | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 01D98DE38E58E6C8 / 0` | Valhalla | Missiles armed and loaded. | 导弹已武装并装载 | 导弹已激活并装填完毕 | armed 指武器已激活 |
| `DLGE 01E1B131CE259B4D / 0` | 邦德 | Q, what do you know of Operation Knightfall? | Q，你对“骑陨行动”了解多少？ | Q，你对“骑士陨落行动”了解多少？ | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `DLGE 01E68E18C997CC19 / 0` | 安保 | Farewell. | 永别了 | 再见 | 安保送客用语 Farewell，原译“永别了” |
| `DLGE 01E6D77B63806048 / 0` | 平民 | No shit. You need some extra help? | 我服了。你需要帮手吗？ | 还用你说。你需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 01EDA25C52A24270 / 0` | 员工 | Yes, sir. | 遵命，长官 | 好的，先生 | 员工对客人说 Yes, sir，不是“遵命，长官” |
| `DLGE 01F5D1F9C003CD59 / 0` | 安保 | No shit. Need some extra muscle? | 我服了。需要帮手吗？ | 还用你说。需要帮手吗？ | No shit 意为“这还用说”，原译“我服了”意思不对 |
| `DLGE 01F7E680D52E6B52 / 0` | 邦德 | Roger. He wasn't needing it. | 收到，反正他也用不着了 | 罗杰的，反正他也用不着了 | Roger 指罗杰·芬奇（门禁卡是他的；日文作“ロジャーのだ”），不是“收到” |
| `LOCR 01016CE7AFD99CDA / 5423389F` |  | Bond travels to Vietnam on a covert solo operation. THEIA, it appears, has detected another big data “phantom pattern”, mistaking the statistically un… | 邦德受命单兵潜入越南展开调查。目前看起来，THEIA再一次在大数据中识别出了所谓的“幽灵模式”——将两位绿色能源先驱在统计上极为罕见、而又毫无关联的死亡事件，误判为神秘恐怖分子卡利班所为。然而，国际刑警组织的最新报告早已确认卡利班数月前就已身亡。为了掩盖这场算法误判，达米安正悄然前往海岸的豪华度假村“珍珠酒店”，策划一起模仿杀人案，以“证明”卡利班依然在行动。 | 邦德受命独自潜入越南展开调查。目前看起来，THEIA再一次在大数据中识别出了所谓的“幽灵模式”——将两位绿色能源先驱在统计上极为罕见、而又毫无关联的死亡事件，误判为神秘恐怖分子卡利班所为。然而，国际刑警组织的最新报告早已确认卡利班数月前就已身亡。为了掩盖这场算法误判，达米安正悄然前往海岸的豪华度假村“珍珠酒店”，策划一起模仿杀人案，以“证明”卡利班依然在行动。 | solo 指独自行动，不是士兵 |
| `LOCR 01016CE7AFD99CDA / 56176FE3` |  | Bond goes on a covert solo operation at The Pearl, a luxury resort in Vietnam, to stop Damien Webb from covering up another of THEIA’s mistakes and re… | 邦德单兵前往越南豪华度假村“珍珠酒店”展开调查，以阻止达米安·韦伯掩盖THEIA的另一项错误，并获取韦伯家族不当行为的确凿证据。 | 邦德独自前往越南豪华度假村“珍珠酒店”展开调查，以阻止达米安·韦伯掩盖THEIA的另一项错误，并获取韦伯家族不当行为的确凿证据。 | solo 指独自行动，不是士兵 |
| `LOCR 010D87B96C8BC0BF / 6B6C072D` |  | How you dune? | 我名声臭了 | 沙丘狂飙 | 挑战名（毛里塔尼亚海滩越野驾驶，谐音 How you doin'），原译“我名声臭了”与内容无关 |
| `LOCR 0119FDF6FA06C404 / 48E05D3F` |  | The recruits accompany Greenway on an undercover mission to apprehend the rogue 009 during the World Chess Championship in Slovakia. But Greenway, who… | 新兵们跟随格林威执行一项卧底任务，目标是在斯洛伐克举行的世界国际象棋锦标赛期间抓捕叛逃的009。但格林威不信任邦德，不想让他参与行动，于是安排他担任司机。 | 学员们跟随格林威执行一项卧底任务，目标是在斯洛伐克举行的世界国际象棋锦标赛期间抓捕叛逃的009。但格林威不信任邦德，不想让他参与行动，于是安排他担任司机。 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 0119FDF6FA06C404 / 787D46DD` |  | 009, a rogue MI6 operative guilty of high treason, has resurfaced after years off the grid. He claims to hold evidence of a conspiracy against the sta… | 009是一名犯了叛国罪的叛变军情六处特工，在脱离监控多年后重新出现。<br>他声称掌握证据，指向一起针对国内的阴谋，并打算将其交给约翰·格林威以换取赦免。<br>会面将在斯洛伐克大喀尔巴阡酒店的世界国际象棋锦标赛期间举行，M派遣00新兵作为卧底后援。<br>然而格林威并不信任邦德，想让他远离行动场地，派他担任司机这个平平无奇的角色。<br>看来邦德的第一次外勤任务将受限于停车场。 | 009是一名犯了叛国罪的叛变军情六处特工，在脱离监控多年后重新出现。<br>他声称掌握证据，指向一起针对国内的阴谋，并打算将其交给约翰·格林威以换取赦免。<br>会面将在斯洛伐克大喀尔巴阡酒店的世界国际象棋锦标赛期间举行，M派遣00学员作为卧底后援。<br>然而格林威并不信任邦德，想让他远离行动场地，派他担任司机这个平平无奇的角色。<br>看来邦德的第一次外勤任务将受限于停车场。 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 011E219C785493F4 / 3C6AC1B8` |  | Complete "Knightfall". | 完成“骑陨”。 | 完成“骑士陨落”。 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 011E219C785493F4 / B9D3299D` |  | Knightfall | 骑陨 | 骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 0120ADA8FBD3074E / D2E37A17` |  | M has called the recruits to MI6. She’s suspending exams to send them on a mission. Rogue agent 009 is coming in from the cold. | M暂停了新兵的考核，召集他们前往军情六处执行新任务。叛变特工009再次现身，开始行动。 | M暂停了学员的考核，召集他们前往军情六处执行新任务。叛变特工009再次现身，开始行动。 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 012A22CFB455E37C / 39E30F8B` |  | Snap | 吸附 | 分段 | VR 的 snap rotation 是分段转向，不是“吸附”（瞄准辅助的 aim snap 才是吸附） |
| `LOCR 012A22CFB455E37C / 7C294EAB` |  | Adjust the speed of the smooth snap rotation. | 调节平滑吸附旋转的速度。 | 调节平滑分段转向的速度。 | VR 的 snap rotation 是分段转向，不是“吸附”（瞄准辅助的 aim snap 才是吸附） |
| `LOCR 012A22CFB455E37C / 91F0AFAC` |  | Adjust the rotation degree per snap. | 调节每次吸附旋转的角度。 | 调节每次分段转向的角度。 | VR 的 snap rotation 是分段转向，不是“吸附”（瞄准辅助的 aim snap 才是吸附） |
| `LOCR 012A22CFB455E37C / CB2D562F` |  | Smooth snap | 平滑吸附 | 平滑分段 | VR 的 snap rotation 是分段转向，不是“吸附”（瞄准辅助的 aim snap 才是吸附） |
| `LOCR 0133F8407AD41C5B / 5DEB62E8` |  | Bond impersonates Pike and successfully makes her call her handler. The recruits are informed that extraction will take place outside the club in 2 mi… | 在派克被成功制伏后，邦德只得假冒派克与指挥官会面。会面结束时，新晋特工们已掌握全部所需情报。任务完成之际，新晋特工们收到指令，2分钟后于夜店外进行撤离。 | 在派克被成功制伏后，邦德只得假冒派克联系其上线。会面结束时，新晋特工们已掌握全部所需情报。任务完成之际，新晋特工们收到指令，2分钟后于夜店外进行撤离。 | handler 指派克的上线，不是指挥官 |
| `LOCR 01404AF21B80A07E / 752604DC` |  | In Iceland Bond defied the advice of his impromptu MI6 handler and, against all odds, saved an MI6 retrieval team. But his actions caused the destruct… | 在冰岛，邦德不顾临时军情六处指挥官的劝告，冒险救出了一个回收小组。但他的行为却导致任务目标——一枚具有战略价值的敌方卫星被毁，使英国错失重大情报优势。<br>如今重返伦敦总部，等待他的不知是嘉奖还是审判。 | 在冰岛，邦德不顾临时军情六处联络员的劝告，冒险救出了一个回收小组。但他的行为却导致任务目标——一枚具有战略价值的敌方卫星被毁，使英国错失重大情报优势。<br>如今重返伦敦总部，等待他的不知是嘉奖还是审判。 | handler 指联络员 |
| `LOCR 0143C985A773BFA7 / 9EE22280` |  | Jump railing | 翻越滑轨 | 翻越栏杆 | railing 是栏杆，不是“滑轨” |
| `LOCR 014DF8359D8104B3 / 6D67C33B` |  | Photo of recruits | 新兵合影 | 学员合影 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 0168051CBBE7A893 / 45F7B242` |  | Find a way inside and plant the Q-Trak on Ramon. | 想办法潜入内部，将Q追踪器植入拉蒙身上。 | 想办法潜入内部，把Q追踪器放到拉蒙身上。 | plant on 是“放到…身上”，原译“植入拉蒙身上”不通 |
| `LOCR 0168051CBBE7A893 / B31D0A4D` |  | Find a way inside and plant the Q-Trak on Theresa Lorca. | 想办法进去并把Q追踪器植入洛尔卡体内。 | 想办法进去，把Q追踪器放到特蕾莎·洛尔卡身上。 | plant on 是“放到…身上”，不是“植入体内”（Q追踪器是贴在皮肤上的凝胶胶囊） |
| `LOCR 017019D55AFCAD6F / 4C8CA079` |  | Pacifist: Knightfall | 和平主义者：骑陨 | 和平主义者：骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 017019D55AFCAD6F / 7D64BAE4` |  | Ghost: Knightfall | 幽灵：骑陨 | 幽灵：骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 017019D55AFCAD6F / A77BA14A` |  | Complete all challenges in "Knightfall" to unlock the white tux for TacSim. | 完成“骑陨”的所有挑战，即可解锁战术模拟系统的白色礼服。 | 完成“骑士陨落”的所有挑战，即可解锁战术模拟系统的白色礼服。 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 017019D55AFCAD6F / DB13B150` |  | Assault: Knightfall | 突击：骑陨 | 突击：骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 017019D55AFCAD6F / EAFBABCD` |  | Completionist: Knightfall | 完美主义者：骑陨 | 完美主义者：骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 01815574989C4717 / 280B4797` |  | &lt;b&gt;Age:&lt;/b&gt; 57 (deceased).&lt;br&gt;&lt;b&gt;Nationality:&lt;/b&gt; British.&lt;br&gt;&lt;b&gt;Occupation:&lt;/b&gt; Criminal consultant.&lt;br&gt;&lt;b&gt;Background:&lt;/b&gt; A top-ranking 00 agent, Be… | …·韦伯爵士诬陷犯有叛国罪。在骑陨行动后转入地下，并成为毛里塔尼… | …·韦伯爵士诬陷犯有叛国罪。在骑士陨落行动后转入地下，并成为毛里塔尼… | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 01815574989C4717 / B4762D53` |  | &lt;b&gt;Age:&lt;/b&gt; 56. &lt;br&gt;&lt;b&gt;Nationality:&lt;/b&gt; British. &lt;br&gt;&lt;b&gt;Occupation:&lt;/b&gt; MI6 Officer and 00 Training Instructor.&lt;br&gt;&lt;b&gt;Background:&lt;/b&gt; Starting out a S… | …捕或清除三名叛变00特工的“骑陨”行动中扮演了关键角色。00部… | …捕或清除三名叛变00特工的“骑士陨落”行动中扮演了关键角色。00部… | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 0186AC07B4F4058C / 0960D306` |  | Hack a grenade before it explodes | 在手榴弹爆炸前将其引爆 | 在手榴弹爆炸前将其黑入 | 意思反了：hack 是黑入，原译“将其引爆” |
| `LOCR 0186AC07B4F4058C / 75406890` |  | Complete your training as a recruit in Malta | 在马耳他完成新兵培训 | 在马耳他完成学员培训 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 0186AC07B4F4058C / 953FBD04` |  | Damp squib | 事倍功半 | 哑炮 | 挑战说明是在手榴弹爆炸前黑入它；Damp squib 意为哑炮、落空，不是“事倍功半” |
| `LOCR 018D94E35C8F5183 / 273E4F6C` |  | A uniform and dress cap belonging to a Royal Navy Commander. | 皇家海军指挥官的制服和礼帽。 | 皇家海军中校的制服和礼帽。 | Commander 是海军军衔“中校” |
| `LOCR 018D94E35C8F5183 / 97179838` |  | A special edition Royal Navy Commander uniform and dress cap with yellow stripes on the hems. | 一套皇家海军指挥官特别版制服和礼帽，帽檐饰有黄色条纹。 | 一套皇家海军中校特别版制服和礼帽，帽檐饰有黄色条纹。 | Commander 是海军军衔“中校” |
| `LOCR 018D94E35C8F5183 / 996FCB63` |  | Obsidian Gold Suit | 黑曜金西装 | 黑曜金服装 | 这套是黑色战术服配金色面具（见描述），不是西装；与繁中“黑曜金服裝”一致 |
| `LOCR 0196341B19836B90 / 3CE8A154` |  | KNIGHTFALL, WEBB INDUSTRIES | 骑陨，韦伯工业 | 骑士陨落，韦伯工业 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 0196341B19836B90 / C6D1542B` |  | KNIGHTFALL | 骑陨 | 骑士陨落 | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 019ACD7BF6EEE5FD / 1D50C41D`<br>`LOCR 01F66B96654B7259 / 76202997` |  | Tank | 坦克 | 重装兵 | Tank 是敌人类型（重甲精英雇佣兵），不是坦克 |
| `LOCR 019ACD7BF6EEE5FD / 74154357` |  | Tanks are heavy armoured elite mercenaries that know no fear and will advance relentlessly to eliminate any threat. | 坦克是重甲精英雇佣兵，无所畏惧，会无情地推进以消灭任何威胁。 | 重装兵是重甲精英雇佣兵，无所畏惧，会无情地推进以消灭任何威胁。 | Tank 是敌人类型（重甲精英雇佣兵），不是坦克 |
| `LOCR 01AB1EEECEA509BF / 28079E47` |  | Group photo of the recruits | 新兵合照 | 学员合照 | recruit 指 00 计划学员，不是军队新兵 |
| `LOCR 01AE4D67D3D72FCE / 04B3D04C` |  | Buy | 升级 | 购买 | 商城按钮 Buy 应为“购买”，原译“升级”与下一条 Upgrade 重复 |
| `LOCR 01AE4D67D3D72FCE / 0B20DCD1` |  | Campaign | 活动 | 战役 | 主菜单进入“故事”后顶部的层级名，Campaign 指战役（剧情模式）；原译“活动”与 Activities 撞名 |
| `LOCR 01AFE843D8688CA8 / 6A7CB2C5` |  | What is Operation Knightfall? | 什么是“骑陨行动”？ | 什么是“骑士陨落行动”？ | Knightfall 是行动代号，“骑陨”不是现成词语，容易误读；繁中版译作“騎士隕落” |
| `LOCR 01B83ECB108C9A33 / 1A7C1121` |  | Eye to eye | 违规者 | 当面对质 | 对话选项按现行英文 Eye to eye（繁中正面交锋、日、德同）；原译“违规者”对应旧版英文（法语 Fauteurs de troubles 同） |
| `LOCR 01C907E04C9A964E / 0BE75A4A` |  | No setpieces | 戒骄戒躁 | 不碰场景装置 | 挑战说明是不与场景装置互动；原译“戒骄戒躁”与内容无关 |
| `LOCR 01CF5B1F67C9AC83 / 87885B2E` |  | Back | 后退 | 返回 | 菜单按钮 Back 应为“返回”，不是“后退” |
| `LOCR 01D9E3EC689A6B6E / 38BFFFE6` |  | Deflect | 转向 | 格开 | 互动提示 Deflect（格开、拨开），不是“转向” |
| `LOCR 01DBF9AE296DD042 / ADB5BCFE` |  | Poisoned | 感染者 | 中毒 | Poisoned 是“中毒”，不是“感染者” |
| `LOCR 01F66B96654B7259 / 5B113302` |  | Disorient | 迷失 | 迷乱 | 状态效果 Disorient（失去方向感），与眩晕、踉跄并列，不是“迷失” |
| `LOCR 01F66B96654B7259 / 9D27F085` |  | Resistant | 抵抗军 | 抗性 | Resistant 是敌人状态（有抗性），不是“抵抗军” |
| `LOCR 01F66B96654B7259 / E4C6DEEC` |  | Sick | 生病 | 不适 | Sick 是麻醉针手机造成的负面状态（恶心、头晕），不是“生病” |
| `LOCR 01FF73FDDFA54DC7 / 859873E3` |  | MI6 Handler | 军情六处指挥官 | 军情六处联络员 | Handler 指特工的联络员 |

## 漏译或残留旧稿（12）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 0112EF46ECEDC58F / 0`<br>`DLGE 01C001257C39341E / 0` | 军情六处员工{0} | [Whispers] |  | [耳语] | 漏译（繁中已译） |
| `DLGE 014605C509B8F14E / 0` | 克蕾西达 | And again! Give it everything you've got! | 快点，再快点！ | 再来一次！使出全力！ | 漏译：英文台词后来改过，繁中、日、德已按新英文翻译，简中仍是旧稿“快点，再快点” |
| `DLGE 0157E67FD3B5FD26 / 0` | 韦伯特工{0} | [Laughs] That's a good one, must remember it. | 哈哈，你可真逗 | 哈哈，这个笑话不错，我得记下来 | 漏译后半句 must remember it（日、法、德均译出） |
| `DLGE 018046A2F49A5C01 / 7` | 安保 | I need you to step out from behind that. | 请你从出来 | 请你从那后面出来 | 漏译：漏了“那后面”，句子不通 |
| `DLGE 01C2648297F7C28C / 0` | 邦德 | Oh no you don't!<br>Not without me! | 你别想跑！ | 休想！别想丢下我！ | 漏译后半句 Not without me（繁中/日/德均译出）；Oh no you don’t 是“休想”，不是“别想跑” |
| `LOCR 01179467BC0E9F2F / 755FDDD7` |  | In this game you will encounter a variety of visual effects (including but not limited to: strobing light effects, red flashing lights, contrasting pa… | …致少数人出现癫痫发作或失去意识。&lt;br&gt;&lt;br&gt;如果您或您的… …br&gt;&lt;br&gt;如果您在玩游戏时以下任何症状：头晕、视力改变、… …或抽搐，请立即停止游戏并就医。以下提示可能有助于减少癫痫发作… | …致少数人出现癫痫发作或失去意识。即使是从未有过癫痫发作史或癫痫病史的人，这些效果也可能引发癫痫发作。&lt;br&gt;&lt;br&gt;如果您或您的… …br&gt;&lt;br&gt;如果您在玩游戏时出现以下任何症状：头晕、视力改变、… …或抽搐，请立即停止游戏并就医。&lt;br&gt;&lt;br&gt;以下提示可能有助于减少癫痫发作… | 补译漏掉的一句安全提示；补“出现”；恢复段落换行 |
| `LOCR 018D94E35C8F5183 / 06695C67` |  | Black satin tuxedo with matching vest, fitted white dress shirt and silk bow-tie. | 头等舱 | 黑色缎面礼服，配同款马甲、修身白色正装衬衫和真丝领结。 | 描述误填为服装名称“头等舱” |
| `LOCR 018D94E35C8F5183 / 0D6A6280` |  | A black and gold satin tuxedo jacket with black pants and white dress shirt. | 镀金燕尾服 | 黑金配色缎面礼服外套，搭配黑色长裤和白色正装衬衫。 | 描述误填为服装名称 |
| `LOCR 019ACD7BF6EEE5FD / 52E64FE4` |  | Keypads | 使用爆炸物或环境危险来破坏仿生人的装甲。 | 密码键盘 | 描述误填：标题“Keypads”显示成了仿生人教程里的一句说明 |
| `LOCR 019ACD7BF6EEE5FD / F9607BD9` |  | By pressing {ES_QuickMeleeAttack/NoGesture} you can also strike enemies while they are grabbed. | 按{ES_QuickMeleeAttack/NoGesture}擒住敌人并攻击。 | 擒住敌人时，也可以按{ES_QuickMeleeAttack/NoGesture}攻击敌人。 | 漏译：原译读起来像是用这个操作擒住敌人，实际说的是擒住敌人后还可以用它攻击（繁中/日文等均如此） |
| `LOCR 01B39390AE998B76 / 7AD4928D` |  | For this mission we have equipped you with infinite agency resources. Bluff away! | 邦德在此任务中拥有无限特工能力 | 在此任务中，我们为你提供了无限的特工能力资源。尽情虚张声势吧！ | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注）；并补译漏掉的“Bluff away!” |

## 人称性别错误（3）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 010C730408D7EC41 / 3` | 门罗 | Punching's no good. Block him. | 出拳不行，防住她的拳 | 出拳不行，防住他的拳 | 她→他：原文 him，练拳对手为男性 |
| `DLGE 0181F1A5082C41E0 / 0` | 克蕾西达 | Well done, Bond.<br>Now we just need Monroe to scare the socks off her so she calls her boss. | 做得好，邦德。<br>现在我们只需要门罗去把他吓跑，让他给老板打电话 | 做得好，邦德。<br>现在只需要门罗去把她吓个半死，让她给老板打电话 | her 指女性目标，他→她 |
| `DLGE 01FEBF261430FF73 / 0` | 门罗 | Cressida's our top driver. She'll take you through the drill. | 克蕾西达是我们的顶级司机，他会带着你通过训练 | 克蕾西达是我们的顶级司机，她会带你完成训练 | 克蕾西达是女性，他→她 |

## 人名、术语不统一（65）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 0107A58EF9A314C5 / 0` | 邦德 | This all looks very expensive.<br>Best not touch anything,<br>or Basil from accounting will have my head. | 这些看着都价值连城<br>最好什么也别碰，否则财务部的巴兹尔会杀了我 | 这些看着都价值连城<br>最好什么也别碰，否则财务部的巴西尔会杀了我 | Basil 统一译为“巴西尔” |
| `DLGE 018A194B21D13EE3 / 0` | 塞琳娜 | Oh! Hi Gary. This place is starting to look the part. | 嘿！你好，盖瑞，这地方开始变得像样了啊 | 嘿！你好，加里，这地方开始变得像样了啊 | Gary 统一译为“加里”（说话人名和大部分对白都用加里） |
| `DLGE 01CEB46F7F3C9E97 / 0` | 邦德 | Wake up! Secretary Bright’s security detail. We’re checking up on you and your team. | 醒醒！我是布赖特部长的安保组，来检查你们和你们团队的情况 | 醒醒！我是布莱特部长的安保组，来检查你们和你们团队的情况 | Bright 统一译为“布莱特” |
| `DLGE 01DA929DBD509CD7 / 0` | 军情六处员工 | Point taken, Gary. No more free haircuts. | 好的，盖瑞，我们不会再提供免费理发了 | 好的，加里，我们不会再提供免费理发了 | Gary 统一译为“加里”（说话人名和大部分对白都用加里） |
| `DLGE 01F8BDA3DCD79F5B / 0` | 康耶维奇 | I am Nikola Konjevic. | 我是尼古拉·科里耶维奇 | 我是尼古拉·康耶维奇 | Konjevic 统一译为“康耶维奇” |
| `LOCR 0102E49C3D7707C6 / 35460926` |  | Perform a silent takedown inside a camera's field of view while it is hacked. | 趁摄像头被入侵时，在其监控范围内完成一次无声处决。 | 趁摄像头被入侵时，在其监控范围内完成一次无声击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0102E49C3D7707C6 / 4FC4463E` |  | Take out a guard during "The workshop", by performing a silent takedown from an elevated position. | 在“工作间”任务中，于制高点无声处决一名守卫。 | 在“工作间”任务中，于制高点无声击倒一名守卫。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0102E49C3D7707C6 / 7D22BFE9` |  | Take out the guards in the reception before completing the mission on any tier. | 在前台处决所有守卫，再完成任意等级的任务。 | 在前台击倒所有守卫，再完成任意等级的任务。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01031B2E6CC6A7E3 / AA2788CB` |  | Use your dart phone on a concrete bag to create a smoke screen, then perform a silent takedown or finisher while hidden inside. | 对水泥袋使用飞镖电话制造烟雾屏障，然后在烟雾中执行无声处决或终结技。 | 对水泥袋使用飞镖电话制造烟雾屏障，然后在烟雾中执行无声击倒或终结技。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01231BC0C60DA43A / 01AA93FC` |  | Chunk added | 数据块已添加 | 特工能力格已增加 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注）；Chunk 指能力槽的一格，不是“数据块” |
| `LOCR 01231BC0C60DA43A / 543BFF2E` |  | Agency gained | 获得特工局能力 | 获得特工能力 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 01231BC0C60DA43A / BAAB9263` |  | Agency max | 特工局能力已满值 | 特工能力已满 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 012AEE294C87AB81 / 2D120BDD`<br>`LOCR 012AEE294C87AB81 / 56B3F1AC`<br>`LOCR 012AEE294C87AB81 / F57DC0EE`<br>`LOCR 0191FD901264FC15 / 10AFEC89`<br>`LOCR 0191FD901264FC15 / B17F5081`<br>`LOCR 019ACD7BF6EEE5FD / 834D335F` |  | Takedown | 处决 | 击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 012BEB206C0B1897 / B513FB3D` |  | Take down the intruder. | 处决入侵者 | 击倒入侵者 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 012FE9B5D6943262 / 1D5F1FD4` |  | Do three takedowns from above in a mission. | 在一次任务中从高处完成三次击杀。 | 在一次任务中从高处完成三次击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“击杀”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0133ECB47979E665 / 6D962ECE` |  | Take down the guards to access the ID upgrade station. | 处决守卫们以到达身份证明升级站。 | 击倒守卫们以到达身份证明升级站。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 013C9CB95EEBC692 / 5E87880A` |  | {ES_CloseCombat_Finisher} to perform a takedown. | {ES_CloseCombat_Finisher}处决。 | {ES_CloseCombat_Finisher}击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0143C985A773BFA7 / EA03EA3E` |  | Not enough agency | 特工局能力不足 | 特工能力不足 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 0150E1E74D041BAA / 2AC3363B` |  | Murto has learned from the previous encounter. &lt;br&gt;&lt;br&gt;He's armed with a knife. Performing a silent takedown will no longer work. Find different ways … | 穆尔托已经从之前的交锋中学到了教训。&lt;br&gt;&lt;br&gt;他现在手持匕首，无声处决已不再奏效，得想别的办法攻击敌人。 | 穆尔托已经从之前的交锋中学到了教训。&lt;br&gt;&lt;br&gt;他现在手持匕首，无声击倒已不再奏效，得想别的办法攻击敌人。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0150E1E74D041BAA / 55018270` |  | Silent takedowns no longer work. Find different ways to hurt him. | 无声处决已不再奏效，得想别的办法攻击敌人。 | 无声击倒已不再奏效，得想别的办法攻击敌人。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0150E1E74D041BAA / 9354F3B6` |  | {ES_SilentTakedown} to do a takedown from behind an enemy. | 绕到敌人背后后，{ES_SilentTakedown}执行处决 | 绕到敌人背后后，{ES_SilentTakedown}执行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0150E1E74D041BAA / 98EF24B2` |  | Use confrontation {ES_Bluff/NoGesture} to diffuse situations: &lt;br&gt;Bluff to get out of trouble. &lt;br&gt;Distract enemies by hacking nearby objects. &lt;br&gt;Fak… | 使用对峙{ES_Bluff/NoGesture}来化解局面：&lt;br&gt;- 通过虚张声势摆脱麻烦。&lt;br&gt;入侵附近目标以转移敌人注意力。&lt;br&gt;假意投降后进行处决。 | 使用对峙{ES_Bluff/NoGesture}来化解局面：&lt;br&gt;- 通过虚张声势摆脱麻烦。&lt;br&gt;入侵附近目标以转移敌人注意力。&lt;br&gt;假意投降后进行击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0150E1E74D041BAA / 9EEAE132` |  | {ES_SilentTakedown} to do a takedown from above. | {ES_SilentTakedown}从高处执行处决 | {ES_SilentTakedown}从高处执行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0150E1E74D041BAA / E78B3625` |  | {ES_SilentTakedown} to do a cover takedown. | 按{ES_SilentTakedown/NoGesture}从掩体中执行处决 | 按{ES_SilentTakedown/NoGesture}从掩体中执行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01679BA07B61C09F / F0D48C1E` |  | Bridget - Critical gadgets field certified. Waiting for next batch to test.<br>Gary - Equipment requests have been sent off to procurement.<br>Henry - Q-W… | 布里奇特：重要装置已通过实战认证。正在等待下一批测试。<br>盖瑞：已向采购部门提交设备需求。<br>亨利：Q博士腕表已通过实战认证。当前正在进行压力测试，等待最终审核。<br>沃特斯：最新一代配枪已送达。已被记录在案、存放于军械库。 | 布里奇特：重要装置已通过实战认证。正在等待下一批测试。<br>加里：已向采购部门提交设备需求。<br>亨利：Q博士腕表已通过实战认证。当前正在进行压力测试，等待最终审核。<br>沃特斯：最新一代配枪已送达。已被记录在案、存放于军械库。 | Gary 统一译为“加里”（说话人名和大部分对白都用加里） |
| `LOCR 017019D55AFCAD6F / 8798D850` |  | Take down eight guards in the data centre, hack the three servers and return to Greenway without alerting anyone. | 在不惊动任何人的情况下，处决数据中心的八名守卫，黑入三个服务器，然后回到格林威身边。 | 在不惊动任何人的情况下，击倒数据中心的八名守卫，黑入三个服务器，然后回到格林威身边。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 0176ED1012C4CEAB / BD985CB2` |  | Time to see if you can stay in the shadows and not get seen. While this may challenge your ego, in this mission we only allow silent takedowns. No gun… | 现在，是时候考验你融入暗影的能力了。这也许会让你觉得有些憋屈，但本次任务仅限无声处决。禁止开枪，禁止投掷，更别指望能拿茶壶当手雷扔。记住，一旦暴露，直接出局！ | 现在，是时候考验你融入暗影的能力了。这也许会让你觉得有些憋屈，但本次任务仅限无声击倒。禁止开枪，禁止投掷，更别指望能拿茶壶当手雷扔。记住，一旦暴露，直接出局！ | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01815574989C4717 / 5825AF3E` |  | After being resigned to the dust bin of history for the better part of a decade, the newly appointed M resurrected the defunct 00 branch. <br>Seven outs… | …勤团行动人员。<br>克蕾西达·布赖特，国防情报局网络情报官。<br>… | …勤团行动人员。<br>克蕾西达·布莱特，国防情报局网络情报官。<br>… | Bright 统一译为“布莱特” |
| `LOCR 01815574989C4717 / FE52A48A` |  | &lt;b&gt;Age:&lt;/b&gt; 60.&lt;br&gt;&lt;b&gt;Nationality:&lt;/b&gt; British.&lt;br&gt;&lt;b&gt;Occupation:&lt;/b&gt; UK Foreign Secretary.&lt;br&gt;&lt;b&gt;Background:&lt;/b&gt; Belongs to one of Britain’s wealthie… | …00部门并在斯洛伐克受伤后，布赖特大臣变得愈发反对重启00部门… | …00部门并在斯洛伐克受伤后，布莱特大臣变得愈发反对重启00部门… | Bright 统一译为“布莱特” |
| `LOCR 0192B79AAABA4790 / 6A2A658C` |  | For this training exercise you are provided with unlimited agency resource to practice with. | 在此训练练习中，为你提供了无限的专注以供练习。 | 在此训练练习中，你拥有无限的特工能力资源可供练习。 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 0192B79AAABA4790 / 98319D8C` |  | Gamechanger: Unlimited Agency | 游戏规则变化：无限使用专注 | 游戏规则变化：无限特工能力 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 019ACD7BF6EEE5FD / 11A073BA` |  | Use the environment to stay hidden and distract/lure guards: &lt;br&gt;- Hack objects with the Q-Lens ({ES_GadgetView/NoGesture} and {ES_ActivateGadget/NoGe… | 利用环境保持隐蔽、分散或吸引守卫注意力：&lt;br&gt;-{ES_GadgetView/NoGesture}和{ES_ActivateGadget/NoGesture}激活Q眼镜并黑入物体。&lt;br&gt;-吹口哨({ES_Whistle/NoGesture})，将守卫引诱到邦德的位置。&lt;br&gt;-在隐蔽状态下按{ES_QuickMeleeAttack/NoGesture}处决敌人。 | 利用环境保持隐蔽、分散或吸引守卫注意力：&lt;br&gt;-{ES_GadgetView/NoGesture}和{ES_ActivateGadget/NoGesture}激活Q眼镜并黑入物体。&lt;br&gt;-吹口哨（{ES_Whistle/NoGesture}），将守卫引诱到邦德的位置。&lt;br&gt;-在隐蔽状态下按{ES_QuickMeleeAttack/NoGesture}击倒敌人。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒”；半角括号改为全角，与其他教程说明一致 |
| `LOCR 019ACD7BF6EEE5FD / 3978D9B5` |  | Takedown finisher | 处决终结技 | 击倒终结技 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 019ACD7BF6EEE5FD / 4E7FE923` |  | Disarm finisher | 缴械处决 | 缴械终结技 | 统一：finisher 为“终结技”（同 Takedown finisher），原译“缴械处决” |
| `LOCR 019ACD7BF6EEE5FD / 6AF9CB02` |  | {ES_SilentTakedown} to perform a takedown on an unsuspecting enemy. | {ES_SilentTakedown}对毫无防备的敌人进行处决。 | {ES_SilentTakedown}对毫无防备的敌人进行击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 019ACD7BF6EEE5FD / A071880F` |  | Takedown stealth | 潜行处决 | 潜行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 019ACD7BF6EEE5FD / ED1C12ED` |  | Use armour piercing weapons like rifles and heavy pistols. Alternative focus fire on the weaker helmet, arms or leg plates.<br>If they get close, try an… | 使用步枪和重型手枪等穿甲武器。或者集中火力攻击较弱的头盔、手臂或腿甲。<br>如果坦克靠近，尝试在其换弹时冒险使用战斗冲刺，并用拳击和环境打击来打掉坦克的头盔，或使用投掷物和装置将其震晕。 | 使用步枪和重型手枪等穿甲武器。或者集中火力攻击较弱的头盔、手臂或腿甲。<br>如果重装兵靠近，尝试在其换弹时冒险使用战斗冲刺，并用拳击和环境打击来打掉重装兵的头盔，或使用投掷物和装置将其震晕。 | 统一：敌人类型 Tank 为“重装兵”，此条漏改 |
| `LOCR 019ACD7BF6EEE5FD / F3F09AB8` |  | {ES_CloseCombat_Finisher/NoGesture} to perform a takedown on a dazed enemy. | {ES_CloseCombat_Finisher}对眩晕的敌人进行处决。 | {ES_CloseCombat_Finisher}对眩晕的敌人进行击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01AE4D67D3D72FCE / 0D0C9930` |  | Colour for agency elements in the UI. | 用于在界面中显示机构相关元素的颜色。 | 用于在界面中显示特工能力相关元素的颜色。 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 01AE4D67D3D72FCE / 12E34A4E` |  | Agency | 情报机构 | 特工能力 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 01AE4D67D3D72FCE / 3B46599D`<br>`LOCR 01FAB37E89190CAE / 77BE118A` |  | Stealth takedown | 潜行处决 | 潜行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01B39390AE998B76 / 14415C26` |  | Only silent takedowns allowed. | 只能进行无声处决。 | 只能进行无声击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01B39390AE998B76 / 3F37AC14` |  | Silent takedowns not allowed. | 禁止无声处决。 | 禁止无声击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01B39390AE998B76 / 50B0D0E6` |  | No agency resources available. | 无情报机构资源可用。 | 无特工能力资源可用。 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 01B39390AE998B76 / 88B0A0C8` |  | No silent takedowns | 禁用无声处决 | 禁用无声击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01B39390AE998B76 / 98C54C03` |  | Infinite agency resource. | 无限情报机构资源。 | 无限特工能力资源。 | 统一：Agency 是驱动专注、虚张声势、引诱的能力资源，统一为“特工能力”（原译混用特工局能力/情报机构/专注） |
| `LOCR 01B39390AE998B76 / A3C650FA` |  | Silent takedowns only | 仅用无声处决 | 仅用无声击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01B39390AE998B76 / DD26729A` |  | For the duration of this mission, silent takedowns of all kinds have been disabled. | 此任务禁用无声处决 | 本次任务期间，所有类型的无声击倒均已禁用。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；并补全原译省略的“所有类型” |
| `LOCR 01B39390AE998B76 / F65082A8` |  | This mission will only allow silent takedowns. Get the jump on hostiles from above, from behind a cover or sneak up on them while they look the other … | 此任务仅允许进行无声处决。你可以从高处或掩体后突袭敌人，也可以趁他们不注意时悄悄靠近将其制服。 | 此任务仅允许进行无声击倒。你可以从高处或掩体后突袭敌人，也可以趁他们不注意时悄悄靠近将其制服。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C238405C7C62CA / 2F7C486E` |  | Eliminate all enemies with stealthy takedowns only. | 仅使用潜行处决消灭所有敌人。 | 仅使用潜行击倒消灭所有敌人。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C907E04C9A964E / 098C2DDF` |  | Do a takedown and a bluff in the span of 10 seconds. | 在10秒内，完成一次处决和一次虚张声势。 | 在10秒内，完成一次击倒和一次虚张声势。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C907E04C9A964E / 33864CAF` |  | Do a silent takedown every 30 seconds until you complete the mission. | 每30秒无声处决一人，直至完成任务。 | 每30秒无声击倒一人，直至完成任务。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C907E04C9A964E / 3A0F40D7` |  | Takedown marathon | 处决马拉松 | 击倒马拉松 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C907E04C9A964E / 9C784B63` |  | Toxic takedown | 毒气中的处决 | 毒气击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01C907E04C9A964E / F8DA9F0A` |  | Do 3 silent takedowns inside a gas leak. | 在毒气泄漏区域内完成3次无声处决。 | 在毒气泄漏区域内完成3次无声击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01E796AB9E4791E5 / 124D0C92` |  | Perform 5 silent takedowns while hidden inside foliage. | 隐藏在植物丛中时进行5次无声处决。 | 隐藏在植物丛中时进行5次无声击倒。 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |
| `LOCR 01F66B96654B7259 / 9C25E056` |  | Gary | 盖瑞 | 加里 | Gary 统一译为“加里”（说话人名和大部分对白都用加里） |
| `LOCR 01F66B96654B7259 / E41C6709` |  | Hack | 骇入 | 黑入 | Hack 统一为“黑入”（其余 35 处都不用“骇入”） |
| `LOCR 01FAB37E89190CAE / 066DCFF6` |  | Strike / stealth takedown | 攻击/潜行处决 | 攻击/潜行击倒 | 统一：Takedown 是击倒（教程说明为“击晕敌人”），原译“处决”意为杀死；游戏里其余挑战说明已用“击倒” |

## 音效标注未翻译（24）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 012EA53F03E19B09 / 0`<br>`DLGE 016931952A800397 / 0` | 平民 | That’s it. [sigh] Again. | 很好，[sigh]第二次了 | 很好，[叹气]第二次了 | 音效标注未翻译 |
| `DLGE 013EFDFE24DF65C4 / 2`<br>`DLGE 01D684E326B14BF7 / 2` | 平民 | [scoff] What is wrong with people today? | [scoff]今天这些人是怎么回事？ | [嗤笑]今天这些人是怎么回事？ | 音效标注未翻译 |
| `DLGE 01485B90B4CCD4A0 / 2` | 平民 | Could I just [scoff] squeeze by? | 我能[scoff]挤过去吗？ | 我能[嗤笑]挤过去吗？ | 音效标注未翻译 |
| `DLGE 014ECAC0597B9D18 / 3`<br>`DLGE 018CBED34FC9D339 / 3` | 平民 | [sigh] Why are you still here? | [sigh]你怎么还在这儿？ | [叹气]你怎么还在这儿？ | 音效标注未翻译 |
| `DLGE 01770178C14F4CA3 / 0` | 雇佣兵 | [scoff] Make it fast. | [scoff]动作快点 | [嗤笑]动作快点 | 音效标注未翻译 |
| `DLGE 017DE74B03FFE6EB / 3`<br>`DLGE 019B60F5502F460A / 3` | 平民 | Hello. [scoff] Did I not just tell you? | 你好，[scoff]我不是刚跟你说过吗？ | 你好，[嗤笑]我不是刚跟你说过吗？ | 音效标注未翻译 |
| `DLGE 019E840EC7BD4E2C / 3` | 雇佣兵 | [Scoffs] You again? Leave or I'll break your legs! | [scoff]又是你？离开，否则我打断你的腿！ | [嗤笑]又是你？离开，否则我打断你的腿！ | 音效标注未翻译 |
| `DLGE 01A9F2479AB29C1C / 0`<br>`DLGE 01FE930525918E29 / 0` | 平民、雇佣兵 | [whistle] Didn't see that coming. Well, don’t let me stop you. | [whistle]这倒是没想到。行吧，我不碍你的事 | [口哨]这倒是没想到。行吧，我不碍你的事 | 音效标注未翻译 |
| `DLGE 01AA58FC41FC8725 / 0` | 雇佣兵 | Oh, [chuckle] you're not stupid after all... | 噢，[chuckle]看来你也没那么蠢嘛...... | 噢，[轻笑]看来你也没那么蠢嘛…… | 音效标注未翻译 |
| `DLGE 01B6977010BF9C2C / 0` | 雇佣兵 | [scoff] Are you kidding me? | [scoff]你逗我呢？ | [嗤笑]你逗我呢？ | 音效标注未翻译 |
| `DLGE 01BC81F6E136D7D7 / 2` | 雇佣兵 | [scoff] Show some respect now. | [scoff]放尊重点 | [嗤笑]放尊重点 | 音效标注未翻译 |
| `DLGE 01C3DF1774DA38B8 / 0` | 平民 | Right... [sigh] Well, you better get out of here. | 好吧......[sigh]你最好离开这儿 | 好吧……[叹气]你最好离开这儿 | 音效标注未翻译 |
| `DLGE 01CA4A7DFD0BDF6B / 1` | 平民 | What!? [scoff] Right, you need to leave, ok? | 什么！？[scoff]行了，你该走了，明白吗？ | 什么？！[嗤笑]行了，你该走了，明白吗？ | 音效标注未翻译 |
| `DLGE 01CA4A7DFD0BDF6B / 2`<br>`DLGE 01D63AFA62E78793 / 0` | 平民 | Huh? [scoff] You certainly shouldn't be here. Get moving. | 哈？[scoff]你绝对不该来这儿。赶紧离开 | 哈？[嗤笑]你绝对不该来这儿。赶紧离开 | 音效标注未翻译 |
| `DLGE 01E3121648B35615 / 0` | 雇佣兵 | [scoff] Some people have no shame. Hope you catch them. | [scoff]有些人真不要脸。希望你能抓着他们 | [嗤笑]有些人真不要脸。希望你能抓着他们 | 音效标注未翻译 |
| `DLGE 01F5C856B5E89F9C / 3` | 雇佣兵 | [Scoffs] Unbelievable. I said leave! | [scoff]难以置信，我说了离开！ | [嗤笑]难以置信，我说了离开！ | 音效标注未翻译 |
| `DLGE 01FD621EFDB446DE / 0` | 雇佣兵 | [scoff] Sounds like my Christmas lights. Go ahead, do your thing. | [scoff]听着跟我家那圣诞彩灯一个德行。行了，干你的活儿吧 | [嗤笑]听着跟我家那圣诞彩灯一个德行。行了，干你的活儿吧 | 音效标注未翻译 |
| `DLGE 01FEA750FD9E4ED6 / 2` | 平民 | [sigh] Sir, we are very busy today! | [sigh]先生，我们今天非常忙！ | [叹气]先生，我们今天非常忙！ | 音效标注未翻译 |

## 错别字与繁体字（7）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 012053C30BD16737 / 2` | 安保 | Excuse me? Are you meant to be here? | 打扰一下？你又在这里的权限吗？ | 打扰一下？你有在这里的权限吗？ | 错别字：“又”应为“有” |
| `DLGE 0197BE20955D0E59 / 1` | 门罗 | Flipping hell. If you're trying to break character you're doing a cracking job. | 该死，你再这样下去，身份可就要曝露了 | 该死，你再这样下去，身份可就要暴露了 | 错别字：身份“曝露”应为“暴露” |
| `LOCR 01179467BC0E9F2F / 461CCE33` |  | Playing 007 First Light with a guest profile is not supported. | 我们不支持使用游客帐号玩《007 初露锋芒》。 | 我们不支持使用游客账号玩《007 初露锋芒》。 | “帐号”→规范写法“账号” |
| `LOCR 01179467BC0E9F2F / DA4F27C9` |  | You must be signed into a profile to play 007 First Light. | 你必须登录帐号才能玩《007 初露锋芒》。 | 你必须登录账号才能玩《007 初露锋芒》。 | “帐号”→规范写法“账号” |
| `LOCR 019ACD7BF6EEE5FD / 8629037D` |  | Use armour piercing weapons like rifles or heavy pistols. When those are unavailable aim for unarmored parts, power through with volume of fire or res… | 使用步枪或重型手枪等穿甲武器，若没有上诉武器，则瞄准未装甲部位，用密集火力压制，或诉诸近战。 | 使用步枪或重型手枪等穿甲武器，若没有上述武器，则瞄准未装甲部位，用密集火力压制，或诉诸近战。 | 错别字：“上诉”应为“上述” |
| `LOCR 01C5D7160A3D5566 / BB23292F` |  | Lift | 電梯 | 电梯 | 繁体字 |
| `LOCR 01FAB37E89190CAE / F113F136` |  | Charged strike | 畜力攻击 | 蓄力攻击 | 错别字 |

## 字幕说话人名（129）

| 现有说话人名 | 建议 | 说明 | 范围 |
| --- | --- | --- | --- |
| 军情六处指挥官 | 军情六处联络员 | 英文为 MI6 Handler，指特工的联络员，不是指挥官 | 凡说话人名为“军情六处指挥官”的字幕，全部 117 条 |
| 人型机器人 | 仿生人 | 英文为 Android，与界面敌人标签“仿生人”统一 | 凡说话人名为“人型机器人”的字幕，全部 11 条 |
| 新兵 | 学员们 | 英文为 Recruits，指 00 计划的学员，不是军队新兵 | `DLGE 013E0A9B2BB46171 / 0` |

## 标点（1,947）

| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `DLGE 010191EE9CC126F6 / 2` | 钱班霓 | Get over here, Bond. The techs need to focus. | 过来，邦德,技术人员需要集中注意力 | 过来，邦德，技术人员需要集中注意力 | 半角逗号 |
| `DLGE 0111006A2BB734B2 / 0` | 客人{0} | Sure. And "spiritual stuff".<br>Why don't we all focus inwards and enjoy a bit of silence. | 当然，还有”精神修行”。为什么我们大家不都关注内心，享受片刻宁静呢 | 当然，还有“精神修行”。为什么我们大家不都关注内心，享受片刻宁静呢 | 引号方向用错 |
| `DLGE 011FEABD66B82043 / 0` | 园丁 | Oh, I know. It never ends. The Pearl is the gift that keeps on giving. | 可不是嘛，活儿永远干不完，珍珠酒店简直是个"福报"不断的地方 | 可不是嘛，活儿永远干不完，珍珠酒店简直是个“福报”不断的地方 | 半角引号改为中文引号 |
| `DLGE 0187FD62CEAD9174 / 0` | 员工 | Indeed. It seems he was most impressed with your presentation at the summit and said,<br>I quote, 'ensure she is taken care of in a setting equal to her … | 正是，他对您在峰会上的演讲印象深刻，<br>原话是”务必让她在配得上其远见的环境中受到款待”，因此帝王别墅将为您开放 | 正是，他对您在峰会上的演讲印象深刻，<br>原话是“务必让她在配得上其远见的环境中受到款待”，因此帝王别墅将为您开放 | 引号方向用错 |
| `DLGE 018F9ED6D6A1450F / 5` | 邦德 | Eyes wide. Watch your corners. | 睁大眼睛，看好角落， | 睁大眼睛，看好角落 | 标点：句末多了逗号 |
| `DLGE 01B5F8E57978CA20 / 0` | 员工{0} | Ugh, puppy eyes and that "cute" raised eyebrow.<br>Or the pulling off the sweatshirt and the tee "accidentally" lifts to reveal the six-pack. | 呃，睁着那双"无辜"大眼，还故意挑眉"装可爱"<br>要么就是脱卫衣时"不小心"把T恤卷起来，秀他们的腹肌 | 呃，睁着那双“无辜”大眼，还故意挑眉“装可爱”<br>要么就是脱卫衣时“不小心”把T恤卷起来，秀他们的腹肌 | 半角引号改为中文引号 |
| `DLGE 01BEBBD67043913B / 2` | 钱班霓 | Som– thi- | 有——点- | 有——点—— | 标点：中文里用连字符表示话被打断，应为破折号 |
| `DLGE 01CA63BA0BD1F2B1 / 0` | 客人{0} | I didn't ask.<br>I did ask the barman though, he said he'd heard the stories too,<br>that they would come here to have their souls cleansed by the ocean. | 我没问,不过我倒是问过酒保，<br>他说他也听过这些故事，说他们会来这里通过海洋净化灵魂 | 我没问，不过我倒是问过酒保，<br>他说他也听过这些故事，说他们会来这里通过海洋净化灵魂 | 半角逗号改为全角 |
| `LOCR 0102E49C3D7707C6 / 82063F37` |  | Complete "Extraction Avenues" on any tier without getting spotted. | 完成任意等级的"撤离路线"，且全程不被发现。 | 完成任意等级的“撤离路线”，且全程不被发现。 | 半角引号改为中文引号 |
| `LOCR 01031B2E6CC6A7E3 / 6ADAD993` |  | Grab and throw ({ES_Grab/NoGesture}) an enemy into an object to knock them out | 抓取并投掷({ES_Grab/NoGesture})一名敌人撞向物体以将其击晕。 | 抓取并投掷（{ES_Grab/NoGesture}）一名敌人撞向物体以将其击晕。 | 半角括号改为全角，与其他教程说明一致 |
| `LOCR 010A962C5D1FE762 / 4609E417` |  | Complete "Green fingers", "All clear", "Health &amp; safety" and "Art attack". | 完成“园艺能手”、“一切正常”、“健康与安全“和”艺术袭击“。 | 完成“园艺能手”、“一切正常”、“健康与安全”和“艺术袭击”。 | 引号方向用错 |
| `LOCR 012B2BCE40B783D2 / 9E8B9ADB` |  | Complete "Getting Dirty" and "Indiscrete". | 完成“衣衫褴褛“和”粗枝大叶“。 | 完成“衣衫褴褛”和“粗枝大叶”。 | 引号方向用错 |
| `LOCR 0150E1E74D041BAA / C1E2AD65` |  | When in Q-Lens ({ES_GadgetView/NoGesture}), with the dart phone equipped: &lt;br&gt;-{ES_ActivateGadget} with an enemy selected to disorient them. &lt;br&gt;-{ES_… | 在装备飞镖手机的Q眼镜({ES_GadgetView/NoGesture})后：&lt;br&gt;-选中敌人时按{ES_ActivateGadget}使其迷惑。&lt;br&gt;-未选中敌人时按{ES_ActivateGadget}向目标发射飞镖以引诱敌人。 | 在装备飞镖手机的Q眼镜（{ES_GadgetView/NoGesture}）后：&lt;br&gt;-选中敌人时按{ES_ActivateGadget}使其迷惑。&lt;br&gt;-未选中敌人时按{ES_ActivateGadget}向目标发射飞镖以引诱敌人。 | 半角括号改为全角，与其他教程说明一致 |
| `LOCR 015E489BBC58ABAD / E367B54B` |  | Valhalla protocol: Night | Valhalla协议 夜间 | Valhalla协议：夜间 | 标点：缺冒号，与“Valhalla协议：日间”一致 |
| `LOCR 0196341B19836B90 / 9BEB286B` |  | BEYOND THE GRAVE, MAURITANIA | 死亡之后， 毛里塔尼亚 | 死亡之后，毛里塔尼亚 | 标点：逗号后多余空格 |
| `LOCR 01B4B8D71B46C3B8 / 224992B3` |  | Set the number of VBLANKS between flips.&lt;br&gt;&lt;br&gt;For a 60 Hz screen:&lt;br&gt;&lt;br&gt;1 = Max 60 FPS&lt;br&gt;&lt;br&gt;2 = Max 30 FPS | 设置两次翻转之间的垂直消隐数量。 &lt;br/&gt;&lt;br/&gt;对于60赫兹显示器：&lt;br/&gt;&lt;br/&gt;1 = 最高60帧&lt;br/&gt;&lt;br/&gt;2 = 最高30帧 | 设置两次翻转之间的垂直消隐数量。&lt;br/&gt;&lt;br/&gt;对于60赫兹显示器：&lt;br/&gt;&lt;br/&gt;1 = 最高60帧&lt;br/&gt;&lt;br/&gt;2 = 最高30帧 | 标点：句号后多余空格 |
| `LOCR 01B4B8D71B46C3B8 / BB6E647D` |  | Off: Don't show the speaker name next to the subtitle.&lt;br&gt;&lt;br&gt;Character Colour: show the speaker name next to the subtitle in predefined colours for t… | 关闭：不在字幕旁显示说话者名称。&lt;br&gt;&lt;br&gt;角色颜色：在字幕旁以预设的角色颜色显示说话者名称。 &lt;br&gt;&lt;br&gt;自定义颜色：在字幕旁以自定义颜色显示说话者名称。 | 关闭：不在字幕旁显示说话者名称。&lt;br&gt;&lt;br&gt;角色颜色：在字幕旁以预设的角色颜色显示说话者名称。&lt;br&gt;&lt;br&gt;自定义颜色：在字幕旁以自定义颜色显示说话者名称。 | 标点：句号后多余空格 |

### 省略号

游戏里共 1,838 条把省略号写成了英文句点（多为“......”，也有“...”“............”）。GB/T 15834-2011 规定中文省略号为“……”，游戏界面文本也是这样写的，统一替换即可。

### 问叹号

共 108 条把问叹号写成了“！？”，游戏里另有约同样多的写作“？！”。GB/T 15834-2011 规定问号在前，统一替换为“？！”即可。
