@echo off
setlocal
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0bootsel-windows.ps1" %*
set "RC=%ERRORLEVEL%"
echo.
pause
exit /b %RC%
