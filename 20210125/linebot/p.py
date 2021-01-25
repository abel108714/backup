from ProgressBar import *

# def main(argv):
   # args = sys.argv[1:]
   # print(argv[1])
   # print(args[2])
   # print(args[3])

# if __name__ == "__main__":
#    main(sys.argv)
from openpyxl import load_workbook
path = 'S:\\網通部\\◎資訊\\年度績效數字分析\\COPR2320210120000088202101200001.xlsx'
wb2 = load_workbook(path)
i=1
print("1")
pb=ProgressBar(len(wb2.worksheets))
print("2")

for i in range(100):
   time.sleep(0.5)
   print(i)
   
   pb.updateProgressbar(i)









































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