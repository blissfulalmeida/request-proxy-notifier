# How to set up windows instance

1. Installation
   ```powershell
   Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vs_BuildTools.exe" -OutFile "vs_BuildTools.exe"
   .\vs_BuildTools.exe
   ```
   Choose "Desktop development with C++"
   ```powershell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/blissfulalmeida/request-proxy-notifier/main/data/installer.ps1" -OutFile "installer.ps1"
   .\installer.ps1
   ```

   For Octo Browser
   https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download
   https://octobrowser.net/download/windows/

2. Download certificate

3. Set TELEGRAM_BOT_TOKEN and CHAT_ID in request-proxy-notifier/src/mitmproxy/addon.py

   TELEGRAM_BOT_TOKEN = ''
   CHAT_ID = ''

4. Run mitmdump
   With upstream:
   ```powershell
   C:\Users\Administrator\.local\bin\mitmdump.exe -s request-proxy-notifier/src/mitmproxy/addon.py
   ```
   No upstream:
   ```powershell
   C:\Users\Administrator\.local\bin\mitmdump.exe --mode upstream:http://gate.smartproxy.com:10010 --upstream-auth user-spvlqzff00-country-es-city-madrid:47M52piURbtigoiLj~ -s request-proxy-notifier/src/mitmproxy/addon.py
   ```

---
1. `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
1. `iex "& {$(irm get.scoop.sh)} -RunAsAdmin"`
1. `scoop install git`
1. `scoop install nodejs`
1. `mkdir projects`
1. `cd projects`
1. `git clone https://github.com/blissfulalmeida/radio-shop.git`
1. Install VSCode from browser
1. Open VSCode and open radio-shop from C:\\Users\Administrator\projects\radio-shop
1. `npm install`
1. `npx cross-env NODE_ENV=PROFILE_NAME node .\src\index.js`

https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download
https://octobrowser.net/download/windows/