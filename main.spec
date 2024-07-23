# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\installed\\QGIS316\\apps\\qgis\\plugins', 'qgis\\plugins'), ('D:\\installed\\QGIS316\\apps\\Python37\\Lib\\site-packages\\PyQt5\\*.pyd', 'PyQt5'), ('D:\\installed\\QGIS316\\apps\\qt5\\plugins\\styles', 'PyQt5\\Qt\\plugins\\styles'), ('D:\\installed\\QGIS316\\apps\\qt5\\plugins\\iconengines', 'PyQt5\\Qt\\plugins\\iconengines'), ('D:\\installed\\QGIS316\\apps\\qt5\\plugins\\imageformats', 'PyQt5\\Qt\\plugins\\imageformats'), ('D:\\installed\\QGIS316\\apps\\qt5\\plugins\\platforms', 'PyQt5\\Qt\\plugins\\platforms'), ('D:\\installed\\QGIS316\\apps\\qt5\\plugins\\platformthemes', 'PyQt5\\Qt\\plugins\\platformthemes')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
