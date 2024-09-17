# How to setup windows instance

1. `iex "& {$(irm get.scoop.sh)} -RunAsAdmin"`
1. `scoop install python`
1. `scoop install pipx`
1. `pipx ensurepath`
1. `pipx install mitmproxy`
1. `pipx inject mitmproxy httpx`
1. `scopp install git`
1. `git clone https://github.com/blissfulalmeida/request-proxy-notifier.git`
1. `mitmdump.exe --mode upstream:http://gate.smartproxy.com:10015 --upstream-auth user-spvlqzff00-country-es-city-madrid:47M52piURbtigoiLj~ -p 8080 -s src/mitmproxy/addon.py`
Or
`mitmdump.exe --mode upstream:http://51.38.93.202:10241 --upstream-auth grundansvad5573:172578 -p 8080 -s src/mitmproxy/addon.py`
