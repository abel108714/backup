@echo off 
setlocal enabledelayedexpansion enableextensions

::�ʤέ�
start /w wscript C:\auto\�w�s����.vbs S:\���q��\����T\data\�Z�ĸ��\Book1.xlsm

::���~��
start /w C:\auto\GetINVOfCMReport.exe
start /w C:\auto>Python GetINVDB01002.py C:\Users\udev77\Documents\COSMOS_ERP\C_Data\INVQ02_1.XLSX

exit

