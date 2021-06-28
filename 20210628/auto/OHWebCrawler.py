from selenium import webdriver
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
# from test import getSearchString
# import Levenshtein as l
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
import re

def replaceAllSymbolToBlank(value):
    # 去除value中的所有非字母內容，包括標點符號、空格、換行、下劃線等
    # \W 表示匹配非數字字母下劃線
    result = re.sub('\W+', ' ', value).replace("_", '')
    return result

def getSearchString(s):
    # s='和風高纖蒟蒻乾320g(Q薄)'
    #去除數字
    result = re.split(r'(\d+)', s)
    # print(result)
    #串起來 過濾數字
    i=1
    s=""
    for i in range(len(result)):
        if result[i].isdigit() == False:
            s=s+str(result[i])
    # print(s)

    #去除英文
    result = re.split(r'([a-zA-Z0-9_])', s)
    # print(result)
    #串起來 過濾英文
    i=1
    s=""
    for i in range(len(result)):
        if result[i].encode('UTF-8').isalpha() == False:
            s=s+str(result[i])
    # print(s)
    s=replaceAllSymbolToBlank(s)#.rstrip()
    print(s)
    return s

def isSubstringExist(substr,string):
    if len(substr)>len(string):
        temp=substr
        substr=string
        string=temp
    pos = string.find(substr)
    if pos >= 0:   #有找到
        return True
    else:   #沒有找到
        return False

def isSubstringPos(substr,string):
    if len(substr)>len(string):
        temp=substr
        substr=string
        string=temp
    pos = string.find(substr)
    if pos >= 0:   #有找到
        return pos
    else:   #沒有找到
        return -1

def replaceStr(string,ReplacedStr,ReplaceStr):
    NewString=string.replace(ReplacedStr,ReplaceStr)
    return NewString

def replaceWithWebPageTypos(string):
    # if isSubstringExist(string,'十穀米')==True:
    #     string=replaceStr(string,'穀','榖')
    # if isSubstringExist(string,'甜菜根植物纖奶')==True:
    #     string=replaceStr(string,'甜菜根植物纖奶','康健生機-甜菜根植物纖奶')
    if isSubstringExist(string,'天然冰湖野米十穀米')==True:
        string=replaceStr(string,'天然冰湖野米十穀米','冰湖野米十榖米')
    if isSubstringExist(string,'起司原片')==True:
        string=replaceStr(string,'起司原片','起司脆片')
    if isSubstringExist(string,'枸杞菊花飲')==True:
        string=replaceStr(string,'枸杞菊花飲','枸杞菊花養生飲')
    if isSubstringExist(string,'方形瓶')==True:
        string=replaceStr(string,'方形瓶','')
    if isSubstringExist(string,'瓶')==True:
        string=replaceStr(string,'瓶','')
    if isSubstringExist(string,'版')==True:
        string=replaceStr(string,'版','')
    if isSubstringExist(string,'統健')==True:
        string=replaceStr(string,'統健','')

    if isSubstringExist(string,'康健生機')==True:
        string=replaceStr(string,'康健生機','')
    if isSubstringExist(string,'康健')==True:
        string=replaceStr(string,'康健','')
    if isSubstringExist(string,'自然')==True:
        string=replaceStr(string,'自然','')
    if isSubstringExist(string,'盒')==True:
        string=replaceStr(string,'盒','')

    if isSubstringExist(string,'大賣場')==True:
        string=replaceStr(string,'大賣場','')
    # if isSubstringExist(string,'康健有機')==True:
    #     string=replaceStr(string,'康健有機','')
    if isSubstringExist(string,'正直村')==True:
        string=replaceStr(string,'正直村','')
    if isSubstringExist(string,'罐')==True:
        string=replaceStr(string,'罐','')
    # if isSubstringExist(string,'荷蘭')==True:
    #     string=replaceStr(string,'荷蘭','')
    # if isSubstringExist(string,'袋')==True:
    #     string=replaceStr(string,'袋','')
    if isSubstringExist(string,'祕魯')==True:
        string=replaceStr(string,'祕魯','')
    if isSubstringExist(string,'手工醇釀醬油')==True:
        string=replaceStr(string,'手工醇釀醬油','手工純釀醬油')
    if isSubstringExist(string,'香鬆')==True:
        string=replaceStr(string,'香鬆','素香鬆')
    if isSubstringExist(string,'罐裝')==True:
        string=replaceStr(string,'罐裝','')
    # if isSubstringExist(string,'純濃鮮豆奶')==True:
    #     string=replaceStr(string,'純濃鮮豆奶','純濃鮮豆奶 500')
    if isSubstringExist(string,'蕎麥口味')==True:
        string=replaceStr(string,'蕎麥口味','')
    # if isSubstringExist(string,'波浪麵(蕎麥口味)')==True:
    #     string=replaceStr(string,'波浪麵(蕎麥口味)','波浪麵')
    if isSubstringExist(string,'珍品高山烏龍')==True:
        string=replaceStr(string,'珍品高山烏龍','珍品 烏龍')
    if isSubstringExist(string,'有機黑芝麻粉')==True:
        string=replaceStr(string,'有機黑芝麻粉','黑芝麻粉')
#     if isSubstringExist(string,'甜菜根植物纖奶')==True:
#         string=replaceStr(string,'甜菜根植物纖奶','康健生機-甜菜根植物纖奶')
#康健生機-甜菜根植物纖奶800g	康健生機-甜菜根植物纖奶	
#康健生機－甜菜根植物纖奶30g*25	甜菜根植物纖奶(盒)	
    return string

def getOHWebsite(keyword):
    SimpleProductName=getSearchString(keyword)
    SearchProductName=replaceWithWebPageTypos(SimpleProductName)

    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    chrome_options.add_argument('--user-agent=%s' % user_agent)#偽裝使用者
    chrome_options.add_argument('-headless')#無頭模式啟動
    chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
    # chrome_options.add_argument('--headless')#不顯示視窗執行畫面
    chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
    DriverPath="C:\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(DriverPath,options=chrome_options)
    driver.get("http://www.ohealth.tw/front/bin/home.phtml")


    try:
        search_textbox=driver.find_element_by_name("Sch_txt")
        search_textbox.send_keys(SearchProductName)
        search_button=driver.find_element_by_xpath("//td[@class='schbtntd1']/input")
        # print("driver.current_url : " +str(driver.current_url))
        search_button.click()
        i=1
        font_text=""
        SearchProductName=SearchProductName.rstrip()
       #  font_text=font_text.rstrip()
        Maxlen=0
        MaxlenIndex=0
        while font_text != SearchProductName:
              print("---------------------------")
              print("i : " +str(i))
              # print("len(font_text) : " +str(len(font_text)))
              # print("len(keyword) : " +str(len(keyword)))
              print("font_text : " +str(font_text))
              print("SearchProductName : " +str(SearchProductName))
              print("---------------------------")
              try:
                     font_text=driver.find_element_by_xpath("(//a[@class='shadow-link']/font)["+str(i)+"]").text
                     # print("font_text : " +str(font_text))
                     # print("keyword2 : " +str(keyword))
                     # if len(keyword)>Maxlen:
                     #        Maxlen=len(keyword)
                     #        MaxlenIndex=i
                     print("font_text2 : " +str(font_text))
                     print("SearchProductName2 : " +str(SearchProductName))
                     if font_text == SearchProductName:

                            search_result=driver.find_element_by_xpath("(//a[@class='shadow-link']/img)["+str(i)+"]")
                            search_result.click()
                            # items = driver.find_elements_by_tag_name("a")
                            # print(items)
                            # for item in items:
                            # href = item.get_attribute('href')
                            # print(href)
                            srcs=driver.find_element_by_xpath("(//td[@valign='top']/img)")
                            print("srcs : " +str(srcs))
                            for src in srcs:
                                   href = src.get_attribute('src')
                                   print(href)
                            current_url=driver.current_url
                            driver.quit()#關閉瀏覽器
                            print("current_url : " +str(current_url))
                            return str(current_url)
                     i=i+1
              except Exception as e:
                     print("e : "+str(e))
                     print("MaxlenIndex : "+str(MaxlenIndex))
                     i=1

                     while font_text != SearchProductName:
                            print("---------------------------")
                            print("i_2 : " +str(i))
                            # print("len(font_text) : " +str(len(font_text)))
                            # print("len(keyword) : " +str(len(keyword)))
                            print("font_text : " +str(font_text))
                            print("SearchProductName : " +str(SearchProductName))
                            print("---------------------------")
                            try:
                                   font_text=driver.find_element_by_xpath("(//a[@class='shadow-link']/font)["+str(i)+"]").text
                                   # print("font_text : " +str(font_text))
                                   # if len(keyword)>Maxlen:
                                   #        Maxlen=len(keyword)
                                   #        MaxlenIndex=i
                                   font_text=getSearchString(font_text)
                                   font_text=replaceWithWebPageTypos(font_text)
                                   # keyword=keyword.rstrip()
                                   font_text=font_text.rstrip().lstrip()
                                   print("font_text3 : " +str(font_text))
                                   print("SearchProductName3 : " +str(SearchProductName))
                                   if font_text == SearchProductName:

                                          search_result=driver.find_element_by_xpath("(//a[@class='shadow-link']/img)["+str(i)+"]")
                                          search_result.click()
                                          srcs=driver.find_element_by_xpath("(//td[@valign='top']/img)")
                                          print("srcs : " +str(srcs))
                                          for src in srcs:
                                                 href = src.get_attribute('src')
                                                 print(href)
                                          current_url=driver.current_url
                                          driver.quit()#關閉瀏覽器
                                          print("current_url : " +str(current_url))
                                          return str(current_url)
                                   i=i+1
                            except Exception as e:
                                   print("e : "+str(e))
                                   print("MaxlenIndex : "+str(MaxlenIndex))
                                   return "NULL"





                     # if MaxlenIndex!=0:
                     #        search_result=driver.find_element_by_xpath("(//a[@class='shadow-link']/img)["+str(MaxlenIndex)+"]")
                     #        search_result.click()
                     #        current_url=driver.current_url
                     #        driver.quit()#關閉瀏覽器
                     #        print("current_url : " +str(current_url))
                     #        return str(current_url)
                     # else:
                     #        return "NULL"

       #  elements=driver.find_element_by_xpath("//a[@class='shadow-link']/img").get_attribute('title')shadow-link

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

   

