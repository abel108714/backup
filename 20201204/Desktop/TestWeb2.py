#2020/12/1
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select

class WebCrawler:

    def __init__(self,AutoLogin='false',WebDriver='None',WebSide='None'):
        self.AutoLogin = AutoLogin
        if WebDriver = 'chrome':
            for root, dirs, files in os.walk("/"):#找整個根目錄
                for file in files:
                    if file.endswith("chromedriver.exe"):#要找的檔案
                        self.WebDriver = os.path.join(root, file)
        else:
            self.WebDriver = WebDriver
        self.WebSide = WebSide

    def setAccount(self,Account,Pwd):
        self.Account = Account
        self.Pwd = Pwd

    def getWebsiteData(self,KeyStr):
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        for line in Lines: 
            if KeyStr == line.strip().split(self.SplitStr)[self.key]:
                return count
            else:
                count+=1




import time

username = "OGB"
password = "OG140"

driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
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

list = []
new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
for text in new_text:
   list.append(text.text)

print(list[1])
print(list[1].split(" ")[3])






