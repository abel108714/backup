#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

from datetime import datetime, timezone, timedelta
import requests as rq
import os
import socket
import logging
import datetime as dt
import Date as d

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('my.log', 'a', 'utf-8'), ])

#rqt = rq.get(OSMC_url)
#if rqt.status_code != 200:
#    OSMC_url = "https://github.com/abel108714/test/blob/master/%E5%B0%9A%E6%9C%AA%E7%94%A2%E7%94%9F%E5%A0%B1%E8%A1%A8.png"

#rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + ysdy_date_str + '_1.jpg.jpg')
#if rqt.status_code == 200:
    #ysdy_date_str = ysdy_date_str + 'Web site exists'
#else:
    #ysdy_date_str = ysdy_date_str
    #image_url
#https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_1.jpg.jpg

    #rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_'+ str(x) +'.jpg.jpg')
    #if rqt.status_code != 200:
        #urls[x]='https://raw.githubusercontent.com/abel108714/test/master/尚未產生報表.png'

    #if rqt.status_code == 200:
    #    urls[x]=urls[x]#Web site exists
    #else:
    #    urls[x]='https://raw.githubusercontent.com/abel108714/test/master/尚未產生報表.jpg.jpg'

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                # ImageCarouselColumn(
                #     image_url="https://i.imgur.com/uKYgfVs.jpg",
                #     action=URITemplateAction(
                #         label="新鮮水果",
                #         uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url="https://i.imgur.com/QOcAvjt.jpg",
                #     action=URITemplateAction(
                #         label="新鮮蔬菜",
                #         uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url="https://i.imgur.com/Np7eFyj.jpg",
                #     action=URITemplateAction(
                #         label="可愛狗狗",
                #         uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                #     )
                # ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message
# Store Performance Report
def StorePerformanceReport():
    # 設定為 +8 時區
    tz = dt.timezone(dt.timedelta(hours=+8))
    date = dt.datetime.now(tz)
    oneday = dt.timedelta(days=1)
    ydate = date-oneday



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
    yes_y=str(ydate.year)
    if int(ydate.month) < 10:
        yes_m = '0' + str(ydate.month)
    else:
        yes_m = str(ydate.month)
    if int(ydate.day) < 10:
        yes_d = '0' + str(ydate.day)
    else:
        yes_d = str(ydate.day)
    tdy_date_str = y + m + d
    ysdy_date_str = yes_y + yes_m + yes_d
    BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d

    urls = []
    for x in range(1,9):
        urls.append('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_'+ str(x) +'.jpg.jpg')
        #print(str(urls[x]))
    #logging.info('門市部日報表' + str(ysdy_date_str))
    message = TemplateSendMessage(
        alt_text='門市部日報表' + str(ysdy_date_str),
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=str(urls[0]),
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_1.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="報表1",
                        uri = urls[0]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_1.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[1],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_2.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_29_200_0_0_1228_499.jpg",
                    action=URITemplateAction(
                        label="報表2",
                        uri = urls[1]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_2.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[2],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_3.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="報表3",
                        uri = urls[2]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_3.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[3],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_4.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="報表4",
                        uri = urls[3]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_4.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[4],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_5.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="報表5",
                        uri = urls[4]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_5.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[5],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="報表6",
                        uri = urls[5]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
                # ,
                # ImageCarouselColumn(
                #     image_url=urls[6],
                #     #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg',
                #     #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                #     action=URITemplateAction(
                #         label="第1,2組",
                #         uri = urls[6]
                #         #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg'
                #         #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=urls[7],
                #     #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg',
                #     #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                #     action=URITemplateAction(
                #         label="第3,4組",
                #         uri = urls[7]
                #         #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg'
                #         #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                #     )
                # ),
                # ImageCarouselColumn(
                #     image_url=urls[8],
                #     #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg',
                #     #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                #     action=URITemplateAction(
                #         label="第5,6組",
                #         uri = urls[8]
                #         #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg'
                #         #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                #     )
                # )
            ]
        )
    )
    return message


#NewGroup
def StoreNewGroupPerformanceReport():
    # 設定為 +8 時區
    tz = dt.timezone(dt.timedelta(hours=+8))
    date = dt.datetime.now(tz)
    oneday = dt.timedelta(days=1)
    ydate = date-oneday



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
    yes_y=str(ydate.year)
    if int(ydate.month) < 10:
        yes_m = '0' + str(ydate.month)
    else:
        yes_m = str(ydate.month)
    if int(ydate.day) < 10:
        yes_d = '0' + str(ydate.day)
    else:
        yes_d = str(ydate.day)
    tdy_date_str = y + m + d
    ysdy_date_str = yes_y + yes_m + yes_d
    BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d

    urls = []
    for x in range(7,13):
        print(x)
        urls.append('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_'+ str(x) +'.jpg.jpg')
        print('https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_'+ str(x) +'.jpg.jpg')
    #logging.info('門市部日報表' + str(ysdy_date_str))
    message = TemplateSendMessage(
        alt_text='門市部日報表' + str(ysdy_date_str),
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=urls[0],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_1.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="第1組",
                        uri = urls[0]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_1.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[1],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_2.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_29_200_0_0_1228_499.jpg",
                    action=URITemplateAction(
                        label="第2組",
                        uri = urls[1]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_2.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[2],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_3.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="第3組",
                        uri = urls[2]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_3.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[3],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_4.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="第4組",
                        uri = urls[3]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_4.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[4],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_5.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="第5組",
                        uri = urls[4]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_5.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url=urls[5],
                    #image_url='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg',
                    #image_url="https://github.com/lixiuchou/report_image_host/raw/master/screen_30_200_0_0_708_456.jpg",
                    action=URITemplateAction(
                        label="第6組",
                        uri = urls[5]
                        #uri='https://raw.githubusercontent.com/abel108714/test/master/門市部日報表' + str(ysdy_date_str) + '_6.jpg.jpg'
                        #uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

def getInventoryReminderMsg():
    path = 'C:\\Users\\udev77\\Documents\\InventoryReminder.txt'
    f = open(path, 'r')
    lines = f.readlines()
    i = 0
    message = ""
    for line in lines:
        message = message + "\n" + line
        i=i+1
    f.close()
    print(message)
    return message
        # print(InvRem)

def updateInventoryReminder():
    import os
    import win32com.client
    # 開啟 Excel
    excel = win32com.client.Dispatch("Excel.Application")
    # 開啟 hello.xlsm 活頁簿檔案
    excel.Workbooks.Open(Filename="S:\網通部\◎資訊\data\績效資料\Book1.xlsm")
    # 執行巨集程式
    excel.Application.Run("Book1.xlsm!INV.庫存水位")
    # 離開 Excel
    excel.Application.Quit()
    # 清理 com 介面
    del excel

#Online Shopping & marketing channel Performance Report
    #image_message = ImageSendMessage(
    #    original_content_url='https://example.com/original.jpg',
    #    preview_image_url='https://example.com/preview.jpg'
    #)
        #message = TemplateSendMessage(
        #alt_text=BegMonthOfTodayPeriod + '累計達成比',
def SpecOCPerformanceReport(msg):
    rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/'+msg+'網通目標達成比.jpg')
    if rqt.status_code == 200:
        message = ImageSendMessage(
            original_content_url="https://raw.githubusercontent.com/abel108714/test/master/"+msg+"%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg",
            preview_image_url="https://raw.githubusercontent.com/abel108714/test/master/"+msg+"%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg"
        )
        return message
    else:
        message=TextSendMessage(text="")
        return message

def OCPerformanceReport():

    NewDate=d.Date()
    #獲取今天的日期
    tdy_date_str = NewDate.getYear() + NewDate.getMonth() + NewDate.getDay()
    #獲取昨天的日期
    ysdy_date_str = NewDate.getYear(days=1) + NewDate.getMonth(days=1) + NewDate.getDay(days=1)
    #日期區間字串
    BegMonthOfTodayPeriod = NewDate.getMonth() + str("01") + str("_") + NewDate.getMonth() + NewDate.getDay()

    OSMC_url="https://raw.githubusercontent.com/abel108714/test/master/"+BegMonthOfTodayPeriod+"%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg"
    rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/'+BegMonthOfTodayPeriod+'網通目標達成比.jpg')
    print('https://raw.githubusercontent.com/abel108714/test/master/'+BegMonthOfTodayPeriod+'網通目標達成比.jpg')

    logging.info('https://raw.githubusercontent.com/abel108714/test/master/'+BegMonthOfTodayPeriod+'網通目標達成比.jpg')


    if rqt.status_code == 200:
        message = ImageSendMessage(
            original_content_url="https://raw.githubusercontent.com/abel108714/test/master/"+BegMonthOfTodayPeriod+"%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg",
            preview_image_url="https://raw.githubusercontent.com/abel108714/test/master/"+BegMonthOfTodayPeriod+"%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg"
        )
        return message
    else:
        #print('無報表')
        message=TextSendMessage(text="目前無報表，抱歉")
        return message
        #message=TextSendMessage(text="")
        #return message
    #message = TemplateSendMessage(
    #    alt_text=BegMonthOfTodayPeriod + '累計達成比',
    #    template=ImageCarouselTemplate(
    #        columns=[
    #            ImageCarouselColumn(
    #                image_url="https://raw.githubusercontent.com/abel108714/test/master/"+BegMonthOfTodayPeriod+"網通目標達成比.jpg",
    #                action=URITemplateAction(
    #                    uri = "https://raw.githubusercontent.com/abel108714/test/master/"+BegMonthOfTodayPeriod+"網通目標達成比.jpg"
    #                )
    #            )
    #        ]
    #    )
    #)
    #return message
def PAPerformanceReport():


    # 設定為 +8 時區
    tz = dt.timezone(dt.timedelta(hours=+8))
    date = dt.datetime.now(tz)
    oneday = dt.timedelta(days=1)
    ydate = date-oneday



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
    yes_y=str(ydate.year)
    if int(ydate.month) < 10:
        yes_m = '0' + str(ydate.month)
    else:
        yes_m = str(ydate.month)
    if int(ydate.day) < 10:
        yes_d = '0' + str(ydate.day)
    else:
        yes_d = str(ydate.day)
    tdy_date_str = y + m + d
    ysdy_date_str = yes_y + yes_m + yes_d
    BegMonthOfTodayPeriod = m + str("01") + str("_") + m + d
    print('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+'實體通路目標達成比.jpg')
    print("https://raw.githubusercontent.com/abel108714/test/master/"+str(tdy_date_str)+"%E5%AF%A6%E9%AB%94%E9%80%9A%E8%B7%AF%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg")
    rqt = rq.get('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+'實體通路目標達成比.jpg')
    logging.info('https://raw.githubusercontent.com/abel108714/test/master/'+str(tdy_date_str)+'實體通路目標達成比.jpg')
    if rqt.status_code == 200:
        message = ImageSendMessage(
            original_content_url="https://raw.githubusercontent.com/abel108714/test/master/"+str(tdy_date_str)+"%E5%AF%A6%E9%AB%94%E9%80%9A%E8%B7%AF%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg",
            preview_image_url="https://raw.githubusercontent.com/abel108714/test/master/"+str(tdy_date_str)+"%E5%AF%A6%E9%AB%94%E9%80%9A%E8%B7%AF%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg"
        )
        return message
    else:
        #message=TextSendMessage(text="報表產生中，稍等")
        print('無報表')
        return message
        #https://github.com/abel108714/test/blob/master/20201014%E5%AF%A6%E9%AB%94%E9%80%9A%E8%B7%AF%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg
#OSMC_url
        #original_content_url="https://raw.githubusercontent.com/abel108714/test/master/" + str(BegMonthOfTodayPeriod) + "網通目標達成比.jpg",
        #preview_image_url="https://raw.githubusercontent.com/abel108714/test/master/" + str(BegMonthOfTodayPeriod) + "網通目標達成比.jpg"
#https://raw.githubusercontent.com/abel108714/test/master/0901_0916%E7%B6%B2%E9%80%9A%E7%9B%AE%E6%A8%99%E9%81%94%E6%88%90%E6%AF%94.jpg
#original_content_url="https://www.google.com.tw/images/branding/googlelogo/1x/"+str(dd),
#preview_image_url="https://www.google.com.tw/images/branding/googlelogo/1x/"+str(dd)
#https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
#'https://raw.githubusercontent.com/abel108714/test/master/' + str(BegMonthOfTodayPeriod) + '網通目標達成比.jpg'
#關於LINEBOT聊天內容範例