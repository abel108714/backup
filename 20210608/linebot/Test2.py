

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

def insertData(id,\
            product_id,\
            product_name,\
            packing,\
            inv_qty,\
            packing_qty,\
            exp,\
            avg_mthly_sales,\
            avg_daily_sales,\
            days_sold_out,\
            days_of_arrival,\
            rep_notice,\
            mfd,days_after_manu,\
            six_mos_warning,\
            three_mos_warning\
            ):

    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # sql="INSERT INTO inv(id,product_id) VALUES(%s,%s)"
        # sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
    #     sql="insert into inv(product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning)
    # values('10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')"
        sql="insert inv(\
            id,\
            product_id,\
            product_name,\
            packing,\
            inv_qty,\
            packing_qty,\
            exp,\
            avg_mthly_sales,\
            avg_daily_sales,\
            days_sold_out,\
            days_of_arrival,\
            rep_notice,\
            mfd,days_after_manu,\
            six_mos_warning,\
            three_mos_warning\
            )\
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(id,\
            product_id,\
            product_name,\
            packing,\
            inv_qty,\
            packing_qty,\
            exp,\
            avg_mthly_sales,\
            avg_daily_sales,\
            days_sold_out,\
            days_of_arrival,\
            rep_notice,\
            mfd,days_after_manu,\
            six_mos_warning,\
            three_mos_warning\
            )
        cursor.execute(sql,data)
        # 儲存變更
        conn.commit()

def updateData(id, product_id, product_name=None, packing=None, inv_qty=None, packing_qty=None, exp=None, avg_mthly_sales=None, avg_daily_sales=None, days_sold_out=None, days_of_arrival=None, rep_notice=None, mfd=None, days_after_manu=None, six_mos_warning=None, three_mos_warning=None):
    print(product_name)
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql="update inv set product_id=%s, product_name=%s, packing=%s, inv_qty=%s, packing_qty=%s, exp=%s, avg_mthly_sales=%s, avg_daily_sales=%s, days_sold_out=%s, days_of_arrival=%s, rep_notice=%s, mfd=%s, days_after_manu=%s, six_mos_warning=%s, three_mos_warning=%s where id=%s"
#         sql="update inv set product_id='%d',product_name='',packing='',inv_qty='',packing_qty='',exp='',avg_mthly_sales='',avg_daily_sales='',days_sold_out='',days_of_arrival='',rep_notice='',mfd='',days_after_manu='',six_mos_warning='',three_mos_warning=''
# where 條件式 (例如 sn='5' 或 name='塔司尼' )
        print(sql)
        data=(id, product_id, product_name, packing, inv_qty, packing_qty, exp, avg_mthly_sales, avg_daily_sales, days_sold_out, days_of_arrival, rep_notice, mfd, days_after_manu, six_mos_warning, three_mos_warning)
        cursor.execute(sql,data)
        # 儲存變更
        conn.commit()

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
ws.used_range.shape
print(ws.used_range.shape)

u = ws.api.UsedRange
r = u.Row + u.Rows.Count - 1
c = u.Column + u.Columns.Count - 1
print("------")
print(u)
print(r)
print(c)
# print(ws.range('2:2').value)
print("------")
# a = ws.range(str('2')+':'+str('2')).value
# print(a)
# print("j")
for j in range(2,r+1):
    print(j)
    # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
    RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= 23]

    # print(RowData[2])
    # print(RowData[8])
    DateRowData=str(RowData[8])
    DateStr = DateRowData.split(' 00:00:00')[0]
    print(DateStr)
    RowData[8]=DateStr
    id=str(round(RowData[3]))+str(convertDateFormat(DateStr,"%Y-%m-%d","%Y%m%d"))
    product_id=RowData[3]
    # print(RowData)
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    print(RowData.pop(0))
    insertData(id,\
            product_id,\
            product_name,\
            packing,\
            inv_qty,\
            packing_qty,\
            exp,\
            avg_mthly_sales,\
            avg_daily_sales,\
            days_sold_out,\
            days_of_arrival,\
            rep_notice,\
            mfd,days_after_manu,\
            six_mos_warning,\
            three_mos_warning\
            )
    print(id)
    


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