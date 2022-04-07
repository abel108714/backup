

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

# def setWebsite(product_name):
#     #查是否有網址，若無則爬取網址儲存
#     pass

# def isProductExist(product_id):
#     conn = pymysql.connect(**setDB())
#     with conn.cursor() as cursor:
#         try:
#             sql="select product_id from product where product_id = '"+str(product_id)+"'"#顯示資料
#             print("sql : "+str(sql))
#             cursor.execute(sql)
#         except Exception as e:
#             print(e)

# def insertProduct(product_id,product_name):#輸入品號品名
#     # sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
#     conn = pymysql.connect(**setDB())
#     # 建立Cursor物件
#     if isProductExist(product_id) == True:
#         with conn.cursor() as cursor:
#             try:
#                 sql="insert product(product_id,product_name) values('"+str(product_id)+"','"+str(product_name)+"')"
#                 print("insertProduct")
#                 print("sql : "+str(sql))
#                 cursor.execute(sql)
#             except Exception as e:
#                 print(e)
#             # 儲存變更
#             conn.commit()
def insertPromData(id,product_name,special_offer,special_purchase_price,note):
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:

        print("insertPPData123")
        try:
            print("insertPPData456")
            if id is None:
                id=""
            if product_name is None:
                product_name=""
            if special_offer is None:
                special_offer=""
            if special_purchase_price is None:
                special_purchase_price=""
            if note is None:
                note=""
            print("ttttttttttttttttttt")#,second_stage_average_price
            # sql="insert pp(id,international_barcode,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,
            # average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,
            # gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,
            # avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(international_barcode)+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage,second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')"
            print("insertPromData")
            sql="insert prom(id,product_name,special_offer,special_purchase_price,note) values('"+str(id)+"','"+str(product_name)+"','"+str(special_offer)+"','"+str(special_purchase_price)+"','"+str(note)+"')"#+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)
            print("sql : "+str(sql))
            #select id,international_barcode as 國際條碼,spec as 規格,broken_number as 折數,suggested_price as 建議售價,purchase_price as 進價,tax as 免應稅,normal_gift as 常態搭贈,average_price as 均價,first_stage as 第一階,second_stage as 第二階,first_stage_average_price as 第一階均價,second_stage_average_price as 第二階均價,gp_after_new_avg_price_of_5_boxes as 新5箱均價後毛利,old_declared_purchase_price as 舊申報進價,old_way_to_declare_discounts as 舊申報優惠方式,avg_price_of_old_declaration as 舊申報均價,more_than_five_boxes as 五箱以上 from pp;
            cursor.execute(sql)#,data)
        except Exception as e:
            print(e)
            print("錯誤")
            sql2 = "DELETE FROM prom where id"+str(id)
            cursor.execute(sql2)
            cursor.execute(sql)
        # 儲存變更
        conn.commit()


def insertPPData(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes):
                                                                                                                                                                             #second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes
#insert pp(id,international_barcode,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,more_than_five_boxes)values('11702023','4719859749386','30g*25入/盒*6','260','600','260','應','(2入800)11組贈1組','238.33','250(12盒以上)','22+2盒','250.00','238.33','230.00');
 
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:

        # print("insertPPData123")
        try:
            # print("insertPPData456")
            if id is None:
                id=""
            if international_barcode is None:
                international_barcode=""
            if product_name is None:
                product_name=""
            if spec is None:
                spec=""
            if broken_number is None:
                broken_number=""
            if suggested_price is None:
                suggested_price=""
            if purchase_price is None:
                purchase_price=""
            if tax is None:
                tax=""
            if normal_gift is None:
                normal_gift=""
            if average_price is None:
                average_price=""
            if first_stage is None:#second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes
                first_stage=""
            if second_stage is None:
                second_stage=""
            
            if first_stage_average_price is None:
                first_stage_average_price=""
            print(second_stage_average_price)
            if second_stage_average_price is None:
                second_stage_average_price=""
            print(gp_after_new_avg_price_of_5_boxes)
            if gp_after_new_avg_price_of_5_boxes is None:
                gp_after_new_avg_price_of_5_boxes=""
            print(old_declared_purchase_price)
            if old_declared_purchase_price is None:
                old_declared_purchase_price=""
            print(old_way_to_declare_discounts)
            if old_way_to_declare_discounts is None:
                old_way_to_declare_discounts=""
            print(avg_price_of_old_declaration)
            if avg_price_of_old_declaration is None:
                avg_price_of_old_declaration=""
            if more_than_five_boxes is None:
                more_than_five_boxes=""
            # print("ttttttttttttttttttt")#,second_stage_average_price
            # sql="insert pp(id,international_barcode,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,
            # average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,
            # gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,
            # avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(international_barcode)+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage,second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')"
            print("insertPPData")
            sql="insert pp(\
                    id,international_barcode,product_name,spec,broken_number,suggested_price,\
                    purchase_price,tax,normal_gift,average_price,\
                    first_stage,second_stage,first_stage_average_price,second_stage_average_price,\
                    gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,\
                    avg_price_of_old_declaration,more_than_five_boxes\
                ) \
                values('\
                    "+str(id)+"','"+str(round(international_barcode))+"','"+str(product_name)+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"',\
                    '"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"',\
                    '"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"',\
                    '"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"',\
                    '"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"'\
                )"#+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)
            print("sql = "+str(sql))
            #print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
            #select id,international_barcode as 國際條碼,spec as 規格,broken_number as 折數,suggested_price as 建議售價,purchase_price as 進價,tax as 免應稅,normal_gift as 常態搭贈,average_price as 均價,first_stage as 第一階,second_stage as 第二階,first_stage_average_price as 第一階均價,second_stage_average_price as 第二階均價,gp_after_new_avg_price_of_5_boxes as 新5箱均價後毛利,old_declared_purchase_price as 舊申報進價,old_way_to_declare_discounts as 舊申報優惠方式,avg_price_of_old_declaration as 舊申報均價,more_than_five_boxes as 五箱以上 from pp;
            cursor.execute(sql)#,data)
        except Exception as e:
            print(e)
            print("錯誤")
            sql2 = "DELETE FROM pp where id"+str(id)
            cursor.execute(sql2)
            cursor.execute(sql)

            # print(exp)
            # seq=int(getDataSeq(product_id,exp))+int(1)
            # id=id[:len(str(id))-1]+str(seq)

            # str = '211030150000000001'
            # print(len(str))
            # print(str[-1:])  # 輸出字串右邊1位
            # print(str)
            # print(str[:17])  # 輸出字串左邊17位
            # str = '211030150000000001'
            # print(len(seq))
            # print(seq[:len(seq)])

            

            # id=seq[:len(str(seq))]+str(seq)
            # print("seq:"+str(seq))
            # print("id:"+str(id))
            # sql="insert inv(id,product_id,product_name,packing,inv_qty,packing_qty,exp,avg_mthly_sales,avg_daily_sales,days_sold_out,days_of_arrival,rep_notice,mfd,days_after_manu,six_mos_warning,three_mos_warning,seq)values('"+str(id)+"','"+str(product_id)+"','"+checkString(str(product_name))+"','"+str(packing)+"','"+str(inv_qty)+"','"+str(packing_qty)+"','"+str(exp)+"','"+str(avg_mthly_sales)+"','"+str(avg_daily_sales)+"','"+str(days_sold_out)+"','"+str(days_of_arrival)+"','"+str(rep_notice)+"','"+str(mfd)+"','"+str(days_after_manu)+"','"+str(six_mos_warning)+"','"+str(three_mos_warning)+"','"+str(seq)+"')"
            # print("insertData e")
            # print("sql:"+str(sql))
            # # insertProduct(product_id,product_name)
            # cursor.execute(sql)#,data)
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


def getDataArr(product_id):
    conn = pymysql.connect(**setDB())
    with conn.cursor() as cursor:
        sql="select product_id as 品號,product_name as 品名,packing as 包裝方式,inv_qty as 庫存數量,packing_qty as 包裝數量,exp as 有效期限 from inv where product_id='"+str(product_id)+"'"
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



def delAllPPData():
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # sql="delete from inv where id=%s"
        # data=(id)
        # cursor.execute(sql,data)
        sql="truncate table pp"
        cursor.execute(sql)
        # 儲存變更
        conn.commit()
def delAllPromData():
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # sql="delete from inv where id=%s"
        # data=(id)
        # cursor.execute(sql,data)
        sql="truncate table prom"
        cursor.execute(sql)
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

# exit()
import xlwings as xw
import sys

import time

def main(argv):
    print(argv)
    # import pymysql
    #import charts

    
    app = xw.App(visible=False)

    #讀取excel檔

    path=argv
    print(path)
    wb = xw.Book(path)

    ws=wb.sheets[0]

    print("------")

    used_ranges = ws.api.UsedRange
    max_row = used_ranges.Rows.Count - used_ranges.Row + 1
    max_col = used_ranges.Columns.Count - used_ranges.Column + 1

    print(max_row)
    print(max_col)

    try:
        #清空所有舊資料
        #delAllPPData()
        print("清空所有舊資料")
    except Exception as e:
        print("錯誤: 清空所有舊資料")
        print(e)

    # print(ws.range('2:2').value)
    print("------")
    # a = ws.range(str('2')+':'+str('2')).value
    # print(a)
    i=""
    print("j")
    for j in range(5,max_row+1):
        print("i = "+str(i))
        # if j==150:
        #     time.sleep(15)
        print("j = "+str(j))
        # if j==4:
        #     break
        # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
        RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
        print("(i) = "+str(i))
        if RowData[0]==None or RowData[1]==None:
            continue
        # # time.sleep(1)
        print(RowData[0])
        print(RowData[1])
        # print(RowData[2])
        print(RowData[3])
        print(RowData[4])
        print(RowData[5])
        print(RowData[6])
        print(RowData[7])
        print(RowData[8])
        # print(RowData[9])
        print(RowData[10])
        print(RowData[11])
        print(RowData[12])
        print(RowData[13])
        print(RowData[14])
        print(RowData[15])
        print(RowData[16])
        print(RowData[17])
        print(RowData[18])
        print(RowData[19])
        # # DateRowData=str(RowData[9])
        print("max_row = "+str(max_row))

        insertPPData(RowData[0],RowData[1],RowData[2],RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[8],RowData[10],RowData[11],RowData[12],RowData[13],RowData[14],RowData[15],RowData[16],RowData[17],RowData[18],RowData[19])

    wb.close()
    app.quit()

def main2(argv):
    print(argv)
    # import pymysql
    #import charts

    
    app = xw.App(visible=False)

    #讀取excel檔

    path=argv
    wb = xw.Book(path)

    ws=wb.sheets[0]

    print("------")

    used_ranges = ws.api.UsedRange
    max_row = used_ranges.Rows.Count - used_ranges.Row + 1
    max_col = used_ranges.Columns.Count - used_ranges.Column + 1

    print(max_row)
    print(max_col)

    try:
        #清空所有舊資料
        #delAllPromData()
        print("清空所有舊資料")
    except Exception as e:
        print("錯誤: 清空所有舊資料")
        print(e)

    # print(ws.range('2:2').value)
    print("------")
    # a = ws.range(str('2')+':'+str('2')).value
    # print(a)
    i=""
    print("j")
    for j in range(5,max_row+1):
        # print("i = "+str(i))
        
        # print("j = "+str(j))
        # if j==4:
        #     break
        # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
        RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
        # print("i = "+str(i))
        if RowData[2]==None:
            break
        # time.sleep(1)
        # print(RowData[0])
        # print(RowData[1])
        # # print(RowData[2])
        # print(RowData[3])
        # print(RowData[4])
        # print(RowData[5])
        # print(RowData[6])
        # print(RowData[7])
        # print(RowData[8])
        # # print(RowData[9])
        # print(RowData[10])
        # print(RowData[11])
        # print(RowData[12])
        # print(RowData[13])
        # print(RowData[14])
        # print(RowData[15])
        # print(RowData[16])
        # print(RowData[17])
        # print(RowData[18])
        # print(RowData[19])
        # # DateRowData=str(RowData[9])
        print("max_row = "+str(max_row))
        RowData[6]=str(RowData[6]).replace(" ", "").replace("\n", "")
        insertPromData(RowData[1],RowData[2],RowData[4],RowData[5],RowData[6])

    wb.close()
    app.quit()
    # id='1090300820220512'
    # product_id='10903008'

    # db_settings={}







    # try:
    #     insertData('10903008202205120','10903008','天然冰湖野米十穀米600g','6包/箱','856','142箱4包','2022/5/12','109.83','4','214','25','','2021/5/12','23','','')
    #     print("已新增資料")
    # except Exception as e:
    #     print(e)
    #     print("已有資料")
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
if __name__ == "__main__":
    print("start")
    # main(sys.argv)
    #main("S:\開發部\◆業績資料\★開發部績效小幫手專用★\★產品折數表_申報優惠方式★確認版07.xls")
    #main2("S:\\開發部\◆業績資料\★開發部績效小幫手專用★\康健年中慶+中元節促銷案-確定版(加品號).xlsx")
    main(r"C:\\Users\\udev77\\Desktop\\產品折數表-04月.xlsx")
    


    