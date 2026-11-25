"""从原文与有效文本（text/fixes.json 的更正 + 批量规则）的差异生成勘误表 Errata.csv。

用法（项目根目录）:  python -I tools/report.py
每条字符串一行，按类别排序；UTF-8 带 BOM，Excel 可直接打开。格式说明见 README。
"""
import os, sys, csv, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import check, fix

ROOT = os.path.join(HERE, '..')
ERRATA = 'Errata.csv'  # 相对项目根目录
SPEAKER_NOTE = {'军情六处指挥官': '英文为 MI6 Handler，指特工的联络员，不是指挥官',
                '人型机器人': '英文为 Android，与界面敌人名称“仿生人”统一',
                '新兵': '英文为 Recruits，指 00 计划的学员，不是军队新兵'}
BULK_NOTE = {'ellipsis': '省略号统一为“……”', 'qe': '问叹号统一为“？！”'}

# 类别: (名称, note 关键词)。按顺序匹配关键词，都不匹配的归入“错译”；说话人名单独判断
CATS = {
    'markup': ('标签或按键', ['标签', '</b>', '{ES_', '键', '内部字符串', '</br>']),
    'meaning': ('错译', ['误译']),
    'missing': ('漏译', ['漏译', '补译', '旧稿残留', '描述误填']),
    'gender': ('人称性别', ['他→她', '她→他']),
    'terms': ('不统一', ['统一']),
    'tags': ('音效标注', ['音效']),
    'typo': ('错别字', ['错别字', '繁体', '账号']),
    'speaker': ('说话人名', []),
    'punct': ('标点', ['引号', '半角', '标点', '括号']),
    'bulk': ('省略号和问叹号', []),  # 只差批量规则的条目，单独统计
}
ORDER = list(CATS)


def category(note):
    for key in ORDER:
        if any(k in note for k in CATS[key][1]):
            return key
    return 'meaning'


def collect():
    rows = []
    for kind, rid, k, e, f in check.effective():
        o = fix.original(kind)[rid][k]
        base = {'ID': f'{"LOCR" if kind == "ui" else "DLGE"} {rid} / {k}', '说话人': o.get('speaker', ''), '英文原文': o['en']}
        if e['cn'] != o['cn']:
            if f and 'cn' in f:
                cat, note = category(f.get('note', '')), f.get('note', '')
            else:  # 只差批量规则
                cat = 'bulk'
                note = '；'.join(BULK_NOTE[n] for n, pat, rep in fix.BULK if pat.sub(rep, o['cn']) != o['cn'])
            rows.append(dict(base, 类别=cat, 现有译文=o['cn'], 建议译文=e['cn'], 说明=note))
        if f and 'speaker' in f:
            rows.append(dict(base, 类别='speaker', 现有译文=f['was_speaker'], 建议译文=f['speaker'],
                             说明=SPEAKER_NOTE.get(f['was_speaker'], '说话人名不统一')))
    rows.sort(key=lambda r: (ORDER.index(r['类别']), r['ID']))
    for r in rows:
        r['类别'] = CATS[r['类别']][0]
    return rows


def main():
    rows = collect()
    cols = ['ID', '类别', '说话人', '英文原文', '现有译文', '建议译文', '说明']
    with open(os.path.join(ROOT, ERRATA), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, cols, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    print(f'共 {len(rows)} 条 -> {ERRATA}')
    for name, n in collections.Counter(r['类别'] for r in rows).items():
        print(f'  {name}: {n}')


if __name__ == '__main__':
    main()
