import re

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

def addPerSignToSpacing(string):
    StringArr=string.split(' ')
    NewStr=""
    for i in range(len(StringArr)):
        NewStr = NewStr + "%" + str(StringArr[i])
    NewStr = NewStr + "%"
    return NewStr


import pymysql

# print(getData([78,79,80])+getData([78,79,80]))

def isSubstringExist(substr,string):
    pos = string.find(substr)
    if pos >= 0:   # 有找到
        #print('位置：' + str(pos))
        return pos
    else:   # 沒有找到
        #print('找不到')
        return -1
      
def isQuotationMarksExist(string):
    pos=isSubstringExist('\'',string)
    return pos

def checkString(string):
    pos=isQuotationMarksExist(string)
    if pos!= -1:
        split_strings = string.split("\'")
        return split_strings[pos-1]+"\\\'"+split_strings[pos]
    else:
        return string

import datetime

from xlwings.utils import exception
def convertDateFormat(DateStr,OldFormat,NewFormat):
    print("DateStr : "+str(DateStr))
    print("OldFormat : "+str(OldFormat))
    print("NewFormat : "+str(NewFormat))
    try:
        print("NewFormat : "+str(datetime.datetime.strptime(DateStr, OldFormat).strftime(NewFormat)))
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
        if days_of_arrival is None:
            days_of_arrival=0
        print("product_name : "+checkString(str(product_name)))

        if days_after_manu is None:
            days_after_manu=0

        if avg_mthly_sales is None:
            avg_mthly_sales=0

        if days_sold_out is None:
            days_sold_out=0

        try:
            sql="insert inv(id,product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)values('"+str(id)+"','"+str(product_id)+"','"+checkString(str(product_name))+"','"+str(packing)+"','"+str(inv_qty)+"','"+str(packing_qty)+"','"+str(exp)+"','"+str(avg_mthly_sales)+"','"+str(avg_daily_sales)+"','"+str(days_sold_out)+"','"+str(days_of_arrival)+"','"+str(rep_notice)+"','"+str(mfd)+"','"+str(days_after_manu)+"','"+str(six_mos_warning)+"','"+str(three_mos_warning)+"')"

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
                    # print(days_of_arrival)
            print("insertData")
            print("sql : "+str(sql))
            cursor.execute(sql)#,data)
        except Exception as e:
            print(e)
            print(exp)
            seq=int(getDataSeq(product_id,exp))+int(1)
            id=id[:len(str(id))-1]+str(seq)

            # str = '211030150000000001'
            # print(len(str))
            # print(str[-1:])  # 輸出字串右邊1位
            # print(str)
            # print(str[:17])  # 輸出字串左邊17位
            # str = '211030150000000001'
            # print(len(seq))
            # print(seq[:len(seq)])

            

            # id=seq[:len(str(seq))]+str(seq)
            print("seq:"+str(seq))
            print("id:"+str(id))
            sql="insert inv(id,product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning,seq)values('"+str(id)+"','"+str(product_id)+"','"+checkString(str(product_name))+"','"+str(packing)+"','"+str(inv_qty)+"','"+str(packing_qty)+"','"+str(exp)+"','"+str(avg_mthly_sales)+"','"+str(avg_daily_sales)+"','"+str(days_sold_out)+"','"+str(days_of_arrival)+"','"+str(rep_notice)+"','"+str(mfd)+"','"+str(days_after_manu)+"','"+str(six_mos_warning)+"','"+str(three_mos_warning)+"','"+str(seq)+"')"
            print("insertData e")
            print("sql:"+str(sql))
            cursor.execute(sql)#,data)
        # 儲存變更
        conn.commit()

# def updateData(product_id, product_name=None, packing=None, inv_qty=None, packing_qty=None, exp=None, avg_mthly_sales=None, avg_daily_sales=None, days_sold_out=None, days_of_arrival=None, rep_notice=None, mfd=None, days_after_manu=None, six_mos_warning=None, three_mos_warning=None):
#     print(product_name)
#     conn = pymysql.connect(**setDB())
#     # 建立Cursor物件
#     # seq=getDataSeq(product_id,exp)
    
#     with conn.cursor() as cursor:
#         sql="update inv set id=%s,product_id=%s, product_name=%s, packing=%s, inv_qty=%s, packing_qty=%s, exp=%s, avg_mthly_sales=%s, avg_daily_sales=%s, days_sold_out=%s, days_of_arrival=%s, rep_notice=%s, mfd=%s, days_after_manu=%s, six_mos_warning=%s, three_mos_warning=%s where id=%s"
# #         sql="update inv set product_id='%d',product_name='',packing='',inv_qty='',packing_qty='',exp='',avg_mthly_sales='',avg_daily_sales='',days_sold_out='',days_of_arrival='',rep_notice='',mfd='',days_after_manu='',six_mos_warning='',three_mos_warning=''
# # where 條件式 (例如 sn='5' 或 name='塔司尼' )
#         print(sql)
#         data=(id, product_id, product_name, packing, inv_qty, packing_qty, exp, avg_mthly_sales, avg_daily_sales, days_sold_out, days_of_arrival, rep_notice, mfd, days_after_manu, six_mos_warning, three_mos_warning)
#         cursor.execute(sql,data)
#         # 儲存變更
#         conn.commit()
def splitAllCharWithPct(string):
    # 寫出正則表示式 任意2個字元
    pattern = re.compile('.{1}')
    # findall是找到所有的字元,再在字元中新增空格，當然你想新增其他東西當然也可以
    return '%'.join(pattern.findall(string))

def getDataArr(product_msg):
    print("7777")
    conn = pymysql.connect(**setDB())
    if product_msg.isdigit() == True:
        with conn.cursor() as cursor:
            # sql="select product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 from inv where product_id='"+str(product_msg)+"'"
            #sql="select product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 from inv where product_id='"+str(product_msg)+"'"+"and STR_TO_DATE(exp, '%Y-%m-%d') IS NOT NULL ORDER BY DATE_FORMAT(exp, '%Y-/%m-/%d') ASC limit 1"
            sql="select product_id as 品號, product_name as 品名, spec as 規格, factory_code as 廠別代號, factory_name as 廠別名稱, inv_qty as 庫存數量, unit as 單位, small_unit as 小單位, storage_spaces as 儲位, quantity_at_the_beginning_of_the_month as 月初數量, the_most_recent_storage_date as 月初數量, the_most_recent_out_of_the_warehouse as 最近出庫日, st_count_date as 上次盤點日, safety_stock as 安全存量, replenishment_point as 補貨點, economic_batch as 經濟批量, standard_inventory as 標準存貨量, standard_turnover_rate as 標準週轉率, inventory_packaging_quantity as 庫存包裝數量, package_quantity_at_the_beginning_of_the_month as 月初包裝數量 from inv01002 where product_id='"+str(product_msg)+"'"+"and STR_TO_DATE(exp, '%Y-%m-%d') IS NOT NULL ORDER BY DATE_FORMAT(exp, '%Y-/%m-/%d') ASC limit 1"
            print(sql)
            cursor.execute(sql)
            myresult = cursor.fetchall()
            # print(myresult)
            conn.commit()
            cursor.close()
            # data=[]
            # i=0
            # for x in myresult:
                
            #     data[i]=x
            #     # print("data="+str(data))
            #     i=i+1

            return myresult
    elif product_msg.isdigit() == False:
        product_msg=addPerSignToSpacing(product_msg)
        product_msg=splitAllCharWithPct(product_msg)
        with conn.cursor() as cursor:
            # sql="select product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 from inv where product_name like '%"+str(product_msg)+"%'"
            # sql="select product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 from inv where product_name like '%"+str(product_msg)+"%'"+"and STR_TO_DATE(exp, '%Y-%m-%d') IS NOT NULL ORDER BY DATE_FORMAT(exp, '%Y-/%m-/%d') ASC limit 1"
            sql="SELECT product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 FROM inv WHERE product_name like '%"+str(product_msg)+"%'"+"and STR_TO_DATE(exp, '%Y-%m-%d') IS NOT NULL GROUP BY product_id, product_name ORDER BY DATE_FORMAT(exp, '%Y-%m-%d') ASC"
            print(sql)
            cursor.execute(sql)
            myresult = cursor.fetchall()
            # print(myresult)
            conn.commit()
            cursor.close()
            # data=[]
            # i=0
            # for x in myresult:
                
            #     data[i]=x
            #     # print("data="+str(data))
            #     i=i+1

            return myresult        


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

# import Date as d

# a=d.Date()
# # a.isDate('2017-12-31')
# DataArr=getDataArr('21103001')
# i=0
# print("品號 : "+str(DataArr[i][0]))
# print("品名 : "+str(DataArr[i][1]))
# print("包裝方式 : "+str(DataArr[i][2]))
# for i in range(len(DataArr)):
#     # print("i = "+str(i))
#     # print("品號 : "+str(DataArr[i][0]))
#     # print("品名 : "+str(DataArr[i][1]))
    
#     if a.isDate(str(DataArr[i][5])):
#         print("----------------------")
#         print("庫存數量 : "+str(DataArr[i][3]))
#         print("包裝數量 : "+str(DataArr[i][4]))
#         print("有效期限 : "+str(DataArr[i][5]))
# print("----------------------")
# import Date as d

# a=d.Date()
# print(a.getDay())
# print(a.isDate('2017-12-31'))
# print(a.isDate('2017/12/31'))
# a.setDateFormat('%Y/%m/%d')
# print(a.isDate('2017/12/31'))



# import pymysql
# #import charts

# import xlwings as xw
# app = xw.App(visible=False)

# #讀取excel檔
# path="S:\開放公用區\★每日更新庫存水位警示表★\★庫存水位-唯讀參閱不可修改★.xlsm"
# wb = xw.Book(path)

# ws=wb.sheets[0]
# # ws.range('a:a').value
# print("------")
# # print(ws.used_range.shape)

# # ur = ws.used_range
# # r = ur.row + ur.rows.count - 1
# # c = ur.column + ur.columns.count - 1
# # print(ur)
# # print(r)
# # print(c)
# used_ranges = ws.api.UsedRange
# max_row = used_ranges.Rows.Count - used_ranges.Row + 1
# max_col = used_ranges.Columns.Count - used_ranges.Column + 1

# print(max_row)
# print(max_col)


# # print(ws.range('2:2').value)
# print("------")
# # a = ws.range(str('2')+':'+str('2')).value
# # print(a)
# print("j")
# for j in range(2,max_row+1):
#     print(j)
#     # if j==4:
#     #     break
#     # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
#     RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]

#     # print(RowData[2])
#     # print(RowData[8])
#     DateRowData=str(RowData[9])
#     print("---------------------------------------"+str(RowData[9]))#
#     ExpDateStr = DateRowData.split(' 00:00:00')[0]
#     print("---------------------------------------"+str(RowData[9]))#
#     RowData[9]=ExpDateStr
#     print("---------------------------------------"+str(RowData[9]))#
#     DateRowData=str(RowData[19])
#     MfdDateStr = DateRowData.split(' 00:00:00')[0]
#     RowData[19]=MfdDateStr
#     print("---------------------------------------")#
#     print(" : "+str(RowData[1]))#
#     print(" : "+str(RowData[2]))#
#     RowData[3]=round(RowData[3])
#     print("product_id : "+str(RowData[3]))#product_id
#     print("product_name : "+str(RowData[4]))#product_name
#     isSubstringExist('\'',RowData[4])
#     split_strings = RowData[4].split("\'")
#     print(split_strings)
#     print("packing : "+str(RowData[5]))#packing
#     RowData[6]=round(RowData[6])
#     print("inv_qty : "+str(RowData[6]))#inv_qty
#     # RowData[7]=round(RowData[7])
#     print("packing_qty : "+str(RowData[7]))#packing_qty,
#     print(" : "+str(RowData[8]))#
#     print("exp : "+str(RowData[9]))#exp,
#     print(" : "+str(RowData[10]))#
#     print(" : "+str(RowData[11]))#,
#     print(" : "+str(RowData[12]))#,
#     print(" : "+str(RowData[13]))#,
#     if not RowData[14] is None:
#         RowData[14]=round(RowData[14])
#     print("avg_mthly_sales : "+str(RowData[14]))#avg_mthly_sales,
#     RowData[15]=round(RowData[15])
#     print("avg_daily_sales : "+str(RowData[15]))#avg_mthly_sales,
#     if not RowData[16] is None:
#         RowData[16]=round(RowData[16])
#     print("days_sold_out : "+str(RowData[16]))#avg_daily_sales
#     # print("days_of_arrival : "+str(RowData[17]))#days_sold_out
#     if j==6:
#         print("days_of_arrival : "+str(RowData[17]))
#         # break
#     # if RowData[17] is None:#!=str("None"):# or RowData[17]!="":
#     #     RowData[17]=RowData[17]
#     # else:
#     #     RowData[17]=round(RowData[17])
#     if not RowData[17] is None:#!=str("None"):# or RowData[17]!="":
#         RowData[17]=round(RowData[17])
#     print("days_of_arrival : "+str(RowData[17]))#days_sold_out
#     # RowData[18]=round(RowData[18])
#     print("rep_notice : "+str(RowData[18]))#days_of_arrival
#     # RowData[19]=round(RowData[19])
#     print("mfd : "+str(RowData[19]))#rep_notice
#     if not RowData[20] is None:
#         RowData[20]=round(RowData[20])
#     print("days_after_manu : "+str(RowData[20]))
#     # RowData[21]=round(RowData[21])
#     print("six_mos_warning : "+str(RowData[21]))
#     # RowData[22]=round(RowData[22])
#     print("three_mos_warning : "+str(RowData[22]))
#     id=str(round(RowData[3]))+str(convertDateFormat(RowData[9],"%Y-%m-%d","%Y%m%d"))+str(getDataSeq(round(RowData[3]),RowData[9]))
#     print("======================================>id : "+ str(id))
#     print(str(id),str(RowData[3]),str(RowData[4]),str(RowData[5]),str(RowData[6]),str(RowData[7]),str(RowData[9]),str(RowData[14]),str(RowData[15]),str(RowData[16]),str(RowData[17]),str(RowData[18]),str(RowData[19]),str(RowData[20]),str(RowData[21]),str(RowData[22]))
#     # insertData(str(id),str(RowData[3]),str(RowData[4]),str(RowData[5]),str(RowData[6]),str(RowData[7]),str(RowData[9]),str(RowData[14]),str(RowData[15]),str(RowData[16]),str(RowData[17]),str(RowData[18]),str(RowData[19]),str(RowData[20]),str(RowData[21]),str(RowData[22]))
#     # for i in range(3,len(RowData)):
#     #     checkString(RowData)
#     insertData(id,RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[9],RowData[14],RowData[15],RowData[16],RowData[17],RowData[18],RowData[19],RowData[20],RowData[21],RowData[22])
#     # insertData(id,RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[9],RowData[14],RowData[15],RowData[16],RowData[17],RowData[18],RowData[19],RowData[20],RowData[21],RowData[22])
# # 2024-03-02 exp,
# # 997.0 剩餘有效天數
# # 4800.0 下單批量
# # 692.0 迴轉率

# # 23.0 迴轉天數

# # 208.17 每月均銷量 avg_mthly_sales,

# # 7.0 每日均銷量 avg_daily_sales,

# # 230.0 預估幾日售完 days_sold_out,

# # 30.0 到貨天數 days_of_arrival,

# # None 補貨通知 rep_notice,

# # 2021-03-03
    
#     # product_id=RowData[3]
#     # print(RowData)
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # print(RowData.pop(0))
#     # insertData(id,\
#     #         product_id,\
#     #         product_name,\
#     #         packing,\
#     #         inv_qty,\
#     #         packing_qty,\
#     #         exp,\
#     #         avg_mthly_sales,\
#     #         avg_daily_sales,\
#     #         days_sold_out,\
#     #         days_of_arrival,\
#     #         rep_notice,\
#     #         mfd,days_after_manu,\
#     #         six_mos_warning,\
#     #         three_mos_warning\
#     #         )
#     # print(id)
    
# # print(getDataSeq('10903008','2022/5/12'))

# # for i in range(2,r+1):
# #     print(i)
# #     a = ws.range(str(i)+':'+str(i)).value
# #     print(a)
#     # try:
#     #     if str(round(ws.range(i, 4).value)) == str(data):
#     #         # print("i="+str(i))
#     #         # print(str(round(ws.range(i, 7).value)))
#     #         print("1")
#     #         # sum=sum+int(round(ws.range(i, 7).value))
#     #         exp_data=str(ws.range(i, 10).value)
#     #         exp = exp_data.split(' 00:00:00')[0]
#     #         # time.strftime("%Y-%m-%d", time.localtime())
#     #         print("2")
#     #         print("exp="+str(exp))
#     #         print("3")
#     #         exp_list.append(exp)
#     #         print("4")
#     #         print("exp_list="+str(exp_list))
#     #         print("5")
#     # except Exception as e:
#     #     print(e)
#     #     # print("無資料")
            


# wb.close()
# app.quit()


# # id='1090300820220512'
# # product_id='10903008'

# # db_settings={}







# # try:
# #     insertData('10903008202205120','10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')
# #     print("已新增資料")
# # except Exception as e:
# #     print(e)
# #     print("已有資料")
#     # delData(id)
#     # print("已刪除資料")

# # try:
# #     updateData(id,product_id,'123')
# #     print("已更新資料")
# # except Exception as e:
# #     print(e)

# # try:
# #     delData(id)
# #     print("已刪除資料")
# # except Exception as e:
# #     print(e)
    
# # product_name='123456'
# # updateData(id,product_id,product_name)