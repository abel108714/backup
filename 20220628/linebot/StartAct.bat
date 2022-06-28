@echo off
set PATH=%PATH%;C:\Program Files\Heroku\bin;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64;C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts;C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts;C:\Program Files\MySQL\MySQL Server 5.7\bin;C:\ngrok-stable-windows-amd64;C:\"Program Files"\Git\usr\bin;C:\Users\udev77\AppData\Local\Tesseract-OCR;C:\Windows\Microsoft.NET\Framework64\v4.0.30319;C:\pypy3.7-v7.3.3-win32

set PATH=%PATH%;C:\Java\jdk-16.0.1\bin

echo %PATH%


doskey act=C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate


set PATH=%PATH%;C:\linebot
set TESSDATA_PREFIX = C:\Users\udev77\AppData\Local\Tesseract-OCR\tessdata;C:\Users\udev77\AppData\Local\Tesseract-OCR

::start C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate
start C:%HOMEPATH%\djangogirls\djangogirls_venv\Scripts\activate -echo 123 -launch

exit