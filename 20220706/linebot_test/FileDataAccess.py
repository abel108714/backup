﻿#2020/10/28
class FileDataAccess:

    def __init__(self,key=1,SplitStr='None',FileName='None'):
        self.key = key
        self.SplitStr = SplitStr
        self.FileName = FileName

    def setFileSource(self,key,SplitStr,FileName):
        self.key = key
        self.SplitStr = SplitStr
        self.FileName = FileName

    def getDataRow(self,KeyStr):
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        for line in Lines: 
            if KeyStr == line.strip().split(self.SplitStr)[self.key]:
                return count
            else:
                count+=1

    def getData(self,Index,KeyStr):
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        DataRow = self.getDataRow(KeyStr)
        for line in Lines: 
            if count == DataRow:
                return line.strip().split(self.SplitStr)[Index]
            else:
                count+=1
                
    def setData(self,KeyStr,DataArr):
        #更新資料
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        NewLines = ''
        TempLine=''
        i=0
        #找KeyStr
        DataRow = self.getDataRow(KeyStr)
        for line in Lines: #一列一列讀取
            if count == DataRow:#需更新資料列
                for i in range(0,len(line.strip().split(self.SplitStr))):
                    if i==self.key:#需更新資料列的key欄位
                        if i==0:#如果是資料列開頭，不加self.SplitStr分隔符號
                            NewLines = NewLines + line.strip().split(self.SplitStr)[i]
                        else:#如果不是資料列開頭，加self.SplitStr分隔符號
                            NewLines = NewLines + self.SplitStr + line.strip().split(self.SplitStr)[i]
                    else:#不需更新資料列的key欄位
                        TempLine=DataArr.pop(0)
                        if i==0:#如果是資料列開頭，不加self.SplitStr分隔符號
                            NewLines = NewLines + TempLine
                        else:#如果不是資料列開頭，加self.SplitStr分隔符號
                            NewLines=NewLines + self.SplitStr + TempLine
            else:#不需更新資料列
                NewLines = NewLines + line
                count+=1
            i += 1
        #寫入資料
        fp = open(self.FileName, "w")
        fp.writelines(NewLines)
        fp.close()