Dim args', var1, var2, var3
Set args = WScript.Arguments

'Parameter1, begin with index0
'var1 = args(0)

'Parameter2
'var2 = args(1)

'Parameter3
'var3 = args(2)

'msgbox "First parameter passed was " _
'       & var1 & " and second parameter passed was " & var2 & " and third parameter passed was " & var3

Set objExcel = CreateObject("Excel.Application")
'Set objExcel = GetObject("S:\網通部\◎資訊\data\績效資料\book1.xlsm")
objExcel.visible = true
objExcel.workbooks.Open args(0) 
objExcel.Run "'Book1.xlsm'!INV.庫存水位"

'Clear the objects at the end of your script.
set args = Nothing
set objExcel = Nothing