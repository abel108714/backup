@echo off 
setlocal enabledelayedexpansion enableextensions

cd /d S:\���q��\����T\data\�Z�ĸ��
echo S:\���q��\����T\data\�Z�ĸ��\

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


::�ƻs����������ɦW
dir C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx
copy C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx S:\���q��\����T\data\�Z�ĸ��\COPR38%aa%??????%aa%????.xlsx

echo copy C:\MyDocu~1\COPR3820200902??????%aa2%????.xlsx S:\���q��\����T\data\�Z�ĸ��\COPR38%aa%??????%aa%????.xlsx

echo �ƻs������ճ�����

::��ܽƻs������ճ����ɦW
set list=S:\���q��\����T\data\�Z�ĸ��\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
	for %%i in (%list%) do (
		::echo������
		echo|set /p= %%i
		echo()
)

::���O����
del C:\Users\udev77\Documents\temp.txt
set list=S:\���q��\����T\data\�Z�ĸ��\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
 for %%j in (%list%) do (
  echo %%~nj.XLSX>>C:\Users\udev77\Documents\temp.txt
 )
)
echo �w���O����

set i=0

for /f %%f in (C:\Users\udev77\Documents\temp.txt) do (
	set NameArr[!i!]=%%f
	set /a i=!i!+1
)

set /a lastindex=!i!-1

for /L %%f in (0,1,!lastindex!) do ( 
	echo !NameArr[%%f]!
)

echo S:\���q��\����T\data\�Z�ĸ��\%NameArr[0]%
echo S:\���q��\����T\data\�Z�ĸ��\%NameArr[1]%
set file1=S:\���q��\����T\data\�Z�ĸ��\%NameArr[0]%
set file2=S:\���q��\����T\data\�Z�ĸ��\%NameArr[1]%
wscript ���ͺ��q�ؼйF����.vbs S:\���q��\����T\data\�Z�ĸ��\Book1.xlsm %file1% %file2%


exit


