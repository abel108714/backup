from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

import time
import schedule
import time

from flask import request
from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest
import requests
import json
#from lib.db import Database
import psycopg2.extras
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import sys

from FileDataAccess import *




#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====
from datetime import datetime, timezone, timedelta
# 設定為 +8 時區
tz = timezone(timedelta(hours=+8))
date = datetime.now(tz)
yes_date = datetime.now(tz)-timedelta(days=1) 
#獲取今天的日期
y=str(date.year)

if int(date.month) < 10:
	m = '0' + str(date.month)
else:
	m = str(date.month)

if int(date.day) < 10:
	d = '0' + str(date.day)
else:
	d = str(date.day)

#獲取昨天的日期
yes_y=str(yes_date.year)

if int(yes_date.month) < 10:
	yes_m = '0' + str(yes_date.month)
else:
	yes_m = str(yes_date.month)

if int(yes_date.day) < 10:
	yes_d = '0' + str(yes_date.day)
else:
	yes_d = str(yes_date.day)
tdy_date_str = y + m + d
ysdy_date_str = yes_y + yes_m + yes_d
BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d


urls = []
for x in range(1,7):
    urls.append('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_'+ str(x) +'.jpg.jpg')
import requests as rq
#rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + '20200915' + '_1.jpg.jpg')
#if rqt.status_code == 200:
#    ysdy_date_str = ysdy_date_str + 'Web site exists'
#else:
#    ysdy_date_str = ysdy_date_str + 'Web site does not exist'
app = Flask(__name__)

#======python的函數庫==========
import tempfile, os
#import datetime
import time
#======python的函數庫==========
import json
from linebot import LineBotApi
from linebot.models import *

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token

#line_bot_api = LineBotApi('ZbWIGQOfoxOLqko0Fhh/OTjBMeeXrd+Py4xyAaNeFsa0bVP3vY05ZyOZEVj8cS9Zu+PDXGMfIUDzAGhFEjHVMN8J9ocEZsuGotbuRhzeQTML221ynVdVwXntBcIP4Ft+Sy0omAoemN84m8OxTJbFWQdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('vauGF3Izm5n9vuUeVjO6yPDCNCXXa5J7vX9dVGkD+R5gm0RzUJNK76EwMU4tH2WADcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4llQeprGrfPUI81yk/tXI88bQTyjgAvEc9OWcLp3RmyQdB04t89/1O/w1cDnyilFU=')
#line_bot_api = LineBotApi('NXL5slcCmS07Y27t7j7zGfe/2FHWeE/9Pm3XKk9cVhhD1Fuh7ATn6jlp4Y1RNaBtw+xlLb+5gLYF72LzaB2Oy2fneBAKy5GmONWlJOQAD2gqDhgvIpOtUdlMxbQr+hLix9NBgXu2AC69A5jRw8kOcQdB04t89/1O/w1cDnyilFU=')
#line_bot_api = LineBotApi('8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler = WebhookHandler('eeed6c17319b3f197e255e08bc2e98c3')
handler = WebhookHandler('b4ee9629a3ee5fd3a17142d34cc0598e')
#handler = WebhookHandler('b436af4b6826703b9437c8eb66af84ca')
#handler = WebhookHandler('3a4aed1e40707e83f48bf67ab2f418ed')

import json
import requests

import os
import re



from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


import requests




import json


import pymysql

import mysql.connector

import requests
import json



import requests

from linebot.models import RichMenu
import requests

def job2():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("1")))
    tz = timezone(timedelta(hours=+8))
    date = datetime.now(tz)
    print('123')
    print(str(date.strftime("%H:%M")))
    weekno = datetime.today().weekday()
    if weekno<6:
        #print("yes")
        #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=str(date.strftime("%H:%M"))))
        if date.strftime("%H:%M") == "17:41":#自動發網通報表
            print('case1')
            #網通群組
            line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
            #自己
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
            #測試用群組
            #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())
        elif date.strftime("%H:%M") == "07:30":#自動發門市報表
            print('case2')
            #怡君
            line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
            #測試用群組
            #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", StorePerformanceReport())
            #自己
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StorePerformanceReport())
        elif date.strftime("%H:%M") == "17:47":
            print('case3')
            #網通群組
            #line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
            #自己
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
            #測試用群組
            #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())
            #----------------------------------------------------------------------------------------
            #測試用群組
            #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", StorePerformanceReport())
            #怡君
            #line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
            #自己
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StorePerformanceReport())
            line_bot_api.push_message("C5fd1c0d2f75eb01ad8935d719076012b", OCPerformanceReport())
            #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", OCPerformanceReport())
        elif date.strftime("%H:%M") == "16:46":#測試用時間
            print('case4')
            
            #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", OCPerformanceReport())
    else:
        print("no")



        



#def job3():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("55556")))




#exe_t=0





# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
#@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    #print("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    #print('OK')
    return 'OK'

#def hello():
#	name=request.args.get("name","world")
#	return f'hello,{name}!'

schedule.every(1).minutes.do(job2)




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):#
        
        #
        #user_id = event.source.user_id
    #while True:
        msg = event.message.text
        user_id = event.source.user_id
        print('msg: ' + msg)
        print('user_id: ' + user_id)
        keymsg_regex = r"\W*[未][入][績][效]\s?"
        keymsg_str = msg
        keymsg_matches = re.search(keymsg_regex, keymsg_str)
        if keymsg_matches:
            keymsg_match = keymsg_matches.group()
            print('keymsg_match: ' + keymsg_match)
            
            regex = r"\W*[@]?\w*\W*[@]?\w*\W*[東][森][未][入][績][效]\W*\d*[/]\d*[止]\d*[,]?\d*[,]?\d*\D*"
            expected_perf_str = msg
            matches = re.search(regex, expected_perf_str)
            if matches:#訊息
                match = matches.group()
                print('match: ' + match)
                title_regex = r"\w*[東][森]\W*"
                title_matches = re.search(title_regex, expected_perf_str)
                if title_matches:#標題
                    title_match = title_matches.group()
                    print('title_match: ' + title_match)
                date_regex = r"\d*[/]\d*\W*"
                date_matches = re.search(date_regex, expected_perf_str)
                if date_matches:#日期
                    date_match = date_matches.group()
                    #print(date_match)
                    print('date_match:' + date_match.split('/')[1])
                amount_regex = r"[0-9]+[,]?[0-9]+[,]?[0-9]+[,]?[0-9]+"
                amount_matches = re.search(amount_regex, expected_perf_str)
                if amount_matches:#金額
                    amount_match = amount_matches.group()
                    print('amount_match: ' + amount_match)
                newDataAccess=FileDataAccess(0,'-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
                updateArr=[date_match.split('/')[1],amount_match]
                #寫入資料
                newDataAccess.setData(title_match,updateArr)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 已更新')))

            # else:
            #     keymsg_match = keymsg_matches.group()
            #     print(keymsg_match+'123')
                
            #     regex = r"\W*[@]?\w*\W*[@]?\w*\W*[博][客][來][未][入][績][效]\W*\d*[/]\d*[止]\d*[,]?\d*[,]?\d*\D*"
            #     expected_perf_str = msg
            #     matches = re.search(regex, expected_perf_str)
            #     if matches:#訊息
            #         match = matches.group()
            #         print(match)
            #         title_regex = r"\w*[博][客][來]\W*"
            #         title_matches = re.search(title_regex, expected_perf_str)
            #         if title_matches:#標題
            #             title_match = title_matches.group()
            #             print(title_match)
            #         date_regex = r"\d*[/]\d*\W*"
            #         date_matches = re.search(date_regex, expected_perf_str)
            #         if date_matches:#日期
            #             date_match = date_matches.group()
            #             print(date_match)
            #             print(date_match.split('/')[1])
            #         amount_regex = r"[0-9]+[,]?[0-9]+[,]?[0-9]+[,]?[0-9]+"
            #         amount_matches = re.search(amount_regex, expected_perf_str)
            #         if amount_matches:#金額
            #             amount_match = amount_matches.group()
            #             print(amount_match)
            #         newDataAccess=FileDataAccess(0,'-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
            #         updateArr=[date_match.split('/')[1],amount_match]
            #         print(newDataAccess.setData(title_match,updateArr))
            #         line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 已更新')))
        #if '最新合作廠商' in msg:
            #message = imagemap_message()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif '最新活動訊息' in msg:
            #message = buttons_message()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif '註冊會員' in msg:
            #message = Confirm_Template()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif '旋轉木馬' in msg:
            #message = Carousel_Template()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif '圖片畫廊' in msg:
            #message = image_carousel_message1()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif '功能列表' in msg:
            #message = function_list()
            #line_bot_api.reply_message(event.reply_token, message)
        #if '門市業績報表' in msg:
            # message = image_carousel_message1()
            #message = StorePerformanceReport()
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif '門市部日報表' in msg:
            # message = image_carousel_message1()
            #message = StorePerformanceReport()
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif 'R' in msg:
            # message = image_carousel_message1()
            #message = TextSendMessage(text="https://raw.githubusercontent.com/abel108714/test/master/" + BegMonthOfTodayPeriod + "網通目標達成比.jpg")
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif 'SS' in msg:
            # message = image_carousel_message1()
            #message = StorePerformanceReport()
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif 'ss' in msg:
            # message = image_carousel_message1()
            #message = StorePerformanceReport()
            #line_bot_api.reply_message(event.reply_token, message)
        #elif 'PA' in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            #message = PAPerformanceReport()
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            #line_bot_api.reply_message(event.reply_token, message)    
        #elif BegMonthOfTodayPeriod + '累計達成比' in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            #message = OCPerformanceReport()
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif msg in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            #message = SpecOCPerformanceReport(msg)
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            #line_bot_api.reply_message(event.reply_token, message)  
        #elif event.message.text == 'ID?' or event.message.text == 'id?':
            #User_ID = TextMessage(text=event.source.user_id)
            #line_bot_api.reply_message(event.reply_token, User_ID)
            #print ('Reply User ID =>' + event.source.user_id)
        #elif event.message.text == 'GroupID?':
            #Group_ID = TextMessage(text=event.source.group_id)
            #line_bot_api.reply_message(event.reply_token, Group_ID)
            #print ('Reply Group ID =>' + event.source.group_id)
        if 'run' in msg:

            #User_ID = TextMessage(text=event.source.user_id)
            #line_bot_api.reply_message(event.reply_token, message)

            #CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
            #to = str(event.source.user_id)#"YOUR USER ID"
            #line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

            #文字訊息
            #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #try:
            #profile = line_bot_api.get_profile('')
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(int(date.strftime("%H%M")))))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(profile.display_name)))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.user_id)))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.group_id)))
            # 建立Connection物件
            #conn = pymysql.connect(**db_settings)
            # 建立Cursor物件
            #try:
                #mydb=mysql.connector.connect(
                #    host= '127.21.7.39',
                #    port= '3306',
                #    user= 'root',
                #    password= '16264386',
                #    db= 'usersDB'
                #)
                #cur=mydb.cursor()
                #sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
                #my_id=str(event.source.user_id)
                #data=(my_id,'',str(profile.display_name),'')
                #cur.execute(sql,data)
                #mydb.commit()
            profile = line_bot_api.get_profile(event.source.user_id)
            message = TextSendMessage(text=str(profile.display_name))
            #try:
                #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(event.source.group_id)))
                #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", TextSendMessage(text=str(event.source.group_id)))
            #except:#AttributeError
                #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(event.source.user_id)))
                #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", TextSendMessage(text=str(event.source.user_id)))

            # try:
            #     db_settings = {
            #         "host": "127.21.7.39",
            #         "port": 3306,
            #         "user": "root",
            #         "password": "16264386",
            #         "db": "usersDB",
            #         "charset": "utf8"
            #     }
            #     # 建立Connection物件
            #     conn = pymysql.connect(**db_settings)
            #     # 建立Cursor物件
            #     with conn.cursor() as cursor:
            #         sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
            #         data=(str(event.source.user_id),'',str(profile.display_name),'')
            #         cursor.execute(sql,data)
            #         conn.commit()
            #     print('sql done.')
            # except:
            #     print('sql except.')
                

            
            #U03f8575fac6ad12b612c6222ad37678e'
            #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str(event.source.user_id)))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.user_id)))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(profile.display_name)))
            #print('0')
            
            #line_bot_api.push_message(event.source.user_id, TextSendMessage(text=str("1")))
            #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", TextSendMessage(text=str("1")))
            #U03f8575fac6ad12b612c6222ad37678e 2號id

            

            #select checked from users where UID="U03f8575fac6ad12b612c6222ad37678e";
            #with mydb.cursor() as cursor:

            mydb = mysql.connector.connect(
                host = "127.21.7.39",
                port = 3306,
                user = "root",
                password = "16264386",
                db = "usersDB",
                charset = "utf8"
            )
            cursor = mydb.cursor()
            try:
                sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
                data=(str(event.source.user_id),'',str(profile.display_name),'')
                cursor.execute(sql,data)
                conn.commit()
                print('sql done.')
            except:
                print('sql except.')

                #檢查是否有發過報表，檢查checked的日期
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(event.source.user_id)+"已記錄"))
                sql="select checked from users where UID=\""+str(event.source.user_id)+"\""
                cursor.execute(sql)
                for myresult in cursor.fetchall():
                    my_data=myresult[0]
                print(my_data)
                mydb.commit()
                if str(tdy_date_str) == my_data:#若跟今天日期相同，則代表已發過報表，跳出函式
                    print('已發過報表')
                    #sys.exit() 
            
            try:
                #記錄checked的日期
                sql="UPDATE users SET checked=\""+str(tdy_date_str)+"\" where UID=\""+str(event.source.user_id)+"\"" 
                cursor.execute(sql)
                mydb.commit()
                

                cursor.close()#最後在關閉
                print("已儲存")
                working_count=0
                while True:
                    # for working_count in [0,1,2]:
                    #     if working_count==0:
                    #         cls()    
                    #         print('working.')
                    #         time.sleep(1)
                    #     elif working_count==1:
                    #         cls()
                    #         print('working..')
                    #         time.sleep(1)
                    #     elif working_count==2:
                    #         cls()
                    #         print('working...')
                    #         time.sleep(1)                   
                    schedule.run_pending()
                    time.sleep(1)
            except:
                print("未儲存")
            #myresult = cursor.fetchall()#fetchone()#fetchall()
            #print('myresult:'+ str(myresult).strip('[').strip(']'))
            #mydb.commit()
            #cursor.close()
            #print('myresult:'+ str(myresult).strip('[').strip(']'))
            # if str(myresult).strip('[').strip(']') != "":
            #     print('4')
            # if str(myresult).strip('[').strip(']') != tdy_date_str:
            #     print('6')

            # if str(myresult).strip('[').strip(']') == "":
            #     print('5')

            #for x in myresult:
            #    print(4)
            #    print(x)

                    #cursor.execute('SELECT * FROM users;')
                    #data = cursor.fetchone()     
                    #index = data[0]
                    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(index)))
                        # 儲存變更
                    #conn.commit()
                    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(profile.display_name)+"已記錄"))
            # 資料庫設定



            #cursor.execute('SELECT * FROM users;')
            #data = cursor.fetchone()     
            #except:
                #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("資料庫未連線")))
            
            #cur=mydb.cursor()
            #sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
            #my_id=str(event.source.user_id)
            #data=(my_id,'',str(profile.display_name),'')
            #cur.execute(sql,data)
            #mydb.commit()
            
            
            
 
            # 建立Cursor物件
            #with conn.cursor() as cursor:
            #    sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
            #    data=(5,'網通',3,4)
            #    cursor.execute(sql,data)
                # 儲存變更
            #    conn.commit()
            #with conn.cursor() as cursor:

            #if my_id == "" :
                #my_id = event.source.group_id
            
            #cursor.execute(sql,data)




                # 儲存變更
                #conn.commit()

            #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("123")))
            #while date.strftime("%H:%M") == "16:31":
                #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("333")))
            #line_bot_api.push_message(to, TextSendMessage(text=str(date.minutes)))
            #line_bot_api.push_message(to, TextSendMessage(text=str(date.seconds)))
            #except LineBotApiError as e:
                # error handle
                #raise e
            #message = TextSendMessage(text=event.source.user_id)
            #line_bot_api.reply_message(event.reply_token, message)   
        else:
            #message = TextSendMessage(text=msg)
            #message = TextSendMessage(text="")
            #message = SpecOCPerformanceReport(msg)
            #line_bot_api.reply_message(event.reply_token, message)
            #profile = line_bot_api.get_profile(event.source.user_id)
            #message = TextSendMessage(text=str(profile.display_name))
            #User_ID = TextMessage(text=event.source.user_id)
            #line_bot_api.reply_message(event.reply_token, message)
            print("else")
            #CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
            #to = str(event.source.user_id)#"YOUR USER ID"
            #line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

            #文字訊息
            #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #try:
            #profile = line_bot_api.get_profile('')
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(int(date.strftime("%H%M")))))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.group_id)))
            #while True:
                #now_t=int(int(date.strftime("%H"))*60+int(date.strftime("%M")))
                #set_t=int(11*60+11)
                #exe_t=set_t-now_t
                #schedule.run_pending()
                #time.sleep(1)
    



    #if date.strftime("%H:%M") == "16:11":
    #    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("123")))
    #else:
    #    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("456")))
    
    
    #if date.strftime("%H:%M") == "16:19":
    #    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("333")))



    #elif '報表' in msg:
        #message = TextSendMessage(text=str(getOSMCAppendFileName()))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif 'O' in msg:
        #message = TextSendMessage(text=str(datetime.now(tz).isoformat()))
        #line_bot_api.reply_message(event.reply_token, message)    
    #elif 'T' in msg:
        #message = TextSendMessage(text=str(tdy_date_str))
        #line_bot_api.reply_message(event.reply_token, message)    
    #elif 'Y' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '1' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[0]))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '2' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[1]))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '3' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[2]))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '4' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[3]))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '5' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[4]))
        #line_bot_api.reply_message(event.reply_token, message)   
    #elif '6' in msg:
        #message = TextSendMessage(text=str(ysdy_date_str) + str(urls[5]))
        #line_bot_api.reply_message(event.reply_token, message)   


#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
    # get user id when reply
    #user_id = event.source.user_id
    #return user_id
    #print("user_id =", user_id)

#CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
#to = "YOUR USER ID"
#line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

#文字訊息

#try:
#    line_bot_api.push_message(to, TextSendMessage(text='台科大電腦研習社'))
#except LineBotApiError as e:
#    # error handle
#    raise e
#if date.strftime("%H:%M") == "08:52":
#    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("222")))
#while date.strftime("%H:%M") == "08:52":
#    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("333")))
#if date.strftime("%H:%M") == "08:52":
#    line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
import subprocess, platform
def cls():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
    else: #Linux and Mac
        print("\033c", end="")



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)





#Line bot參數設定，及傳遞訊息涵式
#line_bot_api = LineBotApi(channel_access_token)

#schedule.every().day.at("16:17").do(handle_message)


