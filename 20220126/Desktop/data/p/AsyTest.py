# from tkinter import *
# from tkinter.ttk import *
# import time


# def updateProgressbar(speed):
#     time.sleep(0.05)
#     bar['value']+=(speed/100)*100
#     # download+=speed
#     # percent.set(str(int((download/GB)*100))+"%")
#     # text.set(str(download)+"/"+str(GB)+" GB completed")
#     window.update_idletasks()


# # def start():
# #     GB = 100
# #     download = 0
# #     speed = 1
# #     while(download<GB):
# #         download+=speed
# #         updateProgressbar(download)
#         # time.sleep(0.05)
#         # bar['value']+=(speed/GB)*100
#         # download+=speed
        
#         # # percent.set(str(int((download/GB)*100))+"%")
#         # # text.set(str(download)+"/"+str(GB)+" GB completed")
#         # window.update_idletasks()

# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()
# GB = 100
# download = 0
# speed = 1
# while(download<GB):
#     download+=speed
#     updateProgressbar(download)
#     # button = Button(window,text="download",command=updateProgressbar(download)).pack()

# window.mainloop()



# from xml.etree.ElementTree import iterparse
# from openpyxl import load_workbook
# path="S:\網通部\◎資訊\年度績效數字分析\COPR2320210120000088202101200001.xlsx"
# wb=load_workbook("S:\網通部\◎資訊\年度績效數字分析\COPR2320210120000088202101200001.xlsx")
# ws=wb.worksheets[0]
# xml = ws._xml_source
# xml.seek(0)
# wb = load_workbook(filename=r'S:\\網通部\\◎資訊\\年度績效數字分析\\COPR2320210120000088202101200001.xlsx')
# ws = wb.active
# # 定義你所要連接的檔案名稱
# wb = xw.Book(path)
# ws=wb.worksheets[0]
# xml = ws._xml_source
# xml.seek(0)
# for _,x in iterparse(xml):

#     name= x.tag.split("}")[-1]
#     if name=="col":
#         width = x.attrib["width"]
#         print(width)
#         print(x.attrib)
#         # print "Column %(max)s: Width: %(width)s",%x.attrib,width

#     if name=="cols":
#         # print "break before reading the rest of the file"
#         break


# from openpyxl import load_workbook
 
# wb = load_workbook(filename=r'S:\\網通部\\◎資訊\\年度績效數字分析\\COPR2320210120000088202101200001.xlsx')
 
# sheets = wb.get_sheet_names()   # 获取所有表格(worksheet)的名字
# sheet0 = sheets[0]  # 第一个表格的名称
# ws = wb.get_sheet_by_name('sheet_name') # 获取特定的 worksheet
 
# # 获取表格所有行和列，两者都是可迭代的
# rows = ws.rows
# columns = ws.columns
 
# # 行迭代
# content = []
# for row in rows:
#     line = [col.value for col in row]
#     content.append(line)
 
# # 通过坐标读取值
# print(ws.cell('B12').value)    # B 表示列，12 表示行
# print(ws.cell(row=12, column=2).value)
# import xlwings as xw
# from openpyxl import Workbook
# path="S:\\網通部\\◎資訊\\年度績效數字分析\\COPR2320210120000088202101200001.xlsx"
# wb = Workbook()
# ws = wb.active
# # 定義你所要連接的檔案名稱
# wb = xw.Book(path)
# rows = ws.rows
# # columns = ws.columns
# print('儲存格 欄名', ws['A1'].column)
# print('儲存格 列名', ws['A1'].row)
# print('儲存格名', ws['A1'].coordinate)

# print('工作表有資料最大欄數', ws.max_column)
# print('工作表有資料最小欄數', ws.min_column)
# print('工作表有資料最大列數', ws.max_row)
# print('工作表有資料最小列數', ws.min_row)

# import openpyxl



# wb = xw.Book(path)

# ws = wb.sheets[0]

# for cell in ws['C']: # 讀取C欄所有資料，並列印出來
#     print(cell.value)
    
# for cell in ws['2']: # 讀取第2列所有資料，並列印出來
#     print(cell.value)
# import win32com.client

# xl = win32com.client.Dispatch("Excel.Application")
# print(xl.ActiveWorkbook.FullName)
# # print(xl.active)
# from openpyxl import load_workbook
# path = 'S:\\網通部\\◎資訊\\年度績效數字分析\\COPR2320210120000088202101200001.xlsx'
# path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
# # wb2 = load_workbook(path)
# # print(wb2.worksheets.index(wb2[1]))
# import os
# import win32com.client

# # 開啟 Excel
# excel = win32com.client.Dispatch("Excel.Application")

# # 開啟 hello.xlsm 活頁簿檔案
# excel.Workbooks.Open(Filename=path)

# # 執行巨集程式
# # excel.Application.Run("Book1.xlsm!年度績效數字分析")
# excel.Application.Run("Book1.xlsm!AP.run2",4,1)

# # # 傳入參數，並取得計算結果
# # result = excel.Application.Run("hello.xlsm!hello2", "OfficeGuide.cc")
# # print(result)

# # 離開 Excel
# excel.Application.Quit()

# # 清理 com 介面
# del excel
# import xlrd
# xl = xlrd.open_workbook(path)
# for sht in xl.sheets():
#     # sht.sheet_visible value of 1 is "active sheet"
#     print(sht.name, sht.sheet_selected, sht.sheet_visible)
# print (wb2['第 1 頁'].max_row)
# wb2['第 1 頁']['A71']=123
# print (wb2['第 1 頁'].max_row)

# print (len(wb2.worksheets))

# workbook = openpyxl.load_workbook(path)

# sheet = workbook['第 1 頁']
# sheet['A1'] = 6
import os
import win32com.client
import sys
def main(argv):
        args = sys.argv[1:]
        print(argv[1])
        print(argv[2])
        path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
        # wb2 = load_workbook(path)
        # print(wb2.worksheets.index(wb2[1]))

        # 開啟 Excel
        excel = win32com.client.Dispatch("Excel.Application")
        # wb = xl.Workbooks.Open(file_path, ReadOnly=1)
        # 開啟 hello.xlsm 活頁簿檔案
        # excel.Workbooks.Open(Filename=path, ReadOnly=1)
        wb = excel.Workbooks.Open(path, None, True)

        # 執行巨集程式
        # excel.Application.Run("Book1.xlsm!年度績效數字分析")
        excel.Application.Run("Book1.xlsm!AP.run2",argv[1],argv[2])
        print("end: "+str(argv[1]))
        print("end: "+str(argv[2]))
        # # 傳入參數，並取得計算結果
        # result = excel.Application.Run("hello.xlsm!hello2", "OfficeGuide.cc")
        # print(result)

        # 離開 Excel
        excel.Application.Quit()

        # 清理 com 介面
        del excel
if __name__ == "__main__":
        main(sys.argv)    


































# import asyncio

# def hello_world(loop):
#     """A callback to print 'Hello World' and stop the event loop"""
#     print('Hello World')
#     loop.stop()

# loop = asyncio.get_event_loop()

# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)

# # Blocking call interrupted by loop.stop()
# try:
#     loop.run_forever()
# finally:
#     loop.close()





# import asyncio
# from concurrent.futures.thread import ThreadPoolExecutor

# from selenium import webdriver

# executor = ThreadPoolExecutor(10)


# def scrape(url, *, loop):
#     loop.run_in_executor(executor, scraper, url)


# def scraper(url):
#     DriverPath="C:\\ChromeDriver\\chromedriver.exe"
#     driver = webdriver.Chrome(DriverPath)
#     driver.get(url)


# loop = asyncio.get_event_loop()
# for url in ["https://www.google.com.tw/"] * 2:
#     scrape(url, loop=loop)

# loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))