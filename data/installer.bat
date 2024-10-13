@echo off
echo Setting PowerShell execution policy...
PowerShell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"

echo Installing Scoop...
PowerShell -Command "iex '& {$(irm get.scoop.sh)} -RunAsAdmin'"

echo Installing Python using Scoop...
scoop install python

echo Installing Pipx using Scoop...
scoop install pipx

echo Installation complete.
pause
