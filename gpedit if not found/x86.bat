@echo off
echo x86
takeown /f %WinDir%\System32\gpedit.dll
icacls %WinDir%\System32\gpedit.dll /grant:r "%username%":f
takeown /f %WinDir%\System32\fde.dll
icacls %WinDir%\System32\fde.dll /grant:r "%username%":f
takeown /f %WinDir%\System32\gptext.dll
icacls %WinDir%\System32\gptext.dll /grant:r "%username%":f
echo.
echo.

takeown /f %WinDir%\System32\appmgr.dll
icacls %WinDir%\System32\appmgr.dll /grant:r "%username%":f
takeown /f %WinDir%\System32\fdeploy.dll
icacls %WinDir%\System32\fdeploy.dll /grant:r "%username%":f

IF NOT EXIST %WinDir%\System32\GPBAK\NUL MKDIR %WinDir%\System32\GPBAK
takeown /f %WinDir%\System32\GPBAK\*
icacls %WinDir%\System32\GPBAK\* /grant:r "%username%":f

IF EXIST %WinDir%\System32\gpedit.dll copy %WinDir%\System32\gpedit.dll %WinDir%\System32\GPBAK\gpedit.dll
IF EXIST %WinDir%\System32\fde.dll copy %WinDir%\System32\fde.dll %WinDir%\System32\GPBAK\fde.dll
IF EXIST %WinDir%\System32\gptext.dll copy %WinDir%\System32\gptext.dll %WinDir%\System32\GPBAK\gptext.dll
IF EXIST %WinDir%\System32\appmgr.dll copy %WinDir%\System32\appmgr.dll %WinDir%\System32\GPBAK\appmgr.dll
IF EXIST %WinDir%\System32\fdeploy.dll copy %WinDir%\System32\fdeploy.dll %WinDir%\System32\GPBAK\fdeploy.dll
IF EXIST %WinDir%\System32\gpedit.msc copy %WinDir%\System32\gpedit.msc %WinDir%\System32\GPBAK\gpedit.msc

copy gpedit.dll %WinDir%\System32\gpedit.dll
copy fde.dll %WinDir%\System32\fde.dll
copy gptext.dll %WinDir%\System32\gptext.dll
copy appmgr.dll %WinDir%\System32\appmgr.dll
copy fdeploy.dll %WinDir%\System32\fdeploy.dll
copy gpedit.msc %WinDir%\System32\gpedit.msc

IF NOT EXIST %WinDir%\System32\GroupPolicy\NUL MKDIR %WinDir%\System32\GroupPolicy
IF NOT EXIST %WinDir%\System32\GroupPolicy\adm\NUL MKDIR %WinDir%\System32\GroupPolicy\adm

copy system.adm %WinDir%\System32\GroupPolicy\Adm\system.adm
copy inetres.adm %WinDir%\System32\GroupPolicy\Adm\inetres.adm
copy conf.adm %WinDir%\System32\GroupPolicy\Adm\conf.adm
copy wmplayer.adm %WinDir%\System32\GroupPolicy\Adm\wmplayer.adm
copy wuau.adm %WinDir%\System32\GroupPolicy\Adm\wuau.adm

regsvr32 /s %WinDir%\System32\gpedit.dll
regsvr32 /s %WinDir%\System32\fde.dll
regsvr32 /s %WinDir%\System32\gptext.dll
regsvr32 /s %WinDir%\System32\appmgr.dll
regsvr32 /s %WinDir%\System32\fdeploy.dll