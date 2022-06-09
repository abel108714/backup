# -*- coding: utf-8 -*-
import os
import socket
from datetime import datetime, timezone, timedelta
import time
#import win32api
# 設定為 +8 時區
tz = timezone(timedelta(hours=+8))
# 取得現在時間、指定時區、轉為 ISO 格式



HOST = '172.21.7.39'#'127.0.0.1''172.21.7.39'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    print('Client message is:', clientMessage)
    if clientMessage == 'Hello!':
        print('ok!')

    #print(datetime.now(tz).isoformat())
    args = str(time.localtime().tm_hour) + str(time.localtime().tm_min) + str(time.localtime().tm_sec)
    #print(str(time.localtime().tm_hour) + str(time.localtime().tm_min) + str(time.localtime().tm_sec))
    os.system("UpdateFileName " + args)
    #time.sleep( 10 )
    serverMessage = args
    #serverMessage = 'I\'m here!'
    conn.sendall(serverMessage.encode())
    conn.close()

os.system("pause")