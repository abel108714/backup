import os
import win32com.client

# 開啟 Excel
excel = win32com.client.Dispatch("Excel.Application")

# 開啟 hello.xlsm 活頁簿檔案
excel.Workbooks.Open(Filename="S:\網通部\◎資訊\data\績效資料\Book1.xlsm")

# 執行巨集程式
excel.Application.Run("Book1.xlsm!INV.庫存水位")

# 傳入參數，並取得計算結果
#result = excel.Application.Run("hello.xlsm!hello2", "OfficeGuide.cc")
#print(result)

# 離開 Excel
excel.Application.Quit()

# 清理 com 介面
del excel