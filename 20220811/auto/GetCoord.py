import pyautogui

#隨時取得滑鼠座標
last_pos=pyautogui.position()
try:
    while True:
        #新位置
        new_pos=pyautogui.position()
        if last_pos!= new_pos:
            print(new_pos) 
            last_pos=new_pos
except KeyboardInterrupt:
    print('\nExit')



