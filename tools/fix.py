"""登记译文修改到 text/fixes.json。

fixes.json 结构: { "ui" | "dialogue": { 资源: { 序号: {
    "cn": 新译文,               （改正时；按时间轴分段的字幕各段用换行分隔，段数不变）
    "speaker": 新说话人名,       （仅 dialogue，可选）
    "ok": true,                （人工确认原译无误，检查时跳过）
    "was": 原译文,              （自动记录，便于复核）
    "note": 说明 } } } }

省略号和问叹号不逐条登记，由 BULK 规则统一套用到全部文本（见 normalize）。

命令行用法（项目根目录）:
  python -I tools/fix.py ui <资源> <序号> --cn "新译文" --note "原因"
  python -I tools/fix.py dialogue <资源> <序号> --ok --note "原因"
也可以 import 后调用 add() 批量登记。
"""
import os, re, json, argparse

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FIXES = os.path.join(ROOT, 'text', 'fixes.json')
_orig = {}

# 批量规则（GB/T 15834-2011）：(名称, 模式, 替换)
BULK = [('ellipsis', re.compile(r'\.{3,}|。{2,}|…+'), '……'),   # ...... / ... / 。。。 / 单个或多于两个的 … → ……
        ('qe', re.compile('！？'), '？！')]                      # 问叹号连用时问号在前


def normalize(text):
    for _, pat, rep in BULK:
        text = pat.sub(rep, text)
    return text


def effective_cn(o, f):
    """原文条目 o 套用修改记录 f（可为 None）和批量规则后的简中。"""
    return normalize(f['cn'] if f and 'cn' in f else o['cn'])


def original(kind):
    if kind not in _orig:
        with open(os.path.join(ROOT, 'text', 'original', f'{kind}.json'), encoding='utf-8') as f:
            _orig[kind] = json.load(f)
    return _orig[kind]


def load():
    if os.path.exists(FIXES):
        with open(FIXES, encoding='utf-8') as f:
            return json.load(f)
    return {}


def save(fx):
    out = {k: {r: dict(sorted(v.items())) for r, v in sorted(fx[k].items())} for k in sorted(fx)}
    with open(FIXES, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)


def add(fx, kind, rid, key, cn=None, speaker=None, ok=False, note=''):
    o = original(kind)[rid][key]
    e = {}
    if cn is not None and kind == 'dialogue' and cn.count('\n') != o['cn'].count('\n'):
        raise ValueError(f'{kind} {rid} {key}: 多段字幕要逐段改，各段用换行分隔，段数须与原文一致'
                         f'（原文 {o["cn"].count(chr(10)) + 1} 段）')
    if cn is not None and normalize(cn) != normalize(o['cn']):  # 只差批量规则的不用登记
        e['cn'] = cn
        e['was'] = o['cn']
    if speaker is not None and speaker != o.get('speaker'):
        e['speaker'] = speaker
        e['was_speaker'] = o.get('speaker')
    if ok:
        e['ok'] = True
    if not e:
        raise ValueError(f'{kind} {rid} {key}: 没有任何改动')
    if note:
        e['note'] = note
    fx.setdefault(kind, {}).setdefault(rid, {})[key] = e
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kind', choices=['ui', 'dialogue'])
    ap.add_argument('rid')
    ap.add_argument('key')
    ap.add_argument('--cn')
    ap.add_argument('--speaker')
    ap.add_argument('--ok', action='store_true')
    ap.add_argument('--note', default='')
    a = ap.parse_args()
    fx = load()
    print(add(fx, a.kind, a.rid, a.key, a.cn, a.speaker, a.ok, a.note))
    save(fx)


if __name__ == '__main__':
    main()
