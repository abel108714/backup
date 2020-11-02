
import calendar
import datetime
from datetime import timedelta
#返回datetime格式：eg：2019-12-07 20:38:35.82816
#now = datetime.datetime.now()

#返回datetime格式：eg：2019-12-07
now = datetime.datetime.now().date()
now = datetime.date.today()
this_month_start = datetime.datetime(now.year, now.month, 1)
#this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
last_month_end = this_month_start - timedelta(days=1) 
#last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)


print(last_month_end)
#print(last_month_start)

