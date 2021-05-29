def getDictIndex(dict,key,data):
    i=0
    for i in range(len(dict)):
        if dict[key][i] == data:
            # del dict[key][i]
            return i

def appendDict(dict,key,data):
    dict[key]=dict[key] + [data]
    # print("Result: ", key, " ", dict[key])

def delDict(dict,key,data,index):
    for key, value in dict.items():
        DictIndex=getDictIndex(dict,key,dict[key][index])
        del dict[key][DictIndex]
        
    # print("Result: ", key, " ", dict[key])
    #del animal['cat']
    # for key, value in dict.items():



#品號	品名	庫存數量	補貨通知

# 建置空的 dictionary
dict = {}

#加入值為array的資料
dict['品號'] = ["10903004", "10903008"]
dict['品名'] = ["十穀米(1800g)", "天然冰湖野米十穀米600g"]
dict['庫存數量'] = ["74", "983"]
dict['補貨通知'] = ["", ""]

#印出剛剛加入的資料
print("dict['品號'] : ", dict['品號'])
print("dict['品名'] : ", dict['品名'])
print("dict['庫存數量'] : ", dict['庫存數量'])
print("dict['補貨通知'] : ", dict['補貨通知'])

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
print("只印出values部分")
for value in dict.values():
    print("Result:", value)

#印出 key, value pair
print("印出 key, value")
for key in dict.keys():
    print("Result: ", key, " ", dict[key])

#印出整個字典
print("印出整個字典")
print(dict.items())


appendDict(dict,'品號','11103035')
appendDict(dict,'品名','洛神桂花烏梅飲350ml(方形瓶)350ml/瓶')
appendDict(dict,'庫存數量','2040')
appendDict(dict,'補貨通知','')
# del dict['10903008']
# delDict(dict,'品號','10903008')
print(dict['品號'][1])
# del dict['品號'][1]
print("印出整個字典2")

print(dict['品號'][1])
print(delDict(dict,'品號',dict['品號'][1],1))
print(dict.items())
# for k in range(dict.items()):
#     print(dict[k][1])
# for key, value in dict.items():
#     print(f'{key}: {value}')
# for key, value in dict.items():
#     print(key)

