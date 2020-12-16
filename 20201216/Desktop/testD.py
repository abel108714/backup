import time
import datetime
#今天日期 (2006-11-18)
today = datetime.date.today()
print ("今天日期 =>" + str(today))
#設定要相減的日期
other_day = datetime.date(2021,9,16)
result = today - other_day
print (result)
#如果只想要把相差的天數拿出來的話
print ("只要看天數 =>" + str(result.days))

path = 'C:\\Users\\udev77\\Documents\\InventoryReminder.txt'
f = open(path, 'r')
lines = f.readlines()
#line=[]
i = 0
for line in lines:
    print(line)
    print(i)
    i=i+1
f.close()
# print(lines)