@echo off

setlocal enabledelayedexpansion enableextensions
::@SET /P ans=1
::cd /d S:\網通部\◎資訊\data\績效資料
::echo S:\網通部\◎資訊\data\績效資料\
set copyFolder=S:\網通部\◎資訊\
::@SET /P ans=2
set y=%date:~0,4%
set m=%date:~5,2%
set d=%date:~8,2%
set /a yes_d=%date:~9,2%-1
::@SET /P ans=2
::若小於10則補0
if %yes_d% LSS 10 set yes_d=0%yes_d% 
::今日日期字串
::@SET /P ans=3
set aa=%y%%m%%d%
::昨日日期字串
set aa2=%y%%m%%yes_d%
set "aa2=%aa2: =%" ::去除空白
::@SET /P ans=1
echo %copyFolder%


xcopy /e /y %copyFolder%* C:\backup_data\backup\%aa%\◎資訊\
xcopy /e /y C:\Users\udev77\Desktop\*.txt C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.bat C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.py C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.vbs C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\linebot\* C:\backup_data\backup\%aa%\linebot\
xcopy /e /y C:\linebot_test\* C:\backup_data\backup\%aa%\linebot_test\
xcopy /e /y C:\Users\udev77\source\repos\* C:\backup_data\backup\%aa%\repos\
xcopy /e /y C:\MyDocu~1\* C:\backup_data\backup\%aa%\"My Documents"\
xcopy /e /y C:\Program Files\MySQL\* C:\backup_data\backup\%aa%\"MySQL"\
xcopy /e /y C:\auto\* C:\backup_data\backup\%aa%\auto\
cd C:\backup_data\backup\
git init
git add .
git commit -m "bak file"
git push

exit
