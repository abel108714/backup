@echo off
start S:\���q��\����T\data\�Z�ĸ��\Book1.xlsm

set list=S:\���q��\����T\data\�Z�ĸ��\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
 for %%i in (%list%) do (
  start %%i
  echo(
 )
)

exit


