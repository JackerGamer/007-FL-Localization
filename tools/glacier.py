"""Glacier 2 通用部分：rpkg 读取、XOR、LZ4、XTEA、密钥与游戏路径。格式说明见 README。"""
import os, struct, zlib

GAME = os.environ.get('FL_GAME_DIR', r'D:\SteamLibrary\steamapps\common\007 First Light')
GAME_VERSION, BUILD_ID, BUILD_DATE = '1.3.2', 10870473, '2026-11-24'  # 本项目对应的游戏版本（Steam），游戏更新后同步修改
CHUNKS = [os.path.join(GAME, 'Runtime', f'chunk{i}.rpkg') for i in (0, 1)]

# LOCR / DLGE 中的语言槽位（共 16 个，见 README）
LANG_EN, LANG_FR, LANG_DE, LANG_CN, LANG_JP, LANG_TC = 1, 2, 4, 10, 11, 12

# ---------------------------------------------------------------- rpkg

XOR_KEY = bytes.fromhex('DC45A69CD3724CAB')


def read_index(path):
    """返回 rpkg 中所有资源的列表：hash, off, packed_size（LZ4 压缩后大小，0 为未压缩）, xor, type,
    size（解包后大小）, refs（原始引用表 bytes）。"""
    with open(path, 'rb') as f:
        hdr = f.read(0x19)
        if hdr[:4] != b'2KPR':
            raise ValueError(f'不是 RPKG v2: {path}')
        count, hash_tbl, info_tbl = struct.unpack_from('<III', hdr, 0x0D)
        if 'patch' in os.path.basename(path).lower():  # patch 包在表前多一个删除列表
            n = struct.unpack('<I', f.read(4))[0]
            f.read(8 * n)
        ent = f.read(hash_tbl)
        info = f.read(info_tbl)
    out, p = [], 0
    for i in range(count):
        h, off, sz = struct.unpack_from('<QQI', ent, i * 20)
        ref_sz, size = struct.unpack_from('<II', info, p + 4)
        out.append({'hash': h, 'off': off, 'packed_size': sz & 0x3FFFFFFF, 'xor': bool(sz & 0x80000000),
                    'type': info[p:p + 4][::-1].decode('latin1'), 'size': size,
                    'refs': info[p + 20:p + 20 + ref_sz]})
        p += 20 + ref_sz
    return out


def lz4_decompress(src, out_size):
    dst, i, n = bytearray(), 0, len(src)
    while i < n:
        token = src[i]; i += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[i]; i += 1; lit += b
                if b != 255: break
        dst += src[i:i + lit]; i += lit
        if i >= n: break
        off = src[i] | (src[i + 1] << 8); i += 2
        ml = token & 15
        if ml == 15:
            while True:
                b = src[i]; i += 1; ml += b
                if b != 255: break
        ml += 4
        start = len(dst) - off
        if off >= ml:
            dst += dst[start:start + ml]
        else:
            for k in range(ml):
                dst.append(dst[start + k])
    if len(dst) != out_size:
        raise ValueError(f'LZ4 解压大小不符: {len(dst)} != {out_size}')
    return bytes(dst)


def read_resource(f, e):
    """f 为已打开的 rpkg 文件对象。"""
    f.seek(e['off'])
    data = bytearray(f.read(e['packed_size'] or e['size']))
    if e['xor']:
        for k in range(len(data)):
            data[k] ^= XOR_KEY[k & 7]
    return lz4_decompress(bytes(data), e['size']) if e['packed_size'] else bytes(data)


def iter_resources(rtype):
    """遍历两个 chunk 中某类型的全部资源，产出 (资源 hash 字符串, 解包后的 bytes)。"""
    for path in CHUNKS:
        es = sorted((e for e in read_index(path) if e['type'] == rtype), key=lambda e: e['off'])
        with open(path, 'rb') as f:
            for e in es:
                yield f"{e['hash']:016X}", read_resource(f, e)

# ---------------------------------------------------------------- XTEA

TEXT_KEY = struct.unpack('<4I', bytes.fromhex('6133ac68a04a2b561f77f2b9e73ceb28'))     # LOCR / DLGE / RTLV
CONFIG_KEY = struct.unpack('<4I', bytes.fromhex('f02c48719f4bdc5f9d56ce861efc0905'))   # packagedefinition / thumbs
CONFIG_MAGIC = bytes.fromhex('B7E2EA00545B6B8711BD6FE84D6AD4BF')
DELTA, M = 0x9E3779B9, 0xFFFFFFFF


def xtea_decrypt(data, key=TEXT_KEY):
    out = bytearray()
    for i in range(0, len(data) - len(data) % 8, 8):
        v0, v1 = struct.unpack_from('<II', data, i)
        s = (DELTA * 32) & M
        for _ in range(32):
            v1 = (v1 - ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (s + key[(s >> 11) & 3]))) & M
            s = (s - DELTA) & M
            v0 = (v0 - ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (s + key[s & 3]))) & M
        out += struct.pack('<II', v0, v1)
    return bytes(out)


def xtea_encrypt(data, key=TEXT_KEY):
    data = data + b'\x00' * (-len(data) % 8)
    out = bytearray()
    for i in range(0, len(data), 8):
        v0, v1 = struct.unpack_from('<II', data, i)
        s = 0
        for _ in range(32):
            v0 = (v0 + ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (s + key[s & 3]))) & M
            s = (s + DELTA) & M
            v1 = (v1 + ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (s + key[(s >> 11) & 3]))) & M
        out += struct.pack('<II', v0, v1)
    return bytes(out)


def decode_str(enc):
    return xtea_decrypt(enc).rstrip(b'\x00').decode('utf-8')


def encode_str(s):
    return xtea_encrypt(s.encode('utf-8'))


def decrypt_config(data):
    """packagedefinition.txt / thumbs.dat → 明文 bytes（校验 CRC32）。"""
    if data[:16] != CONFIG_MAGIC:
        raise ValueError('配置文件头不符')
    pt = xtea_decrypt(data[20:], CONFIG_KEY).rstrip(b'\x00')
    if zlib.crc32(pt) != struct.unpack_from('<I', data, 16)[0]:
        raise ValueError('CRC32 校验失败')
    return pt


def encrypt_config(pt):
    return CONFIG_MAGIC + struct.pack('<I', zlib.crc32(pt)) + xtea_encrypt(pt, CONFIG_KEY)
