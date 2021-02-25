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
# from flask_restful import Resource, reqparse
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
import Date as d


# from controller.notify_controller import NotifyController
# from controller.notify_sqs_controller import SendNotifyBySQSController
# from controller.message_api_controller import LineMessageApiWebhookController
# from richmenu_api_controller import RichmenuApiRelateController
# # from controller.line_login_controller import LineLoginController
# # from dotenv import load_dotenv
# # env_path = Path('.') / '.env'
# # load_dotenv(dotenv_path=env_path)
# from flask_restful import Api
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)
# api = Api(app)

# # api.add_resource(NotifyController, '/notify')
# # api.add_resource(SendNotifyBySQSController, '/notify/sqs')
# # api.add_resource(LineMessageApiWebhookController, '/webhook')
# api.add_resource(RichmenuApiRelateController, '/richmenu')

# api.add_resource(LineLoginController, '/line/auth')
# headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

# body = {
#     "size": {"width": 2500, "height": 1686},
#     "selected": "true",
#     "name": "Controller",
#     "chatBarText": "Controller",
#     "areas":[
#         {
#           "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
#           "action": {"type": "message", "text": "up"}
#         },
#         {
#           "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
#           "action": {"type": "message", "text": "right"}
#         },
#         {
#           "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
#           "action": {"type": "message", "text": "down"}
#         },
#         {
#           "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
#           "action": {"type": "message", "text": "left"}
#         },
#         {
#           "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
#           "action": {"type": "message", "text": "btn b"}
#         },
#         {
#           "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
#           "action": {"type": "message", "text": "btn a"}
#         }
#     ]
#   }

# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
# print(eval(req.text.strip('}').split(':')[1]))
# rich_menu_id = eval(req.text.strip('}').split(':')[1])
# print(req.text)

# try:
#     # with open("C:\\linebot\\image.jpg", 'rb') as f:
#     with open("https://github.com/abel108714/test/blob/master/image.jpg", 'rb') as f:
#         line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
# except Exception as e:
#     print("===Upload Exception===")


# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",
#     chat_bar_text="Tap here",
#     areas=[RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=URIAction(label='Go to line.me', uri='https://line.me'))]
# )
# print("run2")
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# # print("run3")
# # with open("image.jpg", 'rb') as f:
# #     line_bot_api.set_rich_menu_image(rich_menu_id, content_type, f)
# # print("run5")
# # rich_menu_id="richmenu-ed45cf9c43f86c20059bb811cab8e37a"
# # line_bot_api.get_rich_menu(self,rich_menu_id,timeout = None)
# print("run6")
# line_bot_api.link_rich_menu_to_user("Uee6224531167e863e3c08504055d6ed2", str(rich_menu_id))
# print(str(rich_menu_id))
# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+str(rich_menu_id),headers=headers)
# print(req.text)
# print("run6")
# curl -v -X POST https://api-data.line.me/v2/bot/richmenu/richmenu-ed45cf9c43f86c20059bb811cab8e37a/content ^
# -H "Authorization: Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=" ^
# -H "Content-Type: image/jpeg" ^
# -T image.jpg
# req = requests.request('POST', 'https://api-data.line.me/v2/bot/richmenu/'+str(rich_menu_id)+'/content', 
#                        headers=headers,data=json.dumps(body).encode('utf-8'))


# body = {
#     "Content-Type":"application/json"
# }
# req = requests.request('GET', 'https://api.line.me/v2/bot/richmenu/'+eval(req.text.strip('}').split(':')[1]), 
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
# print(req.text)
# requests.request('POST', 'https://api.line.me/v2/bot/richmenu')
# from linebot import (
#     LineBotApi, WebhookHandler
# )

# # line_bot_api = LineBotApi('3Ma92PMIfy790Z...')
# f = open("C:\\Users\\udev77\\Desktop\\image.jpg", "r")
# # with open("C:\\Users\\udev77\\Desktop\\image.jpg", 'rb') as f:
# line_bot_api.set_rich_menu_image('richmenu-4bd2876e032a1c8a9744b814c00eeb16', "image/jpeg", f)
# from linebot import (
#     LineBotApi, WebhookHandler
# )

# # line_bot_api = LineBotApi('3Ma92PMIfy790Z...')

# # with open("C:\\Users\\udev77\\Desktop\\image.jpg", 'rb') as f:
# #     line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
# print(rich_menu_id)

# from linebot import (
#     LineBotApi, WebhookHandler
# )

# with open("C:\\linebot\\image.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
# try:
#     with open("C:\\linebot\\image.jpg", 'rb') as f:
# # rich_menu_id = request.form['richmenu_id']
#         content_type = "image/jpeg"
#     # # 打開一個圖片檔，並存回uploadImageFile變數內
#     # uploadImageFile=open("C:\\Users\\udev77\\Desktop\\image.jpg",'rb')
#     # # 請line_bot_api將圖片上傳到剛剛創建的圖文選單id內
#     # setImageResponse = line_bot_api.set_rich_menu_image(str(rich_menu_id),'image/jpeg',uploadImageFile)
#         line_bot_api.set_rich_menu_image(rich_menu_id, content_type, f)
# except Exception as e:
#     print("===Upload Exception===")
# #     # raise BadRequest(e)
# print("123")
# print("123")
# import requests

# headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+str(rich_menu_id), 
#                        headers=headers)
# print(req.text)
# print(req)
# # 列出圖文選單的列表
# # methods：GET
# # url：https://api.line.me/v2/bot/richmenu/list
# # Authorization：Bearer Token
# headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

# req = requests.request('GET', 'https://api.line.me/v2/bot/richmenu/list/'+str(rich_menu_id), 
#                        headers=headers)
# print(req.text)
# print(req)
# print("123")
# profile = line_bot_api.get_room_member_profile(<room_id>, <user_id>)
# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",  # display name
#     chat_bar_text="我是測試使用",
#     areas=[RichMenuArea(  # 這邊是陣列的格式，可以動態設定自己要的區域想要有什麼功能
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=URIAction(label='Go to line.me', uri='https://line.me'))]
# )
# # rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",
#     chat_bar_text="Tap here",
#     areas=[
#         RichMenuArea(
#             bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#             action=URIAction(label='Go to line.me', uri='https://line.me')
#         )
#     ]
# )
# # rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

# print(rich_menu_id)
# line_bot_api.get_rich_menu(rich_menu_id)
# print(rich_menu.rich_menu_id)
# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",
#     chat_bar_text="Tap here",
#     areas=[RichMenuArea(
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=URIAction(label='Go to line.me', uri='https://line.me'))]
# )
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)
# print("456")
# 查看圖文選單
# methods：GET
# url：https://api.line.me/v2/bot/richmenu/{rich menu id}
# Authorization：Bearer Token
# headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

# requests.request('POST', 'https://api.line.me/v2/bot/richmenu/'+str(rich_menu_id), 
#                        headers=headers)
# print("456")


# from linebot import (
#     LineBotApi, WebhookHandler
# )

# line_bot_api = LineBotApi('3Ma92PMIfy790Z...')

# rich_menu_list = line_bot_api.get_rich_menu_list()

# for rich_menu in rich_menu_list:
#     # line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
#     print(rich_menu.rich_menu_id)


    # line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)

# rich_menu_to_create = RichMenu(
#     size=RichMenuSize(width=2500, height=843),
#     selected=False,
#     name="Nice richmenu",  # display name
#     chat_bar_text="我是測試使用",
#     areas=[RichMenuArea(  # 這邊是陣列的格式，可以動態設定自己要的區域想要有什麼功能
#         bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
#         action=URIAction(label='Go to line.me', uri='https://line.me'))]
# )
# rich_menu_id = line_bot_api.create_rich_menu(
#     rich_menu=rich_menu_to_create)
# print(rich_menu_id)
# rich_menu_id = request.form['richmenu_id']
# try:
#     line_bot_api.set_default_rich_menu(rich_menu_id)
# except:
#     raise BadRequest("Maybe your richmenu id error.")

# line_bot_api.link_rich_menu_to_user("Uee6224531167e863e3c08504055d6ed2", eval(req.text.strip('}').split(':')[1]))
        # function LineAuth2() {
        #     var URL = 'https://access.line.me/dialog/oauth/weblogin?';
        #     URL += 'response_type=code';
        #     URL += '&client_id=1655692204';
        #     URL += '&redirect_uri=https://e16c3e7994e2.ngrok.io/callback';
        #     URL += '&state=abcde';
        #     window.location.href = URL;
        # }
# body = {
#     "response_type": "code",
#     "client_id": "1655692204",
#     "redirect_uri": "https://e16c3e7994e2.ngrok.io/callback",
#     "state": "abcde"
# }
# req = requests.request('POST', 'https://access.line.me/dialog/oauth/weblogin?',data=json.dumps(body).encode('utf-8'))#,response_type=code,client_id=1654386488,redirect_uri=https://c5613467a1c0.ngrok.io/callback,state=abcde)
# print(req.text)
# import webbrowser
# webbrowser.open("C:\\Users\\udev77\\Desktop\\t.html")
newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
updateArr=[]
def isWorkday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    # d_str="2/10"
    s=["02/20","09/11"]
    for s_str in s:
        print(d_str)
        print(s_str)
        if d_str ==s_str:
            print("isWorkday")
            return True
    return False
def isHoliday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    # d_str="2/10"
    s=["01/01","02/10","02/11","02/12","02/15","02/16","03/01","04/02","04/05","04/30","06/14","09/20","09/21","10/11","12/31"]
    for s_str in s:
        print(d_str)
        print(s_str)
        if d_str ==s_str:
            print("isHoliday")
            return True
    return False
def checkExpPerf():
    # print("checkExpPerf")
    weekno = datetime.today().weekday()+1
    
    a=d.Date()
    # print(a.getDay())
    # print(weekno)
    # print(int(a.getDay()) >= 25)
    # print("123")
    if int(a.getDay()) >= 25 and weekno<6: 
        print('day1')
        # newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        # updateArr=[]
        #寫入資料
        updateArr=['','']
        newDataAccess.setData('全聯',updateArr)
    elif int(a.getDay()) == 1: 
        print('day2')
        # newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        # updateArr=[]
        #寫入資料
        updateArr=['25','1,000,000']
        newDataAccess.setData('全聯',updateArr)
        updateArr=['','']
        newDataAccess.setData('博客來',updateArr)
        updateArr=['','']
        newDataAccess.setData('東森',updateArr)
    # else:
    # print('day3')

def job2():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("1")))
    tz = timezone(timedelta(hours=+8))
    date = datetime.now(tz)
    #print('123')
    print(str(date.strftime("%H:%M")))
    weekno = datetime.today().weekday()+1
    
    
        
    #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=str(date.strftime("%H:%M"))))
    if date.strftime("%H:%M") == "17:36":#自動發網通報表
        print('isHoliday() = '+str(isHoliday()))
        print('isWorkday() = '+str(isWorkday()))
        if isWorkday() == True:
            print('case1')
            print(weekno)
            #網通群組
            line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())   
        if weekno<6 and isHoliday() == False:
            print('case1')
            print(weekno)
            #網通群組
            line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
            #print('456')
            #自己
            #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
            #測試用群組
            #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())
    # if date.strftime("%H:%M") == "11:59":#自動發網通報表
    #     print('isHoliday() = '+str(isHoliday()))
    #     print('isWorkday() = '+str(isWorkday()))
    #     if isWorkday() == True:
    #         print('case1')
    #         print(weekno)
    #         #自己
    #         line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport()) 
    #     if weekno<6 and isHoliday() == False:
    #         print('case1')
    #         print(weekno)
    #         #網通群組
    #         # line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
    #         #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
    #         #print('456')
    #         #自己
    #         line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
    #         #測試用群組
    #         #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", OCPerformanceReport())
    elif date.strftime("%H:%M") == "07:30":#自動發門市報表
        print('case2')
        #怡君
        # line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
        line_bot_api.push_message(
            "Uca283ed15fe7664dab50d50ca20f2846", [
                StorePerformanceReport(),
                StoreNewGroupPerformanceReport()
            ]
        )
        # 自己
        # line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str('Ok!')))
        # line_bot_api.push_message(
        #     "Uee6224531167e863e3c08504055d6ed2", [
        #         StorePerformanceReport(),
        #         StoreNewGroupPerformanceReport()
        #     ]
        # )
        print('case2 end')
        #測試用群組
        #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", StorePerformanceReport())
        #自己
        #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StorePerformanceReport())
    elif date.strftime("%H:%M") == "16:07":#自動發門市報表
        print('case2')
        #怡君
        #line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
        #測試用群組
        #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", StorePerformanceReport())
        #自己
        #print(StorePerformanceReport())
        #message,new_group_message = StorePerformanceReport()
        #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StorePerformanceReport())

    elif date.strftime("%H:%M") == "16:46":
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
        #line_bot_api.push_message("C5fd1c0d2f75eb01ad8935d719076012b", OCPerformanceReport())
        #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", OCPerformanceReport())
    elif date.strftime("%H:%M") == "14:22":#測試用時間
        print('case4')
        # line_bot_api.push_message(
        #     "Uee6224531167e863e3c08504055d6ed2", [
        #         StorePerformanceReport(),
        #         StoreNewGroupPerformanceReport()
        #     ]
        # )

        #line_bot_api.push_message("U03f8575fac6ad12b612c6222ad37678e", OCPerformanceReport())
        #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", StoreNewGroupPerformanceReport())
    # elif date.strftime("%H:%M") == "07:50":#提醒
    #     if weekno==4:
    #         print('case6')
    #         line_bot_api.push_message(
    #             "Uee6224531167e863e3c08504055d6ed2", [
    #                 TextSendMessage(text='提醒1:  今天是週四週選開始，記得用亞當'),
    #                 TextSendMessage(text='')
    #             ]
    #         )
    # elif date.strftime("%H:%M") == "08:30":#提醒
    #     if weekno==4:
    #         print('case6')
    #         line_bot_api.push_message(
    #             "Uee6224531167e863e3c08504055d6ed2", [
    #                 TextSendMessage(text='提醒2:  今天是週四週選開始，記得用亞當'),
    #                 TextSendMessage(text='')
    #             ]
    #         )
    elif date.strftime("%H:%M") == "08:00":#提醒庫存
        if weekno==1:
            print('case5')
            # #曉詩
            # line_bot_api.push_message(
            #     "Ud3e3d7c236e4c9bb1116ab0b377bd005", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            # #昱慧
            # line_bot_api.push_message(
            #     "Ud8ea127ff725488a20e30380eda16fbb", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            # #永忠
            # line_bot_api.push_message(
            #     "U3c77f40434fa99e97e2f6e9cfb6ff0f6", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            # #佳容
            # line_bot_api.push_message(
            #     "U4516a5c0c8ee5368ad79385a28482cfd", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            #自己
            # line_bot_api.push_message(
            #     "Uee6224531167e863e3c08504055d6ed2", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            #曉詩Ud3e3d7c236e4c9bb1116ab0b377bd005
            #昱慧Ud8ea127ff725488a20e30380eda16fbb
            #永忠U3c77f40434fa99e97e2f6e9cfb6ff0f6
            #佳容U4516a5c0c8ee5368ad79385a28482cfd
            #麗娟
            # line_bot_api.push_message(
            #     "U8ec81edfb39499a39625be8c3e335ce0", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )
            # 
            # line_bot_api.push_message(
            #     "U8ec81edfb39499a39625be8c3e335ce0", [
            #         TextSendMessage(text='庫存已更新'),
            #         TextSendMessage(text='S:\開放公用區\★每週更新庫存水位警示表★\庫存水位.xlsm')
            #     ]
            # )


        




        



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
schedule.every(1).minutes.do(checkExpPerf)




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):#
        
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
        
        regex = r"\W*[@]?\w*\W*[@]?\w*\W*[東][森][未][入][績][效]\W*\d*[/]\d*\s*[止]\d*[,]?\d*[,]?\d*\D*"
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
            else:
                print('title_matches: 格式不符')
            date_regex = r"\d*[/]\d*\W*\s*"
            date_matches = re.search(date_regex, expected_perf_str)
            if date_matches:#日期
                date_match = date_matches.group()
                #print(date_match)
                print('date_match:' + date_match.split('/')[1].strip())
            else:
                print('date_matches: 格式不符')
            amount_regex = r"[0-9]+[,]?[0-9]+[,]?[0-9]+[,]?[0-9]+"
            amount_matches = re.search(amount_regex, expected_perf_str)
            if amount_matches:#金額
                amount_match = amount_matches.group()
                print('amount_match: ' + amount_match)
            else:
                print('amount_matches: 格式不符')
            newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部每月預入績效.txt')
            updateArr=[date_match.split('/')[1].strip(),amount_match]
            print(title_match)
            print(updateArr)
            #寫入資料
            newDataAccess.setData(title_match,updateArr)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 已更新')))

        else:
            print('match: 格式不符')



    headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
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
    try:
        with open("C:\\linebot\\image.jpeg", 'rb') as f:
            line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
    except Exception as e:
        print("===Upload Exception===")
    print("run3:"+str(rich_menu_id))
    content = line_bot_api.get_rich_menu_image(str(rich_menu_id))
    with open("C:\\linebot\\image.jpeg", 'wb') as fd:
        for chunk in content.iter_content():
            fd.write(chunk)
    print("run6:"+str(rich_menu_id))
    rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
    line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)
    print(str(rich_menu_id))


    if '[run]' in msg and user_id == "Uee6224531167e863e3c08504055d6ed2" :
        print("小幫手自動傳訊功能已啟用")
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('小幫手自動傳訊功能已啟用')))
        profile = line_bot_api.get_profile(event.source.user_id)
        message = TextSendMessage(text=str(profile.display_name))


        
        
        
        
        
        # line_bot_api.link_rich_menu_to_user(user_id, str(rich_menu_id))

        # print(req.text)
        # print("run7")

        # req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+str(rich_menu_id),headers=headers)
        # print("run8")
        # mydb = mysql.connector.connect(
        #     host = "127.21.7.39",
        #     port = 3306,
        #     user = "root",
        #     password = "16264386",
        #     db = "usersDB",
        #     charset = "utf8"
        # )
        # cursor = mydb.cursor()
        # try:
        #     sql="INSERT INTO users(UID,Dept,Name,checked) VALUES(%s,%s,%s,%s)"
        #     data=(str(event.source.user_id),'',str(profile.display_name),'')
        #     cursor.execute(sql,data)
        #     conn.commit()
        #     print('sql done.')
        # except:
        #     print('sql except.')

        # #檢查是否有發過報表，檢查checked的日期
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(event.source.user_id)+"已記錄"))
        # sql="select checked from users where UID=\""+str(event.source.user_id)+"\""
        # cursor.execute(sql)
        # for myresult in cursor.fetchall():
        #     my_data=myresult[0]
        # print(my_data)
        # mydb.commit()
        # if str(tdy_date_str) == my_data:#若跟今天日期相同，則代表已發過報表，跳出函式
        #     print('已發過報表')
        #         #sys.exit() 
        # try:
        #     #記錄checked的日期
        #     sql="UPDATE users SET checked=\""+str(tdy_date_str)+"\" where UID=\""+str(event.source.user_id)+"\"" 
        #     cursor.execute(sql)
        #     mydb.commit()
        #     cursor.close()#最後在關閉
        #     print("已儲存")
        # except:
        #     print("未儲存")
        # print("run2")
        working_count=0
        while True:
            # line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str('ssss')))
            #for working_count in [0,1,2]:
            #    if working_count==0:
            #        cls()    
            # print('working.')
            #        time.sleep(1)
            #    elif working_count==1:
            #        cls()
            #        print('working..')
            #        time.sleep(1)
            #    elif working_count==2:
            #        cls()
            #        print('working...')
            #        time.sleep(1)                   
            schedule.run_pending()
            time.sleep(1)

 


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
    print("start")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)





#Line bot參數設定，及傳遞訊息涵式
#line_bot_api = LineBotApi(channel_access_token)

#schedule.every().day.at("16:17").do(handle_message)


