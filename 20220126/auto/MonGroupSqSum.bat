@ECHO OFF 
mysql --login-path=invdb --silent < AllMonGroupSqSum.sql
ECHO ����!
PAUSE

@ECHO Done! 