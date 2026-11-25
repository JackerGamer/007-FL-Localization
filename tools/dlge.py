"""DLGE（对白 / 剧情字幕）解析与重建。格式见 README。"""
import struct, re
from glacier import decode_str, encode_str

NLANG = 16
SEP = '\\\\'  # 字幕元数据字段分隔符（两个反斜杠）
TIMING = re.compile(r'//\(([^()]*)\)' + re.escape(SEP))  # 字幕分段的时间轴 //(起,止)\\


def parse(data):
    """返回 {header, elements, root}。"""
    elems, p, end = [], 8, len(data) - 2
    while p < end:
        t = data[p]; p += 1
        if t == 1:
            multi = data[p]; p += 1
            if multi not in (0, 1):
                raise ValueError(f'未知 multi 值 {multi} @0x{p - 1:x}')
            e, nvar = {'type': 1, 'multi': multi}, 1
            if multi:
                e['var_ref'], nvar, e['extra'] = struct.unpack_from('<III', data, p); p += 12
                e['nvar'] = nvar
            e['soundtag'], e['wavname'], e['unk2'] = struct.unpack_from('<III', data, p); p += 12
            e['langs'] = []
            for _ in range(NLANG):
                wavs = [struct.unpack_from('<i', data, p)[0]]; p += 4
                if multi and wavs[0] != -1:
                    wavs += struct.unpack_from(f'<{nvar - 1}i', data, p); p += 4 * (nvar - 1)
                flag, ffx, ln = struct.unpack_from('<BiI', data, p); p += 9
                if p + ln > end:
                    raise ValueError(f'字符串越界 @0x{p:x}')
                enc = data[p:p + ln]; p += ln
                text = decode_str(enc) if ln else ''
                e['langs'].append({'wav': list(wavs), 'flag': flag, 'ffx': ffx, 'text': text})
            elems.append(e)
        elif t in (2, 4):
            a, b, n = struct.unpack_from('<III', data, p); p += 12
            fmt, sz = ('<HII', 10) if t == 2 else ('<HI', 6)
            elems.append({'type': t, 'a': a, 'b': b,
                          'entries': [struct.unpack_from(fmt, data, p + sz * i) for i in range(n)]})
            p += sz * n
        elif t == 3:
            key, default, n = struct.unpack_from('<III', data, p); p += 12
            ents = []
            for _ in range(n):
                ref, m = struct.unpack_from('<HI', data, p); p += 6
                ents.append((ref, list(struct.unpack_from(f'<{m}I', data, p)))); p += 4 * m
            elems.append({'type': 3, 'key': key, 'default': default, 'entries': ents})
        else:
            raise ValueError(f'未知元素类型 {t} @0x{p - 1:x}')
    if p != end:
        raise ValueError(f'解析结束位置 0x{p:x} != 0x{end:x}')
    return {'header': bytes(data[:8]), 'elements': elems, 'root': struct.unpack_from('<H', data, end)[0]}


def build(d):
    out = bytearray(d['header'])
    for e in d['elements']:
        t = e['type']
        out.append(t)
        if t == 1:
            out.append(e['multi'])
            if e['multi']:
                out += struct.pack('<III', e['var_ref'], e['nvar'], e['extra'])
            out += struct.pack('<III', e['soundtag'], e['wavname'], e['unk2'])
            for L in e['langs']:
                enc = encode_str(L['text']) if L['text'] else b''
                out += struct.pack(f"<{len(L['wav'])}iBiI", *L['wav'], L['flag'], L['ffx'], len(enc)) + enc
        elif t in (2, 4):
            out += struct.pack('<III', e['a'], e['b'], len(e['entries']))
            for ent in e['entries']:
                out += struct.pack('<HII' if t == 2 else '<HI', *ent)
        else:
            out += struct.pack('<III', e['key'], e['default'], len(e['entries']))
            for ref, cases in e['entries']:
                out += struct.pack(f'<HI{len(cases)}I', ref, len(cases), *cases)
    out += struct.pack('<H', d['root'])
    return bytes(out)


def split_segments(text):
    """字幕 → (元数据前缀, [(时间, 正文), ...])。

    过场等字幕可按时间分成几段：元数据后跟若干个 //(起,止)\\\\正文。
    没有时间轴时元数据到最后一个分隔符为止，返回 [(None, 正文)]。join_segments 是其逆运算。"""
    if not text.startswith('//') or SEP not in text:
        return '', [(None, text)]
    ms = list(TIMING.finditer(text))
    if not ms:
        i = text.rfind(SEP) + len(SEP)
        return text[:i], [(None, text[i:])]
    ends = [m.start() for m in ms[1:]] + [len(text)]
    return text[:ms[0].start()], [(m.group(1), text[m.end():end]) for m, end in zip(ms, ends)]


def join_segments(meta, segs):
    return meta + ''.join(s if t is None else f'//({t}){SEP}{s}' for t, s in segs)


def subtitle(segs):
    """各段正文用换行连接，作为导出、检查和修改的文本。"""
    return '\n'.join(s for _, s in segs)


def meta_field(meta, start, stop):
    """取元数据中以 //start 开头、以 stop 结尾的字段内容，如说话人 ('{', '}')、类别 ('%', '%')。"""
    for f in meta.split(SEP):
        if f.startswith('//' + start) and f.endswith(stop) and len(f) > 3:
            return f[3:-1]
    return ''


def set_meta_field(meta, start, stop, value):
    parts = meta.split(SEP)
    for i, f in enumerate(parts):
        if f.startswith('//' + start) and f.endswith(stop) and len(f) > 3:
            parts[i] = f'//{start}{value}{stop}'
    return SEP.join(parts)
