@echo off
set PATH=%PATH%;C:\Program Files\Heroku\bin;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts;C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts;C:\Program Files\MySQL\MySQL Server 5.7\bin;C:\ngrok-stable-windows-amd64;C:\"Program Files (x86)"\Git\usr\bin;C:\msys64\mingw64\bin

echo %PATH%


doskey act=C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate


set PATH=%PATH%;C:\linebot


cls
%comspec%