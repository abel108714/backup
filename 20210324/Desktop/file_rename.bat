@echo off

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
dir COPR38%aa2%??????%aa2%????.xlsx
copy COPR38%aa2%??????%aa2%????.xlsx COPR38%aa%??????%aa%????.xlsx

echo copy COPR38%aa2%??????%aa2%????.xlsx COPR38%aa%??????%aa%????.xlsx

echo �ƻs������ճ�����

::��ܽƻs������ճ����ɦW
set list=COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
	for %%i in (%list%) do (
		::echo������
		echo|set /p= %%i
		echo()
)

::���O����
del C:\Users\udev77\Documents\temp.txt
set list=COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
 for %%j in (%list%) do (
  echo %%~nj.XLSX>>C:\Users\udev77\Documents\temp.txt
 )
)
echo �w���O����

::������B����ܰT��
timeout /t 2 >nul 

pause