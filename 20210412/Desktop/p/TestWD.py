from chinese_calendar import is_workday, is_holiday
from datetime import date
from datetime import timedelta
from calendar import monthrange
import Date as d
# from datetime import datetime, timezone, timedelta


# def is_work_day(y,m,d):
#     april_last = date(y,m,d)   # datetime.date
#     # if is_workday(april_last):
#     #     weekno = april_last.weekday()+1
#     #     if weekno>0 and weekno<6:
#     #         print(str(y)+"/"+str(m)+"/"+str(d)+" - "+str(weekno))
#     if is_holiday(april_last):
#         weekno = april_last.weekday()+1
#         if weekno>0 and weekno<6:
#             print(str(y)+"/"+str(m)+"/"+str(d)+" - "+str(weekno))
        
#     # print(is_workday(april_last))     # True
#     # print(is_holiday(april_last))     # False
#     # print(april_last.weekday()+1)       # 5-星期六


# # 当前日期N天前的证券交易日
# def get_trade_day(n):
#     dt = date.today()
#     trade_day = '20201016'
#     if n < 0:
#         t = -n
#     else:
#         t = n
#     for i in range(100):
#         if n<0:
#             delta_day = timedelta(days=-i)
#         else:
#             delta_day = timedelta(days=i)
#         trade_day = dt-delta_day
#         if is_workday(trade_day) and trade_day.weekday()<5:       # 工作日并且不是周末
#             if t ==0:
#                 break
#             t = t -1
#     print(trade_day.strftime('%Y%m%d'))
#     return trade_day.strftime('%Y%m%d')


# if __name__ == '__main__':
#     i = 0
#     j=0
#     # for i in range(12):
#     #     print(monthrange(2021,i+1)[1])
#     for i in range(12):
#         # print("2021/"+str(i+1)+"/"+str(monthrange(2021,i+1)[1]))
#         # print("i = "+str(i)+", j = "+str(j))
#         # print(monthrange(2021,i+1)[1])
#         j_max= monthrange(2021,i+1)[1]
#         # print(j_max)
#         for j in range(1, j_max):
#             # print("2021/"+str(i+1)+"/"+str(j+1))
#             is_work_day(2021,int(str(i+1)),int(str(j+1)))
        # print(monthrange(2021,i+1)[1])
    # a=d.Date()
    # print(a.getDay())
    # is_work_day(2021,2,i)
    # get_trade_day(-2)# import datetime

# # 判断 2018年4月30号 是不是节假日
# from chinese_calendar import is_workday, is_holiday
# april_last = datetime.date(2018, 4, 30)
# print(is_workday(april_last))
# print(is_holiday(april_last))

# # 或者在判断的同时，获取节日名
# import chinese_calendar as calendar  # 也可以这样 import
# on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
# print(on_holiday)
# print(calendar.Holiday.labour_day.value, holiday_name)

# # 还能判断法定节假日是不是调休
# import chinese_calendar
# print(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 1)))
# print(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 2)))

# from calendar import monthrange
# # monthrange(2018,9)
# i = 0
# for i in range(12):
# 	print(monthrange(2021,i+1)[1])

# import calendar
# #set firstweekday=0
# cal= calendar.Calendar(firstweekday=5)
# for x in cal.iterweekdays():
# 	print(x)

# c=d.Date()
# print(c.getDay())
# print(c.getMonth())
# print(c.getYear())
# d_str = c.getYear() + "/"+c.getMonth()+ "/"+ c.getYear()
# d_str = "2/10"
# s=["1/1","2/10","2/11","2/12","2/15","2/16","3/1","4/2","4/5","4/30","6/14","9/20","9/21","10/11","12/31"]
# for s_str in s:
#     print(s_str)
#     if d_str ==s_str:
#         print("ok")
def isworkday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    # d_str="2/10"
    s=["2/20","9/11"]
    for s_str in s:
        print(d_str)
        print(s_str)
        if d_str ==s_str:
            print("isworkday")
            return True
    return False
def isHoliday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    # d_str="2/10"
    s=["01/01","2/10","2/11","2/12","2/15","2/16","3/1","4/2","4/5","4/30","6/14","9/20","9/21","10/11","12/31"]
    for s_str in s:
        print(d_str)
        print(s_str)
        if d_str ==s_str:
            print("isHoliday")
            return True
    return False

print(isHoliday())
print(isworkday())
# print(!(isHoliday()))
# print(!(isworkday()))