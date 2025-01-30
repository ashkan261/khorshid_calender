; 📌 setup.iss - فایل نصب برنامه Khorshid Calendar
[Setup]
AppName=Khorshid Calendar
AppVersion=1.0
AppPublisher=Ashkan Mahinfallah
AppPublisherURL=http://www.mahinfallah.com
AppSupportURL=http://www.mahinfallah.com
AppUpdatesURL=http://www.mahinfallah.com
DefaultDirName={pf}\KhorshidCalendar
DefaultGroupName=Khorshid Calendar
UninstallDisplayIcon={app}\khorshid_calendar.exe
OutputDir=.
OutputBaseFilename=KhorshidCalendarInstaller
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\khorshid_calendar.exe"; DestDir: "{app}"
Source: "dist\add_to_startup.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Khorshid Calendar"; Filename: "{app}\khorshid_calendar.exe"
Name: "{userdesktop}\Khorshid Calendar"; Filename: "{app}\khorshid_calendar.exe"

[Run]
Filename: "{app}\add_to_startup.exe"; Description: "Adding to Startup"; Flags: nowait postinstall
Filename: "{app}\khorshid_calendar.exe"; Description: "Run Khorshid Calendar"; Flags: nowait postinstall

[CustomMessages]
WelcomeText="Welcome to Khorshid Calendar - Created by Ashkan Mahinfallah"
InfoText="This software was developed by Ashkan Mahinfallah.\nWebsite: www.mahinfallah.com\nGitHub: https://github.com/ashkan261"

[Code]
procedure InitializeWizard;
begin
  MsgBox(CustomMessage('WelcomeText'), mbInformation, MB_OK);
end;
