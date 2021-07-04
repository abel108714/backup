@echo off

tasklist /FI "IMAGENAME eq ngrok.exe" /FO CSV > search.log
FOR /F %%A IN (search.log) do if %%A == ¸ê°T: goto process_off
:process_on
goto end
:process_off
start C:\auto\123.bat
:end

del search.log