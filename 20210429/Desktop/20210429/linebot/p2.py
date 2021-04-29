from tkinter import *
from tkinter.ttk import *
import time


def updateProgressbar(speed):
    time.sleep(0.05)
    bar['value']+=(speed/100)*100
    window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()
GB = 100
download = 0
speed = 1
while(download<GB):
    download+=speed
    updateProgressbar(download)
    # button = Button(window,text="download",command=updateProgressbar(download)).pack()

window.mainloop()