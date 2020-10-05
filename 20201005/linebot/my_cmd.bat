@echo off
set PATH=%PATH%;C:\Program Files\Heroku\bin;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts;C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts

echo %PATH%


doskey act=C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate

set PATH=%PATH%;C:\linebot


cls
%comspec%