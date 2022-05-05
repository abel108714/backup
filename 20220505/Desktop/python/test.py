import datetime
import schedule
import time

 
def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:", datetime.datetime.now())
 
def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())

def job3():
    print("I'm working for job3")
    time.sleep(2)
    print("job3:", datetime.datetime.now())
 
#def run():
#schedule.every(10).seconds.do(job1)
#schedule.every(10).seconds.do(job2)
schedule.every().day.at("10:25").do(job3)
 
while True:
    schedule.run_pending()
    time.sleep(1)


