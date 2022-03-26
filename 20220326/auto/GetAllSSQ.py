
import calendar
import datetime
from datetime import timedelta
from itertools import count

import time
import sys
sys.path.append('/linebot')
import Date as d
from datetime import datetime, timezone, timedelta

import tkinter as tk
from tkinter import messagebox
import gc

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

def isSubstringExist(substr,string):
    if len(substr)>len(string):
       temp=substr
       substr=string
       string=temp
    pos = string.find(substr)
    if pos >= 0:   # 有找到
        # print('位置：' + str(pos))
        return True
    else:   # 沒有找到
        # print('找不到')
        return False

def isSubstringPosExist(substr,string):
    pos = string.find(substr)
    if pos >= 0:   # 有找到
        #print('位置：' + str(pos))
        return pos
    else:   # 沒有找到
        #print('找不到')
        return -1
        
def isQuotationMarksExist(string):
    pos=isSubstringPosExist('\'',string)
    return pos
    
def checkString(string):
    # print("checkString")
    pos=isQuotationMarksExist(string)
    # print("checkString2")
    split_string=""
    if pos!= -1:
        # print(pos)
        split_strings = string.split("\'")
        for i in range(len(split_strings)):
        	# print(i)
        	# print(len(split_strings))
        	split_string=split_string+split_strings[i]
        	if i<len(split_strings)-1:
        		split_string=split_string+"\\\'"
       	return split_string
    else:
        return string


# def checkString(string):
#     pos=isQuotationMarksExist(string)
#     if pos!= -1:
#         split_strings = string.split("\'")
#         return split_strings[pos-1]+"\\\'"+split_strings[pos]
#     else:
#         return string

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

# def isSubstringExist(substr,string):
#     pos = string.find(substr)
#     if pos >= 0:   # 有找到
#         #print('位置：' + str(pos))
#         return pos
#     else:   # 沒有找到
#         #print('找不到')
#         return -1
      
# def isQuotationMarksExist(string):
#     pos=isSubstringExist('\'',string)
#     return pos

# def checkString(string):
#     print("checkString")
#     pos=isQuotationMarksExist(string)
#     print("checkString2")
#     if pos!= -1:
#         print(pos)
        
#         split_strings = string.split("\'")
#         print(split_strings)
#         print("checkString3")
#         return split_strings[pos-1]+"\\\'"+split_strings[pos]
#     else:
#         return string

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
            #print("sql : "+str(sql))
            #select id,international_barcode as 國際條碼,spec as 規格,broken_number as 折數,suggested_price as 建議售價,purchase_price as 進價,tax as 免應稅,normal_gift as 常態搭贈,average_price as 均價,first_stage as 第一階,second_stage as 第二階,first_stage_average_price as 第一階均價,second_stage_average_price as 第二階均價,gp_after_new_avg_price_of_5_boxes as 新5箱均價後毛利,old_declared_purchase_price as 舊申報進價,old_way_to_declare_discounts as 舊申報優惠方式,avg_price_of_old_declaration as 舊申報均價,more_than_five_boxes as 五箱以上 from pp;
            cursor.execute(sql)#,data)
        except Exception as e:
            print(e)
            print("錯誤")

        # 儲存變更
        conn.commit()
#select concat(year(datetime),'-',month(datetime),'-',day(datetime)) from cu;
#getDataUpdateTime("C020700001")
def getDataUpdateTime(customer_code):
    
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        


        try:
            if customer_code is None:
                customer_code=""
            #select concat(year(datetime),'-',month(datetime),'-',day(datetime)) from cu;
            sql="select concat(year(datetime),'-',month(datetime),'-',day(datetime)) from cu where customer_code='"+str(customer_code)+"'"
            print(sql)
            #time.sleep(20)
            cursor.execute(sql)

            myresult = cursor.fetchone()
            #print(myresult)
            print(myresult[0])
            #print(myresult[1])
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
            #print("sql : "+str(sql))
            print("錯誤")
        # 儲存變更
        conn.commit()


def updateMonSqSum(customer_code,untaxed_amount_in_local_currency):

    now = datetime.date.today()
    
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""
        this_month_start = datetime.datetime(now.year, now.month, 1)
        this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
        last_day_of_last_month= datetime.date(now.year, now.month, 1) - datetime.timedelta(1)


        #若是月初and第一筆(查看資料更新時間是否為上個月的月底)，資料就先清空再加總銷量金額
        if today.getDay(days=0)==1 and getDataUpdateTime(customer_code)==last_day_of_last_month:
            print("case1")
            #print(today.getDay(days=0))
            #print(getDataUpdateTime(customer_code))
            getMonSqSum(customer_code)


        #若不是月初，查看資料更新時間是否為昨日，如果是代表有資料，如果不是，一樣整月全部加總
        #SELECT sum(sales_quantity) into s FROM sq where year(sale_date)=(select year(now())) and month(sale_date)=(select month(now())) and customer_code=customercode;
        else:
            #有資料
            if str(today.getYear(days=1))+str("-")+str(today.getMonth(days=1))+str("-")+str(today.getDay(days=1)) == getDataUpdateTime(customer_code):
                print("case2")
                #print(str(today.getYear(days=1))+str("-")+str(today.getMonth(days=1))+str("-")+str(today.getDay(days=1)))
                #print(getDataUpdateTime(customer_code))
                
            #整月全部加總
            else:
                print("case3")
                #print(str(today.getYear(days=1))+str("-")+str(today.getMonth(days=1))+str("-")+str(today.getDay(days=1)))
                #print(getDataUpdateTime(customer_code))    
                getMonSqSum(customer_code)


        try:
            if customer_code is None:
                customer_code=""
            if untaxed_amount_in_local_currency is None:
                untaxed_amount_in_local_currency=""
            sql="UPDATE CU SET performance_this_month = '"+str(untaxed_amount_in_local_currency)+"' where customer_code='"+str(customer_code)+"'"
            print(sql)
            cursor.execute(sql)
            myresult = cursor.fetchall()
            #print("123")
            #print(myresult[0])
            #print("456")
            #print(myresult[1])
            conn.commit()
            cursor.close()
            # data=[]
            # i=0
            # for x in myresult:
                
            #     data[i]=x
            #     # print("data="+str(data))
            #     i=i+1

            return myresult
        except Exception as e:
            print(e)
            #print("sql : "+str(sql))
            print("錯誤")
        # 儲存變更
        conn.commit()

def getGroup(customer_code):

    now = datetime.date.today()
    
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""


        try:
            if customer_code is None:
                customer_code=""

            #sql="UPDATE CU SET performance_this_month = '"+str(untaxed_amount_in_local_currency)+"' where customer_code='"+str(customer_code)+"'"
            sql="select group_name from cu where customer_code='"+str(customer_code)+"'"
            print(sql)
            cursor.execute(sql)
            myresult = cursor.fetchone()
            if myresult is None:
                print("123")
            else:
                print(myresult[0])

            conn.commit()
            cursor.close()
            # data=[]
            # i=0
            # for x in myresult:
                
            #     data[i]=x
            #     # print("data="+str(data))
            #     i=i+1

            return myresult[0]
        except Exception as e:
            print(e)
            print("sql : "+str(sql))
            print("錯誤")
            
            return ""
        # 儲存變更
        conn.commit()

def getMonSqSum(customer_code):
    now = datetime.date.today()
    
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        #SELECT sum(sales_quantity) into s FROM sq where year(sale_date)=(select year(now())) and month(sale_date)=(select month(now())) and customer_code=customercode;
        try:
            if customer_code is None:
                customer_code=""

            sql="SELECT sum(performance_this_month) into s FROM sq where year(sale_date)=(select year(now())) and month(sale_date)=(select month(now())) and customer_code='"+str(customer_code)+"'"
            print(sql)
            cursor.execute(sql)
            myresult = cursor.fetchall()
            print("123")
            print(myresult[0])
            print("456")
            print(myresult[1])
            conn.commit()
            cursor.close()
            # data=[]
            # i=0
            # for x in myresult:
                
            #     data[i]=x
            #     # print("data="+str(data))
            #     i=i+1

            return myresult
        except Exception as e:
            print(e)
            print("sql : "+str(sql))
            print("錯誤")
        # 儲存變更
        conn.commit()
def getSsqSum(year,month,product_id,store_code):
    conn = pymysql.connect(**setDB())

    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:
            if year is None:
                year=""
            if month is None:
                month=""
            if product_id is None:
                product_id=""
            if store_code is None:
                store_code=""          

            #获取当前日期
            now_time = datetime.datetime.now()
            #获取本月的第一天
            end_day_in_month = now_time.replace(day=1)
            #获取上月的最后一天
            next_month = end_day_in_month - datetime.timedelta(days=1)
            #print(now_time)
            #print(end_day_in_mouth)
            #print(next_month.day)
            #print(next_month.month)
            #print(next_month.year)
            
            this_month = next_month.month
            this_year = next_month.year

            #select sum(sales_quantity) from ssq where year = 2022 and month = 2 and product_id = 10101001;
            #select sum(sales_quantity) from ssq where year = this_year and month = this_month and product_id = product_id;

            
            sql="select sum(sales_quantity) from ssq where year = "+str(year)+" and month = "+str(month)+" and product_id = "+str(product_id)
            id=str(product_id)+str(store_code)+str(year)
            #print("sql : "+str(sql))
            cursor.execute(sql)
            myresult = cursor.fetchone()
            insertSsqSum(id,store_code,product_id,year,month,str(myresult[0]).split('.')[0])#id,store_code,product_id,year,this_month,value
            #print("SsqSum新增")
        except Exception as e:
            pass
            #print(e)
            #print("sql : "+str(sql))
            #print("SsqSum已存在")

        # 儲存變更
        conn.commit()
        cursor.close()

def insertSsqSum(id,store_code,product_id,year,this_month,value):
    conn = pymysql.connect(**setDB())
    
    this_month_arr = [
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # month_dict = {}

    # #加入值為array的資料
    # month_dict['January']=["1"]
    # month_dict['February']=["2"]
    # month_dict['March']=["3"]
    # month_dict['April']=["4"]
    # month_dict['May']=["5"]
    # month_dict['June']=["6"]
    # month_dict['July']=["7"]
    # month_dict['August']=["8"]
    # month_dict['September']=["9"]
    # month_dict['October']=["10"]
    # month_dict['November']=["11"]
    # month_dict['December']=["12"]
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:



            #select sum(sales_quantity) from ssq where year = 2022 and month = 2 and product_id = 10101001;
            #select sum(sales_quantity) from ssq where year = this_year and month = this_month and product_id = product_id;

            #sql="select sum(sales_quantity) from ssq where year = "+str(this_year)+" and month = "+str(this_month)+" and product_id = "+str(product_id)
            
            #this_month換成字串
            #print("----------insertSsqSum----------")
            # print(""+str(",".join(month_dict['January'])))
            # month=""+str(",".join(month_dict['January']))
            #print("====================================")
            #print("this_month = "+str(int(this_month)))
            #print("this_month_arr[this_month] = "+str(this_month_arr[int(this_month)]))
            #print("====================================")
            month=this_month_arr[this_month]
            #print("month = "+str(month))
            # print(str(this_month_arr[this_month]))
            # print(str(this_month_arr[this_month]))
            #print("1")
            sql="insert into mssq (id,store_code,product_id,year,"+str(this_month_arr[int(this_month)])+") values ("+str(id)+","+str(store_code)+","+str(product_id)+","+str(year)+","+str(value)+")"
            #print("2")
            #print("----------insertSsqSum----------")
            # print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
            print("sql : "+str(sql))
            cursor.execute(sql)
            print("MssqSum新增")
        except Exception as e:
            #print(e)
            #sql="delete from mssq where id = "+str(id)
            #cursor.execute(sql)
            #sql="insert into mssq (id,store_code,product_id,year,"+str(this_month_arr[int(this_month)])+") values ("+str(id)+","+str(store_code)+","+str(product_id)+","+str(year)+","+str(value)+")"
            sql="UPDATE mssq SET id = "+str(id)+", store_code = "+str(store_code)+", product_id = "+str(product_id)+", year = "+str(year)+", "+str(this_month_arr[int(this_month)])+" = "+str(value)+" WHERE id = "+str(id)+" "#"UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3"
            #print("sql : "+str(sql))
            cursor.execute(sql)
            #print("MssqSum更新")

        # 儲存變更
        conn.commit()
        gc.collect()
# def insertPPData(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes):
def insertSsqData(
    id, year, month, product_id, store_code, product_name, 
    spec, sales_quantity, total_sales, total_sales_before_tax, average_unit_price,
    net_sales, total_amount_of_discount, number_of_giveaways, weight, giveaway_weight,
    cost_of_goods_sold, gross_sales, gross_profit_margin
    ):                                                                                                                              #second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes


    conn = pymysql.connect(**setDB())

    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:

            if id is None:
                id=""
            if year is None:
                year=""
            if month is None:
                month=""
            if product_id is None:
                product_id=""
            if store_code is None:
                store_code=""
            if product_name is None:
                product_name=""
            if spec is None:
                spec=""
            if sales_quantity is None:
                sales_quantity=""
            if total_sales is None:
                total_sales=""
            if total_sales_before_tax is None:
                total_sales_before_tax=""
            if average_unit_price is None:
                average_unit_price=""
            if net_sales is None:
                net_sales=""
            if total_amount_of_discount is None:
                total_amount_of_discount=""
            if number_of_giveaways is None:
                number_of_giveaways=""
            if weight is None:
                weight=""
            if giveaway_weight is None:
                giveaway_weight=""
            if cost_of_goods_sold is None:
                cost_of_goods_sold=""
            if gross_sales is None:
                gross_sales=""
            if gross_profit_margin is None:
                gross_profit_margin=""


            try:
                sql="insert ssq(\
                        id, year, month, product_id, store_code, product_name,\
                        spec, sales_quantity, total_sales, total_sales_before_tax, average_unit_price,\
                        net_sales, total_amount_of_discount, number_of_giveaways, weight, giveaway_weight,\
                        cost_of_goods_sold, gross_sales, gross_profit_margin\
                    ) \
                    values('\
                        "+(id)+"','"+str(year)+"','"+str(month)+"','"+str(product_id)+"','"+str(store_code)+"','"+checkString(str(product_name))+"','"+str(\
                        spec)+"','"+str(sales_quantity)+"','"+str(total_sales)+"','"+str(total_sales_before_tax)+"','"+str(average_unit_price)+"','"+str(\
                        net_sales)+"','"+str(total_amount_of_discount)+"','"+str(number_of_giveaways)+"','"+str(weight)+"','"+str(giveaway_weight)+"','"+str(\
                        cost_of_goods_sold)+"','"+str(gross_sales)+"','"+str(gross_profit_margin)+"'\
                    )"#+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)
                # print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
                #print("sql : "+str(sql))



                #print("---------------getSsqSum----------------")    
                #print("year = " + str(year))
                #print("month = " + str(month))
                getSsqSum(year,month,product_id,store_code)
                #print("---------------getSsqSum----------------")  
                #print("4")
                #time.sleep(5)
                now = datetime.date.today()
                this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
                if now == this_month_end:#如果是月底，則將加總存至mssq資料表
                    print("insertSsqSum")

                cursor.execute(sql)#,data)
                #print("SsqSum新增")
            except Exception as e:
                pass
                #print(e)
                #print("sql : "+str(sql))
                #print("SsqSum已新增過")
         
        except Exception as e:
            pass
            #print(e)
            #print("sql : "+str(sql))
            #print("SsqData錯誤")

        # 儲存變更
        conn.commit()
        gc.collect()







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



# def delAllPPData():
#     conn = pymysql.connect(**setDB())
#     # 建立Cursor物件
#     with conn.cursor() as cursor:
#         # sql="delete from inv where id=%s"
#         # data=(id)
#         # cursor.execute(sql,data)
#         sql="truncate table pp"
#         cursor.execute(sql)
#         # 儲存變更
#         conn.commit()
# def delAllPromData():
#     conn = pymysql.connect(**setDB())
#     # 建立Cursor物件
#     with conn.cursor() as cursor:
#         # sql="delete from inv where id=%s"
#         # data=(id)
#         # cursor.execute(sql,data)
#         sql="truncate table prom"
#         cursor.execute(sql)
#         # 儲存變更
#         conn.commit()
# import Date as d
def delAllSqData():
    conn = pymysql.connect(**setDB())
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # sql="delete from inv where id=%s"
        # data=(id)
        # cursor.execute(sql,data)
        sql="truncate table sq"
        cursor.execute(sql)
        # 儲存變更
        conn.commit()


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
# import openpyxl
import pandas as pd
import xlrd

# xl = pd.ExcelFile('file.xlsx')
# res = len(xl.sheet_names)
# wb = openpyxl.load_workbook('file.xlsx') 

def getSheetCount(argv):
    #print(argv)
    wb = xlrd.open_workbook(argv, on_demand=True)
    #print(wb)
    res = wb.nsheets # or wb.nsheets
    #print(res)
    return res

# def main(argv):
#     print(argv)
#     # import pymysql
#     #import charts

    
#     app = xw.App(visible=False)

#     #讀取excel檔

#     path=argv
#     wb = xw.Book(path)

#     ws=wb.sheets[0]

#     print("------")

#     used_ranges = ws.api.UsedRange
#     max_row = used_ranges.Rows.Count - used_ranges.Row + 1
#     max_col = used_ranges.Columns.Count - used_ranges.Column + 1

#     print(max_row)
#     print(max_col)

#     try:
#         #清空所有舊資料
#         delAllPPData()
#         # delAllPromData()
#         print("清空所有舊資料")
#     except Exception as e:
#         print("錯誤: 清空所有舊資料")
#         print(e)

#     # print(ws.range('2:2').value)
#     print("------")
#     # a = ws.range(str('2')+':'+str('2')).value
#     # print(a)
#     i=""
#     print("j")
#     for j in range(5,max_row+1):
#         # print("i = "+str(i))
#         # if j==150:
#         #     time.sleep(15)
#         # print("j = "+str(j))
#         # if j==4:
#         #     break
#         # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
#         RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
#         # print("i = "+str(i))
#         if RowData[0]==None:
#             break
#         # # time.sleep(1)
#         # print(RowData[0])
#         # print(RowData[1])
#         # # print(RowData[2])
#         # print(RowData[3])
#         # print(RowData[4])
#         # print(RowData[5])
#         # print(RowData[6])
#         # print(RowData[7])
#         # print(RowData[8])
#         # # print(RowData[9])
#         # print(RowData[10])
#         # print(RowData[11])
#         # print(RowData[12])
#         # print(RowData[13])
#         # print(RowData[14])
#         # print(RowData[15])
#         # print(RowData[16])
#         # print(RowData[17])
#         # print(RowData[18])
#         # print(RowData[19])
#         # # DateRowData=str(RowData[9])
#         print("max_row = "+str(max_row))

#         insertPPData(RowData[0],RowData[1],RowData[2],RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[8],RowData[10],RowData[11],RowData[12],RowData[13],RowData[14],RowData[15],RowData[16],RowData[17],RowData[18],RowData[19])

#     wb.close()
#     app.quit()
def getStoreCode(string):
    RemoveSemicolonStr = string.split(':')
    #print(RemoveSemicolonStr[1])
    RemoveWhitespaceStr = RemoveSemicolonStr[1].split(' ')
    #print(RemoveWhitespaceStr[0])
    return RemoveWhitespaceStr[0]

def input(report_year,report_month,argv):
    # print(argv)
    # import pymysql
    #import charts

    
    app = xw.App(visible=False)

    #讀取excel檔

    path=argv
    wb = xw.Book(path)
    #root = tk.Tk()
    #root.withdraw()
    #messagebox.showinfo('my messagebox', '123')
    ws=wb.sheets[0]

    # print("------")

    used_ranges = ws.api.UsedRange
    max_row = used_ranges.Rows.Count - used_ranges.Row + 1 +2#某部份Sheet多兩列
    max_col = used_ranges.Columns.Count - used_ranges.Column + 1

    # print(max_row)
    # print(max_col)

    try:
        #清空所有舊資料
        #delAllSqData()
        #print("清空所有舊資料")
        print("輸入資料中")
    except Exception as e:
        print("錯誤: 清空所有舊資料")
        print(e)


    res=getSheetCount(argv)

    
    pid=""
    pn=""
    # k=1
    store_code = ""
    year=""
    month=""
    for k in range(1,res+1):
        for j in range(1,max_row+1):
            
            #print("j = "+str(j))
            #print("k = "+str(k))
            #print(str(report_year)+"年"+str(report_month)+"月 - 第"+str(k)+"頁，第"+str(j)+"列，共"+str(res)+"頁") 
            #time.sleep(0.5)           
  

            RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
            # print("年/月:"+str(RowData[7]))
            if j==3:
                #print(RowData[0])
                #print("store_code")
                store_code=getStoreCode(RowData[0])#店號
                #print("store_code")
                #messagebox.showinfo('my messagebox', store_code)
            if j==4 and k==1:
                #print("年:"+str(RowData[7]).split(' ')[1].split('/')[0])#年
                #print("月:"+str(RowData[7]).split(' ')[1].split('/')[1])#月
                year=str(RowData[7]).split(' ')[1].split('/')[0]
                month=str(RowData[7]).split(' ')[1].split('/')[1]
 
            if j>5:

                RowData2 = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
                RowData[18]=RowData2[18]

   	
                    	
                id=str(RowData[0])+str(store_code)+str(year)+str(month)
                #print("id="+str(id))#id=品號+店號+年+月
                #print("年:"+year)
                #print("月:"+month)
                #print("RowData[0]品號="+str(RowData[0]))#品號
                #print("店號="+str(store_code))#店號
                #print("RowData[1]品名="+str(RowData[1]))#品名
                #print("RowData[2]規格="+str(RowData[2]))#規格	
                RowData[3]=str(RowData[3]).split('.')[0]
                #print("RowData[3]銷售數量="+str(RowData[3]))#銷售數量
                RowData[4]=str(RowData[4]).split('.')[0]
                #print("RowData[4]銷售總額="+str(RowData[4]))#銷售總額
                RowData[5]=str(RowData[5]).split('.')[0]
                #print("RowData[5]未稅銷售總金額="+str(RowData[5]))#未稅銷售總金額
                RowData[6]=str(RowData[6]).split('.')[0]
                #print("RowData[6]平均單價="+str(RowData[6]))#平均單價
                RowData[7]=str(RowData[7]).split('.')[0]
                #print("RowData[7]銷售淨額="+str(RowData[7]))#銷售淨額
                RowData[8]=str(RowData[8]).split('.')[0]
                #print("RowData[8]折價總金額="+str(RowData[8]))#折價總金額
                RowData[9]=str(RowData[9]).split('.')[0]
                #print("RowData[9]贈品數量="+str(RowData[9]))#贈品數量
                RowData[10]=str(RowData[10]).split('.')[0]
                #print("RowData[10]重量="+str(RowData[10]))#重量
                RowData[11]=str(RowData[11]).split('.')[0]
                #print("RowData[11]贈品重量="+str(RowData[11]))#贈品重量
                RowData[12]=str(RowData[12]).split('.')[0]
                #print("RowData[12]銷貨成本="+str(RowData[12]))#銷貨成本
                RowData[13]=str(RowData[13]).split('.')[0]
                #print("RowData[13]銷售毛利="+str(RowData[13]))#銷售毛利
                #print("RowData[14]毛利率="+str(RowData[14]))#毛利率

                del RowData2

 
                if RowData[0] != None:
                    insertSsqData(id,year,month,RowData[0],store_code,RowData[1],RowData[2],RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[8],RowData[9],RowData[10],RowData[11],RowData[12],RowData[13],RowData[14])
            
            gc.collect()
            del RowData
            
        #print(k) 
        #print(res) 
        #print(str(report_year)+"年"+str(report_month)+"月 - 第"+str(k)+"頁，共"+str(res)+"頁") 
        if k<res:
            
            ws=wb.sheets[k]#翻頁籤
            #time.sleep(2)  

    wb.close()
    app.quit()
    gc.collect()





def allssq():



    today=d.Date()
    c=d.Date()

    report_month=c.getMonth()
    report_year=c.getYear()



    start=3


    print("今年ssq")

    for i in range(1,start,1):#1 2
        #記錄開始執行時間
        time_start = time.time()
        #print(i)
        report_month=i
        if int(report_month)<10:
            report_month="0"+str(report_month)
        #file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str("2022")+str("01")+str("01")+str("0001A.XLSX")
        if report_month=="01" or "02" or "03" or "04" or "05" or "06":
            continue
        if report_month=="02":
            continue
        file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str(report_year)+str(report_month)+str("01")+str("0001A.XLSX")
                        
        #print(file_name)
        input(report_year,report_month,file_name)
        gc.collect()
        #記錄結束執行時間
        time_end = time.time()
        print("耗時 " + str(time_end-time_start) + " 秒")



    print("----------------")
    print("去年ssq")
    report_year=str(int(report_year)-1)
    print(report_year)
    for i in range(start,13,1):#3 4 5 6 7 8 9 10 11 12
        #記錄開始執行時間
        time_start = time.time()
        #print(i)
        report_month=i
        if int(report_month)<10:
            report_month="0"+str(report_month)
        #file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str("2022")+str("01")+str("01")+str("0001A.XLSX")
        file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str(report_year)+str(report_month)+str("01")+str("0001A.XLSX")
                        
        #print(file_name)
        input(report_year,report_month,file_name)
        gc.collect()
        #記錄結束執行時間
        time_end = time.time()
        print("耗時 " + str(time_end-time_start) + " 秒")






if __name__ == "__main__":
    #print("start")


    allssq()


