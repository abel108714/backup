﻿import os

# def getUesrIndex(UesrName):
#     #file1 = open('data\\UserData.txt', 'r') 
#     file1 = open('S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt', 'r') 
#     Lines = file1.readlines() 
#     count = 0
#     for line in Lines: 
#         #print(UesrName)
#         #print(line.strip().split('-')[0])
#         #print(line.strip().split('-')[1])
#         if UesrName == line.strip().split(',')[1]:
#             return count
#         else:
#             count+=1
            
# def getUesrID(UesrName):
#     #file1 = open('data\\UserData.txt', 'r') 
#     file1 = open('S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt', 'r') 
#     Lines = file1.readlines() 
#     count = 0
#     index = getUesrIndex(UesrName)
#     for line in Lines: 
#         if count == index:
#             return line.strip().split(',')[0]
#         else:
#             count+=1

def getExpectedIndex(Company):
    Str=Company
    FileName=FileName
    SplitStr='-'
    StrDatakey=0
    getIndex(Str,FileName,SplitStr,StrDatakey)

#S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt
#def getExpectedDate(Company):



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


            #for line in Lines:
            #    line.strip().split(self.SplitStr)[Index]



        #if str(self.getData(KeyStr)) != str('None'):
            #d=0
            #陣列轉字串



            #for data in data_arr:
            #    data[d]
            #    d+=1
            #for line in Lines:
                #print(line.strip('\n')+'123')
                #print(Lines[count])
                #if key == 
                #count+=1            

            #lines = ['\n',key,self.SplitStr,data1,self.SplitStr,data2,'\n'] 
        # for line in Lines: 
        #     print(count)
        #     print(line.strip('\n')+'123')
        #     print(Lines[count])
        #     if key == 
        #     count+=1
            # if count == index:
            #     return line.strip().split(self.SplitStr)[index]
            # else:
            #     count+=1

            # if line == '\n':
                
            #     lines = ['\n',key,self.SplitStr,data1,self.SplitStr,data2,'\n'] 
            #     fp = open(self.FileName, "a")
            #     fp.write(lines)
            #     fp.close()
            #     break
            # else:
            #     lines = ['\n',key,self.SplitStr,data1,self.SplitStr,data2,'\n']
            #     fp = open(self.FileName, "a")
            #     fp.writelines(lines)
            #     fp.close()
            #     break


a=FileDataAccess(0,'-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')

#print(a.getIndex('東森'))
print('====================')
#print(a.getData(2,'東森'))
#['28','3,458,880']
b=['21','3,069,201']
print(a.setData('東森',b))
#print(a.getData(2,'博客來'))
#print(a.getData(1,'東森'))
#print(a.getData(1,'博客來'))
print('====================')
#print(a.getData('東西'))
#print(a.setData('東西','10/10','54,321'))
#la2=str(1,2,3)
#la=[1,2,3,4,5]
#print(str(la))
#la=list(la2)+['6','7','8']
#print(str(la))
import numpy as np
#陣列轉字串
arr_list = ['a', 'b', 'c', 'd']
arr_list = arr_list + ['1', '2', '3', '4']
arr = np.array(arr_list)
arr_str = ''.join(arr)
print(arr_str)


#print(getUesrIndex('立修'))
#print(getUesrIndex('陳'))
#print(getUesrID('立修'))
#print(getUesrID('陳'))
#print(getUesrIndex('博客來'))
#print(getUesrIndex('東森'))
#print(getUesrID('博客來'))
#print(getUesrID('東森'))


# class Student:
#     def __init__(self, id=1, name='george', sex='boy'):
#         self.id = id
#         self.name = name
#         self.sex = sex
#     def getID(self,id):
#         return self.id
#     def getName(self, id):
#         return self.name
#     def getSex(self, id):
#         return self.sex
#     def getObjAdd(self,id):
#         return self 
#'\\ADFS\Public\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt'
#網通部每月預入績效


# if __name__ == '__main__':
#     s = Student(1, 'Peter')
#     s2 = Student(2, 'kate', 'girl')
#     s3 = Student()
#     print(s.id, s.name, s.sex)
#     print(s2.id, s2.name, s2.sex)
#     print(s3.id, s3.name, s3.sex)
#     print(s3.getID(1))
#     print(s3.getName(1))
#     print(s3.getSex(1))
#     print(s3.getObjAdd(1))

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def who(self):
#         return self.name

# a = Animal("dog")
# print(a.who())

