import pymysql
# from selenium import webdriver

from OHWebCrawler import getOHWebsite
from GoogleWebCrawler import getProductIntroWebsite

import time
import re 


# def replace_all_blank(value):
#     # 去除value中的所有非字母內容，包括標點符號、空格、換行、下劃線等
#     # \W 表示匹配非數字字母下劃線
#     result = re.sub('\W+', '', value).replace("_", '')
#     return result




def setDB():
    # 資料庫設定
    db_settings = {
        "host": "172.21.7.39",#"localhost",#"172.21.7.39",
        "port": 3306,
        "user": "root",
        "password": "16264386",
        "db": "invdb",
        "charset": "utf8"
    }
    return db_settings

# def initWebCrawler():
    # print("initWebCrawler")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
    # chrome_options.add_argument('--headless')#不顯示視窗執行畫面
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
    # DriverPath="C:\\ChromeDriver\\chromedriver.exe"
    # driver = webdriver.Chrome(DriverPath,options=chrome_options)
    # return driver

# def getWebsiteWithGoogle(keyword,website):
#     print("getWebsiteWithGoogle")
#     keyword=str(keyword) + " " + "site:"+str(website)
#     # driver=initWebCrawler()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
#     chrome_options.add_argument('--headless')#不顯示視窗執行畫面
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
#     DriverPath="C:\\ChromeDriver\\chromedriver.exe"
#     driver = webdriver.Chrome(DriverPath,options=chrome_options)
#     driver.get("https://www.google.com/search?q="+str(keyword))
#     print("https://www.google.com/search?q=" +str(keyword))
#     elements=driver.find_elements_by_class_name("yuRUbf")
#     print("elements : " +str(elements))
#     i=1
#     print("i : " +str(i))
#     for e in elements:
#         print("i : " +str(i))
#         print("e : " +str(e))
#         print("driver.current_url : " +str(driver.current_url))
#         if i == len(elements):
#             return str(driver.current_url)
#         e.click()
#         i=i+1
#     driver.quit()#關閉瀏覽器

# def getProductIntroWebsite(keyword):
#     print("getProductIntroWebsite")
#     return getWebsiteWithGoogle(keyword,"http://www.ohealth.tw/front/bin/ptdetail.phtml?Part=")

def isProductExist(product_id):
    print("isProductExist")
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        try:
            sql="select count(product_id) from product where product_id = '"+str(product_id)+"'"#顯示資料
            print("sql : "+str(sql))
            cursor.execute(sql)
            myresult = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            print(myresult)
        except Exception as e:
            print(e)

        if myresult == 0:
            return False
        else:
            return True


def insertProduct(product_id,product_name):#輸入品號品名
    # sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    # if isProductExist(product_id) == False:
    with conn.cursor() as cursor:
        try:
            sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
            print("insertProduct")
            print("sql : "+str(sql))
            cursor.execute(sql)
        except Exception as e:
            print(e)
        # 儲存變更
        conn.commit()

def checkProduct(product_id,product_name):#輸入品號品名
    print("checkProduct")
    if isProductExist(product_id) == False:
        insertProduct(product_id,product_name)
        print("已新增品號品名")
    else:
        print("未新增品號品名,已有資料")


def saveWebsite(product_name,website):
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    # if isProductExist(product_id) == False:
    with conn.cursor() as cursor:
        try:
            # sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
            # print("insertProduct")
            sql="UPDATE product SET website='" + str(website) + "' where product_name='" +str(product_name) +"'"
            print("saveWebsite")
            print("sql : "+str(sql))
            cursor.execute(sql)
        except Exception as e:
            print(e)
        # 儲存變更
        conn.commit()

def getProductNameAll():
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    # if isProductExist(product_id) == False:
    with conn.cursor() as cursor:
        try:
            # sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
            # print("insertProduct")
            # sql="UPDATE product SET website='" + str(website) + "' where product_name='" +str(product_name) +"'"
            sql="select distinct product_id,product_name from inv"
            print("getProductNameAll")
            cursor.execute(sql)
            myresult = cursor.fetchall()
            conn.commit()
            cursor.close()
            # for x in myresult:
            #     print(x[0])
            return myresult
        except Exception as e:
            print(e)

def getFirstString(string):
    # string = string.replace("(", "", 1).replace("\)", "", 1)
    # string=replace_all_blank(string)
    return re.split(r'(\d+)', string)[0]

def getString(string):
    # string = string.replace("(", "", 1).replace("\)", "", 1)
    # string=replace_all_blank(string)
    StrArr=re.split(r'(\d+)', string)
    i=0
    s=""
    for i in range(len(StrArr)):
        s=str(s) + str(StrArr[i])
    return s

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



def replaceAllSymbol(value):
    # 去除value中的所有非字母內容，包括標點符號、空格、換行、下劃線等
    # \W 表示匹配非數字字母下劃線
    result = re.sub('\W+', '', value).replace("_", '')
    return result
    
def isDigit(string):
	return string.isdigit()

def replaceAllSymbolToBlank(value):
    # 去除value中的所有非字母內容，包括標點符號、空格、換行、下劃線等
    # \W 表示匹配非數字字母下劃線
    result = re.sub('\W+', ' ', value).replace("_", '')
    return result

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
    if isSubstringExist(string,'統健')==True:
        string=replaceStr(string,'統健','')
    if isSubstringExist(string,'康健生機')==True:
        string=replaceStr(string,'康健生機','')
    if isSubstringExist(string,'大賣場')==True:
        string=replaceStr(string,'大賣場','')
    if isSubstringExist(string,'康健有機')==True:
        string=replaceStr(string,'康健有機','')
    if isSubstringExist(string,'正直村')==True:
        string=replaceStr(string,'正直村','')
    if isSubstringExist(string,'罐')==True:
        string=replaceStr(string,'罐','')
    if isSubstringExist(string,'荷蘭')==True:
        string=replaceStr(string,'荷蘭','')
    if isSubstringExist(string,'袋')==True:
        string=replaceStr(string,'袋','')
    if isSubstringExist(string,'祕魯')==True:
        string=replaceStr(string,'祕魯','')
    if isSubstringExist(string,'手工醇釀醬油')==True:
        string=replaceStr(string,'手工醇釀醬油','手工純釀醬油')
    if isSubstringExist(string,'VITA香鬆')==True:
        string=replaceStr(string,'VITA香鬆','Vita素香鬆')
    if isSubstringExist(string,'罐裝')==True:
        string=replaceStr(string,'罐裝','')
    if isSubstringExist(string,'純濃鮮豆奶')==True:
        string=replaceStr(string,'純濃鮮豆奶','純濃鮮豆奶 500')
    if isSubstringExist(string,'波浪麵(蕎麥口味)')==True:
        string=replaceStr(string,'波浪麵(蕎麥口味)','波浪麵')
    if isSubstringExist(string,'珍品高山烏龍')==True:
        string=replaceStr(string,'珍品高山烏龍','珍品 烏龍')
    if isSubstringExist(string,'有機黑芝麻粉')==True:
        string=replaceStr(string,'有機黑芝麻粉','黑芝麻粉')
    if isSubstringExist(string,'甜菜根植物纖奶')==True:
        string=replaceStr(string,'甜菜根植物纖奶','康健生機-甜菜根植物纖奶')
    return string

def saveProductData(ProductID,ProductName):
    # FirstString=getFirstString(ProductName)
    # FirstString=getSearchString(replaceAllSymbolToBlank(ProductName))
    
    # SimpleProductName=replaceAllSymbol(FirstString)
    SimpleProductName=getSearchString(ProductName)
    SearchProductName=replaceWithWebPageTypos(SimpleProductName)
    print("ProductName : "+str(ProductName))
    # print("FirstString : "+str(FirstString))
    print("SimpleProductName : "+str(SimpleProductName))
    print("len(SimpleProductName) : "+str(len(SimpleProductName)))
    print("SearchProductName : "+str(SearchProductName))
    print("len(SearchProductName) : "+str(len(SearchProductName)))
    ProductIntroWebsite=getOHWebsite(SearchProductName)
    # if ProductIntroWebsite == "":
    #     ProductIntroWebsite=getProductIntroWebsite(SimpleProductName)
    print("ProductIntroWebsite : "+str(ProductIntroWebsite))
    checkProduct(ProductID,ProductName)
    saveWebsite(ProductName,ProductIntroWebsite)
    # time.sleep(60)

for x in getProductNameAll():
    print(x[0],x[1])
    ProductID=x[0]
    ProductName=x[1]
    print("ProductID : "+str(ProductID))
    print("ProductName : "+str(ProductName))
    saveProductData(ProductID,ProductName)
    # time.sleep(20)

#   10903004 | 十穀米(1800g)     
#   10903008 | 天然冰湖野米十穀米600g
#   11103036 | 枸杞菊花飲350ml(方形瓶)350ml/瓶
#   11308010 | 起司脆片(自然原味)     
#11303012 | 和風高纖蒟蒻乾320g(Q薄)     
# ProductID="11103036"
# ProductName="枸杞菊花飲350ml(方形瓶)350ml/瓶"
# saveProductData(ProductID,ProductName)
#  11308010 | 起司脆片(自然原味)   
#  11308011 | 起司脆片(辣味)   
#  11308014 | 起司原片(義式香草)(統健) 
# saveProductData("10903004","十穀米(1800g)")
# saveProductData("10903008","天然冰湖野米十穀米600g")
# saveProductData("11103036","枸杞菊花飲350ml(方形瓶)350ml/瓶")
# saveProductData("11303012","和風高纖蒟蒻乾320g(Q薄)")
# saveProductData("11308010","起司脆片(自然原味) ")
# saveProductData("11308011","起司脆片(辣味)")
# saveProductData("11308014","起司原片(義式香草)(統健)")

