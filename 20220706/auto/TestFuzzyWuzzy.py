from fuzzywuzzy import fuzz
from fuzzywuzzy import process




# print(process.extractOne("数据挖掘", title_list))
#return score(type int)
 #function1:get fuzzy compare score(item vs one data)
    
compareScore = fuzz.ratio('資料分析師','資料科學家')
print(compareScore)

#function2:get the matchest data from database
#return list (data,score)
comparelist = ['股票分析師','資料工程師','資料科學家']
compareWinner = process.extractOne('資料分析師',comparelist)
print(compareWinner)



