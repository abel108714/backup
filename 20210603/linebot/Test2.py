

def checkSubstring(s1,s2):
    
    sc_len = len(s1)
    s_len = len(s2)

    if sc_len > s_len:
        LongS=s1
        ShortS=s2
    elif sc_len < s_len:
        LongS=s1
        ShortS=s2

    if ShortS in LongS:   # 使用in運算子檢查
        print('字串中有'+ShortS)
    else:
        print('字串中沒有'+ShortS)



s = '恩里克王子椒鹽蘇打餅(奇亞籽添'
sc = '恩里克'
if sc in s:   # 使用in運算子檢查
    print('字串中有'+sc)
else:
    print('字串中沒有'+sc)


checkSubstring('恩里克王子椒鹽蘇打餅(奇亞籽添','恩里克')



