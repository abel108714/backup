import os

# define the name of the directory to be created
path = "data"

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)

# 開啟檔案
fp = open("data\\welcome.txt", "a")#C:\\Users\udev77\Documents\
 
# 將 lines 所有內容寫入到檔案
lines = ["123", ",", "立修\n"]
fp.writelines(lines)
 
# 關閉檔案
fp.close()

