

from tkinter import *
window = Tk()
window.title("你的標題")
window.geometry("300x300") #注意是string，而不是數字
window.maxsize(300,300) #int
window.resizable(0,0) #不可以更改大⼩
window.mainloop()