[Setup]
AppName=SistemaHotel
AppVersion=1.0
DefaultDirName={pf}\SistemaHotel
DefaultGroupName=SistemaHotel
OutputDir=output
OutputBaseFilename=SistemaHotel_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\LOGIN.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\sistemahotel.db"; DestDir: "{app}"; Flags: ignoreversion
Source: "sqlite3.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\imagenes\*"; DestDir: "{app}\imagenes"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SistemaHotel"; Filename: "{app}\LOGIN.exe"
Name: "{group}\Uninstall SistemaHotel"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\LOGIN.exe"; Description: "Iniciar SistemaHotel"; Flags: nowait postinstall skipifsilent
