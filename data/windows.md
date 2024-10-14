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
   Without upstream:
   ```powershell
   .\Quiet.exe C:\Users\Administrator\.local\bin\mitmdump.exe -s request-proxy-notifier/src/mitmproxy/addon.py
   ```
   With upstream:
   ```powershell
   .\Quiet.exe C:\Users\Administrator\.local\bin\mitmdump.exe --mode upstream:http://gate.smartproxy.com:10010 --upstream-auth user-spvlqzff00-country-es-city-madrid:47M52piURbtigoiLj~ -s request-proxy-notifier/src/mitmproxy/addon.py
   ```
   Stop:
   ```powershell
   Stop-Process -Name mitmdump
   ```
4. Change hostname
   ```powershell
   notepad C:\Windows\System32\drivers\etc\hosts
   ```
   You`ll see file like this
   ```powershell
   # Copyright (c) 1993-2009 Microsoft Corp.
   #
   # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
   #
   # This file contains the mappings of IP addresses to host names. Each
   # entry should be kept on an individual line. The IP address should
   # be placed in the first column followed by the corresponding host name.
   # The IP address and the host name should be separated by at least one
   # space.
   #
   # Additionally, comments (such as these) may be inserted on individual
   # lines or following the machine name denoted by a '#' symbol.
   #
   # For example:
   #
   #      102.54.94.97     rhino.acme.com          # source server
   #       38.25.63.10     x.acme.com              # x client host
   
   # localhost name resolution is handled within DNS itself.
   #   127.0.0.1       localhost
   #	::1            localhost
   ```
   We need to modify and uncomment one of the end lines:
   ```
      127.0.0.1       <new_hostname>
   ```
   Test it
   ```powershell
   ping <new_hostname>
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