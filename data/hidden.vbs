Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd.exe /c start /min /wait C:\md.bat", 0, False
