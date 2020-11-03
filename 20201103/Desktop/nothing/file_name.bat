@echo off

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
echo %aa%11111
::昨日日期字串
set aa2=%y%%m%%yes_d%~nx
echo %aa2%11111
::複製成今日報表檔名
dir COPR38%aa2%??????%aa2%????.xlsx
copy COPR38%aa2%??????%aa2%????.xlsx COPR38%aa%??????%aa%????.xlsx

::copy COPR3820200902??????20200902????.xlsx COPR3820200903??????20200903????.xlsx

copy COPR3820200902000181202009020001
echo copy COPR38%aa2%??????%aa2%????.xlsx COPR38%aa%??????%aa%????.xlsx

echo 複製今日測試報表完成

::顯示複製今日測試報表檔名
set list=COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
	for %%i in (%list%) do (
		::echo不換行
		echo|set /p= %%i
		echo()
)

::延遲兩秒且不顯示訊息
timeout /t 2 >nul 

pause