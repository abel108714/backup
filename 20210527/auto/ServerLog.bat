@echo off

set i=0

:do_while
echo %date%,%time%,%computername%,%username%,%sessionname%,%logonserver% >> ServerLog.txt
@ping 127.0.0.1 -n 5 -w 1000 > nul
::echo %i%
set /a i += 1

goto do_while


pause