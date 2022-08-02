import jieba

seg_list = jieba.cut("山裡茶一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("洛神一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("菊花一箱贈洛神一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("條瓜一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("麵斤一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("素鬆一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("台中", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

jieba.suggest_freq('台中', True)

seg_list = jieba.cut("台中", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式



jieba.load_userdict(r'C:\auto\userDict.txt')
#print(jieba.lcut(text))

#jieba.set_dictionary('dict.txt.big.txt')    #詞庫
#jieba.load_userdict('user_dict.txt')        #自定義使用者字典

seg_list = jieba.cut("山裡茶一箱", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

#seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
#print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

#seg_list = jieba.cut("他来到了网易杭研大厦")
#print(", ".join(seg_list))

#seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
#print(", ".join(seg_list))
#jieba.suggest_freq('台中', True)

#check


list1 = ['qqaabb', 'wweerr', '121', 'qbcd', 'plqs']
data = [x for i,x in enumerate(list1) if x.find('qs') != -1]
print(data)     # 返回值为：['plqs']


list1 = ['紅茶', '山裡茶','醇釀醬油']#'純釀醬油'
data = [x for i,x in enumerate(list1) if x.find('純釀') != -1]
print(data)     # 返回值为：['plqs']


import difflib


list1 = ['紅茶', '山裡茶','醇釀醬油']
data = difflib.get_close_matches('純釀', list1, 1, cutoff=0.5)
print(data)     # 返回值为：['plqs']


#山裡茶一箱
#洛神一箱
#菊花一箱贈洛神一箱

#條瓜一箱
#麵筋一箱
#素鬆一箱