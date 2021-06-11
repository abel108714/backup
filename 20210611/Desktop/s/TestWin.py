
# import tkMessageBox
# from tkinter import *
# import tkinter as tk
# window = tk.Tk()
# window.title("你的標題")
# window.geometry("300x300") #注意是string，而不是數字
# window.maxsize(300,300) #int
# window.resizable(0,0) #不可以更改大⼩

# B = tk.Button(window, text ="点我" ).pack()#, command =helloCallBack)
 
# # B.pack()
# # top.mainloop()
# window.mainloop()
# import tkinter as tk

# root = tk.Tk()

# btn = tk.Button(root, text='正常按鈕', state=tk.NORMAL).pack()
# btn2 = tk.Button(root, text='關閉按鈕', state=tk.DISABLED).pack()
# btn3 = tk.Button(root, text='啟動按鈕', state=tk.ACTIVE).pack()

# root.mainloop()

import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas .create_retangle(0,0,100,100, fill = 'red')
canvas ['bg']='green'
canvas.pack()
root.mainloop() 

# import win32gui, win32con

# def CheckScreenSaverState():
#   return win32gui.SystemParametersInfo(win32con.SPI_GETSCREENSAVERRUNNING)

# print(CheckScreenSaverState)

# def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello Runoob")
# import win32gui
# def is_screensaver_running():
        #return win32gui.SystemParametersInfo(win32con.SPI_GETSCREENSAVERRUNNING) 
#         return win32gui.SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)


# is_screensaver_running()
 
        # '關閉螢幕保護程式
        # SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 0, Nothing, SPIF_SENDWININICHANGE)
        # '開啟螢幕保護程式
        # SystemParametersInfo(SPI_SETSCREENSAVERACTIVE, 1, Nothing, SPIF_SENDWININICHANGE) 