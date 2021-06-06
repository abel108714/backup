

# def checkSubstring(s1,s2):
    
#     sc_len = len(s1)
#     s_len = len(s2)

#     if sc_len > s_len:
#         LongS=s1
#         ShortS=s2
#     elif sc_len < s_len:
#         LongS=s1
#         ShortS=s2

#     if ShortS in LongS:   # 使用in運算子檢查
#         print('字串中有'+ShortS)
#     else:
#         print('字串中沒有'+ShortS)



# s = '恩里克王子椒鹽蘇打餅(奇亞籽添'
# sc = '恩里克'
# if sc in s:   # 使用in運算子檢查
#     print('字串中有'+sc)
# else:
#     print('字串中沒有'+sc)


# checkSubstring('恩里克王子椒鹽蘇打餅(奇亞籽添','恩里克')


# test_list=list(str(["78","79","80"]))
# new_list=[]
# new_list=test_list
# print(new_list.pop(0))
# print(new_list.pop(0))
# print(new_list.pop(0))
# print(new_list.pop(0))
# print(new_list.pop(0))
# print(new_list.pop(0))
# # print(test_list.pop(0))
# # print(test_list.pop(0))

# def getData(list):
#     return list.pop(0)


# print(getData([78,79,80])+getData([78,79,80]))





import pymysql
#import charts
# 資料庫設定
db_settings = {
    "host": "127.21.7.39",
    "port": 3306,
    "user": "root",
    "password": "16264386",
    "db": "invdb",
    "charset": "utf8"
}


conn = pymysql.connect(**db_settings)
# 建立Cursor物件
with conn.cursor() as cursor:
    # sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
#     sql="insert into inv(product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)
# values('10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')"
#     sql="insert into inv(product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)
# values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
    data=(5,'網通',3,4)
    cursor.execute(sql,data)
    # 儲存變更
    conn.commit()
