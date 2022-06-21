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

#seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
#print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

#seg_list = jieba.cut("他来到了网易杭研大厦")
#print(", ".join(seg_list))

#seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
#print(", ".join(seg_list))



#山裡茶一箱
#洛神一箱
#菊花一箱贈洛神一箱

#條瓜一箱
#麵筋一箱
#素鬆一箱