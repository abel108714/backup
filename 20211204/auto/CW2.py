
import win32gui
import win32api
import win32con
from win32gui import *
from win32api import *
from win32con import *
import time
import os

titles = set()
def EnumWindowsProc (hwnd,mouse):
    #if you want to show all the window,pls delete the one line below
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd) and GetWindowText(hwnd) != "":
        text = GetWindowText(hwnd)
        titles.add(text)
        classname = GetClassName(hwnd)
        print("the window's text = %s \nhwnd = %d classname = %s" % (text,hwnd,classname))
        #SendMessage(hwnd,win32con.WM_CLOSE,win32con.VK_RETURN,0)
        try:
            SetForegroundWindow(hwnd)
            print(ShowWindow(hwnd,SW_SHOW))
        except Exception as e:
            print(e)
        time.sleep(3)


def PrintSort_ALL_visable_window():
    EnumWindows(EnumWindowsProc, 1)
    print("titles = %s" % titles)
    print(GetCurForWin())
    print("1234")
    lt = [t for t in titles if t]
    lt.sort()
    print(lt)
    for t in lt:
        print(t)
        
# return an Handle of a window
def GetCurForWin():
    print("GetCurForWin")
    for i in range(1,2):
        time.sleep(1)
        hw = win32gui.GetForegroundWindow()
        text = GetWindowText(hw)
        desk = win32gui.GetDesktopWindow()
        print("Current window's hw = %d, desk = %d, text = %s" % (hw,desk,text))
    return str("Current window's hw = %d, desk = %d, text = %s" % (hw,desk,text))

class WindowFinder:
    #"Class to find and make focus on a particular Native OS dialog/Window "
    def __init__ (self):
        self._handle = 527588

    def find_window(self, class_name, window_name = None):
        #"Pass a window class name & window name directly if known to get the window"
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard): 
        #"This function takes a string as input and calls EnumWindows to enumerate through all open windows"
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        #"Get the focus on the desired open window"
        win32gui.SetForegroundWindow(self._handle)

    def SetForWin(hwnd):
        SetForegroundWindow(hwnd)
        SetWindowPos(hwnd,HWND_TOP,0,0,0,0,win32con.SWP_SHOWWINDOW)

    def GetWindByTitile():
        hwnd = FindWindow(None, "RIDE - Win Operate")
        text = GetWindowText(hwnd)
        print(text)
        SetForegroundWindow(hwnd)
#        SetFocus(hwnd)
        ShowWindow(hwnd,SW_RESTORE)


if __name__ == '__main__':
    GetCurForWin()
    #print(dir(win32api))
    PrintSort_ALL_visable_window()
    #print(GetDesktopWindow())
    #GetWindByTitile()

    #print(hwnd)
    #SetForegroundWindow(hwnd) #設置其爲最前，但設置之後並不能讓它顯示出來，接着就要顯示它
    #ShowWindow(hwnd,SW_SHOW) #顯示的這個函數的第二個參數比較重要，它決定着窗口如何顯示