#from datetime #import datetime, timezone, timedelta
import datetime as dt
# 設定為 +8 時區
tz = dt.timezone(dt.timedelta(hours=+8))
date = dt.datetime.now(tz)
oneday = dt.timedelta(days=1)
ydate = date-oneday



#獲取今天的日期
y=str(date.year)
if int(date.month) < 10:
    m = '0' + str(date.month)
else:
    m = str(date.month)

if int(date.day) < 10:
    d = '0' + str(date.day)
else:
    d = str(date.day)
#獲取昨天的日期
yes_y=str(ydate.year)
if int(ydate.month) < 10:
    yes_m = '0' + str(ydate.month)
else:
    yes_m = str(ydate.month)
if int(ydate.day) < 10:
    yes_d = '0' + str(ydate.day)
else:
    yes_d = str(ydate.day)
tdy_date_str = y + m + d
ysdy_date_str = yes_y + yes_m + yes_d
BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d

print(tdy_date_str)
print(ysdy_date_str)
print(BegMonthOfTodayPeriod)

import datetime
day = datetime.datetime.now()
ddelay = datetime.timedelta(days=1)
wdelay = datetime.timedelta(weeks = 5)
ydelay = datetime.timedelta(weeks = 56)

print(day)
print(day - ddelay)  # 一天前的时间
print(day + ddelay)  # 一天后的时间
print(day - wdelay)  # 5 周前
print(day + wdelay)  # 5 周后
print(day - ydelay)  # 一年前
print(day + ydelay)  # 一年后
def getYesterday(): 
    today=dt.date.today() 
    oneday=dt.timedelta(days=1) 
    yesterday=today-oneday
    return yesterday

# 输出
print(getYesterday())