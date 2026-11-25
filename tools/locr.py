"""LOCR（界面文本）解析与重建。格式见 README。"""
import struct
from glacier import decode_str, encode_str


def parse(data):
    """返回 (版本号, 各语言 [(字符串 hash, 文本), ...] 或 None)。"""
    ver = data[0]
    if ver not in (0, 1):
        raise ValueError(f'未知 LOCR 版本 {ver}')
    nlang = (struct.unpack_from('<I', data, 1)[0] - 1) // 4
    langs = []
    for off in struct.unpack_from(f'<{nlang}I', data, 1):
        if off == 0xFFFFFFFF:
            langs.append(None)
            continue
        cnt = struct.unpack_from('<I', data, off)[0]
        p, ents = off + 4, []
        for _ in range(cnt):
            h, ln = struct.unpack_from('<II', data, p); p += 8
            ents.append((h, decode_str(data[p:p + ln]))); p += ln + 1
        langs.append(ents)
    return ver, langs


def build(ver, langs):
    head = bytearray([ver]) + bytearray(4 * len(langs))
    body, offs = bytearray(), []
    for ents in langs:
        if ents is None:
            offs.append(0xFFFFFFFF)
            continue
        offs.append(len(head) + len(body))
        body += struct.pack('<I', len(ents))
        for h, s in ents:
            enc = encode_str(s)
            body += struct.pack('<II', h, len(enc)) + enc + b'\x00'
    struct.pack_into(f'<{len(langs)}I', head, 1, *offs)
    return bytes(head + body)
