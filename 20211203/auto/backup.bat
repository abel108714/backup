@echo off

setlocal enabledelayedexpansion enableextensions
::@SET /P ans=1
::cd /d S:\���q��\����T\data\�Z�ĸ��
::echo S:\���q��\����T\data\�Z�ĸ��\
set copyFolder=S:\���q��\����T\
::@SET /P ans=2
set y=%date:~0,4%
set m=%date:~5,2%
set d=%date:~8,2%
::echo %y%
::echo %m%
::echo %d%
set /a yes_d=%date:~9,2%-2
::echo %yes_d%
::@SET /P ans=2
::�Y�p��10�h��0
if %yes_d% LSS 10 set yes_d=0%yes_d% 
::�������r��
::@SET /P ans=3
set aa=%y%%m%%d%
::�Q�����r��
set aa2=%y%%m%%yes_d%
set "aa2=%aa2: =%" ::�h���ť�


::@SET /P ans=1
::echo %copyFolder%



::�T�ѫe����r��
Call :_GET_DAY_ADD  -3
::echo %DAY_ADD%
set day_add_y=%DAY_ADD:~0,4%
set day_add_m=%DAY_ADD:~5,2%
set day_add_d=%DAY_ADD:~8,2%
::echo %day_add_y%
::echo %day_add_m%
::echo %day_add_d%
set aa3=%day_add_y%%day_add_m%%day_add_d%
::�R���T�ѫe�ɮ�
echo rd/s/q C:\backup_data\backup\%aa3%
rd/s/q C:\backup_data\backup\%aa3%


::�ƥ������ɮצܥ��a
xcopy /e /y %copyFolder%* C:\backup_data\backup\%aa%\����T\
xcopy /e /y C:\Users\udev77\Desktop\*.txt C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.bat C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.py C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\*.vbs C:\backup_data\backup\%aa%\Desktop\
xcopy /e /y C:\Users\udev77\Desktop\test\* C:\backup_data\backup\%aa%\Desktop\test\*
xcopy /e /y C:\linebot\* C:\backup_data\backup\%aa%\linebot\
xcopy /e /y C:\linebot_test\* C:\backup_data\backup\%aa%\linebot_test\
xcopy /e /y C:\Users\udev77\source\repos\* C:\backup_data\backup\%aa%\repos\
xcopy /e /y C:\MyDocu~1\* C:\backup_data\backup\%aa%\"My Documents"\
xcopy /e /y C:\Program Files\MySQL\* C:\backup_data\backup\%aa%\"MySQL"\
xcopy /e /y C:\auto\* C:\backup_data\backup\%aa%\auto\

::�ƥ������ɮצܶ���
cd C:\backup_data\backup\
git init
git config --global core.excludesfile ~/.gitignore
git add .
git commit -m "bak file"
git push


:: ���o���w���
goto :eof
:_GET_DAY_ADD
  (echo d1 = Now^(^)
   echo d2 = d1
   if not "%~2"=="" echo d1 = Replace^("%~2", ".", "-"^)
   if not "%~1"=="" echo d2 = DateAdd^("d", Eval^("%~1"^), d1^)
   echo d2 = Right^(Year^(d2^),4^) ^& "-" ^& Right^("0" ^& Month^(d2^),2^) ^& "-" ^& Right^("0" ^& Day^(d2^),2^)
   echo WScript.Echo d2) > "%temp%\DayAdd.vbs"
   for /f "tokens=1,* delims=??" %%i in ('CScript //NoLogo "%temp%\DayAdd.vbs"') Do (
     set DAY_ADD=%%i
   )
   goto :eof
pause
