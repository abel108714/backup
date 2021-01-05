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

   new_text=driver.find_elements_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody")
   i=0
   for text in new_text:
      # Datalist.append(text.text)
      # print(i)
      print(text.text)
      i=i+1

   #記錄結束執行時間
   end = time.time()

   print("耗時 " + str(end-start) + " 秒")

if __name__ == "__main__":
   main()

   

