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



#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)

#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====
from datetime import datetime, timezone, timedelta
# 設定為 +8 時區
tz = timezone(timedelta(hours=+8))
date = datetime.now(tz)
y=str(date.year)
if int(date.month) < 10:
	m = '0' + str(date.month)
else:
	m = str(date.month)
#獲取今天的日期
if int(date.day) < 10:
	d = '0' + str(date.day)
else:
	d = str(date.day)
#獲取昨天的日期
if int(date.day-1) < 10:
	yes_d = '0' + str(date.day-1)
else:
	yes_d = str(date.day-1)
tdy_date_str = y + m + d
ysdy_date_str = y + m + yes_d

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

# Channel Access Token
#line_bot_api = LineBotApi('ZbWIGQOfoxOLqko0Fhh/OTjBMeeXrd+Py4xyAaNeFsa0bVP3vY05ZyOZEVj8cS9Zu+PDXGMfIUDzAGhFEjHVMN8J9ocEZsuGotbuRhzeQTML221ynVdVwXntBcIP4Ft+Sy0omAoemN84m8OxTJbFWQdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('vauGF3Izm5n9vuUeVjO6yPDCNCXXa5J7vX9dVGkD+R5gm0RzUJNK76EwMU4tH2WADcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4llQeprGrfPUI81yk/tXI88bQTyjgAvEc9OWcLp3RmyQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler = WebhookHandler('eeed6c17319b3f197e255e08bc2e98c3')
handler = WebhookHandler('b4ee9629a3ee5fd3a17142d34cc0598e')

import json


#import pymysql
#import charts
# 資料庫設定
#db_settings = {
#    "host": "127.21.7.39",
#    "port": 3306,
#    "user": "root",
#    "password": "16264386",
#    "db": "usersDB",
#    "charset": "utf8"
#}
#import mysql.connector

#mydb=mysql.connector.connect(
#    host= '127.21.7.39',
#    port= 3306,
#    user= 'root',
#    password= '16264386',
#    db= 'usersDB'
#)


#讀入LINE BOT序號
#with open("data/line_bot_secrets.txt", "r") as json_file:
#  secrets = json.load(json_file)
#  channel_access_token =secrets[0]["Secret"]
#  your_id=secrets[0]["ID"]

#Line bot參數設定，及傳遞訊息涵式
#line_bot_api = LineBotApi(channel_access_token)
#def noti(data):
#  for i in data:
#    srt=""
#    for l in i:
#      srt+=l+":"+i[l]+","
#    print("send:",srt.rstrip(",")) 
#    line_bot_api.push_message(your_id, TextSendMessage(text=srt.rstrip(",")))
#  return True
def job2():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("1")))
    tz = timezone(timedelta(hours=+8))
    date = datetime.now(tz)
    #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=str(date.strftime("%H:%M"))))
    if date.strftime("%H:%M") == "17:48":
        #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("222")))
        #Uee6224531167e863e3c08504055d6ed2
        #C4ec4e31c55ca25cc823f5ab5b4e1b040  測試用id
        #Caa547d0a89e353969160556a34444c64  網通群組id

        line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", TextSendMessage(text=BegMonthOfTodayPeriod + '累計達成比'))
        line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
    elif date.strftime("%H:%M") == "10:02":       
        line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=BegMonthOfTodayPeriod + '累計達成比'))
        line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())



def job3():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("55556")))




#exe_t=0

schedule.every(1).minutes.do(job2) 
#schedule.every(exe_t).minutes.do(job3) 
#schedule.every(exe_t).minutes.do(job3) 
#schedule.every().wednesday.at("10:42").do(job3)
#schedule.every().wednesday.at("10:45").do(job3)
#schedule.every().wednesday.at("10:47").do(job3)
#schedule.every().day.at("13:50").do(job3)
#schedule.every().day.at("10:17").do(job3)
#schedule.every().day.at("10:18").do(job3)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
#@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):#
    #while True:
        msg = event.message.text

            #user_id = event.source.user_id
    
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
        if '門市業績報表' in msg:
            # message = image_carousel_message1()
            message = StorePerformanceReport()
            line_bot_api.reply_message(event.reply_token, message)  
        elif '門市部日報表' in msg:
            # message = image_carousel_message1()
            message = StorePerformanceReport()
            line_bot_api.reply_message(event.reply_token, message)  
        #elif 'R' in msg:
            # message = image_carousel_message1()
            #message = TextSendMessage(text="https://raw.githubusercontent.com/abel108714/test/master/" + BegMonthOfTodayPeriod + "網通目標達成比.jpg")
            #line_bot_api.reply_message(event.reply_token, message)  
        elif 'SS' in msg:
            # message = image_carousel_message1()
            message = StorePerformanceReport()
            line_bot_api.reply_message(event.reply_token, message)  
        elif 'ss' in msg:
            # message = image_carousel_message1()
            message = StorePerformanceReport()
            line_bot_api.reply_message(event.reply_token, message)  
        elif BegMonthOfTodayPeriod + '累計達成比' in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            message = OCPerformanceReport()
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            line_bot_api.reply_message(event.reply_token, message)  
        #elif msg in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            #message = SpecOCPerformanceReport(msg)
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            #line_bot_api.reply_message(event.reply_token, message)  
        elif event.message.text == 'ID?' or event.message.text == 'id?':
            User_ID = TextMessage(text=event.source.user_id)
            line_bot_api.reply_message(event.reply_token, User_ID)
            #print ('Reply User ID =>' + event.source.user_id)
        elif event.message.text == 'GroupID?':
            Group_ID = TextMessage(text=event.source.group_id)
            line_bot_api.reply_message(event.reply_token, Group_ID)
            #print ('Reply Group ID =>' + event.source.group_id)
        elif 'test' in msg:
            profile = line_bot_api.get_profile(event.source.user_id)
            message = TextSendMessage(text=str(profile.display_name))
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
            line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(profile.display_name)))
            line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.user_id)))
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.group_id)))
            # 建立Connection物件
            #conn = pymysql.connect(**db_settings)
            # 建立Cursor物件
            #cur=mydb.cursor()
            #with conn.cursor() as cursor:
            #sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
            #my_id=str(event.source.user_id)
            #if my_id == "" :
                #my_id = event.source.group_id
            #data=(my_id,'',str(profile.display_name),'')
            #cursor.execute(sql,data)
            #cur.execute(sql,data)
            #mydb.commit()
                # 儲存變更
                #conn.commit()
            while True:
                #now_t=int(int(date.strftime("%H"))*60+int(date.strftime("%M")))
                #set_t=int(11*60+11)
                #exe_t=set_t-now_t
                schedule.run_pending()
                time.sleep(1)
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
            profile = line_bot_api.get_profile(event.source.user_id)
            message = TextSendMessage(text=str(profile.display_name))
            #User_ID = TextMessage(text=event.source.user_id)
            #line_bot_api.reply_message(event.reply_token, message)

            #CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
            #to = str(event.source.user_id)#"YOUR USER ID"
            #line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

            #文字訊息
            #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #try:
            #profile = line_bot_api.get_profile('')
            line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(int(date.strftime("%H%M")))))
            line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str(event.source.group_id)))
            while True:
                #now_t=int(int(date.strftime("%H"))*60+int(date.strftime("%M")))
                #set_t=int(11*60+11)
                #exe_t=set_t-now_t
                schedule.run_pending()
                time.sleep(1)
    



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

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)





#Line bot參數設定，及傳遞訊息涵式
#line_bot_api = LineBotApi(channel_access_token)

#schedule.every().day.at("16:17").do(handle_message)


