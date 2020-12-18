

from tkinter import *
window = Tk()
window.title("你的標題")
window.geometry("300x300") #注意是string，而不是數字
window.maxsize(300,300) #int
window.resizable(0,0) #不可以更改大⼩
window.mainloop()


import win32gui
def is_screensaver_running():
        #return win32gui.SystemParametersInfo(win32con.SPI_GETSCREENSAVERRUNNING) 
        return win32gui.SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)


is_screensaver_running()

        # '關閉螢幕保護程式
        # SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)
        # '開啟螢幕保護程式
        # SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 1, Nothing, SPIF_SENDWININICHANGE)