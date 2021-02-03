from threading import *
import os
import win32com.client

class App1(Thread):
    def run(self):
        path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
        # 開啟 Excel
        excel = win32com.client.Dispatch("Excel.Application")

        # 開啟 hello.xlsm 活頁簿檔案
        excel.Workbooks.Open(Filename=path)

        # 執行巨集程式
        excel.Application.Run("Book1.xlsm!AP.run")

        # 離開 Excel
        excel.Application.Quit()

        # 清理 com 介面
        del excel

class App2(Thread):
        path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
        # 開啟 Excel
        excel = win32com.client.Dispatch("Excel.Application")

        # 開啟 hello.xlsm 活頁簿檔案
        excel.Workbooks.Open(Filename=path)

        # 執行巨集程式
        excel.Application.Run("Book1.xlsm!AP.run")

        # 離開 Excel
        excel.Application.Quit()

        # 清理 com 介面
        del excel

class App3(Thread):
        path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
        # 開啟 Excel
        excel = win32com.client.Dispatch("Excel.Application")

        # 開啟 hello.xlsm 活頁簿檔案
        excel.Workbooks.Open(Filename=path)

        # 執行巨集程式
        excel.Application.Run("Book1.xlsm!AP.run")

        # 離開 Excel
        excel.Application.Quit()

        # 清理 com 介面
        del excel




app1 = App1()
app2 = App2()
app3 = App3()

# app1.run()
# app2.run()
# app3.run()

app1.start()
app2.start()
app3.start()