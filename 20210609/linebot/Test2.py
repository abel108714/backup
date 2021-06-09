

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



import datetime
def convertDateFormat(DateStr,OldFormat,NewFormat):
    try:
        return datetime.datetime.strptime(DateStr, OldFormat).strftime(NewFormat)
    except:
        return "00000000"
	

def setDB():
    # 資料庫設定
    db_settings = {
        "host": "127.21.7.39",
        "port": 3306,
        "user": "root",
        "password": "16264386",
        "db": "invdb",
        "charset": "utf8"
    }
    return db_settings

def insertData(id,product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning):
            # product_id,\
            # product_name,\
            # packing,\
            # inv_qty,\
            # packing_qty,\
            # exp,\
            # avg_mthly_sales,\
            # avg_daily_sales,\
            # days_sold_out,\
            # days_of_arrival,\
            # rep_notice,\
            # mfd,days_after_manu,\
            # six_mos_warning,\
            # three_mos_warning\
            # ):
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # sql="INSERT INTO inv(id,product_id) VALUES(%s,%s)"
        # sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
    #     sql="insert into inv(product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)
    # values('10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')"
        sql="insert inv(id,product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)values('"+str(id)+"','"+str(product_id)+"','"+str(product_name)+"','"+str(packing)+"','"+str(inv_qty)+"','"+str(packing_qty)+"','"+str(exp)+"','"+str(avg_mthly_sales)+"','"+str(avg_daily_sales)+"','"+str(days_sold_out)+"','"+str(days_of_arrival)+"','"+str(rep_notice)+"','"+str(mfd,days_after_manu)+"','"+str(six_mos_warning)+"','"+str(three_mos_warning)+"')"

            # id,\
            # product_id,\
            # product_name,\
            # packing,\
            # inv_qty,\
            # packing_qty,\
            # exp,\
            # avg_mthly_sales,\
            # avg_daily_sales,\
            # days_sold_out,\
            # days_of_arrival,\
            # rep_notice,\
            # mfd,days_after_manu,\
            # six_mos_warning,\
            # three_mos_warning\
            # )\


            # str(id)+"','"+\
            # str(product_id)+"','"+\
            # str(product_name)+"','"+\
            # str(packing)+"','"+\
            # str(inv_qty)+"','"+\
            # str(packing_qty)+"','"+\
            # str(exp)+"','"+\
            # str(avg_mthly_sales)+"','"+\
            # str(avg_daily_sales)+"','"+\
            # str(days_sold_out)+"','"+\
            # str(days_of_arrival)+"','"+\
            # str(rep_notice)+"','"+\
            # str(mfd,days_after_manu)+"','"+\
            # str(six_mos_warning)+"','"+\
            # str(three_mos_warning)+"')"
            # values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # data=(id,\
        #     product_id,\
        #     product_name,\
        #     packing,\
        #     inv_qty,\
        #     packing_qty,\
        #     exp,\
        #     avg_mthly_sales,\
        #     avg_daily_sales,\
        #     days_sold_out,\
        #     days_of_arrival,\
        #     rep_notice,\
        #     mfd,days_after_manu,\
        #     six_mos_warning,\
        #     three_mos_warning\
        #     )
        print("sql : "+str(sql))
        cursor.execute(sql)#,data)
        # 儲存變更
        conn.commit()

def updateData(product_id, product_name=None, packing=None, inv_qty=None, packing_qty=None, exp=None, avg_mthly_sales=None, avg_daily_sales=None, days_sold_out=None, days_of_arrival=None, rep_notice=None, mfd=None, days_after_manu=None, six_mos_warning=None, three_mos_warning=None):
    print(product_name)
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    # seq=getDataSeq(product_id,exp)
    
    with conn.cursor() as cursor:
        sql="update inv set id=%s,product_id=%s, product_name=%s, packing=%s, inv_qty=%s, packing_qty=%s, exp=%s, avg_mthly_sales=%s, avg_daily_sales=%s, days_sold_out=%s, days_of_arrival=%s, rep_notice=%s, mfd=%s, days_after_manu=%s, six_mos_warning=%s, three_mos_warning=%s where id=%s"
#         sql="update inv set product_id='%d',product_name='',packing='',inv_qty='',packing_qty='',exp='',avg_mthly_sales='',avg_daily_sales='',days_sold_out='',days_of_arrival='',rep_notice='',mfd='',days_after_manu='',six_mos_warning='',three_mos_warning=''
# where 條件式 (例如 sn='5' 或 name='塔司尼' )
        print(sql)
        data=(id, product_id, product_name, packing, inv_qty, packing_qty, exp, avg_mthly_sales, avg_daily_sales, days_sold_out, days_of_arrival, rep_notice, mfd, days_after_manu, six_mos_warning, three_mos_warning)
        cursor.execute(sql,data)
        # 儲存變更
        conn.commit()

def getDataSeq(product_id,exp):
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        sql="select seq from inv where product_id='"+str(product_id)+"' and exp='"+str(exp)+"'"
        print(sql)
        # data=(product_id,exp)
        # cursor.execute(sql,data)

        # # 儲存變更
        # conn.commit()
        # myresult = cursor.fetchall()
        # print(myresult)

        cursor.execute(sql)
        myresult = cursor.fetchall()
        print(myresult)
        conn.commit()
        cursor.close()
        data=0
        for x in myresult:
            data=x[0]
            print("data="+str(data))

        return data



def delData(id):

    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql="delete from inv where id=%s"
        data=(id)
        cursor.execute(sql,data)
        # 儲存變更
        conn.commit()


import pymysql
#import charts

import xlwings as xw
app = xw.App(visible=False)

#讀取excel檔
path="S:\開放公用區\★每日更新庫存水位警示表★\★庫存水位-唯讀參閱不可修改★.xlsm"
wb = xw.Book(path)

ws=wb.sheets[0]
# ws.range('a:a').value
print("------")
# print(ws.used_range.shape)

# ur = ws.used_range
# r = ur.row + ur.rows.count - 1
# c = ur.column + ur.columns.count - 1
# print(ur)
# print(r)
# print(c)
used_ranges = ws.api.UsedRange
max_row = used_ranges.Rows.Count - used_ranges.Row + 1
max_col = used_ranges.Columns.Count - used_ranges.Column + 1

print(max_row)
print(max_col)


# print(ws.range('2:2').value)
print("------")
# a = ws.range(str('2')+':'+str('2')).value
# print(a)
print("j")
for j in range(2,max_row+1):
    print(j)
    # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
    RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]

    # print(RowData[2])
    # print(RowData[8])
    DateRowData=str(RowData[9])
    DateStr = DateRowData.split(' 00:00:00')[0]
    RowData[9]=DateStr
    DateRowData=str(RowData[19])
    DateStr = DateRowData.split(' 00:00:00')[0]
    RowData[19]=DateStr
    print("---------------------------------------")#
    print(" : "+str(RowData[1]))#
    print(" : "+str(RowData[2]))#
    RowData[3]=round(RowData[3])
    print("product_id : "+str(RowData[3]))#product_id
    print("product_name : "+str(RowData[4]))#product_name
    print("packing : "+str(RowData[5]))#packing
    RowData[6]=round(RowData[6])
    print("inv_qty : "+str(RowData[6]))#inv_qty
    # RowData[7]=round(RowData[7])
    print("packing_qty : "+str(RowData[7]))#packing_qty,
    print(" : "+str(RowData[8]))#
    print("exp : "+str(RowData[9]))#exp,
    print(" : "+str(RowData[10]))#
    print(" : "+str(RowData[11]))#,
    print(" : "+str(RowData[12]))#,
    print(" : "+str(RowData[13]))#,
    RowData[14]=round(RowData[14])
    print("avg_mthly_sales : "+str(RowData[14]))#avg_mthly_sales,
    RowData[15]=round(RowData[15])
    print("avg_daily_sales : "+str(RowData[15]))#avg_mthly_sales,
    RowData[16]=round(RowData[16])
    print("days_sold_out : "+str(RowData[16]))#avg_daily_sales
    RowData[17]=round(RowData[17])
    print("days_of_arrival : "+str(RowData[17]))#days_sold_out
    # RowData[18]=round(RowData[18])
    print("rep_notice : "+str(RowData[18]))#days_of_arrival
    # RowData[19]=round(RowData[19])
    print("mfd : "+str(RowData[19]))#rep_notice
    RowData[20]=round(RowData[20])
    print("days_after_manu : "+str(RowData[20]))
    # RowData[21]=round(RowData[21])
    print("six_mos_warning : "+str(RowData[21]))
    # RowData[22]=round(RowData[22])
    print("three_mos_warning : "+str(RowData[22]))
    id=str(round(RowData[3]))+str(convertDateFormat(DateStr,"%Y-%m-%d","%Y%m%d"))+str(getDataSeq(round(RowData[3]),RowData[9]))
    print(str(id),str(RowData[3]),str(RowData[4]),str(RowData[5]),str(RowData[6]),str(RowData[7]),str(RowData[9]),str(RowData[14]),str(RowData[15]),str(RowData[16]),str(RowData[17]),str(RowData[18]),str(RowData[19]),str(RowData[20]),str(RowData[21]),str(RowData[22]))
    insertData(str(id),str(RowData[3]),str(RowData[4]),str(RowData[5]),str(RowData[6]),str(RowData[7]),str(RowData[9]),str(RowData[14]),str(RowData[15]),str(RowData[16]),str(RowData[17]),str(RowData[18]),str(RowData[19]),str(RowData[20]),str(RowData[21]),str(RowData[22]))
    # insertData(id,RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[9],RowData[14],RowData[15],RowData[16],RowData[17],RowData[18],RowData[19],RowData[20],RowData[21],RowData[22])
    
# 2024-03-02 exp,
# 997.0 剩餘有效天數
# 4800.0 下單批量
# 692.0 迴轉率

# 23.0 迴轉天數

# 208.17 每月均銷量 avg_mthly_sales,

# 7.0 每日均銷量 avg_daily_sales,

# 230.0 預估幾日售完 days_sold_out,

# 30.0 到貨天數 days_of_arrival,

# None 補貨通知 rep_notice,

# 2021-03-03
    
    # product_id=RowData[3]
    # print(RowData)
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # print(RowData.pop(0))
    # insertData(id,\
    #         product_id,\
    #         product_name,\
    #         packing,\
    #         inv_qty,\
    #         packing_qty,\
    #         exp,\
    #         avg_mthly_sales,\
    #         avg_daily_sales,\
    #         days_sold_out,\
    #         days_of_arrival,\
    #         rep_notice,\
    #         mfd,days_after_manu,\
    #         six_mos_warning,\
    #         three_mos_warning\
    #         )
    # print(id)
    
# print(getDataSeq('10903008','2022/5/12'))

# for i in range(2,r+1):
#     print(i)
#     a = ws.range(str(i)+':'+str(i)).value
#     print(a)
    # try:
    #     if str(round(ws.range(i, 4).value)) == str(data):
    #         # print("i="+str(i))
    #         # print(str(round(ws.range(i, 7).value)))
    #         print("1")
    #         # sum=sum+int(round(ws.range(i, 7).value))
    #         exp_data=str(ws.range(i, 10).value)
    #         exp = exp_data.split(' 00:00:00')[0]
    #         # time.strftime("%Y-%m-%d", time.localtime())
    #         print("2")
    #         print("exp="+str(exp))
    #         print("3")
    #         exp_list.append(exp)
    #         print("4")
    #         print("exp_list="+str(exp_list))
    #         print("5")
    # except Exception as e:
    #     print(e)
    #     # print("無資料")
            


wb.close()
app.quit()


id='1090300820220512'
product_id='10903008'

# db_settings={}







try:
    insertData('10903008202205120','10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')
    print("已新增資料")
except Exception as e:
    print(e)
    print("已有資料")
    # delData(id)
    # print("已刪除資料")

# try:
#     updateData(id,product_id,'123')
#     print("已更新資料")
# except Exception as e:
#     print(e)

# try:
#     delData(id)
#     print("已刪除資料")
# except Exception as e:
#     print(e)
    
# product_name='123456'
# updateData(id,product_id,product_name)