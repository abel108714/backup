@echo off

setlocal enabledelayedexpansion enableextensions

::cd /d S:\���q��\����T\data\�Z�ĸ��
::echo S:\���q��\����T\data\�Z�ĸ��\
set copyFolder=S:\���q��\����T\

set y=%date:~0,4%
set m=%date:~5,2%
set d=%date:~8,2%
set /a yes_d=%date:~8,2%-1
::�Y�p��10�h��0
if %yes_d% LSS 10 set yes_d=0%yes_d% 
::�������r��
set aa=%y%%m%%d%

::�Q�����r��
set aa2=%y%%m%%yes_d%
set "aa2=%aa2: =%" ::�h���ť�

echo %copyFolder%


xcopy /e /y %copyFolder%* C:\backup_data\backup\%aa%\����T\
xcopy /e /y C:\Users\udev77\Desktop\*.txt C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.bat C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\linebot\* C:\backup_data\backup\%aa%\linebot\
cd C:\backup_data\backup\
git init
git add .
git commit -m "bak file"
git push

pause  
