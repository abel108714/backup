#import win32gui
#import win32api
#import win32con

#def enumHandler(hwnd, lParam):
#    if win32gui.IsWindowVisible(hwnd):
#        if 'Stack Overflow' in win32gui.GetWindowText(hwnd):
#            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F11, 0)


#win32gui.EnumWindows(enumHandler, None)


import ctypes
import win32gui
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append((hwnd, buff.value))
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)
#print(titles)
#print("1111")
#for i in range(len(titles)):
#    print(range(len(titles)))
#    print(i)
#    print(titles)[i]



#win32gui.MoveWindow((titles)[5][0], 0, 0, 760, 500, True)


import win32gui,win32process
def get_window_pid(title):
   hwnd = win32gui.FindWindow(None, title)
   threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
   return pid

from pywinauto import Desktop
windows = Desktop(backend="uia").windows()
for w in windows:
    print(w.window_text())
    print(get_window_pid(w.window_text()))


print("123")
import win32gui, win32process, psutil
print("456")
def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return(psutil.Process(pid[-1]).name())
    except:
        pass
print("789")

print(active_window_process_name())
import os
import signal

os.kill(12968, signal.SIGTERM)

print("123")




