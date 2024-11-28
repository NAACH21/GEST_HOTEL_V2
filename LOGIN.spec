# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['LOGIN.py'],
    pathex=[],
    binaries=[],
    datas=[
    ('pngwing.com.png', '.'),  # Incluye toda la carpeta de imágenes
	('logo2.PNG', '.'),
	('suite.jpeg', '.'),
	('sencilla.jpeg', '.'),
	('OIP.jpeg', '.'),
	('matrimonial.jpeg', '.'),
	('familiar.jpeg', '.'),
	('doble.jpeg', '.'),
	('user-circle-svgrepo-com.svg', '.'),
	('people-svgrepo-com.svg', '.'),
	('hotel-reception-bell-svgrepo-com.svg', '.'),
	('bed-svgrepo-com.svg', '.'),
    ('sistemahotel.db', '.'),  # Base de datos en el directorio raíz
	('C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\reportlab', 'reportlab'),
],

    hiddenimports=[
    'reportlab',
    'reportlab.platypus',
    'reportlab.pdfbase',
    'reportlab.graphics.barcode',
    'reportlab.lib',  # Incluye librerías auxiliares
    'reportlab.graphics',  # Gráficos de ReportLab
    'reportlab.graphics.charts',
    'PIL',
    'PIL.Image',  # Fuerza la inclusión de PIL.Image
    'PIL._imaging',  # Módulo interno que a veces falta
    'PIL.ImageFile',
    'PIL.ImageDraw',
    'html.parser',
    'PyQt6.QtCore',
    'PyQt6.QtGui',
    'PyQt6.QtWidgets',
],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LOGIN',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
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
    name='LOGIN'
)