from openpyxl import Workbook
import xlwings as xw
path="S:\\開放公用區\★每日更新庫存水位警示表★\★庫存水位-唯讀參閱不可修改★.xlsm"
wb = Workbook()
wb = xw.Book(path)
print(wb.sheets[0].range('A2').value)
print(wb.sheets[0].range('B2').value)
print(wb.sheets[0].range('C2').value)
print(wb.sheets[0].range('D2').value)