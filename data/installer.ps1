# Set execution policy to allow script execution
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Install Scoop
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"

# Install Python and Pipx
scoop install python
scoop install pipx

# Ensure Pipx is in the PATH
pipx ensurepath

# Install mitmproxy and inject httpx
pipx install mitmproxy
pipx inject mitmproxy httpx

# Install Git
scoop install git

# Clone the request-proxy-notifier repository
git clone https://github.com/blissfulalmeida/request-proxy-notifier.git
