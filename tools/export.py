"""从游戏中导出全部简中文本（附英文对照），并对每个资源做 解密→重建→比对 的往返校验。

用法（项目根目录）:  python -I tools/export.py
输出:
  text/original/ui.json         界面文本（LOCR）  {资源: {字符串id: {en, cn}}}
  text/original/dialogue.json   对白与字幕（DLGE）{资源: {元素序号: {en, cn, speaker, cat, unused?}}}
                                按时间轴分段的字幕，各段正文用换行连接；
                                unused: 只有英文有字幕（简中、法、德、日、繁中都为空），应是未使用的台词
original/ 是游戏原文，只读；修改写在 text/fixes.json（见 README）。
"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True  # 不在 tools/ 下生成 __pycache__
import glacier, locr, dlge
from glacier import LANG_EN, LANG_CN, LANG_FR, LANG_DE, LANG_JP, LANG_TC

OUT_DIR = os.path.join(HERE, '..', 'text', 'original')
OTHER_LANGS = (LANG_FR, LANG_DE, LANG_JP, LANG_TC)  # 用于判断台词是否未使用


def export_ui():
    out = {}
    for rid, data in glacier.iter_resources('LOCR'):
        ver, langs = locr.parse(data)
        if locr.build(ver, langs) != data:
            raise SystemExit(f'LOCR 往返校验失败: {rid}')
        if not langs[LANG_CN]:
            continue
        en = dict(langs[LANG_EN] or [])
        out[rid] = {f'{h:08X}': {'en': en.get(h, ''), 'cn': s} for h, s in langs[LANG_CN]}
    return out


def export_dialogue():
    out = {}
    for rid, data in glacier.iter_resources('DLGE'):
        d = dlge.parse(data)
        if dlge.build(d) != data:
            raise SystemExit(f'DLGE 往返校验失败: {rid}')
        res = {}
        for i, e in enumerate(d['elements']):
            if e['type'] != 1:
                continue
            texts = {}
            for lang in (LANG_EN, LANG_CN) + OTHER_LANGS:
                t = e['langs'][lang]['text']
                meta, segs = dlge.split_segments(t)
                if dlge.join_segments(meta, segs) != t:
                    raise SystemExit(f'DLGE 字幕分段往返失败: {rid} {i}')
                texts[lang] = meta, dlge.subtitle(segs)
            en, (meta, cn) = texts[LANG_EN][1], texts[LANG_CN]
            if en or cn:
                r = res[str(i)] = {'en': en, 'cn': cn,
                                   'speaker': dlge.meta_field(meta, '{', '}'),
                                   'cat': dlge.meta_field(meta, '%', '%')}
                if not cn.strip() and not any(texts[lang][1].strip() for lang in OTHER_LANGS):
                    r['unused'] = True  # 只有英文有字幕：应是未使用的台词，简中为空不算缺失
        if res:
            out[rid] = res
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, fn in (('ui', export_ui), ('dialogue', export_dialogue)):
        t0 = time.time()
        data = fn()
        dst = os.path.join(OUT_DIR, f'{name}.json')
        with open(dst, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        n = sum(len(v) for v in data.values())
        print(f'{name}: {len(data)} 个资源, {n} 条, 往返校验通过, {int(time.time() - t0)}s -> {os.path.normpath(dst)}')


if __name__ == '__main__':
    main()
