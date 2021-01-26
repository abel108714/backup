import threading
import time
 
 
def scraper(value):
    print("start"+str(value))
    time.sleep(5)
    print("sleep done"+str(value))
 
 
t = threading.Thread(target=scraper(1))  #建立執行緒
t2 = threading.Thread(target=scraper(2))  #建立執行緒
t.start()  #-執行
print("end")