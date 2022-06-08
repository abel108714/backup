from cgitb import text
from flask import Flask, request, abort
import json
# import js
# import TaChart-min.js.38c8e14764
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, FlexSendMessage
from linebot.exceptions import LineBotApiError

import time
import schedule
from Snapshot import YahooWebCrawler

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
from bcolors import *
from termcolor import colored
from style import *

import math


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
#line_bot_api = LineBotApi('vauGF3Izm5n9vuUeVjO6yPDCNCXXa5J7vX9dVGkD+R5gm0RzUJNK76EwMU4tH2WADcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4llQeprGrfPUI81yk/tXI88bQTyjgAvEc9OWcLp3RmyQdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('vgEDx1nG4UIVHBTFVXz1CFtLrLP6k4orVtpz0ViKz4s5fitpEJBzqdZqqc0700twDcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4tQxmP5cgC8aGYIAhD+XSA8dPMbPnigq/ou3IZB/jR2gdB04t89/1O/w1cDnyilFU=')

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
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage
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
import RunStatus as rs
from linebot.models import RichMenu, RichMenuArea, RichMenuSize, RichMenuBounds, URIAction, MessageAction
# import goto
# from dominate.tags import label
from goto import with_goto

import Date as d
import INVDB
import INVDB01002
#from INVDB import getDataArr
#from INVDB01002 import getDataArr
from PPAndProm import getDataArrOfPPAndProm,isExistProm,isExistPP,getDataArrOfProm,getDataArrOfPP

# import sys
# sys.path.append('/linebot')
from Line import isLineFriendName,insertLineFriendName,getPermission
#from Line import getLineFriendName,
# import INVDB as invdb
# import INVDB as idb
# from controller.notify_controller import NotifyController
# from controller.notify_sqs_controller import SendNotifyBySQSController
# from controller.message_api_controller import LineMessa＿geApiWebhookController
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



newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\\★網通部績效小幫手專用★\\網通部每月預入績效.txt')
updateArr=[]
def isWorkday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    # d_str="2/10"
    s=["",""]
    for s_str in s:
        print(d_str)
        print(s_str)
        if d_str ==s_str:
            print("isWorkday")
            return True
    return False
# def isHoliday(day=None):
#     c=d.Date()
#     s=["01/01","02/10","02/11","02/12","02/15","02/16","03/01","04/02","04/05","04/30","06/14","09/20","09/21","10/11","12/31"]
#     if d==None:
        
#         print(c.getDay())
#         print(c.getMonth())
#         print(c.getYear())
#         d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
#         # d_str="2/10"
        

#     else:
#         d_str = c.getMonth()+ "/"+ day#c.getYear()+ "/"+
    
#     for s_str in s:
#         print(d_str)
#         print(s_str)
#         if d_str ==s_str:
#             print("isHoliday")
#             return True
#     return False    
def isHoliday():
    c=d.Date()
    print(c.getDay())
    print(c.getMonth())
    print(c.getYear())
    d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
    print(d_str)
    # d_str="2/10"
    s=[
        "02/28",
        "04/04",
        "04/05",
        "05/02",
        "06/05",
        "09/09",
        "10/01"
    ]
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
    tz = timezone(timedelta(hours=+8))
    date = datetime.now(tz)
    # print(a.getDay())
    # print(weekno)
    # print(int(a.getDay()) >= 25)
    # print("123")

    #全聯預入,自動於25日以後的第一個工作天16點清除預入金額
    if int(a.getDay()) >= 25 and weekno <= 6 and date.strftime("%H:%M") == "16:00" or int(a.getDay()) == 24 and weekno == 5 and date.strftime("%H:%M") == "16:00": 
        print('day1')
        newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        # newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        # updateArr=[]
        #寫入資料
        if isWorkday() == True:
            print('case1')
            updateArr=['','']
            newDataAccess.setData('全聯',updateArr)
        if weekno<6 and isHoliday() == False:
            print('case2')
            updateArr=['','']
            newDataAccess.setData('全聯',updateArr)
    #全聯預入,自動於1日的11點30輸入預入金額
    elif int(a.getDay()) == 1 and date.strftime("%H:%M") == "15:50": #"11:30": 
        print('day2')
        # newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        # updateArr=[]
        #寫入資料
        # # if a.getMonth()==
        # day=25
        # while isHoliday(day)==True :
        #     day=day+1
        NextMonthDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\全聯下個月預入績效.txt')
        PreEntryDate=NextMonthDataAccess.getData(1,"全聯")
        PreEntryAmount=NextMonthDataAccess.getData(2,"全聯")
        print("全聯預入日: " + str(PreEntryDate))
        print("全聯預入金額: " + str(PreEntryAmount))
        
        newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\網通部每月預入績效.txt')
        updateArr=[str(PreEntryDate), str(PreEntryAmount)]
        newDataAccess.setData('全聯',updateArr)
        updateArr=['','']
        newDataAccess.setData('博客來',updateArr)
        updateArr=['','']
        newDataAccess.setData('東森',updateArr)
    # else:
    # print('day3')
# RunStatusCount=0
# def job2(obj):
def job2():
    # print("job2")
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("1")))
    try:
        tz = timezone(timedelta(hours=+8))
        # print(tz)
        date = datetime.now(tz)
        # print(date)
        print(str(date.strftime("%H:%M")))
        weekno = datetime.today().weekday()+1
        # print(weekno)
    except Exception as e:
        print(e)
    # new_rs.addRunStatusCount(1)

    # print("add: "+str(obj.getRunStatusCount()))
    # print('123')
    # print(RunStatusCount)
    # if RunStatusCount==0:
    #     RunStatus="--"
    # elif RunStatusCount==1:
    #     RunStatus="\\"
    # elif RunStatusCount==2:
    #     RunStatus="|"
    # elif RunStatusCount==3:
    #     RunStatus="/"
    
    # if RunStatusCount==3:
    #     RunStatusCount=0
    # else:
    #     RunStatusCount=RunStatusCount+1

    # print(str(date.strftime("%H:%M"))+" "+str(new_rs.showRunStatus()))

    
    # print("ifff")
    # print(str(date.strftime("%H:%M")))
    #line_bot_api.push_message("C4ec4e31c55ca25cc823f5ab5b4e1b040", TextSendMessage(text=str(date.strftime("%H:%M"))))
    if date.strftime("%H:%M") == "16:26":#"17:55":#自動發網通報表
        print('isHoliday() = '+str(isHoliday()))
        print('isWorkday() = '+str(isWorkday()))
        if isWorkday() == True:
            print('case1')
            print(weekno)
            #網通群組
            #if OCPerformanceReport() == "報表產生中":
            #    print("(1)")
            #    line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", "小幫手報告:沒有報表")
            #    print("(2)")
            #else:
            #    print("(3)")
            #    line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())  
            #    print("(4)") 
            line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
        if weekno<6 and isHoliday() == False:
            print('case1')
            print(weekno)
            #網通群組
            #if OCPerformanceReport() == "報表產生中":
            #    print("(5)")
            #    line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", "小幫手報告:沒有報表")
            #    print("(6)")
            #else:
            #    print("(7)")
            #    line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
            #    print("(8)")
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
    # elif date.strftime("%H:%M") == "09:02":#自動發門市報表
    #     print('case2')
    #     #怡君
    #     # line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport())
    #     line_bot_api.push_message(
    #         "Uca283ed15fe7664dab50d50ca20f2846", [
    #             StorePerformanceReport(),
    #             StoreNewGroupPerformanceReport()
    #         ]
    #     )
    elif date.strftime("%H:%M") == "07:30":#自動發門市報表
        print('case2')
        #怡君
        # line_bot_api.push_message("Uca283ed15fe7664dab50d50ca20f2846", StorePerformanceReport()),""
        line_bot_api.push_message(
            "Uca283ed15fe7664dab50d50ca20f2846", [
                StorePerformanceReport(),
                StoreNewGroupPerformanceReport()
            ]
        )
        #王素月"U87d5ad4d144180d81567984cf4a4240c"
        line_bot_api.push_message(
            "U87d5ad4d144180d81567984cf4a4240c", [
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
    elif date.strftime("%H:%M") == "13:00":# and group_id == "Cb7d45ef695c158c777ced6547bbd2e63":
        print('case stock')
        if weekno<6 == True:
            #裸k研究2所
            YahooWebCrawler(2330)
            # time.sleep(10)
            print('case stock .')
            line_bot_api.push_message(
                "Cb7d45ef695c158c777ced6547bbd2e63",
                R()
            )
        print('case stock end')
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
    # else:
    #     print("error")

        




        



#def job3():
    #your_id="立修"
    #print("I'm working...")
    #message="I'm working..."
    #line_bot_api.reply_message(event.reply_token, message)  
    #line_bot_api.push_message(str(event.source.user_id), TextSendMessage(text=str("555")))
    #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", TextSendMessage(text=str("55556")))




#exe_t=0


# 監聽所有來自 /mainpage 的 Post Request
# @app.route("/mainpage", methods=['GET'])
# def mainpage():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
#     print("Request body: " + body)
    
#     # handle webhook body
#     try:
#         handler.handle(body,signature)
#     except InvalidSignatureError:
#         abort(400)
#     print("hello!")
#     return 'OK'


def isRichMenu(line_bot_api):
    #先檢查是否有rich_menu，若有就不必再新增
    rich_menu_list = line_bot_api.get_rich_menu_list()
    try:
        # 嘗試執行一些程式碼
        for rich_menu in rich_menu_list:
            print(rich_menu.rich_menu_id)
            print("已有rich_menu_id")
            return True
    except:
        # 當程式出現異常時執行這邊的程式碼
        print("無rich_menu_id")
        return False
    return False

def delRichMenu(line_bot_api):
    rich_menu_list = line_bot_api.get_rich_menu_list()
    try:
        # 嘗試執行一些程式碼
        for rich_menu in rich_menu_list:
            print(rich_menu.rich_menu_id)
            line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
        print("已刪除rich_menu_id")
    except:
        # 當程式出現異常時執行這邊的程式碼
        print("無可刪除rich_menu_id")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
#@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Request body: " + body)
    
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




# 收到圖片消息的時候，做下面的方法
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    # msg = event.message.text
    # user_id = event.source.user_id
    # print('msg: ' + msg)
    # print('user_id: ' + user_id)
    print("儲存中")
    # 請api回覆已經上傳
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text='Image has Upload'+ ' ' + event.message.id))
    
    # 請api用get_message_content依照消息id將照片要回
    message_content = line_bot_api.get_message_content(event.message.id)
    
    # 存起來
    # with open('C:/linebot/image/'+event.message.id+'.jpg', 'wb') as fd:
    #     for chunk in message_content.iter_content():
    #         fd.write(chunk)
    #     print("已儲存圖片至C槽")
    with open('Z:/'+event.message.id+'.jpg', 'wb') as fd:
        
        
        print("1")
        for chunk in message_content.iter_content():
            fd.write(chunk)

    print("已儲存圖片至Z槽")
    #print("sleep start")
    #print("sleep end")
    r=1
    print("C:/linebot/PicToStrTest.py Z:/"+event.message.id+".jpg")
    # r=os.system("C:/linebot/PicToStrTest.py Z:/"+event.message.id+".jpg")#13816417264421.jpg
    # print("r : "+str(r))

    #若回傳0,即有接受且輸入業績目標
    if r==0:
        #bot訊息
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 已記錄下個月業績目標')))
        print('Ok! 已記錄下個月業績目標')
        #刪除該圖片
        PicFile = r"Z:/"+event.message.id+".jpg"
        try:
            os.remove(PicFile)
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")
            

    #os.system("C:/linebot/PicToStrTest.py Z:/13816417264421.jpg")
    
        # pytesseract.pytesseract.tesseract_cmd = r"C:/Users/udev77/AppData/Local/Tesseract-OCR/tesseract.exe"
        # print("2")
        # img = Image.open(r'Z:\\'+event.message.id+'.jpg')
        # print("3")
        # # #img.show()
        # # # print(pytesseract.image_to_string(img, lang="chi_tra+eng"))
        # data = pytesseract.image_to_string(img, lang="chi_tra+eng")

        # print("4")
        # dataList=[]
        # dataList = re.split(r' ',data) # split the string1617172996588.jpg
        # #resultList = [int(i.strip()) for i in dataList if i != ''] # remove the '' str and convert str to int.
        # #print(resultList)
        # print(dataList)

    # pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
    # img = Image.open(r'Z:/'+event.message.id+'.jpg')
    # data = pytesseract.image_to_string(img, lang="chi_tra")
    # dataList = re.split(r'\n ',data) # split the string
    # print(dataList)
    # data=dataList[0]
    # print("data: "+data)
    # data=delBlank(data)
    # print("data: "+data)
    # if data in s:   # 使用in運算子檢查
    #     print('字串中有\'月目標\'')
    # else:
    #     print('字串中沒有\'月目標\'')

    # pos = data.find('月目標')
    # if pos != -1:#是業績,寫入文件
    #     newDataAccess=FileDataAccess(0,'1','-','S:\\網通部\★網通部績效小幫手專用★\網通部下個月業積目標.txt')
    #     # updateArr=[date_match.split('/')[1].strip(),amount_match]
    #     print(title_match)
    #     print(updateArr)
    #     #寫入資料
    #     newDataAccess.setData(title_match,updateArr)
    


    # print(checkSubstring(dataList,1,2,"月目標"))
    
    # i=0
    # print("寫入")
    # while i < len(dataList)-1:#len(dataList[i])-1
    #     # print(dataList[i])
    #     ss=dataList[i].strip().replace(',','')
    #     # print(ss)
    #     # print(isDigit(ss))
    #     # print(ss.isdigit())
    #     newDataAccess=FileDataAccess(0,'2','-','S:\\網通部\★網通部績效小幫手專用★\網通部下個月業積目標.txt')
    #     updateArr=dataList[i]
    #     print(i)
    #     print(updateArr)
    #     newDataAccess.setData(i,updateArr)
    #     i=i+1
# new_rs=rs.RunStatus()




# def setDB():
#     # 資料庫設定
#     db_settings = {
#         "host": "127.21.7.39",
#         "port": 3306,
#         "user": "root",
#         "password": "16264386",
#         "db": "invdb",
#         "charset": "utf8"
#     }
#     return db_settings

# def getLineFriendName(line_id):
#     conn = pymysql.connect(**setDB())
#     with conn.cursor() as cursor:
#         sql="select name from line where line_id = "+str(line_id)
#         print(sql)
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         conn.commit()
#         cursor.close()
#         if str(myresult) == str("()"):
#             return 0
#         else:
#             return myresult  

# def insertLineFriendName(user_id,Name):
#     print('===========================================')
#     print("Name: " + str(Name))
#     print("user_id: " + str(user_id))
#     conn = pymysql.connect(**setDB())
#     print("conn")
#     with conn.cursor() as cursor:
#         try:
#             print("insert")
#             sql="INSERT line (line_id,name) VALUES ('" + str(user_id) + "','" + str(Name)+"')"
#             #sql="INSERT line (line_id,name) VALUES ('Uee6224531167e863e3c08504055d6ed2','周立修')"
#             print(sql)
#             cursor.execute(sql)
#             #return 0
#         except Exception as e:
#             print("UPDATE")
#             #sql="UPDATE line SET name="+str(Name)+" where line_id="+str(user_id)
#             #print(sql)
#             #cursor.execute(sql)          

#         conn.commit()
#         cursor.close()

# def ppp(user_id,Name):
#     print('Name: ' + str(Name))
#     print('user_id: ' + str(user_id))

def getDictIndex(dict,key,data):
    i=0
    for i in range(len(dict)):
        if dict[key][i] == data:
            # del dict[key][i]
            return i

def appendDict(dict,key,data):
    dict[key]=dict[key] + [data]
    # print("Result: ", key, " ", dict[key])

def delDict(dict,key,data,index):
    for key, value in dict.items():
        DictIndex=getDictIndex(dict,key,dict[key][index])
        del dict[key][DictIndex]

from flask import Flask, jsonify, request
# import js
# from pure import addint


def closeThread():
    print("關閉此執行緒")
    quit() #方法結束 Python 程式
    # exit() #方法結束 Python 程式
    # sys.exit() #方法結束 Python 程式
    # os.exit() #方法結束 Python 程式



    

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
@with_goto
def handle_message(event):#
    # try:
        
    #     print(addint(5, 7))
    # except Exception as e:
    #     print("e : "+str(e))
    msg = event.message.text
    user_id = event.source.user_id
    
    print('msg: ' + msg)
    print('user_id: ' + user_id)
    # try:
    #     group_id = event.source.group_id
    # except Exception as e:
    #     print('e: ' + e)
        # group_id = ""
    # print('group_id: ' + group_id)

    if(msg == 'profile'):
        FlexMessage = json.load(open('card.json','r',encoding='utf-8'))
        try:
            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()
    # dict = {}
    # #加入值為array的資料
    # dict['id'] = ["Uee6224531167e863e3c08504055d6ed2","U8ec81edfb39499a39625be8c3e335ce0"]
    # id_value=""
    # for value in dict.values():
    #     print("Result:", value)
    #     if value[i] == user_id:
    #         id_value = user_id
    #         break
    # print("id_value="+str(id_value))
    
    # admin_user_id="Uee6224531167e863e3c08504055d6ed2"
    # member_id="Uee6224531167e863e3c08504055d6ed2"#U8ec81edfb39499a39625be8c3e335ce0
    # guest_id="123"
    

    # admin_user_id="Uee6224531167e863e3c08504055d6ed2"
    member_id=""
    #dict = {}
    #加入值為array的資料
    # dict['id'] = ["Uee6224531167e863e3c08504055d6ed2","U8ec81edfb39499a39625be8c3e335ce0"]U3c77f40434fa99e97e2f6e9cfb6ff0f6
    
    admin_user_id=""
    
    
    #寫死
    #dict['id'] = ["U8ec81edfb39499a39625be8c3e335ce0","U3c77f40434fa99e97e2f6e9cfb6ff0f6","U4516a5c0c8ee5368ad79385a28482cfd","U3ecca7dbd50deb231004b055b07d755c","U7a8e507cdeb7304da1963ecdb6b43506","U70849fb74ae0d474e52feb96c12ee31d","U1a39ae260a8d4892abc3101bff50e8fd","U6df2ce1fcbd41372eec173b3f869df9f","Ub865ed90253c4ad6d756af6115093154","U536c0e2bbe48a8a300e0d8d86a6dc8ac","U1b14e7c863a29b5960138da88f7c02b8","Uc698b38f99be4fcf5183b89c2d67f8fe","U45269b35f85175b922c5ba904e2e2644"]
    #admin_user_id="Uee6224531167e863e3c08504055d6ed2"
    admin_user_id=""
    permission = ""

    if isLineFriendName(user_id) == True:
        print("是好友")
        if user_id=="Uee6224531167e863e3c08504055d6ed2":
            #admin_user_id=user_id
            #admin_user_id=""
            member_id=user_id
        else:
            member_id=user_id
    else:
        print("不是好友")

    if getPermission(user_id) == "業務":
        permission = "業務"
    elif getPermission(user_id) == "經銷商":
        permission = "經銷商"
    #改成去資料庫讀取
    #getLineID
    
    
    #admin_user_id=""
    # dict['id'] = ["U8ec81edfb39499a39625be8c3e335ce0","U3c77f40434fa99e97e2f6e9cfb6ff0f6","U4516a5c0c8ee5368ad79385a28482cfd","Uee6224531167e863e3c08504055d6ed2","U3ecca7dbd50deb231004b055b07d755c","U7a8e507cdeb7304da1963ecdb6b43506","U70849fb74ae0d474e52feb96c12ee31d","U1a39ae260a8d4892abc3101bff50e8fd","U6df2ce1fcbd41372eec173b3f869df9f","Ub865ed90253c4ad6d756af6115093154","U536c0e2bbe48a8a300e0d8d86a6dc8ac","U1b14e7c863a29b5960138da88f7c02b8","Uc698b38f99be4fcf5183b89c2d67f8fe"]
    # admin_user_id="123"
    # if user_id != admin_user_id:
    #     for value in dict.values():
    #         print("Result:", value)
    #     i=0
    #     for i in range(len(value)):
    #         print("i:", i)
    #         print("Result:", value[i])
    #         if value[i] == user_id:
    #             print("ok")
    #             member_id=user_id
    #     print("member_id:" ,member_id)



    # for value in dict.values():#核對業務員名單
    #     print("Result:", value)
    #     i=0
    #     for i in range(len(value)):
    #         print("i:", i)
    #         print("Result:", value[i])
    #         if value[i] == user_id:
    #             print("ok")
    #             member_id=user_id
    #             print("member_id:" ,member_id)
    if '我是管理者' in msg and user_id=="Uee6224531167e863e3c08504055d6ed2":
        admin_user_id=user_id
        
    if '我是管理者' in msg and user_id=="Uee6224531167e863e3c08504055d6ed2":
        admin_user_id=""
        
    if user_id == admin_user_id:#核對管理者
        admin_user_id = user_id

    print("member_id : " + member_id)

    if member_id == "" and user_id != admin_user_id:#不是業務也不是管理者，即不是會員
        if '加入會員' in msg:#and (user_id != admin_user_id) and (user_id != member_id):
            print("=======================加入會員")
            if isLineFriendName(user_id) == True:
                print("是好友")
                if user_id=="Uee6224531167e863e3c08504055d6ed2":
                    admin_user_id=user_id
                    admin_user_id=""
                else:
                    member_id=user_id
                print("已是會員!")
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str("已是會員!")))
            else:
                print("不是好友")
                print("請輸入姓名")
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str("請輸入姓名")))
                print(text)
                print(msg)
                # print("123")
                print("user_id : "+str(user_id))

                Name=""
                path='C:\\linebot\\msg\\'
                if not os.path.isdir(path):#沒有資料夾就建資料夾
                    os.makedirs(path)
                print("456")

                print("msg : " + msg)
                print("user_id : " + user_id)
                path='C:\\linebot\\msg\\'
                if not os.path.isdir(path):#沒有資料夾就建資料夾
                    os.makedirs(path)

                newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
                title_match=str(user_id)
                updateArr=[msg]
                print(title_match)
                print(updateArr)
                newDataAccess.setData(title_match,updateArr)

        else:
            print("msg :"+str(msg))    
            try:
                path='C:\\linebot\\msg\\'
                print(path + str(user_id) + '.txt')
                print("user_id : " + str(user_id))
                newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
                old_msg=newDataAccess.getData(1,user_id)
                print("old_msg = " + old_msg)
                if '加入會員' in old_msg:
                    print("非會員msg.")
                    print("user_id : " + str(user_id))
                    #寫入資料庫
                    #ppp(user_id,old_msg)
                    insertLineFriendName(user_id,msg)
                    print("insertLineFriendName")
                    print("已加入會員!")
                    #清空舊訊息
                    updateArr=['']
                    newDataAccess.setData(str(user_id),updateArr)
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str("已加入會員!")))
            except:
                print("無old_msg")





            # path='C:\\linebot\\msg\\'
            # if not os.path.isdir(path):#沒有資料夾就建資料夾
            #     os.makedirs(path)

            # newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
            # title_match=str(user_id)
            # updateArr=[msg]
            # print(title_match)
            # print(updateArr)
            # newDataAccess.setData(title_match,updateArr)
    

    




    if msg.isdigit() and (user_id == admin_user_id or user_id == member_id):
        print("數字msg")
        print("msg : " + msg)
        print("user_id : " + user_id)
        path='C:\\linebot\\msg\\'
        if not os.path.isdir(path):#沒有資料夾就建資料夾
            os.makedirs(path)

        newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
        title_match=str(user_id)
        updateArr=[msg]
        print(title_match)
        print(updateArr)
        newDataAccess.setData(title_match,updateArr)

        # newDataAccess=FileDataAccess(0,'5','-', path + str(user_id) + '.txt')
        # title_match=str(user_id)
        # inv=str(getINV(msg))
        # PN=str(getPN(msg))
        # exp=str(getExp(msg))
        # print("exp : "+ str(exp))
        # updateArr=[msg,PN,inv,exp]
        # print(title_match)
        # print(updateArr)
        # newDataAccess.setData(title_match,updateArr)
    elif msg.isdigit() == False and (user_id == admin_user_id or user_id == member_id) and (msg != "[庫存查詢]" and msg != "[進價與促銷]" and msg != "[庫存及效期]" and msg != "[run]" and msg !="[補發門市報表]" and msg !="[補發網通報表]" and msg !="[網通報表測試]" and msg !="[下一頁]"):
        print("文字msg")
        print("msg : " + msg)
        print("user_id : " + user_id)
        path='C:\\linebot\\msg\\'
        if not os.path.isdir(path):#沒有資料夾就建資料夾
            os.makedirs(path)

        newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
        title_match=str(user_id)
        updateArr=[msg]
        print("title_match ; "+str(title_match))
        print("updateArr ; "+str(updateArr))
        newDataAccess.setData(title_match,updateArr)
    # else:
    #     print(msg)
    #     print("非會員msg")
    #     # print("123")
    #     print("user_id : "+str(user_id))
    #     path='C:\\linebot\\msg\\'
    #     if not os.path.isdir(path):#沒有資料夾就建資料夾
    #         os.makedirs(path)
    #     print("********************************")


    #     print("*********************************789")
    #     try:
    #         newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
    #         old_msg=newDataAccess.getData(1,user_id)
    #     except:
    #         print("無old_msg")

    #     print("old_msg :"+str(old_msg))

    #     if old_msg == "加入會員":#Join Membership
    #         print("加入")
    #         #JoinMembership()

    # if '加入會員' in msg and (user_id != admin_user_id) and (user_id != member_id):
    #     print("=======================加入會員")

    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str("請輸入姓名")))
    #     print(text)
    #     print(msg)
    #     # print("123")
    #     print("user_id : "+str(user_id))

        
    #     path='C:\\linebot\\msg\\'
    #     if not os.path.isdir(path):#沒有資料夾就建資料夾
    #         os.makedirs(path)
    #     print("456")


    #     print("789")
    #     try:
    #         newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
    #         PID=newDataAccess.getData(1,user_id)
    #     except:
    #         print("無PID")

    #     print("PID :"+str(PID))
    # if '加入會員' in msg and ((user_id == admin_user_id) or (user_id == member_id)):
    #     print("已是會員")
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str("已是會員")))

    #     path='C:\\linebot\\msg\\'
    #     if not os.path.isdir(path):#沒有資料夾就建資料夾
    #         os.makedirs(path)

    #     newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
    #     title_match=str(user_id)
    #     updateArr=[msg]
    #     print("title_match : "+str(title_match))
    #     print("updateArr : "+str(updateArr))
    #     newDataAccess.setData(title_match,updateArr)

        # PID=getPID(str(msg))
        # print("PID : "+str(PID))
        # newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
        # title_match=str(user_id)
        # index=getIndex(PID)
        # updateArr=[index]
        # print(title_match)
        # print(updateArr)
        # newDataAccess.setData(title_match,updateArr)


        # PID=getPID(str(msg))
        # print("PID : "+str(PID))
        # newDataAccess=FileDataAccess(0,'5','-', path + str(user_id) + '.txt')
        # title_match=str(user_id)
        # inv=str(getINV(PID))
        # PN=str(getPN(PID))
        # exp=str(getExp(PID))
        # print(exp)
        # updateArr=[PID,PN,inv,exp]
        # print(title_match)
        # print(updateArr)
        # newDataAccess.setData(title_match,updateArr)

    # @app.route('/', methods=['GET'])
    # def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print('ip: '+ request.environ['REMOTE_ADDR'] + str(" (REMOTE_ADDR)"))
    else:
        print('ip: '+ request.environ['HTTP_X_FORWARDED_FOR'] + str(" (HTTP_X_FORWARDED_FOR)"))


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
            newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\網通部每月預入績效.txt')
            updateArr=[date_match.split('/')[1].strip(),amount_match]
            print(title_match)
            print(updateArr)
            #寫入資料
            newDataAccess.setData(title_match,updateArr)
            print("event.reply_token" + event.reply_token)
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 已更新')))
            except Exception as e:
                print("linebot無回應: "+str(e))
                try:
                	print("有效時間超過30秒，使用push回應")
                	line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", TextSendMessage(text=str('Ok! 已更新')))
                except Exception as e:
                	print("linebot無回應2: "+str(e))
            closeThread()
        else:
            print('match: 東森未入績效格式不符')

    keymsg_regex = r"\W*[預][入][績][效]\s?"
    keymsg_str = msg
    keymsg_matches = re.search(keymsg_regex, keymsg_str)
    if keymsg_matches:
        keymsg_match = keymsg_matches.group()
        print('keymsg_match: ' + keymsg_match)
        
        regex = r"\W*[@]?\w*\W*[@]?\w*\W*[全][聯][預][入][績][效]\W*\d*[/]\d*\s*[止]\d*[,]?\d*[,]?\d*\D*"
        # regex = r"\W*[@]?\w*\W*[@]?\w*\W*[全][聯][預][入][績][效]\W?\d*[,]?\d*[,]?\d*\D*"
        expected_perf_str = msg
        matches = re.search(regex, expected_perf_str)
        if matches:#訊息
            match = matches.group()
            print('match: ' + match)
            title_regex = r"\w*[全][聯]\W*"
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
            print("全聯下個月預入績效已紀錄")
            newDataAccess=FileDataAccess(0,'3','-','S:\\網通部\★網通部績效小幫手專用★\全聯下個月預入績效.txt')
            updateArr=[date_match.split('/')[1].strip(),amount_match]
            # updateArr=['25', amount_match]
            print(title_match)
            print(updateArr)
            #寫入資料
            newDataAccess.setData(title_match,updateArr)
            PreEntryDate=newDataAccess.getData(1,"全聯")
            PreEntryAmount=newDataAccess.getData(2,"全聯")
            print("全聯預入日: " + str(PreEntryDate))
            print("全聯預入金額: " + str(PreEntryAmount))
            try:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('Ok! 全聯下個月預入績效已更新')))
            except Exception as e:
                print("linebot無回應: "+str(e))
            closeThread()
        else:
            print('match: 全聯預入績效格式不符')




        
        

    # print("12345678")

    # #先檢查是否有rich_menu，若有就不必再新增
    # rich_menu_list = line_bot_api.get_rich_menu_list()
    # try:
    #      # 嘗試執行一些程式碼
    #     for rich_menu in rich_menu_list:
    #         print(rich_menu.rich_menu_id)
    #     print("已有rich_menu_id")
    # except:
    #     # 當程式出現異常時執行這邊的程式碼
    #     print("無rich_menu_id，準備新增")
    print("RichMenu準備刪除")
    print(user_id)
    print(member_id)
    if msg != "在?" and (user_id == admin_user_id or user_id == member_id):
        print("RichMenu準備刪除")
        if isRichMenu(line_bot_api) == True and (user_id == admin_user_id or user_id == member_id):#若有RichMenu，則刪除，準備新增
            delRichMenu(line_bot_api)
            print("RichMenu，已刪除，準備新增")
            print(isRichMenu(line_bot_api))

        if isRichMenu(line_bot_api) == False and (user_id == admin_user_id or user_id == member_id):#若無RichMenu，則新增
            print("RichMenu開始新增")
            try:
                # 嘗試執行一些程式碼
                # headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
                # headers = {"Authorization":"Bearer "+line_bot_api,"Content-Type":"application/json"}
                headers = {"Authorization":"Bearer vgEDx1nG4UIVHBTFVXz1CFtLrLP6k4orVtpz0ViKz4s5fitpEJBzqdZqqc0700twDcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4tQxmP5cgC8aGYIAhD+XSA8dPMbPnigq/ou3IZB/jR2gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
                # print("rich_menu_id 01")
                if user_id == admin_user_id:#管理頁面
                    print("管理頁面功能")
                    rich_menu_to_create = RichMenu(
                        size=RichMenuSize(width=2500, height=810),
                        selected=False,
                        name="功能選單",
                        chat_bar_text="選單",
                        areas=[RichMenuArea(
                            # bounds=RichMenuBounds(x=0, y=0, width=833.33, height=810),
                            # action=MessageAction(
                            #         label='message',
                            #         text='[run]'#'[庫存查詢]'#'[run]'
                            #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                            # ),
                            # RichMenuArea(
                            # bounds=RichMenuBounds(x=0, y=0, width=1666.66, height=810),
                            # action=MessageAction(
                            #         label='message',
                            #         text='[補發門市報表]'
                            #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                            # ),
                            # RichMenuArea(
                            # bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                            # action=MessageAction(
                            #         label='message',
                            #         text='[補發網通報表]'
                            #     )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                            # )
                            bounds=RichMenuBounds(x=0, y=0, width=833.33, height=405),
                            action=MessageAction(
                                    label='message',
                                    text='[run]'#'[庫存查詢]'#'[run]'
                                )#URIAction(label='Go to line.me', uri='https://line.me')#
                            ),
                            RichMenuArea(
                            bounds=RichMenuBounds(x=0, y=0, width=833.33, height=810),
                            action=MessageAction(
                                    label='message',
                                    text='[補發門市報表]'
                                )#URIAction(label='Go to line.me', uri='https://line.me')#
                            ),
                            RichMenuArea(
                            bounds=RichMenuBounds(x=0, y=0, width=1666.66, height=405),
                            action=MessageAction(
                                    label='message',
                                    text='[庫存查詢]'
                                )#URIAction(label='Go to line.me', uri='https://line.me')#
                            ),
                            RichMenuArea(
                            bounds=RichMenuBounds(x=0, y=0, width=1666.66, height=810),
                            action=MessageAction(
                                    label='message',
                                    text='[補發網通報表]'
                                )#URIAction(label='Go to line.me', uri='https://line.me')#
                            ),
                            RichMenuArea(
                            bounds=RichMenuBounds(x=0, y=0, width=2500, height=405),
                            action=MessageAction(
                                    label='message',
                                    text='[網通報表測試]'
                                )#URIAction(label='Go to line.me', uri='https://line.me')#
                            ),
                            RichMenuArea(
                            bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                            action=MessageAction(
                                    label='message',
                                    text='[下一頁]'
                                )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                            )
                        ]
                    )
                elif user_id == member_id:#成員頁面
                    print("成員頁面功能")
                    print("permission: " + permission)
                    if permission == "業務":
                        print("業務頁面載入")
                        rich_menu_to_create = RichMenu(
                            size=RichMenuSize(width=2500, height=810),
                            selected=False,
                            name="功能選單",
                            chat_bar_text="選單",
                            areas=[
                                # RichMenuArea(
                            #    bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                            #     action=MessageAction(
                            #             label='message',
                            #             text='[庫存查詢]'#'[庫存查詢]'#'[run]'
                            #         )#URIAction(label='Go to line.me', uri='https://line.me')#
                            #     )
                                # bounds=RichMenuBounds(x=0, y=0, width=1250, height=810),
                                # action=MessageAction(
                                #         label='message',
                                #         text='[庫存查詢]'#'[庫存查詢]'#'[run]'
                                #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                                # ),
                                # # RichMenuArea(
                                # # bounds=RichMenuBounds(x=0, y=0, width=1666.66, height=810),
                                # # action=MessageAction(
                                # #         label='message',
                                # #         text='[下單]'
                                # #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                                # # ),
                                # RichMenuArea(
                                # bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                                # action=MessageAction(
                                #         label='message',
                                #         text='[下一頁]'
                                #     )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                                # )
                                RichMenuArea(
                                bounds=RichMenuBounds(x=0, y=0, width=1250, height=810),
                                action=MessageAction(
                                        label='message',
                                        text='[進價與促銷]'
                                    )#URIAction(label='Go to line.me', uri='https://line.me')#
                                ),
                                RichMenuArea(
                                bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                                action=MessageAction(
                                        label='message',
                                        text='[庫存及效期]'
                                    )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                                )
                            ]
                        )      
                    elif permission == "經銷商":
                        print("經銷商頁面載入")
                        rich_menu_to_create = RichMenu(
                            size=RichMenuSize(width=2500, height=810),
                            selected=False,
                            name="功能選單",
                            chat_bar_text="選單",
                            areas=[
                                # RichMenuArea(
                            #    bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                            #     action=MessageAction(
                            #             label='message',
                            #             text='[庫存查詢]'#'[庫存查詢]'#'[run]'
                            #         )#URIAction(label='Go to line.me', uri='https://line.me')#
                            #     )
                                # bounds=RichMenuBounds(x=0, y=0, width=1250, height=810),
                                # action=MessageAction(
                                #         label='message',
                                #         text='[庫存查詢]'#'[庫存查詢]'#'[run]'
                                #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                                # ),
                                # # RichMenuArea(
                                # # bounds=RichMenuBounds(x=0, y=0, width=1666.66, height=810),
                                # # action=MessageAction(
                                # #         label='message',
                                # #         text='[下單]'
                                # #     )#URIAction(label='Go to line.me', uri='https://line.me')#
                                # # ),
                                # RichMenuArea(
                                # bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                                # action=MessageAction(
                                #         label='message',
                                #         text='[下一頁]'
                                #     )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                                # )
                                RichMenuArea(
                                bounds=RichMenuBounds(x=0, y=0, width=2500, height=810),
                                action=MessageAction(
                                        label='message',
                                        text='[下單]'
                                    )#URIAction(label='Go to line.me', uri='http://127.0.0.1:8000/hello/')#
                                )
                            ]
                        )      
                # print("rich_menu_id 02")
                rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
                print("rich_menu_id: "+str(rich_menu_id))
            except:
                # 當程式出現異常時執行這邊的程式碼
                print("rich_menu_id: 取得失敗")

                #網通群組
                # line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
                #自己
                #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())

            try:
                
                
                # with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'rb') as f:
                if user_id == admin_user_id:#管理頁面
                    print("管理頁面載入")
                    with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\six_function_page.jpg", 'rb') as f:
                        line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
                        print("The rich menu image was uploaded successfully.")
                elif user_id == member_id:#成員頁面
                    if permission == "業務":
                        print("業務頁面載入")
                        with open("C:\linebot\\image\\price_and_inv.jpg", 'rb') as f:
                            line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
                            print("The rich menu image was uploaded successfully.")
                    elif permission == "經銷商":
                        print("經銷商頁面載入")
                        with open("C:\linebot\\image\\order.jpg", 'rb') as f:
                            line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
                            print("The rich menu image was uploaded successfully.")
            except Exception as e:
                print("The rich menu image upload exception.")

            try:
                # 嘗試執行一些程式碼
                content = line_bot_api.get_rich_menu_image(str(rich_menu_id))
                if user_id == admin_user_id:#管理頁面
                    print("管理頁面載入完成")
                    # with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'wb') as fd:
                    with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\six_function_page.jpg", 'wb') as fd:
                        for chunk in content.iter_content():
                            fd.write(chunk)
                elif user_id == member_id:#成員頁面
                    if permission == "業務":
                        print("業務頁面載入完成")
                        # with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'wb') as fd:
                        with open("C:\linebot\\image\\price_and_inv.jpg", 'wb') as fd:
                            for chunk in content.iter_content():
                                fd.write(chunk)
                    elif permission == "經銷商":
                        print("經銷商頁面載入完成")
                        # with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'wb') as fd:
                        with open("C:\linebot\\image\\order.jpg", 'wb') as fd:
                            for chunk in content.iter_content():
                                fd.write(chunk)

                rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
                line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)
                print("The rich menu image link successfully.")
            except:
                # 當程式出現異常時執行這邊的程式碼
                print("The rich menu image link failure.")
    # elif isRichMenu(line_bot_api) == False and user_id == admin_user_id:#若無RichMenu，則新增
    #     print("RichMenu開始新增")
    #     try:
    #         # 嘗試執行一些程式碼
    #         # headers = {"Authorization":"Bearer 8GR7MNmmUmntbkHzoZK4YszKb4hOktoAxy+Bzp429ktQgNCMPP+KnKGwxeotxQY2ti1GrWqcgez0P0egY1iIA1BXx8/9WTMdPGnTaK/rUMD3wSn6eHzuU6cg/aj4BPx/phaQusTMdx3bYwh2iQfStgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
    #         # headers = {"Authorization":"Bearer "+line_bot_api,"Content-Type":"application/json"}
    #         headers = {"Authorization":"Bearer vgEDx1nG4UIVHBTFVXz1CFtLrLP6k4orVtpz0ViKz4s5fitpEJBzqdZqqc0700twDcYpdMSgJQUjPmlq1pbna/pv34S6zCoeFOF34qHujH4tQxmP5cgC8aGYIAhD+XSA8dPMbPnigq/ou3IZB/jR2gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
    #         # print("rich_menu_id 01")
    #         rich_menu_to_create = RichMenu(
    #             size=RichMenuSize(width=2500, height=810),
    #             selected=False,
    #             name="功能選單",
    #             chat_bar_text="功能",
    #             areas=[RichMenuArea(
    #                 bounds=RichMenuBounds(x=0, y=0, width=833.33, height=810),
    #                 action=MessageAction(
    #                         label='message',
    #                         text='[run]'
    #                     )#URIAction(label='Go to line.me', uri='https://line.me')#
    #                 )
    #             ]
    #         )
    #         # print("rich_menu_id 02")
    #         rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    #         print("rich_menu_id: "+str(rich_menu_id))
    #     except:
    #         # 當程式出現異常時執行這邊的程式碼
    #         print("rich_menu_id: 取得失敗")

    #     try:
    #         with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'rb') as f:
    #             line_bot_api.set_rich_menu_image(str(rich_menu_id), "image/jpeg", f)
    #             print("The rich menu image was uploaded successfully.")
    #     except Exception as e:
    #         print("The rich menu image upload exception.")

    #     try:
    #         # 嘗試執行一些程式碼
    #         content = line_bot_api.get_rich_menu_image(str(rich_menu_id))
    #         with open("C:\Program Files (x86)\Apache Software Foundation\Apache2.2\htdocs\\image.jpeg", 'wb') as fd:
    #             for chunk in content.iter_content():
    #                 fd.write(chunk)

    #         rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
    #         line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)
    #         print("The rich menu image link successfully.")
    #     except:
    #         # 當程式出現異常時執行這邊的程式碼
    #         print("The rich menu image link failure.")
    else:
        print("RichMenu無法新增")

    if user_id != admin_user_id:
        print("非linebot管理員id")
        
    # label.begin

    
    # try:
    #      # 嘗試執行一些程式碼
    #     for rich_menu in rich_menu_list:
    #         print(rich_menu.rich_menu_id)
    #         line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
    # except:
    #     # 當程式出現異常時執行這邊的程式碼
    #     print("rich_menu_id刪除失敗")






    # print(f"{bcolors.WARNING}The rich menu image link successfully.{bcolors.ENDC}")
    
    # print(termcolor.COLORS('The rich menu image link successfully.', 'green'))
    # print(style.YELLOW + "Hello, World!")

    # print(style.YELLOW + "Hello, World!")


        #insertLineId()
    if '[run]' in msg and user_id == "Uee6224531167e863e3c08504055d6ed2" :
        #                             Uee6224531167e863e3c08504055d6ed2
        # print(new_rs.addRunStatusCount(1))
        # print(new_rs.getRunStatusCount())
        print("小幫手自動傳訊功能已啟用")
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('小幫手自動傳訊功能已啟用')))
        profile = line_bot_api.get_profile(event.source.user_id)
        message = TextSendMessage(text=str(profile.display_name))


        
    if 'SDD' in msg :#and user_id == admin_user_id :
        print("SDD")
        #網通群組
        try:
            line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", SDReport())
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()
        # line_bot_api.link_rich_menu_to_user(user_id, str(rich_menu_id))

        # print(req.text)
        # print("run7")
        # print("777777777777777777")
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
            # print('working.')
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
            # print("134")             
            schedule.run_pending()
            time.sleep(1)


    if '[dstr]' in msg and user_id == admin_user_id :
        c=d.Date()
        print(c.getDay())
        print(c.getMonth())
        print(c.getYear())
        d_str = c.getMonth()+ "/"+ c.getDay()#c.getYear()+ "/"+
        print(d_str)
        try:
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(
                    text=str(
                        d_str
                    )
                )
            )
        except Exception as e:
            print("linebot無回應: "+str(e))

    if '[補發門市報表]' in msg :#and user_id == admin_user_id :
        print("[補發門市報表]")
        #怡君
        line_bot_api.push_message(
            "Uca283ed15fe7664dab50d50ca20f2846", [
                StorePerformanceReport(),
                StoreNewGroupPerformanceReport()
            ]
        )
        #素月
        line_bot_api.push_message(
            "U87d5ad4d144180d81567984cf4a4240c", [
                StorePerformanceReport(),
                StoreNewGroupPerformanceReport()
            ]
        )
        #自己
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('已補發門市報表')))
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()
        # line_bot_api.push_message(
        #     "Uee6224531167e863e3c08504055d6ed2", [
        #         StorePerformanceReport(),
        #         StoreNewGroupPerformanceReport()
        #     ]
        # )
    if '[sss]' in msg and (user_id == admin_user_id or user_id == member_id):
        # YahooWebCrawler(2330)
        print('123')
        # # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(str("https://s.yimg.com/nb/tw_stock_frontend/scripts/TaChart/tachart.3de240ea9a.html?sid=2330"))))
        # with open("C:\linebot\\image\\price_and_inv.jpg", 'rb') as f:
        #     line_bot_api.reply_message(event.reply_token, f)
    if '[進價與促銷]' in msg  and (user_id == admin_user_id or user_id == member_id):
        print(msg)
        # print("123")
        print("user_id : "+str(user_id))
        path='C:\\linebot\\msg\\'
        if not os.path.isdir(path):#沒有資料夾就建資料夾
            os.makedirs(path)
        print("456")


        print("789")
        try:
            newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
            PID=newDataAccess.getData(1,user_id)
        except:
            print("無PID")

        print("PID :"+str(PID))
        a=d.Date()
        # a.isDate('2017-12-31')

        # print("getDataArrOfPPAndProm start")
        # DataArr=getDataArrOfPPAndProm(PID)
        # print("getDataArrOfPPAndProm end")
        # print(DataArr)
        # print(len(DataArr))
        # i=0
        # MsgStr=""
        # prePID=""
        # for i in range(len(DataArr)):
        #     # print("i = "+str(i))
        #     # print("len(DataArr) = "+str(len(DataArr)))
        #     # print("品號 : "+str(DataArr[i][0]))
        #     # print("品名 : "+str(DataArr[i][1]))
            
        #     # if a.isDate(str(DataArr[i][5])):
                
        #     # if str(DataArr[i][0])!=prePID:
        #         # if i != 0:
        #             # MsgStr=MsgStr+"\n"
        #     if i > 0:
        #         print("\n")
        #         MsgStr=MsgStr+"\n"
        #         print("\n")
        #         MsgStr=MsgStr+"\n"
        #     # print("==========================")
        #     # MsgStr=MsgStr+"=========================="+"\n"
        #     print(str(DataArr[i][2]))
        #     MsgStr=MsgStr+str(DataArr[i][2])+"\n"
        #     # print("==========================")
        #     # MsgStr=MsgStr+"=========================="+"\n"
        #     # print("\n")
        #     # MsgStr=MsgStr+"\n"
        #     print("-------------------")
        #     MsgStr=MsgStr+"-------------------"+"\n"
        #     print("促銷")
        #     MsgStr=MsgStr+"促銷"+"\n"
        #     print("-------------------")
        #     MsgStr=MsgStr+"-------------------"+"\n"
        #     print("特價 : "+str(DataArr[i][19]))
        #     MsgStr=MsgStr+"特價 : "+str(DataArr[i][19])+"\n"
        #     print("特進價 : "+str(DataArr[i][20]))
        #     MsgStr=MsgStr+"特進價 : "+str(DataArr[i][20])+"\n"
        #     print("備註 : "+str(DataArr[i][21]))
        #     MsgStr=MsgStr+"備註 : "+str(DataArr[i][21])+"\n"
        #     print("-------------------")
        #     MsgStr=MsgStr+"-------------------"+"\n"
        #     print("進價")
        #     MsgStr=MsgStr+"進價"+"\n"
        #     print("-------------------")
        #     MsgStr=MsgStr+"-------------------"+"\n"
        #     print("品號 : "+str(DataArr[i][0]))
        #     prePID=str(DataArr[i][0])
        #     MsgStr=MsgStr+"品號 : "+str(DataArr[i][0])+"\n"
        #     print("國際條碼 : "+str(DataArr[i][1]))
        #     MsgStr=MsgStr+"國際條碼 : "+str(DataArr[i][1])+"\n"

        #     print("規格 : "+str(DataArr[i][3]))
        #     MsgStr=MsgStr+"規格 : "+str(DataArr[i][3])+"\n"
        #     print("折數 : "+str(DataArr[i][4]))
        #     MsgStr=MsgStr+"折數 : "+str(DataArr[i][4])+"\n"
        #     print("建議售價 : "+str(DataArr[i][5]))
        #     MsgStr=MsgStr+"建議售價 : "+str(DataArr[i][5])+"\n"
        #     print("進價 : "+str(DataArr[i][6]))
        #     MsgStr=MsgStr+"進價 : "+str(DataArr[i][6])+"\n"
        #     # print("免應稅 : "+str(DataArr[i][7]))
        #     # MsgStr=MsgStr+"免應稅 : "+str(DataArr[i][7])+"\n"
        #     print("常態搭贈 : "+str(DataArr[i][8]))
        #     MsgStr=MsgStr+"常態搭贈 : "+str(DataArr[i][8])+"\n"

        #     print("均價 : "+str(DataArr[i][9]))
        #     MsgStr=MsgStr+"均價 : "+str(DataArr[i][9])+"\n"
        #     print("第一階 : "+str(DataArr[i][10]))
        #     MsgStr=MsgStr+"第一階 : "+str(DataArr[i][10])+"\n"
        #     print("第二階 : "+str(DataArr[i][11]))
        #     MsgStr=MsgStr+"第二階 : "+str(DataArr[i][11])+"\n"
        #     # print("第一階均價 : "+str(DataArr[i][12]))
        #     # MsgStr=MsgStr+"第一階均價 : "+str(DataArr[i][12])+"\n"
        #     # print("第二階均價 : "+str(DataArr[i][13]))
        #     # MsgStr=MsgStr+"第二階均價 : "+str(DataArr[i][13])+"\n"
        #     # print("新5箱均價後毛利 : "+str(DataArr[i][14]))
        #     # MsgStr=MsgStr+"新5箱均價後毛利 : "+str(DataArr[i][14])+"\n"
        #     # print("舊申報進價 : "+str(DataArr[i][15]))
        #     # MsgStr=MsgStr+"舊申報進價 : "+str(DataArr[i][15])+"\n"
        #     # print("舊申報優惠方式 : "+str(DataArr[i][16]))
        #     # MsgStr=MsgStr+"舊申報優惠方式 : "+str(DataArr[i][16])+"\n"
        #     # print("舊申報均價 : "+str(DataArr[i][17]))
        #     # MsgStr=MsgStr+"舊申報均價 : "+str(DataArr[i][17])+"\n"
        #     # print("五箱以上 : "+str(DataArr[i][18]))
        #     # MsgStr=MsgStr+"五箱以上 : "+str(DataArr[i][18])+"\n"
        #     # print("\n")
        #     # MsgStr=MsgStr+"\n"

        #     if i >= 0:
        #         print("=============")
        #         MsgStr=MsgStr+"============="+"\n"
        # # print("-------------------")
        # # MsgStr=MsgStr+"-------------------"+"\n"
        # try:
        #     line_bot_api.reply_message(
        #         event.reply_token, 
        #         TextSendMessage(
        #             text=str(
        #                 MsgStr
        #             )
        #         )
        #     )
        # except Exception as e:
        #     print("linebot無回應: "+str(e))
        #     #check prom

        if isExistProm(PID)==True and isExistPP(PID)==True:
            print("case1")
            DataArr=getDataArrOfProm(PID)
            print("getDataArrOfProm end")
            print(DataArr)
            print(len(DataArr))
            i=0
            MsgStr=""
            prePID=""
            if len(DataArr)==0:
                print("缺貨或無此品項，或請減少關鍵字，再重新查詢")
                MsgStr=MsgStr+"缺貨或無此品項，或請減少關鍵字，再重新查詢"
            else:
                for i in range(len(DataArr)):
                    # print("i = "+str(i))
                    # print("len(DataArr) = "+str(len(DataArr)))
                    # print("品號 : "+str(DataArr[i][0]))
                    # print("品名 : "+str(DataArr[i][1]))
                    
                    # if a.isDate(str(DataArr[i][5])):
                        
                    # if str(DataArr[i][0])!=prePID:
                        # if i != 0:
                            # MsgStr=MsgStr+"\n"
                    if i > 0:
                        print("\n")
                        MsgStr=MsgStr+"\n"
                        print("\n")
                        MsgStr=MsgStr+"\n"
                    # print("==========================")
                    # MsgStr=MsgStr+"=========================="+"\n"
                    print(str(DataArr[i][2]))
                    MsgStr=MsgStr+str(DataArr[i][2])+"\n"
                    # print("==========================")
                    # MsgStr=MsgStr+"=========================="+"\n"
                    # print("\n")
                    # MsgStr=MsgStr+"\n"
                    print("-------------------")
                    MsgStr=MsgStr+"-------------------"+"\n"
                    print("促銷")
                    MsgStr=MsgStr+"促銷"+"\n"
                    print("-------------------")
                    MsgStr=MsgStr+"-------------------"+"\n"

                    #-------------------------促銷暫不顯示-----------------------
                    # if str(DataArr[i][19])!=str(None):
                    #     print("特價 : "+str(DataArr[i][19]))
                    #     MsgStr=MsgStr+"特價 : "+str(DataArr[i][19])+"\n"
                    # if str(DataArr[i][20])!=str(None):
                    #     print("特進價 : "+str(DataArr[i][20]))
                    #     MsgStr=MsgStr+"特進價 : "+str(DataArr[i][20])+"\n"
                    # if str(DataArr[i][21])!=str(None):
                    #     print("備註 : "+str(DataArr[i][21]))
                    #     MsgStr=MsgStr+"備註 : "+str(DataArr[i][21])+"\n"
                    #-------------------------促銷暫不顯示-----------------------

                    print("-------------------")
                    MsgStr=MsgStr+"-------------------"+"\n"
                    print("進價")
                    MsgStr=MsgStr+"進價"+"\n"
                    print("-------------------")
                    MsgStr=MsgStr+"-------------------"+"\n"
                    print("品號 : "+str(DataArr[i][0]))
                    prePID=str(DataArr[i][0])
                    MsgStr=MsgStr+"品號 : "+str(DataArr[i][0])+"\n"
                    print("國際條碼 : "+str(DataArr[i][1]))
                    MsgStr=MsgStr+"國際條碼 : "+str(DataArr[i][1])+"\n"

                    print("規格 : "+str(DataArr[i][3]))
                    MsgStr=MsgStr+"規格 : "+str(DataArr[i][3])+"\n"
                    print("折數 : "+str(DataArr[i][4]))
                    MsgStr=MsgStr+"折數 : "+str(DataArr[i][4])+"\n"
                    print("建議售價 : "+str(DataArr[i][5]))
                    MsgStr=MsgStr+"建議售價 : "+str(DataArr[i][5])+"\n"
                    print("進價 : "+str(DataArr[i][6]))
                    MsgStr=MsgStr+"進價 : "+str(DataArr[i][6])+"\n"
                    # print("免應稅 : "+str(DataArr[i][7]))
                    # MsgStr=MsgStr+"免應稅 : "+str(DataArr[i][7])+"\n"
                    print("常態搭贈 : "+str(DataArr[i][8]))
                    MsgStr=MsgStr+"常態搭贈 : "+str(DataArr[i][8])+"\n"

                    print("均價 : "+str(DataArr[i][9]))
                    MsgStr=MsgStr+"均價 : "+str(DataArr[i][9])+"\n"
                    print("第一階 : "+str(DataArr[i][10]))
                    MsgStr=MsgStr+"第一階 : "+str(DataArr[i][10])+"\n"
                    print("第二階 : "+str(DataArr[i][11]))
                    MsgStr=MsgStr+"第二階 : "+str(DataArr[i][11])+"\n"
                    # print("第一階均價 : "+str(DataArr[i][12]))
                    # MsgStr=MsgStr+"第一階均價 : "+str(DataArr[i][12])+"\n"
                    # print("第二階均價 : "+str(DataArr[i][13]))
                    # MsgStr=MsgStr+"第二階均價 : "+str(DataArr[i][13])+"\n"
                    # print("新5箱均價後毛利 : "+str(DataArr[i][14]))
                    # MsgStr=MsgStr+"新5箱均價後毛利 : "+str(DataArr[i][14])+"\n"
                    # print("舊申報進價 : "+str(DataArr[i][15]))
                    # MsgStr=MsgStr+"舊申報進價 : "+str(DataArr[i][15])+"\n"
                    # print("舊申報優惠方式 : "+str(DataArr[i][16]))
                    # MsgStr=MsgStr+"舊申報優惠方式 : "+str(DataArr[i][16])+"\n"
                    # print("舊申報均價 : "+str(DataArr[i][17]))
                    # MsgStr=MsgStr+"舊申報均價 : "+str(DataArr[i][17])+"\n"
                    # print("五箱以上 : "+str(DataArr[i][18]))
                    # MsgStr=MsgStr+"五箱以上 : "+str(DataArr[i][18])+"\n"
                    # print("\n")
                    # MsgStr=MsgStr+"\n"

                    if i >= 0:
                        print("=============")
                        MsgStr=MsgStr+"============="+"\n"
            # print("-------------------")
            # MsgStr=MsgStr+"-------------------"+"\n"
            try:
                line_bot_api.reply_message(
                    event.reply_token, 
                    TextSendMessage(
                        text=str(
                            MsgStr
                        )
                    )
                )
            except Exception as e:
                print("linebot無回應: "+str(e))
        #check pp
        elif isExistProm(PID)==False and isExistPP(PID)==True:
            print("case2")
            DataArr=getDataArrOfPP(PID)
            print("getDataArrOfPP end")
            print(DataArr)
            print(len(DataArr))
            i=0
            MsgStr=""
            prePID=""
            for i in range(len(DataArr)):
                # print("i = "+str(i))
                # print("len(DataArr) = "+str(len(DataArr)))
                # print("品號 : "+str(DataArr[i][0]))
                # print("品名 : "+str(DataArr[i][1]))
                
                # if a.isDate(str(DataArr[i][5])):
                    
                # if str(DataArr[i][0])!=prePID:
                    # if i != 0:
                        # MsgStr=MsgStr+"\n"
                if i > 0:
                    print("\n")
                    MsgStr=MsgStr+"\n"
                    print("\n")
                    MsgStr=MsgStr+"\n"
                # print("==========================")
                # MsgStr=MsgStr+"=========================="+"\n"
                print(str(DataArr[i][2]))
                MsgStr=MsgStr+str(DataArr[i][2])+"\n"
                # print("==========================")
                # MsgStr=MsgStr+"=========================="+"\n"
                # print("\n")
                # MsgStr=MsgStr+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"+"\n"
                print("促銷")
                MsgStr=MsgStr+"促銷"+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"+"\n"
                # print("無")
                # MsgStr=MsgStr+"無"+"\n"
                # print("特價 : "+str(DataArr[i][19]))
                # MsgStr=MsgStr+"特價 : "+str(DataArr[i][19])+"\n"
                # print("特進價 : "+str(DataArr[i][20]))
                # MsgStr=MsgStr+"特進價 : "+str(DataArr[i][20])+"\n"
                # print("備註 : "+str(DataArr[i][21]))
                # MsgStr=MsgStr+"備註 : "+str(DataArr[i][21])+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"+"\n"
                print("進價")
                MsgStr=MsgStr+"進價"+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"+"\n"
                print("品號 : "+str(DataArr[i][0]))
                prePID=str(DataArr[i][0])
                MsgStr=MsgStr+"品號 : "+str(DataArr[i][0])+"\n"
                print("國際條碼 : "+str(DataArr[i][1]))
                MsgStr=MsgStr+"國際條碼 : "+str(DataArr[i][1])+"\n"

                print("規格 : "+str(DataArr[i][3]))
                MsgStr=MsgStr+"規格 : "+str(DataArr[i][3])+"\n"
                print("折數 : "+str(DataArr[i][4]))
                MsgStr=MsgStr+"折數 : "+str(DataArr[i][4])+"\n"
                print("建議售價 : "+str(DataArr[i][5]))
                MsgStr=MsgStr+"建議售價 : "+str(DataArr[i][5])+"\n"
                print("進價 : "+str(DataArr[i][6]))
                MsgStr=MsgStr+"進價 : "+str(DataArr[i][6])+"\n"
                # print("免應稅 : "+str(DataArr[i][7]))
                # MsgStr=MsgStr+"免應稅 : "+str(DataArr[i][7])+"\n"
                print("常態搭贈 : "+str(DataArr[i][8]))
                MsgStr=MsgStr+"常態搭贈 : "+str(DataArr[i][8])+"\n"

                print("均價 : "+str(DataArr[i][9]))
                MsgStr=MsgStr+"均價 : "+str(DataArr[i][9])+"\n"
                print("第一階 : "+str(DataArr[i][10]))
                MsgStr=MsgStr+"第一階 : "+str(DataArr[i][10])+"\n"
                print("第二階 : "+str(DataArr[i][11]))
                MsgStr=MsgStr+"第二階 : "+str(DataArr[i][11])+"\n"
                # print("第一階均價 : "+str(DataArr[i][12]))
                # MsgStr=MsgStr+"第一階均價 : "+str(DataArr[i][12])+"\n"
                # print("第二階均價 : "+str(DataArr[i][13]))
                # MsgStr=MsgStr+"第二階均價 : "+str(DataArr[i][13])+"\n"
                # print("新5箱均價後毛利 : "+str(DataArr[i][14]))
                # MsgStr=MsgStr+"新5箱均價後毛利 : "+str(DataArr[i][14])+"\n"
                # print("舊申報進價 : "+str(DataArr[i][15]))
                # MsgStr=MsgStr+"舊申報進價 : "+str(DataArr[i][15])+"\n"
                # print("舊申報優惠方式 : "+str(DataArr[i][16]))
                # MsgStr=MsgStr+"舊申報優惠方式 : "+str(DataArr[i][16])+"\n"
                # print("舊申報均價 : "+str(DataArr[i][17]))
                # MsgStr=MsgStr+"舊申報均價 : "+str(DataArr[i][17])+"\n"
                # print("五箱以上 : "+str(DataArr[i][18]))
                # MsgStr=MsgStr+"五箱以上 : "+str(DataArr[i][18])+"\n"
                # print("\n")
                # MsgStr=MsgStr+"\n"

                if i >= 0:
                    print("=============")
                    MsgStr=MsgStr+"============="+"\n"
                
                
            # print("-------------------")
            # MsgStr=MsgStr+"-------------------"+"\n"
            try:
                line_bot_api.reply_message(
                    event.reply_token, 
                    TextSendMessage(
                        text=str(
                            MsgStr
                        )
                    )
                )
            except Exception as e:
                print("linebot無回應: "+str(e))
        elif isExistProm(PID)==True and isExistPP(PID)==False:
            MsgStr="無資料"
            try:
                line_bot_api.reply_message(
                    event.reply_token, 
                    TextSendMessage(
                        text=str(
                            MsgStr
                        )
                    )
                )
            except Exception as e:
                print("linebot無回應: "+str(e))
        else:
            print("例外")
        closeThread()
    if ('[庫存查詢]' in msg or '[庫存及效期]' in msg ) and (user_id == admin_user_id or user_id == member_id):
        print(msg)
        # print("123")
        print("user_id : "+str(user_id))
        path='C:\\linebot\\msg\\'
        if not os.path.isdir(path):#沒有資料夾就建資料夾
            os.makedirs(path)
        print("456")


        print("789")
        try:
            newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
            PID=newDataAccess.getData(1,user_id)
        except:
            print("無PID")

        print("PID :"+str(PID))
        a=d.Date()
        # a.isDate('2017-12-31')
        DataArrOfINVDB=INVDB.getDataArr(PID)
        DataArrOfINVDB01002=INVDB01002.getDataArr(PID)
        i=0
        MsgStr=""
        prePID=""
        print("====================")
        try:
            print(len(DataArrOfINVDB))
            #print(DataArrOfINVDB)
            print(len(DataArrOfINVDB01002))
            #print(DataArrOfINVDB01002)
        except:
            print("DataArr錯誤")
        print("====================")
        if len(DataArrOfINVDB)==0:
            if len(DataArrOfINVDB01002)==0:
                print("[百及倉]缺貨或無此品項，或請減少關鍵字，再重新查詢")
                MsgStr=MsgStr+"[百及倉]缺貨或無此品項，或請減少關鍵字，再重新查詢"
                #if len(DataArrOfINVDB01002) > 0:
                #    print("\n")
                #    MsgStr=MsgStr+"\n"
        else:
            for i in range(len(DataArrOfINVDB)):
                # print("i = "+str(i))
                # print("品號 : "+str(DataArrOfINVDB[i][0]))
                # print("品名 : "+str(DataArrOfINVDB[i][1]))
                print(" : "+str(DataArrOfINVDB[i][5]))
                if a.isDate(str(DataArrOfINVDB[i][5])):
                    
                    if str(DataArrOfINVDB[i][0])!=prePID:
                        if i != 0:
                            MsgStr=MsgStr+"\n"
                        print("=============")
                        MsgStr=MsgStr+"============="+"\n"
                        print("品號 : "+str(DataArrOfINVDB[i][0]))
                        prePID=str(DataArrOfINVDB[i][0])
                        MsgStr=MsgStr+"品號 : "+str(DataArrOfINVDB[i][0])+"\n"
                        print("品名 : "+str(DataArrOfINVDB[i][1]))
                        MsgStr=MsgStr+"品名 : "+str(DataArrOfINVDB[i][1])+"\n"
                        print("包裝方式 : "+str(DataArrOfINVDB[i][2]))
                        MsgStr=MsgStr+"包裝方式 : "+str(DataArrOfINVDB[i][2])+"\n"
                    print("-------------------")
                    MsgStr=MsgStr+"-------------------"+"\n"
                    print("庫存數量 : "+str(DataArrOfINVDB[i][3]))
                    MsgStr=MsgStr+"庫存數量 : "+str(DataArrOfINVDB[i][3])+"\n"
                    print("包裝數量 : "+str(DataArrOfINVDB[i][4]))
                    MsgStr=MsgStr+"包裝數量 : "+str(DataArrOfINVDB[i][4])+"\n"
                    print("有效期限 : "+str(DataArrOfINVDB[i][5]))
                    MsgStr=MsgStr+"有效期限 : "+str(DataArrOfINVDB[i][5])+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"+"\n"
                MsgStr=MsgStr+"\n"

        # try:
        #     line_bot_api.reply_message(
        #         event.reply_token, 
        #         TextSendMessage(
        #             text=str(
        #                 MsgStr
        #             )
        #         )
        #     )
        # except Exception as e:
        #     print("linebot無回應: "+str(e))
        print("123")
        if len(DataArrOfINVDB01002)==0:
            print("5555")
            if len(DataArrOfINVDB)==0:
                print("[成品倉]缺貨或無此品項，或請減少關鍵字，再重新查詢")
                MsgStr=MsgStr+"[成品倉]缺貨或無此品項，或請減少關鍵字，再重新查詢"
        else:
            print("6666")
            print(range(len(DataArrOfINVDB01002)))
            #print("\n")
            #MsgStr=MsgStr+"\n"


            for i in range(len(DataArrOfINVDB01002)):
                # print("i = "+str(i))
                # # print("品號 : "+str(DataArrOfINVDB01002[i][0]))
                # # print("品名 : "+str(DataArrOfINVDB01002[i][1]))
                # print(" 0: "+str(DataArrOfINVDB01002[i][0]))
                # print(" 1: "+str(DataArrOfINVDB01002[i][1]))
                # print(" 2: "+str(DataArrOfINVDB01002[i][2]))
                # print(" 3: "+str(DataArrOfINVDB01002[i][3]))
                # print(" 4: "+str(DataArrOfINVDB01002[i][4]))
                # print(" 5: "+str(DataArrOfINVDB01002[i][5]))
                print("[成品倉]")
                MsgStr=MsgStr+"[成品倉]\n"
                print("=============")
                MsgStr=MsgStr+"=============\n"
                print("品號 : "+str(DataArrOfINVDB01002[i][0]))
                MsgStr=MsgStr+"品號 : "+str(DataArrOfINVDB01002[i][0])+"\n"
                print("品名 : "+str(DataArrOfINVDB01002[i][1]))
                MsgStr=MsgStr+"品名 : "+str(DataArrOfINVDB01002[i][1])+"\n"
                
                # if str(DataArrOfINVDB01002[i][2]) == "None":
                #     print("nnn")
                #     DataArrOfINVDB01002[i][2] = None

                print("規格 : "+str(DataArrOfINVDB01002[i][2]))
                MsgStr=MsgStr+"規格 : "+str(DataArrOfINVDB01002[i][2])+"\n"
                # print("廠別代號 : "+str(DataArrOfINVDB01002[i][3]))
                # MsgStr=MsgStr+"廠別代號 : "+str(DataArrOfINVDB01002[i][3])+"\n"
                # print("廠別名稱 : "+str(DataArrOfINVDB01002[i][4]))
                # MsgStr=MsgStr+"廠別名稱 : "+str(DataArrOfINVDB01002[i][4])+"\n"
                print("庫存數量 : "+str(DataArrOfINVDB01002[i][5]))
                MsgStr=MsgStr+"庫存數量 : "+str(DataArrOfINVDB01002[i][5])+"\n"
                #print("庫存數量 : "+str(DataArrOfINVDB01002[i][5]).split(str='.'))
                # print("單位 : "+str(DataArrOfINVDB01002[i][6]))
                # MsgStr=MsgStr+"單位 : "+str(DataArrOfINVDB01002[i][6])+"\n"
                # print("小單位 : "+str(DataArrOfINVDB01002[i][7]))
                # MsgStr=MsgStr+"小單位 : "+str(DataArrOfINVDB01002[i][7])+"\n"
                # print("儲位 : "+str(DataArrOfINVDB01002[i][8]))
                # MsgStr=MsgStr+"儲位 : "+str(DataArrOfINVDB01002[i][8])+"\n"
                # print("月初數量 : "+str(DataArrOfINVDB01002[i][9]))
                # MsgStr=MsgStr+"月初數量 : "+str(DataArrOfINVDB01002[i][9])+"\n"
                # print("最近入庫日 : "+str(DataArrOfINVDB01002[i][10]))
                # MsgStr=MsgStr+"最近入庫日 : "+str(DataArrOfINVDB01002[i][10])+"\n"
                # print("最近出庫日 : "+str(DataArrOfINVDB01002[i][11]))
                # MsgStr=MsgStr+"最近出庫日 : "+str(DataArrOfINVDB01002[i][11])+"\n"
                # print("上次盤點日 : "+str(DataArrOfINVDB01002[i][12]))
                # MsgStr=MsgStr+"上次盤點日 : "+str(DataArrOfINVDB01002[i][12])+"\n"
                # print("安全存量 : "+str(DataArrOfINVDB01002[i][13]))
                # MsgStr=MsgStr+"安全存量 : "+str(DataArrOfINVDB01002[i][13])+"\n"
                # print("補貨點 : "+str(DataArrOfINVDB01002[i][14]))
                # MsgStr=MsgStr+"補貨點 : "+str(DataArrOfINVDB01002[i][14])+"\n"
                # print("經濟批量 : "+str(DataArrOfINVDB01002[i][15]))
                # MsgStr=MsgStr+"經濟批量 : "+str(DataArrOfINVDB01002[i][15])+"\n"
                # print("標準存貨量 : "+str(DataArrOfINVDB01002[i][16]))
                # MsgStr=MsgStr+"標準存貨量 : "+str(DataArrOfINVDB01002[i][16])+"\n"
                # print("標準週轉率 : "+str(DataArrOfINVDB01002[i][17]))
                # MsgStr=MsgStr+"標準週轉率 : "+str(DataArrOfINVDB01002[i][17])+"\n"
                # print("庫存包裝數量 : "+str(DataArrOfINVDB01002[i][18]))
                # MsgStr=MsgStr+"庫存包裝數量 : "+str(DataArrOfINVDB01002[i][18])+"\n"
                # print("月初包裝數量 : "+str(DataArrOfINVDB01002[i][19]))
                # MsgStr=MsgStr+"月初包裝數量 : "+str(DataArrOfINVDB01002[i][19])+"\n"

                print("i = "+str(i))
                # if a.isDate(str(DataArrOfINVDB01002[i][5])):
                    
                #     if str(DataArr[i][0])!=prePID:
                #         if i != 0:
                #             MsgStr=MsgStr+"\n"
                #         print("=============")
                #         MsgStr=MsgStr+"============="+"\n"
                #         print("品號 : "+str(DataArr[i][0]))
                #         prePID=str(DataArr[i][0])
                #         MsgStr=MsgStr+"品號 : "+str(DataArr[i][0])+"\n"
                #         print("品名 : "+str(DataArr[i][1]))
                #         MsgStr=MsgStr+"品名 : "+str(DataArr[i][1])+"\n"
                #         print("包裝方式 : "+str(DataArr[i][2]))
                #         MsgStr=MsgStr+"包裝方式 : "+str(DataArr[i][2])+"\n"
                #     print("-------------------")
                #     MsgStr=MsgStr+"-------------------"+"\n"
                #     print("庫存數量 : "+str(DataArr[i][3]))
                #     MsgStr=MsgStr+"庫存數量 : "+str(DataArr[i][3])+"\n"
                #     print("包裝數量 : "+str(DataArr[i][4]))
                #     MsgStr=MsgStr+"包裝數量 : "+str(DataArr[i][4])+"\n"
                #     print("有效期限 : "+str(DataArr[i][5]))
                #     MsgStr=MsgStr+"有效期限 : "+str(DataArr[i][5])+"\n"
                print("-------------------")
                MsgStr=MsgStr+"-------------------"
                if len(DataArrOfINVDB01002) > 1:
                    print("\n")
                    MsgStr=MsgStr+"\n"
                #print("\n")
                #MsgStr=MsgStr+"\n"
        print("1")
        try:
            print("11")
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(
                    text=str(
                        MsgStr
                    )
                )
            )
            print("2")
        except Exception as e:
            print("linebot無回應: "+str(e))
            print("3")
        
        closeThread()
        print("4")
        # print("Done.")
        # print("888888888888888888888888888888888888888888888")
        # # newDataAccess=FileDataAccess(0,'2','-', path + str(user_id) + '.txt')
        # # PID=newDataAccess.getData(1,user_id)
        # newDataAccess=FileDataAccess(0,'5','-', path + str(user_id) + '.txt')
        # PID=newDataAccess.getData(1,user_id)
        # inv=0
        # if str(PID) == "":
        #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('請先輸入品號或品名')))
        # else:
        #     print(user_id+"查"+str(PID)+"庫存")
        #     print("查"+str(PID)+"庫存")
        #     #品號查庫存
        #     # inv=str(getINV(PID))
        #     # print("庫存為:" + inv)
        #     # updateArr=["",""]
        #     # newDataAccess.setData(user_id,updateArr)
        #     # line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(inv)))
        #     PN=newDataAccess.getData(2,user_id)
        #     inv=newDataAccess.getData(3,user_id)

        #     exp_list=getExp(PID)
        #     print("品名為:" + PN)
        #     print("庫存為:" + inv)
        #     print("123")
        #     print("效期為:" + str(exp_list))
        #     print("456")
        #     # updateArr=["","","",""]
        #     # newDataAccess.setData(user_id,updateArr)
        #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="[品名]:\n"+str(PN)+"\n\n"+"[庫存數量]:\n"+str(inv))+"\n\n"+"[庫存數量]:\n"+str(exp_list))
    if '[下單]' in msg and (user_id == admin_user_id or user_id == member_id) :
        print("[下單]")

    if '[補發網通報表]' in msg :#and user_id == admin_user_id :
        print("[補發網通報表]")
        #網通群組
        try:
            line_bot_api.push_message("Caa547d0a89e353969160556a34444c64", OCPerformanceReport())
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()
        #自己
        #line_bot_api.push_message("Uee6224531167e863e3c08504055d6ed2", OCPerformanceReport())
    if '[網通報表測試]' in msg and user_id == admin_user_id :
        print("[網通報表測試]")
        #昱慧
        try:
            line_bot_api.push_message("Ud8ea127ff725488a20e30380eda16fbb", OCPerformanceReport())
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()
    if '[下一頁]' in msg and (user_id == admin_user_id or user_id == member_id) :
        print("[下一頁]")

    if ('在?' in msg or '在？' in msg or '在嗎' in msg ) and user_id == admin_user_id :
        # print("在?")
        #自己
        try:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str('我在')))
        except Exception as e:
            print("linebot無回應: "+str(e))
        closeThread()

# new_rs=None
# schedule.every(1).minutes.do(job2,new_rs)
schedule.every(1).minutes.do(job2)
schedule.every(1).minutes.do(checkExpPerf)

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

# from flask import Flask, jsonify, request
# # @app.route('/', methods=['GET'])
# # def get_tasks():
#     if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#         print('ip:'+ request.environ['REMOTE_ADDR'])
#         return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
#     else:
#         print('ip:'+ request.environ['HTTP_X_FORWARDED_FOR'])
#         return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200

import os
if __name__ == "__main__":
    print("start")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=port, debug=True)
    # app.run(host='172.21.7.39', port=port)
    # app.run(host='172.21.7.39', port=port)
    
    # app.run(debug=True)





#Line bot參數設定，及傳遞訊息涵式
#line_bot_api = LineBotApi(channel_access_token)

#schedule.every().day.at("16:17").do(handle_message)


