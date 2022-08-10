


# 1. 開啟鼎新

# 2-1. 確認視窗位置函數
# 2-2. 密碼處輸入密碼

# 3-1. 確認視窗位置函數
# 3-2. 按工作序列

# 4. 按週期性

# 5. 報表序列函數
# 5. 按報表

import subprocess
import pyautogui
import time

cmd_str="C:\Conductor\C_dsbin\MainMenu.exe"

#開啟程式
process = subprocess.Popen(cmd_str, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

#等5秒程式開啟
time.sleep(5)

#點擊輸入密碼欄位
pyautogui.click(x=830, y=497, duration=0.01)

#輸入密碼
pyautogui.typewrite('01439')

#按enter
pyautogui.press('enter')

#點擊報表工作佇列
pyautogui.click(x=256, y=86, duration=1)

time.sleep(2)

#點擊週期性
pyautogui.click(x=691, y=389, duration=1)

#530,520
#下拉箭頭


#598,430
#

#按tab三次
pyautogui.press('enter')

#取報表序號
getCMReportIndex()


# stdout, stderr = process.communicate()
# exit_code = process.communicate()
# print(stdout, stderr, exit_code)
# print(process)
# if subprocess.check_returncode():
#     print("ok!!!!!!")


#382,497
#將滑鼠移動到(382,497)的位置，週期1秒鐘
# pyautogui.moveTo(830,497,duration=0.01)

# import pyautogui

#屏幕大小
# size=pyautogui.size()
# print(size)

#滑鼠位置
# mouse_pose=pyautogui.position()
# print(mouse_pose)

#判斷點是否在螢幕內
# print(pyautogui.onScreen(100,100))

#將滑鼠移動到(10,10)的位置，週期1秒鐘
#pyautogui.moveTo(10,10,duration=1)

#將滑鼠移動到畫面中間的位置，週期0.5秒鐘
#pyautogui.moveTo(size.width/2,size.height/2,duration=0.5)

#以當前滑鼠的位置相對移動x軸向右100，週期1秒
#pyautogui.moveRel(100,None,duration=1)

 

#隨時取得滑鼠座標
# print('12345')
# last_pos=pyautogui.position()
# try:
#     while True:
#         #新位置
#         new_pos=pyautogui.position()
#         if last_pos!= new_pos:
#             print(new_pos) 
#             last_pos=new_pos
# except KeyboardInterrupt:
#     print('\nExit')
# print('4343')


