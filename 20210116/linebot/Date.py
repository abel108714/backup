#2020/11/18
import time as t
import datetime as dt
class Date:

    def __init__(self):
        self.microseconds=0
        self.milliseconds=0
        self.minutes=0
        self.hours=0
        self.days=0
        self.weeks=0
        # 設定為 +8 時區
        self.tz = dt.timezone(dt.timedelta(hours=+8))
        self.date = dt.datetime.now(self.tz)
        #獲取今天的日期
        self.Year=str(self.date.year)
        if int(self.date.month) < 10:
            self.Month = '0' + str(self.date.month)
        else:
            self.Month = str(self.date.month)
        if int(self.date.day) < 10:
            self.Day = '0' + str(self.date.day)
        else:
            self.Day = str(self.date.day)

    def getTimedelta(self,microseconds = None, milliseconds = None, minutes = None, hours = None, days = None, weeks = None):#取得時間間隔TimeInterval
        self.microseconds=microseconds
        self.milliseconds=milliseconds
        self.minutes=minutes
        self.hours=hours
        self.days=days
        self.weeks=weeks
        if microseconds == None:
            self.microseconds = 0
        if milliseconds == None:
            self.milliseconds = 0
        if minutes == None:
            self.minutes =0
        if hours == None:
            self.hours = 0
        if days == None:
            self.days = 0
        if weeks == None:
            self.weeks = 0
        return dt.timedelta(microseconds=self.microseconds,milliseconds=self.milliseconds,minutes=self.minutes,hours=self.hours,days=self.days,weeks=self.weeks)

    def getDay(self,microseconds = None, milliseconds = None, minutes = None, hours = None, days = None, weeks = None):#microseconds = None, milliseconds = None, minutes = None, hours = None, days = None, weeks = None):#取得日,可重載一個參數
        self.microseconds=microseconds
        self.milliseconds=milliseconds
        self.minutes=minutes
        self.hours=hours
        self.days=days
        self.weeks=weeks
        if microseconds == None and milliseconds == None and minutes == None and hours == None and days == None and weeks == None:#參數為空表無間隔
            return self.Day
        else:#參數不為空表有間隔
            self.new_date = self.date - self.getTimedelta(self.microseconds, self.milliseconds, self.minutes, self.hours, self.days, self.weeks)
            return self.new_date.day

    def getMonth(self,microseconds = None, milliseconds = None, minutes = None, hours = None, days = None, weeks = None):#取得月
        self.microseconds=microseconds
        self.milliseconds=milliseconds
        self.minutes=minutes
        self.hours=hours
        self.days=days
        self.weeks=weeks
        if microseconds == None and milliseconds == None and minutes == None and hours == None and days == None and weeks == None:#參數為空表無間隔
            return self.Month
        else:#參數不為空表有間隔
            self.new_date = self.date - self.getTimedelta(self.microseconds, self.milliseconds, self.minutes, self.hours, self.days, self.weeks)
            return self.new_date.month

    def getYear(self,microseconds = None, milliseconds = None, minutes = None, hours = None, days = None, weeks = None):#取得年
        self.microseconds=microseconds
        self.milliseconds=milliseconds
        self.minutes=minutes
        self.hours=hours
        self.days=days
        self.weeks=weeks
        if microseconds == None and milliseconds == None and minutes == None and hours == None and days == None and weeks == None:#參數為空表無間隔
            return self.Year
        else:#參數不為空表有間隔
            self.new_date = self.date - self.getTimedelta(self.microseconds, self.milliseconds, self.minutes, self.hours, self.days, self.weeks)
            return self.new_date.year

    def findSubString(self,Str,SubString):
        pos = Str.find(SubString)
        if pos > -1:
            return True
        else:
            return False

    def getDiffDate(self,StartDate,EndDate):
        StartDateArr = []
        EndDateArr = []
        if self.findSubString(StartDate,"/"):
            StartDateArr=StartDate.split("/")
        elif self.findSubString(StartDate,"-"):
            StartDateArr=StartDate.split("-")

        print(str(StartDateArr))
        print(str(StartDateArr[1]))
        print(str(StartDateArr[2]))
        startday = dt.date(int(StartDateArr[0]),int(StartDateArr[1]),int(StartDateArr[2]))
        print(startday)
        if self.findSubString(EndDate,"/"):
            EndDateArr=EndDate.split("/")
        elif self.findSubString(EndDate,"-"):
            EndDateArr=EndDate.split("-")
        other_day = dt.date(int(EndDateArr[0]),int(EndDateArr[1]),int(EndDateArr[2]))
        print(other_day)
        result = startday - other_day
        return result.days

#使用範例

# import Date as d

# a=d.Date()
# print(a.getDay())

# b=d.Date()
# b.getTimedelta(days=1,weeks =1)
# print(b.getDay())

# c=d.Date()
# print(c.getDay(days=1))
# print(c.getMonth(days=1))
# print(c.getYear(days=1))


# from Date import *

# a=Date()
# print(a.getDay())

# b=Date()
# b.getTimedelta(days=1,weeks =1)
# print(b.getDay())

# c=Date()
# print(c.getDay(days=1))
# print(c.getMonth(days=1))
# print(c.getYear(days=1))


