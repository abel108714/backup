from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium.webdriver.common.alert
import time
import os
from openpyxl import Workbook
import xlwings as xw
from xlwings.constants import DeleteShiftDirection
import re
import time
import datetime
from datetime import date
import sys
from FileDataAccess import *


def main():
   # args = sys.argv[1:]
   # print(argv[1])
   # print(args[2])
   # print(args[3])

   #記錄開始執行時間
   start = time.time()

   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
   chrome_options.add_argument('--headless')#不顯示視窗執行畫面
   chrome_options.add_argument('--disable-gpu')#關閉警告
   chrome_options.add_argument("--log-level=3")#關閉log
   chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
   DriverPath="C:\\ChromeDriver\\chromedriver.exe"
   driver = webdriver.Chrome(DriverPath,options=chrome_options)
   driver.get("https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse")

   new_text=driver.find_elements_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr")
   i=0
   Datalist = []
   Data = []
   s=""
   for text in new_text:
      Datalist.append(text.text)
      RowData=Datalist[i].split("\n")
      Data=RowData[0].split(" ")
      s=Data[5].split("%")[0]

      if i>1 and float(s) > 8.5:#首行不印，漲幅大於8.5%
         print(Data[0] + "\t" + Data[1] + "\t" + Data[2] +  "\t\t" + Data[5])
      

      #new物件給初始值
      a=FileDataAccess(0,'3','-','C:\\Users\\udev77\\Desktop\\StockMarketGainsRecord.txt')#C:\\My Documents\\StockMarketGainsRecord.txt')

      #使用方法
      b=['21','3,069,201']
      print(a.setData('東森',b))

      i=i+1

   #記錄結束執行時間
   end = time.time()
   print("耗時 " + str(end-start) + " 秒")
   driver.quit()#關閉瀏覽器

if __name__ == "__main__":
   main()

   

