
import sys
import pyscreenshot as ImageGrab
from io import BytesIO

import tkinter as tk
from tkinter import messagebox


def main(argv):
    try:
        args = sys.argv[1:]
        print(argv[0])
        print(argv[1])
        print(argv[2])
        #path = "C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\SD\\"
        path = "S:\網通部\◎資訊\\test\\"
        #path = argv[4]
        img_buffer = BytesIO()
        img = ImageGrab.grab(bbox=(28,200,1247,942))  # X1, Y1, X2, Y2
        print(path+argv[1]+argv[2]+"銷貨明細_"+argv[3]+".jpg")
        #messagebox.showinfo('my messagebox', path+argv[1]+argv[2]+"銷貨明細_"+argv[3]+".jpg")
        img.save(path+argv[1]+argv[2]+"銷貨明細_"+argv[3]+".jpg")
    except:
        messagebox.showinfo('my messagebox', '發生錯誤')

if __name__ == "__main__":
	main(sys.argv)



# root = tk.Tk()
# root.withdraw()
# try:
#     img_buffer = BytesIO()
#     img = ImageGrab.grab(bbox=(28,200,1219,704))  # X1, Y1, X2, Y2
#     img.save("C:\\auto\SDPic.png")
# except:
#     messagebox.showinfo('my messagebox', '發生錯誤')
#     print('發生錯誤')


