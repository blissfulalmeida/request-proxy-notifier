@echo off

REM Download NirCmd zip file
powershell -Command "Invoke-WebRequest -Uri 'https://www.nirsoft.net/utils/nircmd.zip' -OutFile 'nircmd.zip'"

REM Extract NirCmd zip file to C:\Program Files\nircmd
powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('nircmd.zip', 'C:\Program Files\nircmd')"

REM Set execution policy to RemoteSigned
powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"

REM Install Scoop and Python
powershell -Command "iex '& {$(irm get.scoop.sh)} -RunAsAdmin'"

REM Install Python and Pipx
powershell -Command "scoop install python"
powershell -Command "scoop install pipx"
powershell -Command "pipx ensurepath"
powershell -Command "pipx install mitmproxy"
powershell -Command "pipx inject mitmproxy httpx"

REM Install Git
powershell -Command "scoop install git"

REM Clone the GitHub repository
powershell -Command "git clone https://github.com/blissfulalmeida/request-proxy-notifier.git"

echo All commands executed successfully!
pause
