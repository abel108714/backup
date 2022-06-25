#pip install PIL 
#pip install pytesseract 
#安裝模組以後，我們還需要下載OCR會使用到的資料到你的模組資料夾中。
#下載位置：https://github.com/UB-Mannheim/tesseract/wiki

#接下來，將圖片放到與你python程式同樣位置的資料夾中，並執行以下範例程式

import win32gui, win32ui, win32con, win32api
from PIL import Image
import pytesseract
from win32api import GetSystemMetrics
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
    #左上角為起點 758 508
    #左上角為起點 721 487
    #37  21
    saveBitMap.CreateCompatibleBitmap(mfcDC, 37, 21)
    #saveBitMap.CreateCompatibleBitmap(mfcDC, GetSystemMetrics(0), GetSystemMetrics(1))
    # 高度saveDC，將截圖儲存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 擷取從左上角（0，0）長寬為（w，h）的圖片
    # saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    # saveDC.BitBlt((0, 100), (w, h), mfcDC, (565, 306), win32con.SRCCOPY)
    # saveDC.BitBlt((565, 306), (w, h), mfcDC, (0, 100), win32con.SRCCOPY)
    #起點 0,0
    #圖片大小 565, 306
    #截圖起點 0, 114
    #saveDC.BitBlt((0, 0), (565, 306), mfcDC, (0, 114), win32con.SRCCOPY)
    #saveDC.BitBlt((721, 487), (37, 21), mfcDC, (37, 21), win32con.SRCCOPY)

    #第一個設定截圖相對於預設的左上角原點(0,0)的起點，
    # 例如(-50,-100)就是左上角往右50往下100
    #第三個設定是截圖範圍起點，使用截圖相對起點作為相對起點算起再進行設定截圖範圍起點，
    # 例如(-50,-100)就是左上角往右50往下100，如果再設定(-25,-25),那就是左上角往右75往下125
    
    #saveDC.BitBlt((-721, -487), (565, 306), mfcDC, (-721, -487), win32con.SRCCOPY)
    #import pyautogui
    #pyautogui.size()
    #print(pyautogui.size())
    

    #print("Width =", GetSystemMetrics(0))
    #print("Height =", GetSystemMetrics(1))
    saveDC.BitBlt((-721, -487), (GetSystemMetrics(0), GetSystemMetrics(1)), mfcDC, (0, 0), win32con.SRCCOPY)
    #saveDC.BitBlt((0, 0), (GetSystemMetrics(0), GetSystemMetrics(1)), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)



import pygetwindow
win = pygetwindow.getWindowsWithTitle('cmd')[0]
win.size = (0, 0)


pytesseract.pytesseract.tesseract_cmd='C:\\Users\\udev77\AppData\Local\Tesseract-OCR\\tesseract.exe'


window_capture("p.png")

#ImageText = pytesseract.image_to_string( Image.open( "test.png" ),lang = "chi_tra" )
ImageText = pytesseract.image_to_string( Image.open( "p.png" ),lang = "chi_tra" )
print( ImageText )

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
messagebox.showinfo('my messagebox', ImageText)

sys.exit()
#return ImageText