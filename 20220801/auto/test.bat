
@ECHO OFF

SET SQLCMD="C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE"

SET PATH="C:\auto\"

SET SERVER="172.21.7.39"

SET DB="invdb"

SET LOGIN="root"

SET PASSWORD="16264386"

SET OUTPUT="C:\OutputLog.txt"

CD %PATH%

::ECHO %date% %time% > %OUTPUT%

::for %%f in (*.sql) do (

::%SQLCMD% -S %SERVER% -d %DB% -U %LOGIN% -P %PASSWORD% -i %%~f >> %OUTPUT%

::)

::%SQLCMD% -S %SERVER% -d %DB% -U %LOGIN% -P %PASSWORD% -i AmsData.sql >> %OUTPUT%

pause