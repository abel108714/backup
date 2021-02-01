
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

# root = tkinter.Tk()
# root.geometry("165x68")
# canvas = tkinter.Canvas(root, width=165, height=68)# width=165.75, height=68.25)
# canvas.create_rectangle(10,15,100,30, fill = 'red')
# canvas.create_rectangle(100,150,200,200, fill = 'yellow')
# canvas ['bg']='White'
# canvas.pack()
# root.mainloop() S
import tkinter 
from tkinter import *
my_w=Tk()
label_1=Label(my_w,width="40",height="3",bg="red")
label_1.grid(row=0,column=0)
my_w.mainloop() 
label_1=Label(my_w,width="30",height="3",bg="red")
# label_1.update()
my_w.update()
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