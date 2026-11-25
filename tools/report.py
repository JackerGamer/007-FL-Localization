"""从原文与有效文本（text/fixes.json 的更正 + 批量规则）的差异生成勘误表。

用法（项目根目录）:  python -I tools/report.py
输出 Errata.md（项目根目录）：按类别列出全部更正。
英文、现有、建议译文都相同的多个资源合并为一行；长文本只摘出改动处；省略号、问叹号在文末统一说明。
"""
import os, sys, re, difflib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import check, fix, glacier

ROOT = os.path.join(HERE, '..')
ERRATA = 'Errata.md'  # 相对项目根目录
VERSION = f'{glacier.GAME_VERSION}（Steam BuildID {glacier.BUILD_ID}，{glacier.BUILD_DATE}）'  # 勘误表开头的适用版本
SPEAKER_NOTE = {'军情六处指挥官': '英文为 MI6 Handler，指特工的联络员，不是指挥官',
                '人型机器人': '英文为 Android，与界面敌人标签“仿生人”统一',
                '新兵': '英文为 Recruits，指 00 计划的学员，不是军队新兵'}

# 类别: (标题, note 关键词, 说明)。按顺序匹配关键词，都不匹配的归入“错译”；
# 说话人名单独判断；只差批量规则（省略号、问叹号）的条目归入“标点”，在该节末尾统一说明
CATS = {
    'markup': ('标签或按键提示错误', ['标签', '</b>', '{ES_', '键', '内部字符串', '</br>'],
               '格式标签或按键占位符与英文不一致，导致显示异常或提示了错误的按键。'),
    'meaning': ('错译', ['误译'],
                '意思与英文不符，多因缺少上下文：多义词（armed、handler、commander、tank、Roger、recruit、No shit 等）、'
                '邦德自言自语被译成对别人说、车内台词、菜单短词（Back、Campaign、Buy），以及生造难懂的译名（Knightfall 译作“骑陨”）。'),
    'missing': ('漏译或残留旧稿', ['漏译', '补译', '旧稿残留', '描述误填'],
                '英文的一部分没有译出、残留旧版台本的文字，或显示成了另一条字符串的内容。'),
    'gender': ('人称性别错误', ['他→她', '她→他'], '人称代词“他”“她”用错。'),
    'terms': ('人名、术语不统一', ['统一'],
              '同一人名或术语有多种译法，或译名会造成误解（如 Takedown 译作“处决”，教程说明却是击晕敌人）。'),
    'tags': ('音效标注未翻译', ['音效'], '方括号里的音效描述保留了英文。'),
    'typo': ('错别字与繁体字', ['错别字', '繁体', '账号'], '错别字和混入的繁体字。'),
    'speaker': ('字幕说话人名', [], '说话人名译错或不统一，如 MI6 Handler 应为“军情六处联络员”，不是“指挥官”。'),
    'punct': ('标点', ['引号', '半角', '标点', '括号'],
              '省略号和问叹号的写法（{bulk:,} 条，批量替换即可，见文末），以及半角标点、引号方向、多余空格等。都以 GB/T 15834-2011 为准。'),
}
ORDER = list(CATS)


def category(note):
    for key in ORDER:
        if any(k in note for k in CATS[key][1]):
            return key
    return 'meaning'


def collect(orig):
    """逐条比较原文与有效文本（更正 + 批量规则）。只差批量规则的归入标点（bulk 为真），其余按 note 分类。"""
    rows = []
    for kind, rid, k, e, f in check.effective():
        o = orig[kind][rid][k]
        base = {'type': '界面' if kind == 'ui' else '字幕',
                'id': f'{"LOCR" if kind == "ui" else "DLGE"} {rid} / {k}',
                'speaker': o.get('speaker', ''), 'english': o['en']}
        if e['cn'] != o['cn']:
            if f and 'cn' in f:
                cat, bulk = category(f.get('note', '')), None
            else:
                cat, bulk = 'punct', True
            rows.append(dict(base, category=cat, bulk=bulk, current=o['cn'], suggested=e['cn'], note=f.get('note', '') if f else ''))
        if f and 'speaker' in f:
            rows.append(dict(base, category='speaker', bulk=None, type='说话人名',
                             current=f['was_speaker'], suggested=f['speaker'],
                             note=SPEAKER_NOTE.get(f['was_speaker'], '说话人名不统一')))
    rows.sort(key=lambda r: (ORDER.index(r['category']), r['id']))
    return rows


def md_cell(t):
    """转义为 Markdown 表格单元格：标签原样显示（不被渲染），换行改为 <br>。"""
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = t.replace('|', r'\|').replace('*', r'\*').replace('`', r'\`')
    return re.sub(r'\r?\n', '<br>', t.strip())


def excerpt(a, b, ctx=15, limit=200):
    """长文本只保留改动处及前后文，返回 (a 片段, b 片段)。"""
    if len(a) <= limit and len(b) <= limit:
        return a, b
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != 'equal']
    spans = []
    for _, i1, i2, j1, j2 in ops:
        s = (max(0, i1 - ctx), min(len(a), i2 + ctx), max(0, j1 - ctx), min(len(b), j2 + ctx))
        if spans and s[0] <= spans[-1][1]:
            p = spans[-1]
            spans[-1] = (p[0], max(p[1], s[1]), p[2], max(p[3], s[3]))
        else:
            spans.append(s)
    pa = ['…' * (s[0] > 0) + a[s[0]:s[1]] + '…' * (s[1] < len(a)) for s in spans]
    pb = ['…' * (s[2] > 0) + b[s[2]:s[3]] + '…' * (s[3] < len(b)) for s in spans]
    return ' '.join(pa), ' '.join(pb)


def write_errata(rows, cnt, speaker_total, nbulk):
    """speaker_total: 原文中每个说话人名出现的次数，用于判断某个名字是否被整体替换。
    nbulk: 原文中每条批量规则涉及的条数（含前面各节已逐条列出的）。"""
    # 英文、现有、建议、说明都相同的行合并，ID 列在一起（说话人名不看英文）
    groups = collections.defaultdict(list)
    for r in rows:
        if not r['bulk']:
            en = r['english'] if r['category'] != 'speaker' else ''
            groups[(r['category'], r['type'], en, r['current'], r['suggested'], r['note'])].append(r)
    bulk = sum(1 for r in rows if r['bulk'])
    L = ['# 《007 初露锋芒》简体中文勘误表', '',
         f'> 适用版本：{VERSION}', '',
         f'本表列出游戏简体中文文本中需要更正的 {len(rows):,} 条字符串，每条附建议译文。'
         f'其中 {bulk:,} 条只是省略号或问叹号的写法，批量替换即可，见文末“标点”一节；其余 {len(rows) - bulk:,} 条按类别逐条列出。', '',
         '**范围**：每条都对照了英文，必要时也对照了繁中、日、法、德版本。只收简中独有的错误；'
         '与英文不一致、但与繁中意思相同的（多半依据了配音台本）不在此列。', '',
         '**表格说明**', '',
         '- **ID**：`LOCR` 为界面文本，`DLGE` 为对白字幕，后接资源 hash 和字符串 hash 或元素序号；'
         '同一句出现在多个资源中时合并为一行。',
         '- 长文本（如 EULA）只摘出改动处。',
         '- 分段显示的字幕各段之间换行，建议译文的分段与现有译文相同。',
         '- 建议译文里的省略号、问叹号已按文末“标点”一节统一。', '',
         '## 分类统计', '', '| 类别 | 条数 | 说明 |', '| --- | --- | --- |']
    L += [f'| {CATS[k][0]} | {cnt[k]:,} | {CATS[k][2].format(bulk=bulk)} |' for k in ORDER if cnt[k]]
    for k in ORDER:
        if not cnt[k]:
            continue
        L += ['', f'## {CATS[k][0]}（{cnt[k]:,}）', '']
        listed = any(key[0] == k for key in groups)  # 标点类可能只有批量规则，没有逐条的
        if listed and k == 'speaker':
            L += ['| 现有说话人名 | 建议 | 说明 | 范围 |', '| --- | --- | --- | --- |']
        elif listed:
            L += ['| ID | 说话人 | 英文原文 | 现有译文 | 建议译文 | 说明 |', '| --- | --- | --- | --- | --- | --- |']
        for key, rs in groups.items():
            if key[0] != k:
                continue
            r = rs[0]
            ids = '<br>'.join(f'`{x["id"]}`' for x in rs)
            if k == 'speaker':
                if len(rs) > 1 and len(rs) == speaker_total[r['current']]:
                    ids = f'凡说话人名为“{r["current"]}”的字幕，全部 {len(rs)} 条'
                L.append(f'| {md_cell(r["current"])} | {md_cell(r["suggested"])} | {md_cell(r["note"])} | {ids} |')
                continue
            a, b = excerpt(r['current'], r['suggested'])
            en = r['english'] if len(r['english']) <= 150 else r['english'][:150] + '…'
            sp = '、'.join(sorted({x['speaker'] for x in rs if x['speaker']}))
            L.append(f'| {ids} | {md_cell(sp)} | {md_cell(en)} | {md_cell(a)} | {md_cell(b)} | {md_cell(r["note"])} |')
        if k == 'punct':  # 批量规则不逐条列出，统一说明；条数按全部原文算（含前面各节已列出的）
            if nbulk['ellipsis']:
                L += ['', '### 省略号', '',
                      f'游戏里共 {nbulk["ellipsis"]:,} 条把省略号写成了英文句点（多为“......”，也有“...”“............”）。'
                      'GB/T 15834-2011 规定中文省略号为“……”，游戏界面文本也是这样写的，统一替换即可。']
            if nbulk['qe']:
                L += ['', '### 问叹号', '',
                      f'共 {nbulk["qe"]:,} 条把问叹号写成了“！？”，游戏里另有约同样多的写作“？！”。'
                      'GB/T 15834-2011 规定问号在前，统一替换为“？！”即可。']
    with open(os.path.join(ROOT, ERRATA), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')


def main():
    orig = {k: fix.original(k) for k in ('ui', 'dialogue')}
    rows = collect(orig)
    cnt = collections.Counter(r['category'] for r in rows)
    speaker_total = collections.Counter(v['speaker'] for items in orig['dialogue'].values()
                                        for v in items.values() if v.get('speaker'))
    texts = [v['cn'] for d in orig.values() for items in d.values() for v in items.values()]
    nbulk = {name: sum(pat.sub(rep, t) != t for t in texts) for name, pat, rep in fix.BULK}
    write_errata(rows, cnt, speaker_total, nbulk)
    print(f'共 {len(rows)} 条 -> {ERRATA}')
    for k in ORDER:
        print(f'  {CATS[k][0]}: {cnt[k]}')


if __name__ == '__main__':
    main()
