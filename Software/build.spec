# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\Tausand\\AbacusSoftware\\Software\\GUI\\MainWindow'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='AbacusSoftware',
          debug=True,
          strip=False,
          upx=True,
          console=True, icon='GUI\\images\\abacus_small.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='AbacusSoftware')