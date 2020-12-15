from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium.webdriver.common.alert
import time
import os
from openpyxl import Workbook
import xlwings as xw
import re
import time
import datetime
from datetime import date

#Python to exe
#pyinstaller -F .\WebCrawler.py & xcopy /y dist\WebCrawler.exe WebCrawler.exe & rd /q/s dist & rd /q/s build & del /q/s WebCrawler.spec & rd /q/s __pycache__




def checkData(findStr):
   regex = r"\b\S*\s\d*[m][l][/][瓶]"
   matches = re.finditer(regex, findStr, re.MULTILINE)
   for matchNum, match in enumerate(matches, start=1):
      if matchNum == 1:
         return True
      else:
         regex = r"\b\S*\s\d*[0-9]*[g]"
         matches = re.finditer(regex, findStr, re.MULTILINE)
         for matchNum, match in enumerate(matches, start=1):
            if matchNum == 1:
               return True
            else: 
               return False   


# def adjustData(Arr):
#    Arr[]
#    if checkData(findStr):
#       return findStr
#    else 

def findSubString(Str,SubString):
   pos = Str.find(SubString)
   if pos > -1:
      return True
   else:
      return False

def getDiffDate(StartDate,EndDate):
   print("StartDate: "+StartDate)
   print("EndDate: "+EndDate)
   StartDateArr = [3]
   EndDateArr = [3]
   if findSubString(StartDate,"/"):
      StartDateArr=StartDate.split("/")
   elif findSubString(StartDate,"-"):
      StartDateArr=StartDate.split("-")
   startday = datetime.date(int(StartDateArr[0]),int(StartDateArr[1]),int(StartDateArr[2]))
   if findSubString(EndDate,"/"):
      EndDateArr=EndDate.split("/")
   elif findSubString(EndDate,"-"):
      EndDateArr=EndDate.split("-")
   other_day = datetime.date(int(EndDateArr[0]),int(EndDateArr[1]),int(EndDateArr[2]))
   result = startday - other_day
   print(result)
   return result.days

def removeRedundantPID(str):
   pass

      #                     0         1        2         3                     4       5                 6        7            8          9        10            11
      #                     商品代號   商品名稱 包裝方式   存量                  包裝量	批號	            有效期限	 供應商代號	   供應商名稱	提示	   剩餘有效天數	USD
      #燈號  庫別	 庫別名稱  品號       品名	    包裝方式	庫存數量	安全庫存水位	                保存期限  有效期限	                                 剩餘有效天數	下單批量	迴轉率	迴轉天數	每月均銷量	每日均銷量	預估幾日售完	到貨天數
      #A     B     C        D          E       F          G       H                              I       J                                          K              L        M        N        O        P           Q           R
def getDataByWebPage():
   Datalist = []
   new_text=driver.find_elements_by_xpath("//table[@id='GridView1']/tbody/tr")
   i = 0
   result = []
   wb = Workbook()
   ws = wb.active
   # 定義你所要連接的檔案名稱
   wb = xw.Book("S:\\網通部\\◎資訊\\庫存水位表\\庫存水位.xlsm")
   #取今天日期串
   today = date.today()
   today_str = today.strftime("%Y/%m/%d")
   for text in new_text:
      


      Datalist.append(text.text)
      RowData=Datalist[i].split("\n")
      Data=RowData[0].split(" ")

      findStr=Data[2]
      print("str: "+findStr)
      #10903008	天然冰湖野米十穀米600g	6包/箱
      #\d*\S[/][箱]
      regex = r"\d*\S[/][箱]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      
      matches = re.search(regex, findStr) #re.search(r"\d*\S[/][箱]", findStr)
      print("1 "+Data[0])
      print("2 "+Data[1])
      print("3 "+Data[2])
      print("4 "+Data[3])
      print("- "+Data[4])
      print("- "+Data[5])
      print("5 "+Data[6])
      print(matches)
      if re.search(r"\d*[瓶]?[支]?[/][箱]?[盒]?", findStr) == None and i != 0:
         # print("1 "+Data[0])
         # print("2 "+Data[1])
         # print("3 "+Data[2])
         # print("4 "+Data[3])
         # print("- "+Data[4])
         # print("- "+Data[5])
         # print("5 "+Data[6])
         Data[1]=Data[1]+Data[2]
         Data[2]=Data[3]
         Data[3]=Data[4]
         Data[4]=Data[5]
         Data[5]=Data[6]
         Data[6]=Data[7]
         Data[7]=""
         # print("1 "+Data[0])
         # print("2 "+Data[1])
         # print("3 "+Data[2])
         # print("4 "+Data[3])
         # print("- "+Data[4])
         # print("- "+Data[5])
         # print("5 "+Data[6])
      elif re.search(r"\d*[m][l][/][瓶]", findStr)  and i != 0:
         Data[1]=Data[1]+Data[2]
         Data[2]=Data[3]
         Data[3]=Data[4]
         Data[4]=Data[5]
         Data[5]=Data[6]
         Data[6]=Data[7]
         Data[7]=""
      else:
         # print("1 "+Data[0])
         # print("2 "+Data[1])
         # print("3 "+Data[2])
         # print("4 "+Data[3])
         # print("- "+Data[4])
         # print("- "+Data[5])
         # print("5 "+Data[6])
         # if re.search(r"\d*[支][/][盒]", findStr) == None and i != 0:
         #    print("1 "+Data[0])
         #    print("2 "+Data[1])
         #    print("3 "+Data[2])
         #    print("4 "+Data[3])
         #    print("- "+Data[4])
         #    print("- "+Data[5])
         #    print("5 "+Data[6])
         #    Data[1]=Data[1]+Data[2]
         #    Data[2]=Data[3]
         #    Data[3]=Data[4]
         #    Data[4]=Data[5]
         #    Data[5]=Data[6]
         #    Data[6]=Data[7]
         #    Data[7]=""
            print("1 "+Data[0])
            print("2 "+Data[1])
            print("3 "+Data[2])
            print("4 "+Data[3])
            print("- "+Data[4])
            print("- "+Data[5])
            print("5 "+Data[6])
         # else:
         #    # print("1 "+Data[0])
         #    # print("2 "+Data[1])
         #    # print("3 "+Data[2])
         #    # print("4 "+Data[3])
         #    # print("- "+Data[4])
         #    # print("- "+Data[5])
         #    # print("5 "+Data[6])
         #    Data[1]=Data[1]+Data[2]
         #    Data[2]=Data[3]
         #    Data[3]=Data[4]
         #    Data[4]=Data[5]
         #    Data[5]=Data[6]
         #    Data[6]=Data[7]
         #    Data[7]=""
         #    # print("1 "+Data[0])
         #    # print("2 "+Data[1])
         #    # print("3 "+Data[2])
         #    # print("4 "+Data[3])
         #    # print("- "+Data[4])
         #    # print("- "+Data[5])
         #    # print("5 "+Data[6])


      # for matchNum, match in enumerate(matches, start=1):
      #    print("???")  
      #    print(matchNum)
      #    print(match)
      #    if matchNum != 1:
      #       Data[1]=Data[1]+" "+Data[2]
      #       Data[2]=Data[3]
      #       Data[3]=Data[4]
      #       Data[4]=Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]=""



      #調整陣列取得的資料，因品名有空白會多切割一次
      # findStr=Data[1]+" "+Data[2]
      # print('6')
      # regex = r"\b\S*\s\d*[m][l]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      # for matchNum, match in enumerate(matches, start=1):      
      #    if matchNum == 1:
      #       Data[1]=Data[1]+" "+Data[2]
      #       Data[2]=Data[3]
      #       Data[3]=Data[4]
      #       Data[4]=Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]=""

      # regex = r"\b\S*\s\d*[(][N][E][W][)]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      # for matchNum, match in enumerate(matches, start=1):      
      #    if matchNum == 1:
      #       Data[1]=Data[1]+" "+Data[2]
      #       Data[2]=Data[3]
      #       Data[3]=Data[4]
      #       Data[4]=Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]=""

      # regex = r"\b\S*\s\d*[0-9]*[g]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      # for matchNum, match in enumerate(matches, start=1):
      #    if matchNum == 1:
      #       Data[1]=Data[1]+" "+Data[2]
      #       Data[2]=Data[3]
      #       Data[3]=Data[4]
      #       Data[4]=Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]="" 

      # regex = r"\D*\d*\D[(]\D*[)]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      # for matchNum, match in enumerate(matches, start=1):
      #    if matchNum == 1:
      #       Data[1]=Data[1]+" "+Data[2]
      #       Data[2]=Data[3]
      #       Data[3]=Data[4]
      #       Data[4]=Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]="" 

      # findStr=Data[4]+" "+Data[5]
      # print("findStr: "+findStr)
      # regex = r"[0-9]*[箱]\s*[0-9]*[袋][0-9]*[包]"
      # matches = re.finditer(regex, findStr, re.MULTILINE)
      # print("0000000000000000000000000000")
      # for matchNum, match in enumerate(matches, start=1):
      #    print("1111111111111111111111111111111")
      #    if matchNum == 1:
      #       print("22222222222222222222222222222222222")
      #       Data[4]=Data[4]+" "+Data[5]
      #       Data[5]=Data[6]
      #       Data[6]=Data[7]
      #       Data[7]="" 

      #排除品號
      if (Data[0] == "70206023") | (Data[0] == "70206024") | (Data[0] == "70303719"):
         continue

      #陣列資料放進資料表
      wb.sheets[0].range('D' + str(i+1)).value  = Data[0]
      wb.sheets[0].range('E' + str(i+1)).value  = Data[1]
      wb.sheets[0].range('F' + str(i+1)).value  = Data[2]
      wb.sheets[0].range('G' + str(i+1)).value  = Data[3]
      wb.sheets[0].range('J' + str(i+1)).value  = Data[6]
      # print("1 "+Data[0])
      # print("2 "+Data[1])
      # print("3 "+Data[2])
      # print("4 "+Data[3])
      # print("- "+Data[4])
      # print("- "+Data[5])
      # print("5 "+Data[6])

      # if i == 5:
      #    break
      # if i+1>=2:
      #    wb.sheets[0].range('K' + str(i+1)).value  = getDiffDate(today_str,Data[6])
      i=i+1

#記錄開始執行時間
start = time.time()

username = "OGB"
password = "OG140"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
chrome_options.add_argument('--headless')#不顯示視窗執行畫面
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
DriverPath="C:\\ChromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(DriverPath,options=chrome_options)
driver.get("http://www.logistics.com.tw/TMP/login.aspx?ReturnUrl=%2FTMP%2FDefault.aspx")

#帳號
username_textbox = driver.find_element_by_id("Login1_UserName")
username_textbox.send_keys(username)

#密碼
password_textbox = driver.find_element_by_id("Login1_Password")
password_textbox.send_keys(password)

#登入
login_button = driver.find_element_by_id("Login1_LoginButton")
login_button.click()

TreeView =driver.find_element_by_id('ctl00_TreeView1n5')
TreeView.click()
#庫別
sel = driver.find_element_by_css_selector("select[id='ctl00_ContentPlaceHolder1_lstWare']")
Select(sel).select_by_visible_text('觀音物流中心')
#良品?
RadioButton = driver.find_element_by_id('ctl00_ContentPlaceHolder1_RadioButton1')
RadioButton.click()
#查詢
Button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
Button.click()
print('1')
getDataByWebPage()
print('1')
driver.quit()#關閉瀏覽器

#記錄結束執行時間
end = time.time()

print("耗時 " + str(end-start) + " 秒")



