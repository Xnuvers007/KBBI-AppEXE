@echo off
echo x64
takeown /f %WinDir%\SysWOW64\gpedit.dll
icacls %WinDir%\SysWOW64\gpedit.dll /grant:r "%username%":f
takeown /f %WinDir%\SysWOW64\fde.dll
icacls %WinDir%\SysWOW64\fde.dll /grant:r "%username%":f
takeown /f %WinDir%\SysWOW64\gptext.dll
icacls %WinDir%\SysWOW64\gptext.dll /grant:r "%username%":f
echo.
echo.

takeown /f %WinDir%\SysWOW64\appmgr.dll
icacls %WinDir%\SysWOW64\appmgr.dll /grant:r "%username%":f
takeown /f %WinDir%\SysWOW64\fdeploy.dll
icacls %WinDir%\SysWOW64\fdeploy.dll /grant:r "%username%":f

IF NOT EXIST %WinDir%\SysWOW64\GPBAK\NUL MKDIR %WinDir%\SysWOW64\GPBAK
takeown /f %WinDir%\SysWOW64\GPBAK\*
icacls %WinDir%\SysWOW64\GPBAK\* /grant:r "%username%":f

IF EXIST %WinDir%\SysWOW64\gpedit.dll copy %WinDir%\SysWOW64\gpedit.dll %WinDir%\SysWOW64\GPBAK\gpedit.dll
IF EXIST %WinDir%\SysWOW64\fde.dll copy %WinDir%\SysWOW64\fde.dll %WinDir%\SysWOW64\GPBAK\fde.dll
IF EXIST %WinDir%\SysWOW64\gptext.dll copy %WinDir%\SysWOW64\gptext.dll %WinDir%\SysWOW64\GPBAK\gptext.dll
IF EXIST %WinDir%\SysWOW64\appmgr.dll copy %WinDir%\SysWOW64\appmgr.dll %WinDir%\SysWOW64\GPBAK\appmgr.dll
IF EXIST %WinDir%\SysWOW64\fdeploy.dll copy %WinDir%\SysWOW64\fdeploy.dll %WinDir%\SysWOW64\GPBAK\fdeploy.dll
IF EXIST %WinDir%\SysWOW64\gpedit.msc copy %WinDir%\SysWOW64\gpedit.msc %WinDir%\SysWOW64\GPBAK\gpedit.msc

copy gpedit.dll %WinDir%\SysWOW64\gpedit.dll
copy fde.dll %WinDir%\SysWOW64\fde.dll
copy gptext.dll %WinDir%\SysWOW64\gptext.dll
copy appmgr.dll %WinDir%\SysWOW64\appmgr.dll
copy fdeploy.dll %WinDir%\SysWOW64\fdeploy.dll
copy gpedit.msc %WinDir%\SysWOW64\gpedit.msc

IF NOT EXIST %WinDir%\SysWOW64\GroupPolicy\NUL MKDIR %WinDir%\SysWOW64\GroupPolicy
IF NOT EXIST %WinDir%\SysWOW64\GroupPolicy\adm\NUL MKDIR %WinDir%\SysWOW64\GroupPolicy\adm

copy system.adm %WinDir%\SysWOW64\GroupPolicy\Adm\system.adm
copy inetres.adm %WinDir%\SysWOW64\GroupPolicy\Adm\inetres.adm
copy conf.adm %WinDir%\SysWOW64\GroupPolicy\Adm\conf.adm
copy wmplayer.adm %WinDir%\SysWOW64\GroupPolicy\Adm\wmplayer.adm
copy wuau.adm %WinDir%\SysWOW64\GroupPolicy\Adm\wuau.adm

regsvr32 /s %WinDir%\SysWOW64\gpedit.dll
regsvr32 /s %WinDir%\SysWOW64\fde.dll
regsvr32 /s %WinDir%\SysWOW64\gptext.dll
regsvr32 /s %WinDir%\SysWOW64\appmgr.dll
regsvr32 /s %WinDir%\SysWOW64\fdeploy.dll