@echo off 
setlocal enabledelayedexpansion enableextensions

cd /d S:\網通部\◎資訊\data\績效資料
echo S:\網通部\◎資訊\data\績效資料\

set y=%date:~0,4%
set m=%date:~5,2%
set d=%date:~8,2%
set /a yes_d=%date:~8,2%-1
::若小於10則補0
if %yes_d% LSS 10 set yes_d=0%yes_d% 
::今日日期字串
set aa=%y%%m%%d%

::昨日日期字串
set aa2=%y%%m%%yes_d%
set "aa2=%aa2: =%" ::去除空白


::複製成今日報表檔名
dir C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx
copy C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx S:\網通部\◎資訊\data\績效資料\COPR38%aa%??????%aa%????.xlsx

echo copy C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx S:\網通部\◎資訊\data\績效資料\COPR38%aa%??????%aa%????.xlsx

echo 複製今日測試報表完成

::顯示複製今日測試報表檔名
set list=S:\網通部\◎資訊\data\績效資料\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
	for %%i in (%list%) do (
		::echo不換行
		echo|set /p= %%i
		echo()
)

::更改記錄檔
del C:\Users\udev77\Documents\temp.txt
set list=S:\網通部\◎資訊\data\績效資料\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
 for %%j in (%list%) do (
  echo %%~nj.XLSX>>C:\Users\udev77\Documents\temp.txt
 )
)
echo 已更改記錄檔

set i=0

for /f %%f in (C:\Users\udev77\Documents\temp.txt) do (
	set NameArr[!i!]=%%f
	set /a i=!i!+1
)

set /a lastindex=!i!-1

for /L %%f in (0,1,!lastindex!) do ( 
	echo !NameArr[%%f]!
)

echo S:\網通部\◎資訊\data\績效資料\%NameArr[0]%
echo S:\網通部\◎資訊\data\績效資料\%NameArr[1]%
set file1=S:\網通部\◎資訊\data\績效資料\%NameArr[0]%
set file2=S:\網通部\◎資訊\data\績效資料\%NameArr[1]%
wscript 產生網通目標達成比.vbs S:\網通部\◎資訊\data\績效資料\Book1.xlsm %file1% %file2%


exit


