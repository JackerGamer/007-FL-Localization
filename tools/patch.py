"""把 text/fixes.json 里的修改（及省略号、问叹号批量规则）打包成 patch rpkg，并安装到游戏 / 从游戏卸载。

用法（项目根目录）:
  python -I tools/patch.py build       生成 build/chunk0patch1.rpkg、build/chunk1patch1.rpkg 并回读校验
  python -I tools/patch.py install     build + 复制到游戏 Runtime + 提高 packagedefinition 的 patchlevel
  python -I tools/patch.py uninstall   删除补丁文件，还原 packagedefinition.txt
  python -I tools/patch.py package     build + 打包给玩家的 build/007FL-zhCN-Fix-<游戏版本>.zip（解压后复制即可安装）

原版 chunk0.rpkg / chunk1.rpkg 不会被修改。packagedefinition.txt 是原版（patchlevel 都为 0）时先备份到 backup/，
游戏更新或验证文件后重新安装会刷新备份，卸载时也不会用旧备份覆盖新版。
"""
import os, sys, re, shutil, struct, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True  # 不在 tools/ 下生成 __pycache__
import glacier, locr, dlge, fix, check
from glacier import LANG_CN

ROOT = os.path.normpath(os.path.join(HERE, '..'))
BUILD = os.path.join(ROOT, 'build')
BACKUP = os.path.join(ROOT, 'backup', 'packagedefinition.txt')
RUNTIME = os.path.join(glacier.GAME, 'Runtime')
PKGDEF = os.path.join(RUNTIME, 'packagedefinition.txt')
PARTITION = {0: 'super', 1: 'base'}  # chunk 编号 → packagedefinition 中的分区名
PATCH_LEVEL = 1


def load_changes():
    """{资源哈希: (类型, {序号: {cn?, speaker?}})}：fixes.json 的更正加上批量规则，只收与原文不同的条目。"""
    typ = {'ui': 'LOCR', 'dialogue': 'DLGE'}
    orig = {kind: fix.original(kind) for kind in typ}
    out = {}
    for kind, rid, k, e, f in check.effective():
        ch = {}
        if e['cn'] != orig[kind][rid][k]['cn']:
            ch['cn'] = e['cn']
        if f and 'speaker' in f:
            ch['speaker'] = f['speaker']
        if ch:
            out.setdefault(int(rid, 16), (typ[kind], {}))[1][k] = ch
    return out


def apply_locr(data, ch):
    ver, langs = locr.parse(data)
    ents = langs[LANG_CN]
    idx = {f'{h:08X}': i for i, (h, _) in enumerate(ents)}
    for k, v in ch.items():
        i = idx[k]
        ents[i] = (ents[i][0], v['cn'])
    out = locr.build(ver, langs)
    got = dict(locr.parse(out)[1][LANG_CN])
    assert all(got[int(k, 16)] == v['cn'] for k, v in ch.items())
    return out


def apply_dlge(data, ch):
    d = dlge.parse(data)
    for k, v in ch.items():
        L = d['elements'][int(k)]['langs'][LANG_CN]
        meta, segs = dlge.split_segments(L['text'])
        if 'speaker' in v:
            if not meta:
                raise ValueError('没有元数据，无法改说话人')
            meta = dlge.set_meta_field(meta, '{', '}', v['speaker'])
        if 'cn' in v:  # 多段字幕按行拆回各段，时间轴不变
            new = v['cn'].split('\n')
            if len(new) != len(segs):
                raise ValueError(f'DLGE {k}: 译文 {len(new)} 段，原字幕 {len(segs)} 段')
            segs = [(t, s) for (t, _), s in zip(segs, new)]
        L['text'] = dlge.join_segments(meta, segs)
    out = dlge.build(d)
    d2 = dlge.parse(out)
    for k, v in ch.items():
        meta, segs = dlge.split_segments(d2['elements'][int(k)]['langs'][LANG_CN]['text'])
        body, sp = dlge.subtitle(segs), dlge.meta_field(meta, '{', '}')
        assert body == v.get('cn', body) and sp == v.get('speaker', sp)
    return out


def write_rpkg(path, chunk, res):
    """res: [(hash, type, refs, data)]。数据不压缩、做 XOR（与原包中部分资源相同的存储方式）。"""
    ht = bytearray(); it = bytearray()
    head = 0x19 + 4
    for h, typ, refs, data in res:
        it += typ[::-1].encode('latin1') + struct.pack('<IIII', len(refs), len(data), 0xFFFFFFFF, 0xFFFFFFFF) + refs
    off = head + 20 * len(res) + len(it)
    body = bytearray()
    for h, typ, refs, data in res:
        ht += struct.pack('<QQI', h, off + len(body), 0x80000000)
        body += bytes(b ^ glacier.XOR_KEY[i & 7] for i, b in enumerate(data))
    hdr = b'2KPR' + struct.pack('<I', 1) + bytes([chunk, 0, PATCH_LEVEL]) + b'xx' + struct.pack('<III', len(res), len(ht), len(it))
    with open(path, 'wb') as f:
        f.write(hdr + struct.pack('<I', 0) + ht + it + body)


def build():
    changes = load_changes()
    os.makedirs(BUILD, exist_ok=True)
    made = {}
    for ci, src in enumerate(glacier.CHUNKS):
        es = sorted((e for e in glacier.read_index(src) if e['hash'] in changes and e['type'] == changes[e['hash']][0]),
                    key=lambda e: e['off'])
        if not es:
            continue
        res = []
        with open(src, 'rb') as f:
            for e in es:
                typ, ch = changes.pop(e['hash'])
                data = glacier.read_resource(f, e)
                new = apply_locr(data, ch) if typ == 'LOCR' else apply_dlge(data, ch)
                res.append((e['hash'], typ, e['refs'], new))
        dst = os.path.join(BUILD, f'chunk{ci}patch{PATCH_LEVEL}.rpkg')
        write_rpkg(dst, ci, res)
        # 回读校验：用读取原包的同一套代码解析补丁
        back = {e['hash']: e for e in glacier.read_index(dst)}
        with open(dst, 'rb') as f:
            for h, typ, refs, data in res:
                e = back[h]
                assert e['type'] == typ and e['refs'] == refs and glacier.read_resource(f, e) == data
        made[ci] = dst
        n = collections.Counter(r[1] for r in res)
        print(f'chunk{ci}patch{PATCH_LEVEL}.rpkg: {dict(n)}, {os.path.getsize(dst):,} 字节, 回读校验通过')
    if changes:
        raise SystemExit(f'有 {len(changes)} 个资源在游戏包里找不到: {[f"{h:016X}" for h in changes][:5]}')
    return made


def with_patchlevels(levels):
    """返回把游戏 packagedefinition.txt 各分区 patchlevel 改为 levels 后的加密内容。"""
    with open(PKGDEF, 'rb') as f:
        pt = glacier.decrypt_config(f.read()).decode('utf-8')
    for name, lv in levels.items():
        pt, n = re.subn(rf'(@partition name={name} .*?patchlevel=)\d+', rf'\g<1>{lv}', pt)
        if n != 1:
            raise SystemExit(f'packagedefinition 里找不到分区 {name}')
    return glacier.encrypt_config(pt.encode('utf-8'))


def set_patchlevels(levels):
    data = with_patchlevels(levels)
    with open(PKGDEF, 'wb') as f:
        f.write(data)


def patched():
    """游戏的 packagedefinition.txt 是否改过 patchlevel（原版都是 0）。"""
    with open(PKGDEF, 'rb') as f:
        return re.search(r'patchlevel=[1-9]', glacier.decrypt_config(f.read()).decode('utf-8')) is not None


def print_partitions(data):
    """打印加密的 packagedefinition 内容里的分区行。"""
    for line in glacier.decrypt_config(data).decode('utf-8').splitlines():
        if line.startswith('@partition'):
            print('  ' + line)


def install():
    made = build()
    if not patched():  # 原版：首次安装，或被游戏更新、验证文件还原（旧备份已过时）
        os.makedirs(os.path.dirname(BACKUP), exist_ok=True)
        shutil.copy2(PKGDEF, BACKUP)
        print(f'已备份 packagedefinition.txt -> {BACKUP}')
    for ci, src in made.items():
        shutil.copy2(src, os.path.join(RUNTIME, os.path.basename(src)))
    set_patchlevels({PARTITION[ci]: PATCH_LEVEL for ci in made})
    print('已安装。packagedefinition 分区：')
    with open(PKGDEF, 'rb') as f:
        print_partitions(f.read())


def uninstall():
    for ci in PARTITION:
        p = os.path.join(RUNTIME, f'chunk{ci}patch{PATCH_LEVEL}.rpkg')
        if os.path.exists(p):
            os.remove(p)
            print(f'已删除 {p}')
    if not patched():  # 已被游戏更新或验证文件还原，备份可能是旧版
        print('packagedefinition.txt 已是原版，不用还原')
    elif os.path.exists(BACKUP):
        shutil.copy2(BACKUP, PKGDEF)
        print('已还原 packagedefinition.txt')
    else:
        set_patchlevels({name: 0 for name in PARTITION.values()})
        print('没有备份，已把 patchlevel 改回 0')


PLAYER_README = f'''《007 初露锋芒》简体中文本地化修正

适用游戏版本：{glacier.GAME_VERSION}（Steam）。游戏是其他版本时请勿使用。
修正了简体中文字幕和界面文本里近 500 处错误：错译、漏译、术语和人名不统一、错别字、标点等；
另按国家标准统一了 1,900 多处省略号和问叹号的写法。

安装
1. 打开游戏目录：在 Steam 库中右键游戏 → 管理 → 浏览本地文件。
2. 先把 Runtime 文件夹里的 packagedefinition.txt 复制一份备用。
3. 把本压缩包 Runtime 文件夹中的 3 个文件复制到游戏的 Runtime 文件夹，替换 packagedefinition.txt。
4. 启动游戏。启动时的光敏癫痫警告比原版多一句安全提示，就说明补丁已生效。

卸载
删除 Runtime 文件夹里的 chunk0patch1.rpkg、chunk1patch1.rpkg，再把备份的 packagedefinition.txt 放回去
（没有备份的话，在 Steam 中右键游戏 → 属性 → 已安装文件 → 验证游戏文件的完整性）。

注意
- Steam 验证文件完整性后，packagedefinition.txt 会被还原，补丁不再生效；游戏版本没变的话，重新复制即可。
- 游戏更新后请不要继续使用本补丁，等待对应新版本的补丁。
- 本补丁只在游戏读取时替换文本，不修改原版 chunk0.rpkg / chunk1.rpkg。
'''
PACKAGE = f'007FL-zhCN-Fix-{glacier.GAME_VERSION}.zip'  # 发布给玩家的压缩包，放在 build/


def package():
    """build + 打包给玩家：Runtime/ 下的补丁包和改好 patchlevel 的 packagedefinition.txt，附安装说明。"""
    import zipfile
    made = build()
    files = {f'Runtime/{os.path.basename(p)}': open(p, 'rb').read() for p in made.values()}
    files['Runtime/packagedefinition.txt'] = with_patchlevels({PARTITION[ci]: PATCH_LEVEL for ci in made})
    files['安装说明.txt'] = b'\xef\xbb\xbf' + PLAYER_README.replace('\n', '\r\n').encode('utf-8')  # BOM + CRLF，记事本能直接看
    dst = os.path.join(BUILD, PACKAGE)
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in files.items():
            z.writestr(zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0)), data, zipfile.ZIP_DEFLATED)  # 固定时间，重复打包结果相同
    with zipfile.ZipFile(dst) as z:  # 回读校验
        assert {n: z.read(n) for n in z.namelist()} == files
    print(f'{PACKAGE}: {os.path.getsize(dst):,} 字节, 回读校验通过')
    print_partitions(files['Runtime/packagedefinition.txt'])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    {'build': build, 'install': install, 'uninstall': uninstall, 'package': package}.get(cmd, lambda: print(__doc__))()
