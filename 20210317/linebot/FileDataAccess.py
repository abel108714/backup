#2020/10/28
class FileDataAccess:

    def __init__(self,key=1,FieldNum='None',SplitStr='None',FileName='None'):
        self.key = key
        if FieldNum=='None':
            self.FieldNum = 2
        else:
            self.FieldNum = FieldNum
        self.SplitStr = SplitStr
        self.FileName = FileName

    def setFileSource(self,key,FieldNum,SplitStr,FileName):
        self.key = key
        self.FieldNum = FieldNum
        self.SplitStr = SplitStr
        self.FileName = FileName

    def getDataRow(self,KeyStr):
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        for line in Lines: 
            # print("line: "+str(line)+" count: "+str(count))
            if line != "":
                if KeyStr == line.strip().split(self.SplitStr)[self.key]:
                    # print("line2: "+str(line.strip().split(self.SplitStr)[self.key]))
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
        # print("KeyStr: "+str(KeyStr))
        # print("DataArr: "+str(DataArr))
        #找KeyStr
        DataRow = self.getDataRow(KeyStr)
        # print("(DataRow): "+str(DataRow))
        if DataRow == None:
            self.addData(KeyStr,DataArr)
        else:
            #更新資料
            file1 = open(self.FileName, 'r') 
            Lines = file1.readlines() 
            count = 0
            NewLines = ''
            TempLine=''
            i=0
            line = ''  
            Lines=[line for line in Lines if line.strip() != ""]#去除空白行
            for line in Lines: #一列一列讀取
                # print("0.line: "+str(line))
                line=line.strip('\n')
                # print("0.line: "+str(line))
                # print("0.NewLines: "+str(NewLines))
                # print("0.count: "+str(count))
                # print("0.DataRow: "+str(DataRow))
                if count == DataRow:#需更新資料列
                    # print("if: "+str(NewLines))
                    for i in range(0,int(self.FieldNum)):
                        if i==self.key:#需更新資料列的key欄位
                            if i==0 and DataRow !=0:#如果是資料列開頭，不加self.SplitStr分隔符號
                                NewLines = NewLines + "\n" + line.strip().split(self.SplitStr)[i]
                            elif i==0 and DataRow ==0:#如果是資料列開頭，不加self.SplitStr分隔符號
                                NewLines = NewLines + line.strip().split(self.SplitStr)[i]
                            else:#如果不是資料列開頭，加self.SplitStr分隔符號
                                NewLines = NewLines + self.SplitStr + line.strip().split(self.SplitStr)[i]
                            # print("x.NewLines: "+str(NewLines))
                        else:#不需更新資料列的key欄位
                            TempLine=DataArr.pop(0)
                            if i==0:#如果是資料列開頭，不加self.SplitStr分隔符號
                                NewLines = NewLines + TempLine
                            else:#如果不是資料列開頭，加self.SplitStr分隔符號
                                NewLines=NewLines + self.SplitStr + TempLine
                            # print("y.NewLines: "+str(NewLines))
                else:#不需更新資料列
                    # print("else: "+str(NewLines))
                    if count == 0:
                        NewLines = NewLines + line
                    else:
                        NewLines = NewLines + "\n" + line
                # print("1.NewLines: "+str(NewLines))
                count+=1
            #寫入資料
            fp = open(self.FileName, "w")
            fp.writelines(NewLines)
            fp.close()

    def addData(self,KeyStr,DataArr):
        #更新資料
        file1 = open(self.FileName, 'r') 
        Lines = file1.readlines() 
        count = 0
        NewLines = ''
        UpdateLines = ''
        TempLine=''
        i=0
        line = ''
        times = 0

        #找KeyStr
        DataRow = self.getDataRow(KeyStr)

        for line in Lines:#一列一列讀取
            NewLines = NewLines + line.strip('\n') + "\n"

        NewLines = NewLines.rstrip('\n')#檔案結尾去除換行

        for i in range(0,int(self.FieldNum)):
            if i==0:#如果是資料列開頭，不加self.SplitStr分隔符號
                NewLines = NewLines + "\n" + KeyStr
            else:#如果不是資料列開頭，加self.SplitStr分隔符號
                TempLine=DataArr.pop(0)
                NewLines=NewLines + self.SplitStr + TempLine

        #寫入資料
        fp = open(self.FileName, "w")
        fp.writelines(NewLines)
        fp.close()
