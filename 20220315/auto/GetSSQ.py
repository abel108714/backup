
import calendar
import datetime
from datetime import timedelta

import time
import sys
sys.path.append('/linebot')
import Date as d
from datetime import datetime, timezone, timedelta

import tkinter as tk
from tkinter import messagebox


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
            print("sql : "+str(sql))
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
            print("sql : "+str(sql))
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
            print("sql : "+str(sql))
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
def getSsqSum(this_year,this_month,product_id,store_code):
    conn = pymysql.connect(**setDB())

    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:
            if this_year is None:
                this_year=""
            if this_month is None:
                this_month=""
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
            print(next_month.day)
            print(next_month.month)
            print(next_month.year)
            
            this_month = next_month.month
            this_year = next_month.year

            #select sum(sales_quantity) from ssq where year = 2022 and month = 2 and product_id = 10101001;
            #select sum(sales_quantity) from ssq where year = this_year and month = this_month and product_id = product_id;

            
            sql="select sum(sales_quantity) from ssq where year = "+str(this_year)+" and month = "+str(this_month)+" and product_id = "+str(product_id)
            id=str(product_id)+str(store_code)+str(this_year)

            
            
            #'sql="insert into mssq (id,product_id,february) values (10101001211012022,10101001,11)"
            # print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
            print("sql : "+str(sql))
            cursor.execute(sql)
            myresult = cursor.fetchone()
            print(id)
            print(myresult[0])
            root = tk.Tk()
            root.withdraw()
            insertSsqSum(id,product_id,this_month,myresult[0])
            # messagebox.showinfo('my messagebox', myresult[0])
            # messagebox.showinfo('my messagebox', myresult[1])
            # messagebox.showinfo('my messagebox', myresult[2])
            if myresult is None:
                print("123")
            else:
                print(myresult[0])

            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
            print("sql : "+str(sql))
            print("getSsqSum錯誤")

        # 儲存變更
        conn.commit()

def insertSsqSum(id,product_id,this_month,value):
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
    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:



            #select sum(sales_quantity) from ssq where year = 2022 and month = 2 and product_id = 10101001;
            #select sum(sales_quantity) from ssq where year = this_year and month = this_month and product_id = product_id;

            #sql="select sum(sales_quantity) from ssq where year = "+str(this_year)+" and month = "+str(this_month)+" and product_id = "+str(product_id)
            
            #this_month換成字串

            sql="insert into mssq (id,store_code,product_id,year,"+str(this_month_arr[this_month])+") values ("+str(id)+","+str(product_id)+","+str(value)+")"
            # print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
            print("sql : "+str(sql))
            cursor.execute(sql)
        except Exception as e:
            print(e)
            print("sql : "+str(sql))
            print("insertSsqSum錯誤")

        # 儲存變更
        conn.commit()
# def insertPPData(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes):
def insertSsqData(
    id, year, month, product_id, store_code, product_name, 
    spec, sales_quantity, total_sales, total_sales_before_tax, average_unit_price,
    net_sales, total_amount_of_discount, number_of_giveaways, weight, giveaway_weight,
    cost_of_goods_sold, gross_sales, gross_profit_margin
    ):                                                                                                                              #second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes
# CREATE Table ssq(
#     id bigint(255) NOT NULL, #id+店號
#     product_id bigint(255) NOT NULL, #品號
#     store_code varchar(50) character set utf8, #店號
#     product_name varchar(50) character set utf8, #品名
#     spec varchar(50) character set utf8, #規格
#     sales_quantity varchar(50) character set utf8, #銷貨數量
#     total_sales varchar(50) character set utf8, #銷售總額
#     total_sales_before_tax varchar(50) character set utf8, #未稅銷售總金額
#     average_unit_price varchar(50) character set utf8, #平均單價
#     net_sales varchar(50) character set utf8, #銷售淨額
#     total_amount_of_discount varchar(50) character set utf8, #折價總金額
#     number_of_giveaways varchar(50) character set utf8, #贈品數量
#     weight varchar(50) character set utf8, #重量
#     giveaway_weight varchar(50) character set utf8, #贈品重量
#     cost_of_goods_sold varchar(50) character set utf8, #銷貨成本
#     gross_sales varchar(50) character set utf8, #銷售毛利
#     gross_profit_margin varchar(50) character set utf8, #毛利率
#     PRIMARY KEY (product_id) #設定主鍵
# )ENGINE = InnoDB;

# id, product_id, store_code, product_name, 
# spec, sales_quantity, total_sales, total_sales_before_tax, average_unit_price,
# net_sales, total_amount_of_discount, number_of_giveaways, weight, giveaway_weight,
# cost_of_goods_sold, gross_sales, gross_profit_margin

# id,
# product_id,
# store_code,
# product_name,
# spec,
# sales_quantity,
# total_sales,
# total_sales_before_tax,
# average_unit_price,
# net_sales,
# total_amount_of_discount,
# number_of_giveaways,
# weight,
# giveaway_weight,
# cost_of_goods_sold,
# gross_sales,
# gross_profit_margin

    conn = pymysql.connect(**setDB())

    # 建立Cursor物件
    with conn.cursor() as cursor:
        sql=""

        try:
# id, product_id, store_code, product_name, 
# spec, sales_quantity, total_sales, total_sales_before_tax, average_unit_price,
# net_sales, total_amount_of_discount, number_of_giveaways, weight, giveaway_weight,
# cost_of_goods_sold, gross_sales, gross_profit_margin
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
                print("sql : "+str(sql))


                #返回datetime格式：eg：2019-12-07 20:38:35.82816
                now = datetime.datetime.now()

                #返回datetime格式：eg：2019-12-07
                today = datetime.datetime.now().date().day
                print(now)

                this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1]).date().day
                this_year=now.year
                this_month=now.month

                print("1")
                print(today)
                print("2")
                print(this_month_end)
                print("3")
                print(this_year)
                print(this_month)
                print(product_id)
                getSsqSum(this_year,this_month,product_id,store_code)
                print("4")
                if now == this_month_end:#如果是月底，則將加總存至mssq資料表
                    print("insertSsqSum")
                    #insertSsqSum(this_year,this_month,product_id)
                    #select sum(sales_quantity) from ssq where year = 2022 and month = 2 and product_id = 10101001;
                #select id,international_barcode as 國際條碼,spec as 規格,broken_number as 折數,suggested_price as 建議售價,purchase_price as 進價,tax as 免應稅,normal_gift as 常態搭贈,average_price as 均價,first_stage as 第一階,second_stage as 第二階,first_stage_average_price as 第一階均價,second_stage_average_price as 第二階均價,gp_after_new_avg_price_of_5_boxes as 新5箱均價後毛利,old_declared_purchase_price as 舊申報進價,old_way_to_declare_discounts as 舊申報優惠方式,avg_price_of_old_declaration as 舊申報均價,more_than_five_boxes as 五箱以上 from pp;
                # print("123456")
                time.sleep(15)
                cursor.execute(sql)#,data)
            except Exception as e:
                print(e)
                print("sql : "+str(sql))
                print("已新增過，正在更新中")
                # sql="update sq set \
                #         product_name = "+checkString(str(product_name))+", customer_code = "+str(customer_code)+",sale_date = "+str(sale_date)+",sales_number = "+str(sales_number)+",\
                #         sales_quantity = "+str(sales_quantity)+",sales_packaging_quantity = "+str(sales_packaging_quantity)+",units = "+str(units)+",currencies = "+str(currencies)+",unit_price = "+str(unit_price)+",\
                #         original_currency_untaxed_amount = "+str(original_currency_untaxed_amount)+",untaxed_amount_in_local_currency = "+str(untaxed_amount_in_local_currency)+",\
                #         cost_of_goods_sold = "+str(cost_of_goods_sold)+",gross_profit_margin = "+str(gross_profit_margin)+",invoice_coupon = "+str(invoice_coupon)+",salesman = "+str(salesman)+",\
                #         factory_code = "+str(factory_code)+",library_code = "+str(library_code)+",group_name = "+str(group_name)+"\
                #     ) \
                #     where id = "+str(id)#+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)
                # # print("sql : insert pp(id,international_barcode,product_name,spec,broken_number,suggested_price,purchase_price,tax,normal_gift,average_price,first_stage,second_stage,first_stage_average_price,second_stage_average_price,gp_after_new_avg_price_of_5_boxes,old_declared_purchase_price,old_way_to_declare_discounts,avg_price_of_old_declaration,more_than_five_boxes) values('"+str(id)+"','"+str(round(international_barcode))+"','"+str(spec)+"','"+str(broken_number)+"','"+str(suggested_price)+"','"+str(purchase_price)+"','"+str(tax)+"','"+str(normal_gift)+"','"+str(average_price)+"','"+str(first_stage)+"','"+str(second_stage)+"','"+str(first_stage_average_price)+"','"+str(second_stage_average_price)+"','"+str(gp_after_new_avg_price_of_5_boxes)+"','"+str(old_declared_purchase_price)+"','"+str(old_way_to_declare_discounts)+"','"+str(avg_price_of_old_declaration)+"','"+str(more_than_five_boxes)+"')")
                # print("sql : "+str(sql))
                #select id,international_barcode as 國際條碼,spec as 規格,broken_number as 折數,suggested_price as 建議售價,purchase_price as 進價,tax as 免應稅,normal_gift as 常態搭贈,average_price as 均價,first_stage as 第一階,second_stage as 第二階,first_stage_average_price as 第一階均價,second_stage_average_price as 第二階均價,gp_after_new_avg_price_of_5_boxes as 新5箱均價後毛利,old_declared_purchase_price as 舊申報進價,old_way_to_declare_discounts as 舊申報優惠方式,avg_price_of_old_declaration as 舊申報均價,more_than_five_boxes as 五箱以上 from pp;
                # print("123456")
                #time.sleep(15)
                #cursor.execute(sql)#,data)           
        except Exception as e:
            print(e)
            print("sql : "+str(sql))
            print("insertSsqData錯誤")
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
    
    # use on_demand=True to avoid loading worksheet data into memory
    # xl = pd.ExcelFile(argv)
    # res = len(xl.sheet_names)
    print(argv)
    wb = xlrd.open_workbook(argv, on_demand=True)
    print(wb)
    res = wb.nsheets # or wb.nsheets
    print(res)
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
    print(RemoveSemicolonStr[1])
    RemoveWhitespaceStr = RemoveSemicolonStr[1].split(' ')
    print(RemoveWhitespaceStr[0])
    return RemoveWhitespaceStr[0]

def main(argv):
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

    # print(ws.range('2:2').value)
    # print("------")
    # a = ws.range(str('2')+':'+str('2')).value
    # print(a)
    # i=""
    # print("j")
    res=getSheetCount(argv)
    # messagebox.showinfo('my messagebox', res)

    # messagebox.showinfo('my messagebox', max_row)
    
    pid=""
    pn=""
    # k=1
    store_code = ""
    year=""
    month=""
    for k in range(1,res+1):
        for j in range(1,max_row+1):
            
            print("j = "+str(j))
            print("k = "+str(k))
            # if j==4:
            #     break
            # RowData = [i for i in ws.range(str(j)+':'+str(j)).value if i != None]
            # print(ws.range(j,2).value)
            # if str(ws.range(j,4).value)=="None":
            #     continue
            # print("=============="+str(ws.range(j,2).value)) 
            # time.sleep(2)
            # if isSubstringExist(str(ws.range(j,2).value),"銷貨小計")==True:
            #     # print("銷貨小計") 
            #     # time.sleep(2)
            #     continue
            # if isSubstringExist(str(ws.range(j,2).value),"退貨小計")==True:
            #     continue
            # print(str(ws.range(j,5).value))
            # print(str(ws.range(j,5).value) == str(None))
            #if str(ws.range(j,5).value) == str(None):#第5行單號為空表無資料，跳過
            #    continue
            print("第"+str(k)+"頁，第"+str(j)+"列")            
            # print("k = "+str(k)+"j = "+str(j))    
            # print(j%2 == 0)  
            # if k==50 and j==59:
            #     time.sleep(2)
            
            # if k==188 and j==23:
            #     time.sleep(4)
            #     print("RowData[0]品號="+str(RowData[0]))
            #     print("RowData[1]品名="+str(RowData[1]))
            #     print("RowData[2]客戶代號="+str(RowData[2]))
            #     print("RowData[3]銷貨日期="+str(RowData[3]))
            #     print("RowData[4]銷貨單號="+str(RowData[4]))
            #     print("RowData[5]銷貨數量="+str(RowData[5]))
            #     print("RowData[6]銷貨包裝數量="+str(RowData[6]))
            #     print("RowData[7]單位="+str(RowData[7]))
            #     print("RowData[8]="+str(RowData[8]))
            #     print("RowData[9]="+str(RowData[9]))
            #     print("RowData[10]="+str(RowData[10]))
            #     print("RowData[11]幣別="+str(RowData[11]))
            #     print("RowData[12]單價="+str(RowData[12]))
            #     print("RowData[13]原幣未稅金額original_currency_untaxed_amount="+str(RowData[13]))
            #     print("RowData[14]本幣未稅金額="+str(RowData[14]))
            #     print("RowData[15]銷貨成本="+str(RowData[15]))
            #     print("RowData[16]毛利率="+str(RowData[16]))
            #     print("RowData[17]發票聯數="+str(RowData[17]))
            #     print("RowData[18]業務員="+str(RowData[18]))
            #     print("RowData[19]廠別代號="+str(RowData[19]))
            #     print("RowData[20]庫別代號="+str(RowData[20]))#library_code	
            #     time.sleep(30)
            #if j%2 == 0:#偶數行
                # print("偶數行")   

            RowData = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
            # print("年/月:"+str(RowData[7]))
            if j==3:
                print(RowData[0])
                store_code=getStoreCode(RowData[0])#店號
                #messagebox.showinfo('my messagebox', store_code)
            if j==4 and k==1:
                print("年:"+str(RowData[7]).split(' ')[1].split('/')[0])#年
                print("月:"+str(RowData[7]).split(' ')[1].split('/')[1])#月
                year=str(RowData[7]).split(' ')[1].split('/')[0]
                month=str(RowData[7]).split(' ')[1].split('/')[1]
            #if k==188 and j==23:
            #    print("RowData[0]="+str(RowData[0]))
                # time.sleep(2)
            #RowData[0]=str(RowData[0]).lstrip() #去除空白
            #if k==188 and j==23:
            #    print("RowData[0]="+str(RowData[0]))
                # time.sleep(2)
            #if str(ws.range(j,1).value) != str(None):#第一行不為空表，記錄品號品名
            #    pid=str(RowData[0])
            #    pn=str(RowData[1])
            #if str(ws.range(j,1).value) == str(None):#第一行為空表同品號品名
            #    RowData[0]=pid
            #    RowData[1]=pn
                # time.sleep(2)
                # print("RowData[0]品號="+str(RowData[0]))
                # print("RowData[1]品名="+str(RowData[1]))
                # print("RowData[2]客戶代號="+str(RowData[2]))
                # print("RowData[3]銷貨日期="+str(RowData[3]))
                # time.sleep(2)
            #else:#奇數行
            if j>5:
                # print("奇數行")   
                #messagebox.showinfo('my messagebox', store_code)
                RowData2 = [i for i in ws.range(str(j)+':'+str(j)).value if j <= max_row]
                RowData[18]=RowData2[18]
                # print("奇數行2")   
                # time.sleep(2)
            # print("RowData[1]品名="+str(RowData[1]))
            # print(isSubstringExist(str(RowData[1]),"銷貨小計")==False and isSubstringExist(str(RowData[1]),"退貨小計")==False)  

                # print(isSubstringExist(str(RowData[3]),"")==False)
                # time.sleep(2)
                #if isSubstringExist(str(RowData[1]),"銷貨小計")==False and isSubstringExist(str(RowData[1]),"退貨小計")==False:
#CREATE Table ssq(
#    id bigint(255) NOT NULL, #id+店號
#    product_id bigint(255) NOT NULL, #品號
#    store_code varchar(50) character set utf8, #店號
#    product_name varchar(50) character set utf8, #品名
#    spec varchar(50) character set utf8, #規格
#    sales_quantity varchar(50) character set utf8, #銷貨數量
#    total_sales varchar(50) character set utf8, #銷售總額
#    total_sales_before_tax varchar(50) character set utf8, #未稅銷售總金額
#    average_unit_price varchar(50) character set utf8, #平均單價
#    net_sales varchar(50) character set utf8, #銷售淨額
#    total_amount_of_discount varchar(50) character set utf8, #折價總金額
#    number_of_giveaways varchar(50) character set utf8, #贈品數量
#    weight varchar(50) character set utf8, #重量
#    giveaway_weight varchar(50) character set utf8, #贈品重量
#    cost_of_goods_sold varchar(50) character set utf8, #銷貨成本
#    gross_sales varchar(50) character set utf8, #銷售毛利
#    gross_profit_margin varchar(50) character set utf8, #毛利率
#    PRIMARY KEY (product_id) #設定主鍵
#)ENGINE = InnoDB;
                    # print("res = "+str(res))
                    	
                    	
                    
                    	
                    	
                    	
                    	
                    	
                    	
                    	
                    	
                    	
                    	
                    	
                id=str(RowData[0])+str(store_code)+str(year)+str(month)
                print("id="+str(id))#id=品號+店號+年+月
                print("年:"+year)
                print("月:"+month)
                print("RowData[0]品號="+str(RowData[0]))#品號
                print("店號="+str(store_code))#店號
                print("RowData[1]品名="+str(RowData[1]))#品名
                print("RowData[2]規格="+str(RowData[2]))#規格	
                RowData[3]=str(RowData[3]).split('.')[0]
                print("RowData[3]銷售數量="+str(RowData[3]))#銷售數量
                RowData[4]=str(RowData[4]).split('.')[0]
                print("RowData[4]銷售總額="+str(RowData[4]))#銷售總額
                RowData[5]=str(RowData[5]).split('.')[0]
                print("RowData[5]未稅銷售總金額="+str(RowData[5]))#未稅銷售總金額
                RowData[6]=str(RowData[6]).split('.')[0]
                print("RowData[6]平均單價="+str(RowData[6]))#平均單價
                RowData[7]=str(RowData[7]).split('.')[0]
                print("RowData[7]銷售淨額="+str(RowData[7]))#銷售淨額
                RowData[8]=str(RowData[8]).split('.')[0]
                print("RowData[8]折價總金額="+str(RowData[8]))#折價總金額
                RowData[9]=str(RowData[9]).split('.')[0]
                print("RowData[9]贈品數量="+str(RowData[9]))#贈品數量
                RowData[10]=str(RowData[10]).split('.')[0]
                print("RowData[10]重量="+str(RowData[10]))#重量
                RowData[11]=str(RowData[11]).split('.')[0]
                print("RowData[11]贈品重量="+str(RowData[11]))#贈品重量
                RowData[12]=str(RowData[12]).split('.')[0]
                print("RowData[12]銷貨成本="+str(RowData[12]))#銷貨成本
                RowData[13]=str(RowData[13]).split('.')[0]
                print("RowData[13]銷售毛利="+str(RowData[13]))#銷售毛利
                #RowData[14]=str(RowData[14]).split('.')[0]
                print("RowData[14]毛利率="+str(RowData[14]))#毛利率
    # id bigint(255) NOT NULL, #id+店號
    # product_id bigint(255) NOT NULL, #品號
    # store_code varchar(50) character set utf8, #店號
    # product_name varchar(50) character set utf8, #品名
    # spec varchar(50) character set utf8, #規格
    # sales_quantity varchar(50) character set utf8, #銷貨數量
    # total_sales varchar(50) character set utf8, #銷售總額
    # total_sales_before_tax varchar(50) character set utf8, #未稅銷售總金額
    # average_unit_price varchar(50) character set utf8, #平均單價
    # net_sales varchar(50) character set utf8, #銷售淨額
    # total_amount_of_discount varchar(50) character set utf8, #折價總金額
    # number_of_giveaways varchar(50) character set utf8, #贈品數量
    # weight varchar(50) character set utf8, #重量
    # giveaway_weight varchar(50) character set utf8, #贈品重量
    # cost_of_goods_sold varchar(50) character set utf8, #銷貨成本
    # gross_sales varchar(50) character set utf8, #銷售毛利
    # gross_profit_margin varchar(50) character set utf8, #毛利率
                #time.sleep(2)

                    #print("RowData[15]銷貨成本="+str(RowData[15]))
                    #print("RowData[16]毛利率="+str(RowData[16]))
                    #print("RowData[17]發票聯數="+str(RowData[17]))
                    #print("RowData[18]業務員="+str(RowData[18]))
                    #print("RowData[19]廠別代號="+str(RowData[19]))
                    #print("RowData[20]庫別代號="+str(RowData[20]))#library_code		
                    #group=getGroup(str(RowData[2]))
                    #print("組別="+str(group))

        #             "+str(id)+"','"+str(product_name)+"','"+str(customer_code)+"','"+str(sale_date)+"','"+str(sales_number)+"','"+str(\
        # sales_quantity)+"','"+str(sales_packaging_quantity)+"','"+str(units)+"','"+str(currencies)+"','"+str(unit_price)+"','"+str(\
        # original_currency_untaxed_amount)+"','"+str(untaxed_amount_in_local_currency)+"','"+str(\
        # cost_of_goods_sold)+"','"+str(gross_profit_margin)+"','"+str(invoice_coupon)+"','"+str(departments)+"','"+str(\
        # factory_code)+"','"+str(library_code)+"'\
                    # print(RowData[21])
                    # print(RowData[22])
                    # print(RowData[23])
                    # print(RowData[24])
                    # print(RowData[25])
                    # print(RowData[26])
                    # # DateRowData=str(RowData[9])
                    # print("max_row = "+str(max_row))

                    # RowData[6]=str(RowData[6]).replace(" ", "").replace("\n", "")
                insertSsqData(id,year,month,RowData[0],store_code,RowData[1],RowData[2],RowData[3],RowData[4],RowData[5],RowData[6],RowData[7],RowData[8],RowData[9],RowData[10],RowData[11],RowData[12],RowData[13],RowData[14])
                    #updateMonSqSum(RowData[2],RowData[14])

        # k=k+1
        print(k) 
        print(res) 
        if k<res:
            
            # sheetindex=k
            ws=wb.sheets[k]#翻頁籤
            # time.sleep(20)
        # try:
            
        # except Exception as e:
            # print(k) 
            # print(e)  
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
    # main("S:\網通部\◎資訊\年月均銷量表\COPR2320210204000156202102040001.XLSX")
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210824000056202108240001.XLS")#2020
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210826000068202108260001.XLS")#2021/1~2021/7
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210830000154202108300001.XLSX")
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210831000508202108310001.XLS")#2020
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210831000509202108310001.XLS")#2021/01/01~2021/07/31
    #getDataUpdateTime("C020700001")
    

    tz = timezone(timedelta(hours=+8))
    date = datetime.datetime.now(tz)
    result = date.strftime("%H:%M")


    #root = tk.Tk()
    #root.withdraw()
    #messagebox.showinfo('my messagebox', 'hello world')

    


    today=d.Date()
    #正式
    #msgbox(result == "16:00")
    #if result >= "16:00" and result <= "16:59":
        #messagebox.showinfo('my messagebox', str(today.getYear(days=1)))
        #(x)file_name=str("C:\My Documents\\") + str("COPR23") + str(today.getYear(days=1))+str("1207")+str("000332")+str(today.getYear(days=1))+ str(today.getMonth(days=1))+ str(today.getDay(days=1)).zfill(2)+str("0001.XLSX")
    #    file_name=str("C:\My Documents\\") + str("COPR23") + str("2021")+str("1207")+str("000332")+str(today.getYear(days=1))+ str(today.getMonth(days=1)).zfill(2)+ str(today.getDay(days=1)).zfill(2)+str("0001.XLSX")
        #messagebox.showinfo('my messagebox', 'case1')
    #else:
        #(x)file_name=str("C:\My Documents\\") + str("COPR23") + str(today.getYear(days=1))+str("1027")+str("000070")+str(today.getYear(days=1))+ str(today.getMonth(days=1))+ str(today.getDay(days=1)).zfill(2)+str("0001.XLSX")
    #    file_name=str("C:\My Documents\\") + str("COPR23") + str("2021")+str("1027")+str("000070")+str(today.getYear(days=1))+ str(today.getMonth(days=1)).zfill(2)+ str(today.getDay(days=1)).zfill(2)+str("0001.XLSX")
        #messagebox.showinfo('my messagebox', 'case2')
    #用前一天測試
    #file_name=str("C:\My Documents\\") + str("COPR23") + str(today.getYear(days=1))+str("1027")+str("000070")+str(today.getYear(days=1))+ str(today.getMonth(days=1))+ str(today.getDay(days=2))+str("0001.XLSX")
    #file_name = str("C:\My Documents\\") + "COPR2320211027000070202111160001.XLSX"


    #測試用
    #file_name = str(r"C:\\Users\\udev77\\Desktop\\") + str("POSR4020210922000213202201010001A.XLSX")
    c=d.Date()

    #print(c.getMonth(weeks=4))
    #print(c.getYear(weeks=4))
    report_month=c.getMonth(weeks=4)
    report_year=c.getYear(weeks=4)
    #print(report_month)
    #print(report_year)
    #print('%02d' % report_month)
    #月份補0
    report_month='%02d' % c.getMonth(weeks=4)
    
    #file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str("2022")+str("01")+str("01")+str("0001A.XLSX")
    file_name = str(r"C:\\My Documents\\") + str("POSR4020210922000213")+str(report_year)+str(report_month)+str("01")+str("0001A.XLSX")
    
    
    print(file_name)
    #time.sleep(20)
    #print(str("C:\My Documents\\") + "COPR2320211027000070202111130001.XLSX")
    main(file_name)
    #main("C:\My Documents\COPR2320211027000070202110270001.XLSX")#2021/10/27

    #getGroup('C010100001')
    #取得日期串，輸入檔名更新資料庫
    #COPR2320211027000070202110300001.XLSX
    #copr23+2021+1027+000070+2021+1030+0001
    #COPR2320211027000070202110300001.XLSX

    #copr23+2021+1027+000070+2021+1031+0001
    #copr23+年+1027+000070+年+月+昨天日期+0001

    #待輸入
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320210902000267202109020001.XLS")#2020/01/01~2021/08/31
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320211007000391202110070001.XLS")#2021/09/01~2021/10/06
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320211015000076202110150001.XLS")#2021/10/07
    #main("S:\網通部\◎資訊\年月均銷量表\COPR2320211027000064202110270001.XLS")#2021/10/08~2021/10/26
    #已輸入

    #main("C:\My Documents\COPR2320211027000070202110270001.XLSX")#2021/10/27
    #main("C:\My Documents\COPR2320211117000030202111170001.XLS")#2021/10/27~2021/11/16
    #main("C:\My Documents\COPR2320211027000070202111160001.XLSX")#2021/11/17


    # main("S:\開發部\◆業績資料\★開發部績效小幫手專用★\★產品折數表_申報優惠方式★確認版07.xls")
    # main2("S:\開發部\◆業績資料\★開發部績效小幫手專用★\康健年中慶+中元節促銷案-確定版(加品號).xlsx")