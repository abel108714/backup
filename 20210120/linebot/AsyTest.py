import asyncio

def hello_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()





import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from selenium import webdriver

executor = ThreadPoolExecutor(10)


def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)


def scraper(url):
    DriverPath="C:\\ChromeDriver\\chromedriver.exe"
    driver = webdriver.Chrome(DriverPath)
    driver.get(url)


loop = asyncio.get_event_loop()
for url in ["https://www.google.com.tw/"] * 2:
    scrape(url, loop=loop)

loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))