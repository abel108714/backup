from threading import *
import os
import win32com.client
# import win32com.client as win32
import sys
import time
class App1(Thread):
        def run(self,TotalThread,ThreadNO):
        #     for i in range(100):
                print ("thread a")
                print (TotalThread)
                os.system("AsyTest.py "+str(TotalThread)+" "+str(ThreadNO))
                # path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # # # 開啟 Excel
                # # excel = win32.gencache.EnsureDispatch('Excel.Application')
                # # excel = win32com.client.Dispatch("Excel.Application")
                # from win32com.client import Dispatch
                # xlsApp = Dispatch("Excel.Application")
                # # 開啟 hello.xlsm 活頁簿檔案
                # excel.Workbooks.Open(Filename=path)

                # # 執行巨集程式
                # excel.Application.Run("Book1.xlsm!AP.run2",4,1)

                # # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App2(Thread):
        def run(self):
                print ("thread b")
                
                os.system("AsyTest.py 4 2")
                # path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # # 開啟 Excel
                # excel = win32com.client.Dispatch("Excel.Application")

                # # 開啟 hello.xlsm 活頁簿檔案
                # excel.Workbooks.Open(Filename=path)

                # # 執行巨集程式
                # excel.Application.Run("Book1.xlsm!AP.run2",4,2)

                # # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App3(Thread):
        def run(self):
                print ("thread c")
                
                os.system("AsyTest.py 4 3")
                # path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # # 開啟 Excel
                # excel = win32com.client.Dispatch("Excel.Application")

                # # 開啟 hello.xlsm 活頁簿檔案
                # excel.Workbooks.Open(Filename=path)

                # # 執行巨集程式
                # excel.Application.Run("Book1.xlsm!AP.run2",4,3)

                # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel

class App4(Thread):
        def run(self):
                print ("thread d")
                
                os.system("AsyTest.py 4 4")
                # path = 'S:\\網通部\\◎資訊\\data\\績效資料\\Book1.xlsm'
                # # 開啟 Excel
                # excel = win32com.client.Dispatch("Excel.Application")

                # # 開啟 hello.xlsm 活頁簿檔案
                # excel.Workbooks.Open(Filename=path)

                # # 執行巨集程式
                # excel.Application.Run("Book1.xlsm!AP.run2",4,4)

                # 離開 Excel
                # excel.Application.Quit()

                # # 清理 com 介面
                # del excel
class app_1(Thread):
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
def job(a,b):
        print('doing job: '+str(a)+str(b))

def run(TotalThread,ThreadNO):
        print ("thread a")
        print (TotalThread)
        os.system("AsyTest.py "+str(TotalThread)+" "+str(ThreadNO))

if __name__ == "__main__":
        # main(sys.argv)       
        # app1 = App1()
        # app2 = App2()
        # app3 = App3()
        # app4 = App4()
        # # app1.run()
        # # app2.run()
        # # app3.run()
        # app1 = Thread(target=App1, args=(4,1))

        # app1 = Thread(target=job, args=(4,1))
        #記錄開始執行時間
        # start = time.time()
        app=[0]*4
        for i in range(1,4):
                app[i] = Thread(target=run, args=(4,i))
                app[i].start()
        #記錄結束執行時間
        # end = time.time()
        # print("耗時 " + str(end-start) + " 秒")
        # app2.start()
        # app3.start()
        # app4.start()
        # t1 = app_1()
        # t2 = app2()

        # t1.start()
        # t2.start()