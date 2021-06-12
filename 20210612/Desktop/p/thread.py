import threading
import time
import os
import win32com.client 
 
def scraper(value):
    print("start"+str(value))
    time.sleep(5)
    print("sleep done"+str(value))



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
 
 
# t = threading.Thread(target=scraper(1))  #建立執行緒
# t2 = threading.Thread(target=scraper(2))  #建立執行緒
# t.start()  #-執行
# print("end")