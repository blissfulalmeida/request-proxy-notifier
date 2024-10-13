Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vs_BuildTools.exe" -OutFile "vs_BuildTools.exe"
vs_BuildTools.exe --layout C:\BuildTools --lang en-US --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended
Invoke-WebRequest -Uri "https://www.nirsoft.net/utils/nircmd.zip" -OutFile "nircmd.zip"
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory("nircmd.zip", "C:\Program Files\nircmd")
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
scoop install python
scoop install pipx
pipx ensurepath
pipx install mitmproxy
pipx inject mitmproxy httpx
scoop install git
git clone https://github.com/blissfulalmeida/request-proxy-notifier.git
