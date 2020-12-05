from selenium import webdriver
from selenium.webdriver.support.select import Select
import selenium.webdriver.common.alert
import time
import os
from openpyxl import Workbook

#getData("xxxxxxxx",3,1)
#getData("xxxxxxxx",3,2)
def getRowData(id,FieldIndex):
   list = []
   new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
   i = 0
   result = 0
   for text in new_text:
      list.append(text.text)
      
      if list[i].split(" ")[0] == id:
         result = text.text
      i=i+1
   
   return result

def getData(id,FieldIndex):
   list = []
   new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
   i = 0
   result = 0
   for text in new_text:
      list.append(text.text)
      
      if list[i].split(" ")[0] == id:
         print(text.text)
         result = list[i].split(" ")[FieldIndex]
      i=i+1
   
   return result
#過濾9 已過期

#Lot No
def isOtherLotNO(id):
   list = []
   new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
   i = 0
   result = 0
   for text in new_text:
      list.append(text.text)
      
      if list[i].split(" ")[0] == id:
         print(text.text)
         if result != 0:
            return true
         else:
            result = list[i].split(" ")[FieldIndex]
            return false
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

# list = []
# new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
# for text in new_text:
#    list.append(text.text)

# print(list[1])
# print(list[1].split(" ")[3])
print(getData("11111111",3))
print(getData("11304021",3))
print(getRowData("11111111",3))
print(getRowData("11304021",3))
NewLines=getRowData("11304021",3)
FileName="123.txt"
fp = open(FileName, "w")
fp.writelines(NewLines)
fp.close()

wb = Workbook()
ws = wb.active
ws['A1'] = getRowData("11304021",3)
#ws.append(getRowData("11304021",3))
wb.save("sss.xlsx")



driver.quit()#關閉瀏覽器

#記錄結束執行時間
end = time.time()


print("耗時 " + str(end-start) + " 秒")




   # print(list[1])
   # print(list[1].split(" ")[FieldIndex])
   # return






