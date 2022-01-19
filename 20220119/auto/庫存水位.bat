@echo off 
setlocal enabledelayedexpansion enableextensions

::百及倉
start /w wscript C:\auto\庫存水位.vbs S:\網通部\◎資訊\data\績效資料\Book1.xlsm

::成品倉
start /w C:\auto\GetINVOfCMReport.exe
start /w C:\auto>Python GetINVDB01002.py C:\Users\udev77\Documents\COSMOS_ERP\C_Data\INVQ02_1.XLSX

exit

