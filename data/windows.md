# How to set up windows instance

1. Install prerequisites
https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download
https://octobrowser.net/download/windows/

2. Download certificate

3. Run commands
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
scoop install python
scoop install pipx
pipx ensurepath
pipx install mitmproxy
pipx inject mitmproxy httpx
scoop install git
scoop install nodejs
git clone https://github.com/blissfulalmeida/request-proxy-notifier.git
C:\Users\Administrator\.local\bin\mitmdump.exe -s request-proxy-notifier/src/mitmproxy/addon.py

-----
mitmdump.exe --mode upstream:http://gate.smartproxy.com:10015 --upstream-auth user-spvlqzff00-country-es-city-madrid:47M52piURbtigoiLj~ -p 8080 -s src/mitmproxy/addon.py`
Or
`mitmdump.exe --mode upstream:http://51.38.93.202:10241 --upstream-auth grundansvad5573:172578 -p 8080 -s src/mitmproxy/addon.py`


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