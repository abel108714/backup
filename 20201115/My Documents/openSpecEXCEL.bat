@echo off
start S:\網通部\◎資訊\data\績效資料\Book1.xlsm

set list=S:\網通部\◎資訊\data\績效資料\COPR38%date:~0,4%%date:~5,2%%date:~8,2%*.xlsx
(
 for %%i in (%list%) do (
  start %%i
  echo(
 )
)

exit


