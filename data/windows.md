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
   For Octo Browser<br>
   - https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download
   - https://octobrowser.net/download/windows/
   - Download certificate

2. Set TELEGRAM_BOT_TOKEN and CHAT_ID in ***request-proxy-notifier/src/mitmproxy/addon.py***

   ```
   TELEGRAM_BOT_TOKEN = ''
   CHAT_ID = ''
   ```

3. Run mitmdump in silent mode
   With upstream:
   ```powershell
   .\Quiet.exe C:\Users\Administrator\.local\bin\mitmdump.exe -s request-proxy-notifier/src/mitmproxy/addon.py
   ```
   No upstream:
   ```powershell
   .\Quiet.exe C:\Users\Administrator\.local\bin\mitmdump.exe --mode upstream:http://gate.smartproxy.com:10010 --upstream-auth user-spvlqzff00-country-es-city-madrid:47M52piURbtigoiLj~ -s request-proxy-notifier/src/mitmproxy/addon.py
   ```
   Stop:
   ```powershell
   Stop-Process -Name mitmdump
   ```

---
1. `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
2. `iex "& {$(irm get.scoop.sh)} -RunAsAdmin"`
3. `scoop install git`
4. `scoop install nodejs`
5. `mkdir projects`
6. `cd projects`
7. `git clone https://github.com/blissfulalmeida/radio-shop.git`
8. Install VSCode from browser
9. Open VSCode and open radio-shop from C:\\Users\Administrator\projects\radio-shop
10. `npm install`
11. `npx cross-env NODE_ENV=PROFILE_NAME node .\src\index.js`

https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download
https://octobrowser.net/download/windows/