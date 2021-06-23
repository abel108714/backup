﻿from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium.webdriver.common.alert
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# import selenium.webdriver.common.alert
# import time
# import os
# from openpyxl import Workbook
# import xlwings as xw
# from xlwings.constants import DeleteShiftDirection
# import re
import time
# import datetime
# from datetime import date
# import sys
# from tqdm import tqdm,trance


#Python to exe
#pyinstaller -F .\WebCrawler.py & xcopy /y dist\WebCrawler.exe WebCrawler.exe & rd /q/s dist & rd /q/s build & del /q/s WebCrawler.spec & rd /q/s __pycache__
from selenium.webdriver.common.action_chains  import ActionChains
def hover(self,by,value):
      element = self.findElement(by,value)
      ActionChains(self.driver).move_to_element(element).perform()
# 通过不同的方式查找界面元素
def findElement(self,by,value):
      if(by == "id"):
            element = self.driver.find_element_by_id(value)
            return element
      elif(by == "name"):
             element = self.driver.find_element_by_name(value)
             return element
      elif(by == "xpath"):
             element = self.driver.find_element_by_xpath(value)
             return element
      elif(by == "classname"):
             element = self.driver.find_element_by_class_name(value)
             return element
      elif(by == "css"):
             element = self.driver.find_element_by_css_selector(value)
             return element
      elif(by == "link_text"):
             element = self.driver.find_element_by_link_text(value)
             return element
      else:
             print("无对应方法，请检查")
             return None
 # 检查是否存在用户退出按钮，存在，登录成功，否则登录失败

#  print(close)
#  if close != None:
#      self.assertEqual(1,1)
#  else:
#      self.assertEqual(1,0)
#      time.sleep(3)

# def checkData(findStr):
#    regex = r"\b\S*\s\d*[m][l][/][瓶]"
#    matches = re.finditer(regex, findStr, re.MULTILINE)
#    for matchNum, match in enumerate(matches, start=1):
#       if matchNum == 1:
#          return True
#       else:
#          regex = r"\b\S*\s\d*[0-9]*[g]"
#          matches = re.finditer(regex, findStr, re.MULTILINE)
#          for matchNum, match in enumerate(matches, start=1):
#             if matchNum == 1:
#                return True
#             else: 
#                return False   

# # def adjustData(Arr):
# #    Arr[]
# #    if checkData(findStr):
# #       return findStr
# #    else 

# def findSubString(Str,SubString):
#    pos = Str.find(SubString)
#    if pos > -1:
#       return True
#    else:
#       return False

# def getDiffDate(StartDate,EndDate):
   
#    # print("StartDate: "+StartDate)
#    # print("EndDate: "+EndDate)
#    StartDateArr = [3]
#    EndDateArr = [3]
#    if findSubString(StartDate,"/"):
#       StartDateArr=StartDate.split("/")
#    elif findSubString(StartDate,"-"):
#       StartDateArr=StartDate.split("-")
#    startday = datetime.date(int(StartDateArr[0]),int(StartDateArr[1]),int(StartDateArr[2]))
#    if findSubString(EndDate,"/"):
#       EndDateArr=EndDate.split("/")
#    elif findSubString(EndDate,"-"):
#       EndDateArr=EndDate.split("-")
#    try:
#       other_day = datetime.date(int(EndDateArr[0]),int(EndDateArr[1]),int(EndDateArr[2]))
#       result = startday - other_day
#       # print(result)
#       return abs(result.days)
#    except:
#       return 0


# def removeRedundantPID(str):
#    pass

#       #                     0         1        2         3                     4       5                 6        7            8          9        10            11
#       #                     商品代號   商品名稱 包裝方式   存量                  包裝量	批號	            有效期限	 供應商代號	   供應商名稱	提示	   剩餘有效天數	USD
#       #燈號  庫別	 庫別名稱  品號       品名	    包裝方式	庫存數量	安全庫存水位	                保存期限  有效期限	                                 剩餘有效天數	下單批量	迴轉率	迴轉天數	每月均銷量	每日均銷量	預估幾日售完	到貨天數
#       #A     B     C        D          E       F          G       H                              I       J                                          K              L        M        N        O        P           Q           R



# def getDataToExcel(driver,path):
#    Datalist = []
#    new_text=driver.find_elements_by_xpath("//table[@id='GridView1']/tbody/tr")
#    i = 0
#    result = []
#    temp = []
#    wb = Workbook()
#    ws = wb.active
#    # 定義你所要連接的檔案名稱
#    wb = xw.Book(path)
#    #取今天日期串
#    today = date.today()
#    today_str = today.strftime("%Y/%m/%d")
#    DelList = []
#    for text in new_text:
#       Datalist.append(text.text)
#       RowData=Datalist[i].split("\n")
#       Data=RowData[0].split(" ")
#       findStr=Data[2]
#       # print(Data[1])
#       # print(Data[2])
#       # print(Data[3])
#       # print(Data[4])
#       # print(Data[5])
#       # print(Data[6])
#       # print(Data[7])
#       # print(Data[9])
#       # print(Data[9])
#       if re.search(r"\d*[瓶]?[支]?[/][箱]?[盒]?", findStr) == None and i != 0:
#          Data[1]=Data[1]+Data[2]
#          Data[2]=Data[3]
#          Data[3]=Data[4]
#          Data[4]=Data[5]
#          Data[5]=Data[6]
#          Data[6]=Data[7]
#          Data[7]=""
#       elif re.search(r"\d*[m][l][/][瓶]", findStr)  and i != 0:
#          Data[1]=Data[1]+Data[2]
#          Data[2]=Data[3]
#          Data[3]=Data[4]
#          Data[4]=Data[5]
#          Data[5]=Data[6]
#          Data[6]=Data[7]
#          Data[7]=""

#       #排除品號
#       if (Data[0] == "70206023") | (Data[0] == "70206024") | (Data[0] == "70303719"):
#          continue

#       findStr=Data[6]
#       if re.search(r"\S?[退]\S?", findStr) != None:
#          Data[5]=Data[5]+Data[6]
#          Data[6]=Data[7]
#          Data[7]=""

#       findStr=Data[5]
#       #若沒批號，保存期限往後移
#       if re.search(r"\d*[/]\d*[/]\d*", findStr) != None:
#          Data[5]=""
#          Data[6]=Data[5]
#          Data[7]=Data[6]
#       if re.search(r"\d*[袋]\S*", findStr) != None:
#          Data[4]=Data[4]+Data[5]
#          Data[5]=Data[6]
#          Data[6]=Data[7]
#          Data[7]=""
#       elif re.search(r"\d*[包]\S*", findStr) != None:
#          Data[4]=Data[4]+Data[5]
#          Data[5]=Data[6]
#          Data[6]=Data[7]
#          Data[7]=""
#       # print('Data[4] = ' + Data[4])
#       # print('Data[5] = ' + Data[5])
#       if re.search(r"\d*\S*?\s?\S?[退]\S?", findStr) != None or re.search(r"\d*?[(][倒][)][凹][箱]", findStr) != None:
#          Data[0]=""
#          Data[1]=""
#          Data[2]=""
#          Data[3]=""
#          Data[4]=""
#          Data[5]=""
#          Data[6]=""
#          Data[7]=""
#          # temp[0]=Data[0]
#          # temp[1]=Data[1]
#          # temp[2]=Data[2]
#          # temp[3]=Data[3]
#          # temp[4]=Data[4]
#          # temp[5]=Data[5]
#          # temp[6]=Data[6]
#          # temp[7]=Data[7]
#          #陣列資料放進資料表
#          # wb.sheets[0].range('D' + str(i+1)).value  = ""
#          # wb.sheets[0].range('E' + str(i+1)).value  = ""
#          # wb.sheets[0].range('F' + str(i+1)).value  = ""
#          # wb.sheets[0].range('G' + str(i+1)).value  = ""
#          # wb.sheets[0].range('H' + str(i+1)).value  = ""
#          # wb.sheets[0].range('J' + str(i+1)).value  = ""
#          # # if i+1>=2:
#          # wb.sheets[0].range('K' + str(i+1)).value  = ""
#          # print('i = ' + str(i))

#          # print('i = ' + str(i))
#          # i=i-1
#       # else:
      
#          #陣列資料放進資料表
#       wb.sheets[0].range('D' + str(i+1)).value  = Data[0]
#       wb.sheets[0].range('E' + str(i+1)).value  = Data[1]
#       wb.sheets[0].range('F' + str(i+1)).value  = Data[2]
#       wb.sheets[0].range('G' + str(i+1)).value  = Data[3]
#       wb.sheets[0].range('H' + str(i+1)).value  = Data[4]
#       wb.sheets[0].range('J' + str(i+1)).value  = Data[6]
#       if i+1>=2:
#          wb.sheets[0].range('K' + str(i+1)).value  = getDiffDate(today_str,Data[6])
#       #記錄品號為空的列
#       if wb.sheets[0].range('D' + str(i+1)).value == None:
#          # print('i+1 = ' + str(i+1))
#          DelList.append(i+1)

#       i=i+1

#    #記錄品號為空的列刪除
#    # print(DelList)
#    j=0
#    for DelRow in DelList:
#       wb.sheets[0].api.Rows(DelRow-j).Delete()
#       #記錄已刪除列數
#       j=j+1


         

      

# 先找有無品號
# "select product_id from product where product_id = '" + str(product_id) + "';"

# 若無就新增品號
# "insert product (product_id) values('" + str(product_id) + "');"

# 再更新
# UPDATE product SET product_id=10903004, website=456;
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 

# def main(argv):



# def GoogleWebCrawlerByWebsite(keyword,website):
#    keyword=str(keyword) + " " + "site:"+str(website)
#    return getWebsiteWithGoogle(keyword)

# def initWebCrawler():
#    chrome_options = webdriver.ChromeOptions()
#    chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
#    chrome_options.add_argument('--headless')#不顯示視窗執行畫面
#    chrome_options.add_argument('--disable-gpu')
#    chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
#    DriverPath="C:\\ChromeDriver\\chromedriver.exe"
#    driver = webdriver.Chrome(DriverPath,options=chrome_options)
#    return driver

def getOHWebsite(keyword):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
    # chrome_options.add_argument('--headless')#不顯示視窗執行畫面
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
    DriverPath="C:\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(DriverPath,options=chrome_options)
    driver.get("http://www.ohealth.tw/front/bin/home.phtml")


    try:
        search_textbox=driver.find_element_by_name("Sch_txt")
        search_textbox.send_keys(keyword)
        search_button=driver.find_element_by_xpath("//td[@class='schbtntd1']/input")
        # print("driver.current_url : " +str(driver.current_url))
        search_button.click()
        search_result=driver.find_element_by_xpath("//a[@class='shadow-link']/img")
        # print("driver.current_url : " +str(driver.current_url))
        search_result.click()
        # print("driver.current_url : " +str(driver.current_url))
        current_url=driver.current_url
        driver.quit()#關閉瀏覽器
        return str(current_url)
    except Exception as e:
        print(e)
        return ""





# def main(argv):
#    # args = sys.argv[1:]
#    # print(argv[1])
#    # print(args[2])
#    # print(args[3])

   #記錄開始執行時間
   # start = time.time()
#    print(getProductIntroWebsite(argv[1]))
   
#    Product_Name=argv[1]
   # InputKeyword=str(Product_Name) + " " + "site:http://www.ohealth.tw/front/bin/ptdetail.phtml?Part="
   # print(InputKeyword)
   
   # chrome_options = webdriver.ChromeOptions()
   # chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
   # # chrome_options.add_argument('--headless')#不顯示視窗執行畫面
   # chrome_options.add_argument('--disable-gpu')
   # chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
   # DriverPath="C:\\ChromeDriver\\chromedriver.exe"
   # driver = webdriver.Chrome(DriverPath,options=chrome_options)

   # driver.get("https://www.google.com/search?q="+str(InputKeyword))
   # #result=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div")yuRUbf
   # elements=driver.find_elements_by_class_name("yuRUbf")
   # print("---------------------------")
   # print("elements: "+str(elements))
   # print("elements: "+str(len(elements)))
   # print("---------------------------")
   # i=1
   # for e in elements:
   #    print("i : " +str(i))
   #    print("e : " +str(e))
   #    print("driver.current_url : " +str(driver.current_url))
   #    if i == len(elements):
   #       break
   #    # wait = WebDriverWait(driver, 10) 
   #    # wait.until(EC.presence_of_element_located(((By.CLASS_NAME, 'yuRUbf')))
   #    e.click()
   #    i=i+1
      # if i > len(elements):
      #    break
      
      # time.sleep(1)

   # driver.quit()#關閉瀏覽器

   #記錄結束執行時間
   # end = time.time()

   # print("耗時 " + str(end-start) + " 秒")

# if __name__ == "__main__":
#    # main(sys.argv)
#    # print(getProductIntroWebsite("天然冰湖野米十穀米600g"))
#    print(getOHWebsite("冰湖野米十榖米"))

# print(getOHWebsite("十榖米"))
# print(getOHWebsite("冰湖野米十榖米"))

   

