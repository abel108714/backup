import numpy as np
# from xlwings import Workbook, Range
import os

# def rand_numbers():
#     wb = Workbook.caller()
#     n = int(Range('Sheet1', 'B1').value) 
#     rand_num = np.random.randn(n, n)
#     Range('Sheet1', 'C3').value = rand_num

# def set_column_width(self):
#     wb = Workbook.caller()
#     # Instantiating a Workbook object by excel file path
#     workbook = wb('\\ADFS\Public\網通部\網通部資料暫存區\★網通部績效小幫手專用★' + 'Book1.xls')

#     # Accessing the first worksheet in the Excel file
#     worksheet = workbook.getWorksheets().get(0)
#     cells = worksheet.getCells()

#     # Setting the width of the second column to 17.5
#     cells.setColumnWidth(1, 17.5)

#     # Saving the modified Excel file in default (that is Excel 2003) format
#     workbook.save(dataDir + "Set Column Width.xls")

#     print("Set Column Width Successfully.")
#rand_numbers()
# def Excel_Layout_Save(ExcelObj, FileName):
#     # """
#     # input : excel object and file name
#     # output: excel 要排版，要斷行，要排序，要存檔
#     # """
#     sheet = ExcelObj.Sheets[0]
#     sheet.Columns.Sort(Key1= sheet.Range("A1"), Order1=2 , Header=1, OrderCustom=1, MatchCase=False, Orientation=1) 
#     #排序，如果Order1 不等於2的話會連subject 都一起排下去
#     sheet.Columns("B:B").ColumnWidth = 60 #指定欄寬
#     sheet.Columns("C:C").EntireColumn.AutoFit() #自動設定欄寬
#     sheet.Columns("D:D").EntireColumn.AutoFit()
#     sheet.Columns("E:E").EntireColumn.AutoFit()
#     sheet.Columns("F:F").EntireColumn.AutoFit()
#     sheet.Columns("H:H").EntireColumn.AutoFit()
#     sheet.Columns("B:B").EntireColumn.WrapText = True #自動斷行
#     #ExcelObj.Sort(Key1 = ExcelObj.get_range("A2"), Order1=1, Header=0, OrderCustom=1, MatchCase=False, Orientation=1) #VBA script 參考用
#     #range.Sort(Key1=self.get_range(key_cell), Order1=1, Header=0, OrderCustom=1, MatchCase=False, Orientation=1)
#     ExcelObj.SaveAs(FileName) # 存成指定檔名

# import win32com.client as win32
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Range("A1:A10").Value = "A"
# ws.Range("B1:B10").Value = "This is a very long line of text"
# ws.Columns(1).ColumnWidth = 1
# ws.Range("B:B").ColumnWidth = 27
# # Alternately, you can autofit all columns in the worksheet
# # ws.Columns.AutoFit()
# wb.SaveAs('C:\\Users\\udev77\\Desktop\\column_widths.xlsm')


import xlwings as xw
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
# 定義你所要連接的檔案名稱
wb = xw.Book("C:\\Users\\udev77\\Desktop\\111.xlsm")

#wb = xw.Book()  # this will create a new workbook
#wb = xw.Book('FileName.xlsx')  # connect to an existing file in the current working directory
#wb = xw.Book('S:\\網通部\\◎資訊\\data\\績效資料\\' + 'Book1.xlsm')  # on Windows: use raw strings to escape backslashes
#wb = xw.Book('C:\\Users\\udev77\\Desktop\\' + '111.xlsm')  # on Windows: use raw strings to escape backslashes
#worksheet = wb.getWorksheets().get(0)
#cells = worksheet.getCells()
#cells.setColumnWidth(1, 17.5)
# sheet = ExcelObj.Sheets[0]
# sheet.Columns("B:B").ColumnWidth = 60
from openpyxl.utils import get_column_letter
#wb.sheets[0].range("D:D").set_column_width=15
# print(wb.sheets[0].range("D:D").setColumnWidth(1, 17.5))

wb.save('C:\\Users\\udev77\\Desktop\\' + '111.xlsm')
#若你有兩個 Excel 的實例開啓同一個檔案，你需要該實例的 PID，而取得 PID 的方法是透過 xw.apps.keys()：

#xw.apps[10559].books['FileName.xlsx']


# set_column_width()

os.system("pause")