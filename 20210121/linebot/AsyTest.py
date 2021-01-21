from tkinter import *
from tkinter.ttk import *
import time


def updateProgressbar(speed):
    time.sleep(0.05)
    bar['value']+=(speed/100)*100
    # download+=speed
    # percent.set(str(int((download/GB)*100))+"%")
    # text.set(str(download)+"/"+str(GB)+" GB completed")
    window.update_idletasks()


# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while(download<GB):
#         download+=speed
#         updateProgressbar(download)
        # time.sleep(0.05)
        # bar['value']+=(speed/GB)*100
        # download+=speed
        
        # # percent.set(str(int((download/GB)*100))+"%")
        # # text.set(str(download)+"/"+str(GB)+" GB completed")
        # window.update_idletasks()

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










































# import asyncio

# def hello_world(loop):
#     """A callback to print 'Hello World' and stop the event loop"""
#     print('Hello World')
#     loop.stop()

# loop = asyncio.get_event_loop()

# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)

# # Blocking call interrupted by loop.stop()
# try:
#     loop.run_forever()
# finally:
#     loop.close()





# import asyncio
# from concurrent.futures.thread import ThreadPoolExecutor

# from selenium import webdriver

# executor = ThreadPoolExecutor(10)


# def scrape(url, *, loop):
#     loop.run_in_executor(executor, scraper, url)


# def scraper(url):
#     DriverPath="C:\\ChromeDriver\\chromedriver.exe"
#     driver = webdriver.Chrome(DriverPath)
#     driver.get(url)


# loop = asyncio.get_event_loop()
# for url in ["https://www.google.com.tw/"] * 2:
#     scrape(url, loop=loop)

# loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))