"""译文自动检查：对 原文 + text/fixes.json 后的简中做规则检查，问题逐条打印，最后一行是各规则条数。

用法（项目根目录）:  python -I tools/check.py
     python -I tools/check.py > check.txt   （问题多时存到文件再看）
规则（按严重程度）:
  原文已变  fixes.json 记下的原译（was / was_speaker）与当前导出的原文不同，或原文里已没有这一条：游戏更新后要逐条重新确认
  缺失      英文有内容、简中为空（只有英文有字幕的未使用台词除外）
  占位符    {0}、<br/>、%s 等标记与英文不一致（会导致游戏显示异常）
  乱码      替换符、控制字符
  未翻译    简中里没有中文字符但英文是句子
  异体字    繁体字、日文假名、韩文
  标点      中文里夹半角 , ? ! : ; 或半角引号、重复标点、括号引号不配对
  长度      与英文长度差异悬殊（可能错位或截断）
省略号和问叹号由 fix.BULK 统一处理，不在检查之列。
"""
import os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
import fix

CJK = r'㐀-鿿豈-﫿'
RE_CJK = re.compile(f'[{CJK}]')
RE_PH = re.compile(r'\{[^{}\s]{0,60}\}|<[^<>]{1,80}>|%[0-9]*[sdif]|\$[A-Za-z_]\w*|\\n')
RE_KANA = re.compile(r'[぀-ヿㇰ-ㇿ]')
RE_HANGUL = re.compile(r'[가-힯ᄀ-ᇿ]')
RE_HALF_PUNCT = re.compile(f'(?<=[{CJK}])[,?!:;]|[,?!:;](?=[{CJK}])')
RE_DUP = re.compile(r'([，、。；：])\1+')
RE_EN_TAG = re.compile(r"\[[A-Za-z][A-Za-z ,'\-]*\]")
RE_BAD = re.compile(r'[�\x00-\x08\x0b\x0c\x0e-\x1f]')
# 常见繁体字（与简体字形不同、简中里不应出现的）
TRAD = set('這個們說過來時對會還與為從後發國問現點應進動種開關當經長門頭電話聽讓認識體機標務氣樣東車邊軍隊員聯網營處將準確實際義讀書買賣錢錯誤殺號碼記錄設計劃請謝裡麼嗎麗愛學習結選擇慣歡幫歲歷響變顯戰鬥護衛擊傷險槍彈藥導艦飛場廳樓層鑰鎖證據報權級較隱廣頻訊資檔環節顏')

PAIRS = [('（', '）'), ('(', ')'), ('《', '》'), ('“', '”'), ('「', '」'), ('【', '】'), ('[', ']')]


def effective(fixes=None):
    """产出 (类别, 资源, 序号, 条目, 修改记录或 None)。条目含 en/cn 及已应用的修改和批量规则。
    fixes 为 None 时从 text/fixes.json 读取；批量登记时请传入内存中的记录，避免读到旧文件。"""
    if fixes is None:
        fixes = fix.load()
    for kind in ('ui', 'dialogue'):
        fx = fixes.get(kind, {})
        for rid, items in fix.original(kind).items():
            for k, v in items.items():
                f = fx.get(rid, {}).get(k)
                e = dict(v, cn=fix.effective_cn(v, f))
                if f and 'speaker' in f:
                    e['speaker'] = f['speaker']
                yield kind, rid, k, e, f


def stale(o, f):
    """修改记录 f 登记时的原译与当前原文 o 不符（游戏更新改了这条）。"""
    return f and ('was' in f and f['was'] != o['cn'] or 'was_speaker' in f and f['was_speaker'] != o.get('speaker'))


def norm_ph(t):
    """/NoGesture（不显示手势图标）与 <br/> 写法各语言混用，视为等价。"""
    return t.replace('/NoGesture', '').replace('<br/>', '<br>').replace('<br />', '<br>')


def problems(e):
    """返回条目 e 的 [(规则, 说明), ...]。"""
    en, cn = e['en'], e['cn']
    out = []
    if en.strip() and not cn.strip():
        return [] if e.get('unused') else [('缺失', '')]
    if not cn:
        return []
    a = collections.Counter(map(norm_ph, RE_PH.findall(en)))
    b = collections.Counter(map(norm_ph, RE_PH.findall(cn)))
    if a != b:
        miss, extra = a - b, b - a
        out.append(('占位符', f'缺 {list(miss.elements())} 多 {list(extra.elements())}'))
    if RE_BAD.search(cn):
        out.append(('乱码', repr(RE_BAD.findall(cn))))
    if not RE_CJK.search(cn) and re.search(r'[A-Za-z]{3,}.*\s.*[A-Za-z]{3,}', cn) and cn.strip() == en.strip():
        out.append(('未翻译', ''))
    tags = RE_EN_TAG.findall(cn)
    if tags:
        out.append(('未翻译', '英文标注 ' + ' '.join(tags)))
    t = sorted(set(cn) & TRAD)
    if t:
        out.append(('异体字', '繁体 ' + ''.join(t)))
    if RE_KANA.search(cn):
        out.append(('异体字', '假名 ' + ''.join(sorted(set(RE_KANA.findall(cn))))))
    if RE_HANGUL.search(cn):
        out.append(('异体字', '韩文'))
    p = []
    body = re.sub(r'<[^<>]*>', '', cn)  # 去掉标签后的正文
    if RE_HALF_PUNCT.search(cn):
        p.append('半角 ' + ''.join(sorted(set(RE_HALF_PUNCT.findall(cn)))))
    if '"' in body and RE_CJK.search(cn):
        p.append('半角引号')
    if RE_DUP.search(cn):
        p.append('重复 ' + ''.join(m.group() for m in RE_DUP.finditer(cn)))
    for l, r in PAIRS:
        if body.count(l) != body.count(r):
            p.append(f'不配对 {l}{r}')
    if cn != cn.strip() and en == en.strip():
        p.append('首尾空白')
    if p:
        out.append(('标点', '；'.join(p)))
    le, lc = len(en.strip()), len(cn.strip())
    if le >= 60 and lc * 8 < le:
        out.append(('长度', f'英文 {le} 字符，中文仅 {lc} 字'))
    elif le and le <= 20 and lc >= 30 and lc > le * 2.5:
        out.append(('长度', f'英文仅 {le} 字符，中文 {lc} 字'))
    return out


ORDER = ['原文已变', '缺失', '占位符', '乱码', '未翻译', '异体字', '标点', '长度']


def main():
    if not sys.stdout.isatty():  # 重定向到文件时用 UTF-8，避免 GBK 编不了的字符
        sys.stdout.reconfigure(encoding='utf-8')
    found = collections.defaultdict(list)
    total = 0
    fixes = fix.load()
    for kind, rid, k, e, f in effective(fixes):
        total += 1
        if stale(fix.original(kind)[rid][k], f):
            found['原文已变'].append((kind, rid, k, e, f"登记时原译为 {f.get('was', f.get('was_speaker'))!r}"))
        if f and f.get('ok'):  # 人工确认无需修改
            continue
        for rule, info in problems(e):
            found[rule].append((kind, rid, k, e, info))
    for kind, items in fixes.items():  # 游戏更新后资源或元素没了，这些修改不会再生效
        for rid, ks in items.items():
            for k, f in ks.items():
                if k not in fix.original(kind).get(rid, {}):
                    found['原文已变'].append((kind, rid, k, {'en': '', 'cn': f.get('cn', '')}, '原文里已没有这一条'))
    for r in ORDER:
        for kind, rid, k, e, info in found[r]:
            sp = f" [{e.get('speaker')}]" if e.get('speaker') else ''
            print(f"[{r}] {kind} {rid} {k}{sp} {info}\n  EN: {e['en']!r}\n  CN: {e['cn']!r}")
    print(f'检查 {total} 条：' + '，'.join(f'{r} {len(found[r])}' for r in ORDER))


if __name__ == '__main__':
    main()
