
class DictDB:

    def __init__(self):
        self.dict={}
        print("init")

    def setKey(self, Field):
        self.key = Field

    def getKey(self):
        return self.key

    def isKey(self, Field):
        # for value in self.__dict__.values():
        #     print("Result:", value)
        # i=0
        for key in self.__dict__.keys():
            print("Result: ", key, " ", self.__dict__[key])

        # for key, value in self.__dict__.items():
        #     print(self.key)
        #     # print(self.value)
        #     print(self.__dict__[key][i])
        #     i=i+1
        # print(self.__dict__[key][0])
        # print(self.__dict__[key][1])

        if Field == self.key:
            return True
        else:
            return False

    def getDictIndex(self, key, data):
        print("getDictIndex")
        print(self.__dict__.items())
        print("123")
        
        print("key = " + key)
        print("data = " + data)
        i=0
        print("len(self.__dict__) = " + str(len(self.__dict__)))
        for i in range(len(self.__dict__)):
            print("i = "+str(i))
            print(self.__dict__.items())
            print(str(self.__dict__['品號'][0]))
            print("self.__dict__[key][i] = "+str(self.__dict__[key][i]))
            print("data = "+str(data))
            if self.__dict__[key][i] == data:
                # del dict[key][i]
                return i

    def insertDict(self, key, dataArr):
        print("insertDict")
        # print("key = " + key)
        print(self.__dict__.items())
        # print(Field)
        # print(dataArr)
        # print(self.key)
        # if self.isKey(Field) == True:
        # print("0")
        for k, value in self.__dict__.items():
            # DictIndex=self.getDictIndex(self,key,self.dict[key][index])
            print("self.key = " + self.key)
            print("key = " + key)
            DictIndex=self.getDictIndex(self.key, key)
            print(self.__dict__.items())
            print("DictIndex = "+DictIndex)
            print(self.__dict__.items())
            self.__dict__[k][DictIndex] = dataArr.pop(0)
            print(self.__dict__[k][DictIndex] + "新增")
            # self.appendDict(self, dict, Field, data)
            # self.appendDict(self, dict, Field, data)
            # self.appendDict(self, dict, Field, data)
            # self.appendDict(self, dict, Field, data)

    # def appendDict(self, key, data):
    #     self.dict[key]=self.dict[key] + [data]
    #     # print("Result: ", key, " ", dict[key])

    # def delDict(self, key, data, index):
    #     for key, value in self.dict.items():
    #         DictIndex=self.getDictIndex(self,key,self.dict[key][index])
    #         print(self.dict[key][DictIndex] + "刪除")
    #         del self.dict[key][DictIndex]

# def getDict(dict,key,data,index):
#     for key, value in dict.items():
#         DictIndex=getDictIndex(dict,key,dict[key][index])
#         print(dict[key][DictIndex] + "刪除")
#         del dict[key][DictIndex]
        # return dict[key][DictIndex]

    # print("Result: ", key, " ", dict[key])
    #del animal['cat']
    # for key, value in dict.items():



#品號	品名	庫存數量	補貨通知

# 建置空的 dictionary
# dict = {}
newDictDB=DictDB()
newDictDB.setKey("品號")
print(newDictDB.getKey())
newDictDB.insertDict("10903004", ["十穀米(1800g)","74",""])


#加入值為array的資料
# dict['品號'] = ["10903004", "10903008"]
# dict['品名'] = ["十穀米(1800g)", "天然冰湖野米十穀米600g"]
# dict['庫存數量'] = ["74", "983"]
# dict['補貨通知'] = ["", ""]

# #印出剛剛加入的資料
# print("dict['品號'] : ", dict['品號'])
# print("dict['品名'] : ", dict['品名'])
# print("dict['庫存數量'] : ", dict['庫存數量'])
# print("dict['補貨通知'] : ", dict['補貨通知'])

#加入值為字串的資料
#11103035	洛神桂花烏梅飲350ml(方形瓶)350ml/瓶	2040
# dict['品號'] = dict['品號'] + ["11103035"]
# dict['品名'] = dict['品名'] + ["洛神桂花烏梅飲350ml(方形瓶)350ml/瓶"]
# dict['庫存數量'] = dict['庫存數量'] + ["2040"]
# dict['補貨通知'] = dict['補貨通知'] + [""]
# append(dict,'品號','11103035')
# append(dict,'品名','洛神桂花烏梅飲350ml(方形瓶)350ml/瓶')
# append(dict,'庫存數量','2040')
# append(dict,'補貨通知','')

#印出所有 dictionary 內的資料
#只印出values部分
# print("只印出values部分")
# for value in dict.values():
#     print("Result:", value)

# #印出 key, value pair
# print("印出 key, value")
# for key in dict.keys():
#     print("Result: ", key, " ", dict[key])

# #印出整個字典
# print("印出整個字典")
# print(dict.items())


# appendDict(dict,'品號','11103035')
# appendDict(dict,'品名','洛神桂花烏梅飲350ml(方形瓶)350ml/瓶')
# appendDict(dict,'庫存數量','2040')
# appendDict(dict,'補貨通知','')
# # del dict['10903008']
# # delDict(dict,'品號','10903008')
# print(dict['品號'][1])
# # del dict['品號'][1]
# print("印出整個字典2")

# print(dict['品號'][1])
# print(dict.items())
# # print(delDict(dict,'品號',dict['品號'][1],1))
# print(delDict(dict,'品號','10903008',1))
# print(getDict(dict,'品號','10903008',1))
# print(dict.items())
# for k in range(dict.items()):
#     print(dict[k][1])
# for key, value in dict.items():
#     print(f'{key}: {value}')
# for key, value in dict.items():
#     print(key)

