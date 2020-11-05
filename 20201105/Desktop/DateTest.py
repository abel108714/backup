from datetime import datetime, timezone, timedelta
# 設定為 +8 時區
tz = timezone(timedelta(hours=+8))
date = datetime.now(tz)
yes_date = datetime.now(tz)-timedelta(days=1) 
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
yes_y=str(yes_date.year)

if int(yes_date.month) < 10:
	yes_m = '0' + str(yes_date.month)
else:
	yes_m = str(yes_date.month)

if int(yes_date.day) < 10:
	yes_d = '0' + str(yes_date.day)
else:
	yes_d = str(yes_date.day)
tdy_date_str = y + m + d
ysdy_date_str = yes_y + yes_m + yes_d
BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d
print("tdy_date_str: ",tdy_date_str)
print("ysdy_date_str: ",ysdy_date_str)
print("BegMonthOfTodayPeriod: ",BegMonthOfTodayPeriod)





