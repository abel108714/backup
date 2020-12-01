from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

username = "OGB"
password = "OG140"
#option = webdriver.ChromeOptions()
#option.add_argument('disable-infobars')
#driver = webdriver.Chrome(chrome_options=option)

driver = webdriver.Chrome("C:\\ChromeDriver\\chromedriver.exe")
driver.get("http://www.logistics.com.tw/TMP/login.aspx?ReturnUrl=%2FTMP%2FDefault.aspx")
print("0")
#帳號
username_textbox = driver.find_element_by_id("Login1_UserName")
username_textbox.send_keys(username)
print("1")
#密碼
password_textbox = driver.find_element_by_id("Login1_Password")
password_textbox.send_keys(password)
print("2")
#登入
login_button = driver.find_element_by_id("Login1_LoginButton")
login_button.click()
print("3")
TreeView =driver.find_element_by_id('ctl00_TreeView1n5')
TreeView.click()
print("4")
#庫別
sel = driver.find_element_by_css_selector("select[id='ctl00_ContentPlaceHolder1_lstWare']")
Select(sel).select_by_visible_text('觀音物流中心')
print("5")
#良品?
RadioButton = driver.find_element_by_id('ctl00_ContentPlaceHolder1_RadioButton1')
RadioButton.click()
print("6")
#查詢
Button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
Button.click()
print("123")


#time.sleep(3)
#print(driver.find_element_by_tag_name('tbody').text)
#print(driver.find_element_by_id('GridView1').text)
i=0
list = []
new_text=driver.find_elements_by_xpath(("//table[@id='GridView1']/tbody/tr"))
for text in new_text:
   list.append(text.text)
   #print(list)
   #print(str(i) + text.text)
   i=i+1

print(list[1])
print(list[1].split(" ")[3])

print("456")




