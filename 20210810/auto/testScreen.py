import win32gui
import win32con

#to turn off use :-
win32gui.SendMessage(win32con.HWND_BROADCAST,
                     win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
#turn on use :-
win32gui.SendMessage(win32con.HWND_BROADCAST,
                     win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)