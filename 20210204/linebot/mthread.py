from threading import *
import os
import win32com.client
import sys
class App1(Thread):
        def run(self):
                path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # 開啟 Excel
                excel = win32com.client.Dispatch("Excel.Application")

                # 開啟 hello.xlsm 活頁簿檔案
                excel.Workbooks.Open(Filename=path)

                # 執行巨集程式
                excel.Application.Run("Book1.xlsm!AP.run2",4,1)

                # # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App2(Thread):
        def run(self):
                path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # 開啟 Excel
                excel = win32com.client.Dispatch("Excel.Application")

                # 開啟 hello.xlsm 活頁簿檔案
                excel.Workbooks.Open(Filename=path)

                # 執行巨集程式
                excel.Application.Run("Book1.xlsm!AP.run2",4,2)

                # # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App3(Thread):
        def run(self):
                path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # 開啟 Excel
                excel = win32com.client.Dispatch("Excel.Application")

                # 開啟 hello.xlsm 活頁簿檔案
                excel.Workbooks.Open(Filename=path)

                # 執行巨集程式
                excel.Application.Run("Book1.xlsm!AP.run2",4,3)

                # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App4(Thread):
        def run(self):
                path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # 開啟 Excel
                excel = win32com.client.Dispatch("Excel.Application")

                # 開啟 hello.xlsm 活頁簿檔案
                excel.Workbooks.Open(Filename=path)

                # 執行巨集程式
                excel.Application.Run("Book1.xlsm!AP.run2",4,4)

                # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel
class app1(Thread):
    def run(self):
        for i in range(100):
            print ("thread 1")
        #     time.sleep(1)

class app2(Thread):
    def run(self):
        for i in range(100):
            print ("thread 2")
        #     time.sleep(1)


def main(argv):
        args = sys.argv[1:]
        print(argv[1])


        # getDataToExcel(driver,argv[1])


if __name__ == "__main__":
        # main(sys.argv)       
        # app1 = App1()
        # app2 = App2()
        # app3 = App3()
        # app4 = App4()
        # # app1.run()
        # # app2.run()
        # # app3.run()

        # app1.start()
        # app2.start()
        # app3.start()
        # app4.start()
        t1 = app1()
        t2 = app2()

        t1.start()
        t2.start()