
import time
import win32gui, win32ui, win32con, win32api

from selenium import webdriver
from selenium.webdriver.support.select import Select

def window_capture(filename):
    hwnd = 0 # 視窗的編號，0號表示當前活躍視窗
    # 根據視窗控制代碼獲取視窗的裝置上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根據視窗的DC獲取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC建立可相容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 建立bigmap準備儲存圖片
    saveBitMap = win32ui.CreateBitmap()
    # 獲取監控器資訊
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    print(w)
    print(h)
    # print w,h　　　#圖片大小
    # 為bitmap開闢空間
    # saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    #畫布大小565, 306
    saveBitMap.CreateCompatibleBitmap(mfcDC, 565, 306)
    # 高度saveDC，將截圖儲存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 擷取從左上角（0，0）長寬為（w，h）的圖片
    # saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    # saveDC.BitBlt((0, 100), (w, h), mfcDC, (565, 306), win32con.SRCCOPY)
    # saveDC.BitBlt((565, 306), (w, h), mfcDC, (0, 100), win32con.SRCCOPY)
    #起點 0,0
    #圖片大小 565, 306
    #截圖起點 0, 114
    saveDC.BitBlt((0, 0), (565, 306), mfcDC, (0, 114), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def YahooWebCrawler(StockCode):
   # args = sys.argv[1:]
   # print(argv[1])
   # print(args[2])
   # print(args[3])

   #記錄開始執行時間
#    start = time.time()

#    username = "OGB"
#    password = "og*16264386"

   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument('blink-settings=imagesEnabled=false')#不載入圖片，提升速度
   # chrome_options.add_argument('--headless')#不顯示視窗執行畫面
   chrome_options.add_argument('--disable-gpu')
   chrome_options.add_argument('--start-maximized')#若要顯示則顯示最大化
   DriverPath="C:\\ChromeDriver\\chromedriver.exe"
   driver = webdriver.Chrome(DriverPath,options=chrome_options)
#    driver.get("https://tw.stock.yahoo.com/q/ta?s="+str(StockCode))
   driver.get("https://s.yimg.com/nb/tw_stock_frontend/scripts/TaChart/tachart.3de240ea9a.html?sid="+str(StockCode))
   beg = time.time()
   for i in range(10):
      #  window_capture("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\haha.jpg")
      window_capture("S:\\網通部\\◎資訊\\test\\stock.jpg")
   end = time.time()
   print(end - beg)
#    PeriodButton=driver.find_element_by_id("TAChartPeriod")
#    PeriodButton.click()
#    time.sleep(10)
#    #帳號
#    username_textbox = driver.find_element_by_id("TAChartPeriod")
#    username_textbox.send_keys(username)

#    #密碼
#    password_textbox = driver.find_element_by_id("Login1_Password")
#    password_textbox.send_keys(password)

#    #登入
#    login_button = driver.find_element_by_id("Login1_LoginButton")
#    login_button.click()

#    TreeView =driver.find_element_by_id('ctl00_TreeView1n5')
#    TreeView.click()
#    #庫別
#    sel = driver.find_element_by_css_selector("select[id='ctl00_ContentPlaceHolder1_lstWare']")
#    Select(sel).select_by_visible_text('觀音物流中心')
#    #良品?
#    RadioButton = driver.find_element_by_id('ctl00_ContentPlaceHolder1_RadioButton1')
#    RadioButton.click()
#    #查詢
#    Button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
#    Button.click()

#    getDataToExcel(driver,argv[1])

   driver.quit()#關閉瀏覽器

#    #記錄結束執行時間
#    end = time.time()

#    print("耗時 " + str(end-start) + " 秒")


# YahooWebCrawler(2330)



