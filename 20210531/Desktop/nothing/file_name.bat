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
echo %aa%11111
::�Q�����r��
set aa2=%y%%m%%yes_d%~nx
echo %aa2%11111
::�ƻs����������ɦW
dir COPR38%aa2%??????%aa2%????.xlsx
copy COPR38%aa2%??????%aa2%????.xlsx COPR38%aa%??????%aa%????.xlsx

::copy COPR3820200902??????20200902????.xlsx COPR3820200903??????20200903????.xlsx

copy COPR3820200902000181202009020001
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

::������B����ܰT��
timeout /t 2 >nul 

pause