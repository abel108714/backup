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
#line_bot_api = LineBotApi('vauGF3Izm5n9vuUeVjO6yPDCNCXXa5J7vX9dVGkD+R5gm0RzUJNK76EwMU4tH2WADcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4llQeprGrfPUI81yk/tXI88bQTyjgAvEc9OWcLp3RmyQdB04t89/1O/w1cDnyilFU=')
#line_bot_api = LineBotApi('NXL5slcCmS07Y27t7j7zGfe/2FHWeE/9Pm3XKk9cVhhD1Fuh7ATn6jlp4Y1RNaBtw+xlLb+5gLYF72LzaB2Oy2fneBAKy5GmONWlJOQAD2gqDhgvIpOtUdlMxbQr+hLix9NBgXu2AC69A5jRw8kOcQdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler = WebhookHandler('eeed6c17319b3f197e255e08bc2e98c3')
#handler = WebhookHandler('b4ee9629a3ee5fd3a17142d34cc0598e')
#handler = WebhookHandler('b436af4b6826703b9437c8eb66af84ca')
handler = WebhookHandler('3a4aed1e40707e83f48bf67ab2f418ed')

import json
import requests
access_token = '8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU='
userId = 'U03f8575fac6ad12b612c6222ad37678e'#'U03f8575fac6ad12b612c6222ad37678e'
profile_data = {'Authorization': 'Bearer ' + access_token}

profile = requests.get('https://api.line.me/v2/bot/profile/'+ userId, headers=profile_data)
#print(profile.text)
y = json.loads(profile.text)
user_id = str(y['userId'])
print(user_id)
import os

print(os.getcwd()) #打印出当前工作路径 
#create
rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=843),
    selected=False,
    name="Nice richmenu",
    chat_bar_text="Tap here",
    areas=[RichMenuArea(
        bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
        action=URIAction(label='Go to line.me', uri='https://line.me'))]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
print(rich_menu_id)
file_path='C:\linebot_test\demofile2.txt'
f = open(file_path, 'r')

print(f.read())
f.close()

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


#upload
file_path='C:\linebot_test\image.jpg'#os.getcwd()+"\image.jpg"
print(file_path)
content_type="image/jpg"#"image/jpeg"
print(content_type)
#Download
#content = line_bot_api.get_rich_menu_image(rich_menu_id)
#print(content)
#with open(file_path, 'wb') as fd:
#    for chunk in content.iter_content():
#        fd.write(chunk)
#with open(file_path, 'rb') as f:
#    line_bot_api.set_rich_menu_image(rich_menu_id, content_type, f)

#from linebot import LineBotApi
#from linebot.exceptions import LineBotApiError

#get_rich_menu_list
#rich_menu_list = line_bot_api.get_rich_menu_list()
#rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
#line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)

#get_rich_menu
#rich_menu_id = line_bot_api.get_rich_menu_id_of_user(user_id)




access_token = '8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU='
profile_data = {'Authorization': 'Bearer ' + access_token}

profile = requests.get('https://api.line.me/v2/profile/', headers=profile_data)
#print(profile)

headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
profile = requests.get('https://api.line.me/v2/profile/', headers=headers)
#print(profile)
#U03f8575fac6ad12b612c6222ad37678e

req = requests.request('GET', 'https://api.line.me/v2/profile/', headers=profile_data)
print(req)


import requests
#access_token = 'C..='
userId = 'U03f8575fac6ad12b612c6222ad37678e'#'U03f8575fac6ad12b612c6222ad37678e'
profile_data = {'Authorization': 'Bearer ' + access_token}

profile = requests.get('https://api.line.me/v2/profile', headers=profile_data)
print(profile)

#user_id = str(profile['userId'])
#displayName = str(profile['displayName'])
#pictureUrl = str(profile['pictureUrl'])
#statusMessage = str(profile['statusMessage'])
#print(user_id)
#print(displayName)
#print(pictureUrl)
#print(statusMessage)


#richmenu=RichmenuApiRelateController(line_bot_api,handler)




import json


import pymysql
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
import mysql.connector

import requests
import json

headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
          "action": {"type": "message", "text": "up"}
        },
        {
          "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "right"}
        },
        {
          "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
          "action": {"type": "message", "text": "down"}
        },
        {
          "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "left"}
        },
        {
          "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn b"}
        },
        {
          "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn a"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(eval(req.text.strip('}').split(':')[1]))
print(req.text)
            #data=json.dumps({
            #    'userIds': user_ids,
            #    'richMenuId': rich_menu_id,
            #}),
            #GET https://api.line.me/v2/profile
req = requests.request('GET', 'https://api.line.me/v2/profile',headers=headers)
print('test1')
print(req.text)

displayName=""
pictureUrl =""
statusMessage=""
body = {
  "userId":userId,
  "displayName":displayName,
  "pictureUrl":pictureUrl,
  "statusMessage":statusMessage
}
req = requests.request('GET', 'https://api.line.me/v2/profile/', headers=headers,data=json.dumps(body).encode('utf-8'))
#https://developers.line.biz/en/docs/social-api/getting-user-profiles/#status-codes
#https://stackoverflow.com/questions/45158199/how-to-get-friends-list-and-friends-profile-on-line-api-using-php-or-shell-scr
print(req)
#with open("control.jpg", 'rb') as f:
#    line_bot_api.set_rich_menu_image("richmenu-70c42235c471b3aa413032a3c275670a", "image/jpeg", f)


import requests

headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-70c42235c471b3aa413032a3c275670a', 
                       headers=headers)

print(req.text)
user_ids = 'U03f8575fac6ad12b612c6222ad37678e'
rich_menu_id = 'richmenu-70c42235c471b3aa413032a3c275670a'
req = requests.request('POST','https://api.line.me/v2/bot/richmenu/bulk/link',headers=headers,data=json.dumps(body).encode('utf-8'))
print(req)
#https://api.line.me/v2/bot/followers/ids

req = requests.request('GET','https://api.line.me/v2/bot/followers/ids',headers=headers)
print(req)
from linebot.models import RichMenu
import requests


#rich_menu_list = line_bot_api.get_rich_menu_list()

#for rich_menu in rich_menu_list:
    #print(rich_menu.rich_menu_id)
# 載圖文選單轉成json
#menuJson=json.loads(menuRawData)
# 拿圖文選單設定檔，請line_bot_api創圖文選單
#lineRichMenuId = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(menuJson))
# 打印圖文選單編號
#print(lineRichMenuId)
#from linebot import (
#    LineBotApi, WebhookHandler
#)

#line_bot_api = LineBotApi('3Ma92PMIfy790Z...')



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
def job2(event):
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("1")))
    tz = timezone(timedelta(hours=+8))
    date = datetime.now(tz)
    print(str(date.strftime("%H:%M")))
    #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=str(date.strftime("%H:%M"))))
    if date.strftime("%H:%M") == "17:45":#自動發網通報表
        print('case1')
        #網通群組
        line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
        #自己
        line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
        #測試用群組
        #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())
    elif date.strftime("%H:%M") == "07:45":#自動發門市報表
        print('case2')
        #怡君
        line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
        #測試用群組
        #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", StorePerformanceReport())
        #自己
        line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StorePerformanceReport())
    elif date.strftime("%H:%M") == "17:42":
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
    elif date.strftime("%H:%M") == "16:06":#測試用時間
        print('case4')
        
        #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", OCPerformanceReport())

        



def job3():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("55556")))




#exe_t=0


#schedule.every(exe_t).minutes.do(job3) 
#schedule.every(exe_t).minutes.do(job3) 
#schedule.every().wednesday.at("10:42").do(job3)
#schedule.every().wednesday.at("10:45").do(job3)
#schedule.every().wednesday.at("10:47").do(job3)
#schedule.every().day.at("13:50").do(job3)
#schedule.every().day.at("10:17").do(job3)
#schedule.every().day.at("10:18").do(job3)


#line_bot_api = LineBotApi('R60lcR7k2nfcCzSfkRpAFkv6DoiXwJLIBf+zdR8qBfRig60rEZrAoTbWd3pLvmuwJ99ko49MPfPOSuxFy2a/ztkgz7UTbnSFb9BHMKR9viDEVCYirsPhufBz3EE6jllolMzE5DE2wMqKNWP7Xui1vQdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler = WebhookHandler('55efd2ee0104755237f28a9567334f3b')
handler = WebhookHandler('3a4aed1e40707e83f48bf67ab2f418ed')




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




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):#
        schedule.every(1).minutes.do(job2,event)  
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
        elif 'PA' in msg:
            # message = image_carousel_message1()
            #name = str(getOSMCAppendFileName())
            message = PAPerformanceReport()
            #message = TextSendMessage(text=str(OCPerformanceReport()))
            line_bot_api.reply_message(event.reply_token, message)    
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
        elif event.message.text == 'ID?' or event.message.text == 'id?':
            User_ID = TextMessage(text=event.source.user_id)
            line_bot_api.reply_message(event.reply_token, User_ID)
            #print ('Reply User ID =>' + event.source.user_id)
        elif event.message.text == 'GroupID?':
            Group_ID = TextMessage(text=event.source.group_id)
            line_bot_api.reply_message(event.reply_token, Group_ID)
            #print ('Reply Group ID =>' + event.source.group_id)
        elif 'run' in msg:

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
                    sys.exit() 
            
            try:
                #記錄checked的日期
                sql="UPDATE users SET checked=\""+str(tdy_date_str)+"\" where UID=\""+str(event.source.user_id)+"\"" 
                cursor.execute(sql)
                mydb.commit()
                

                cursor.close()#最後在關閉
                print("已儲存")
                working_count=1
                while True:
                    if working_count>0:
                        #cls()    
                        print('working...\\')
                    else:
                        #cls()
                        print('working.../')
                    working_count=working_count*-1
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
            message = TextSendMessage(text="")
            #message = SpecOCPerformanceReport(msg)
            #line_bot_api.reply_message(event.reply_token, message)
            #profile = line_bot_api.get_profile(event.source.user_id)
            #message = TextSendMessage(text=str(profile.display_name))
            #User_ID = TextMessage(text=event.source.user_id)
            line_bot_api.reply_message(event.reply_token, message)

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


