
class Date:

    def __init__(self,key=1,SplitStr='None',FileName='None'):
        self.key = key
        self.SplitStr = SplitStr
        self.FileName = FileName

    def setFileSource(self,key,SplitStr,FileName):
        self.key = key
        self.SplitStr = SplitStr
        self.FileName = FileName

    def getDataRow(self,KeyStr):
        # 設定為 +8 時區
        tz = timezone(timedelta(hours=+8))
        date = datetime.now(tz)
        y=str(date.year)
        if int(date.month) < 10:
            m = '0' + str(date.month)
        else:
            m = str(date.month)
        #獲取今天的日期
        if int(date.day) < 10:
            d = '0' + str(date.day)
        else:
            d = str(date.day)
        #獲取昨天的日期
        if int(date.day-1) < 10:
            yes_d = '0' + str(date.day-1)
        else:
            yes_d = str(date.day-1)
        tdy_date_str = y + m + d
        ysdy_date_str = y + m + yes_d

        BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d