from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

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

#GridView = driver.find_element_by_id('GridView1')
#print(GridView)
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

html = urllib.request.urlopen("http://www.logistics.com.tw/TMP/RptQry03.aspx").read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class': 'text'})
print(table)


