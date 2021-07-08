# import pytesseract
# from PIL import Image
# import re

# def main():
#     pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
#     img = Image.open(r"C:\\Users\\udev77\Desktop\\11_0.jpg")
#     #img.show()
#     # # print(pytesseract.image_to_string(img, lang="chi_tra"))
#     # data = pytesseract.image_to_string(img, lang="chi_tra")
#     # dataList = re.split(r' ',data) # split the string

#     # # resultList = [str(i.strip()) for i in dataList if i != ''] # remove the '' str and convert str to int.
#     # # print(resultList)
#     # print(data)
#     # print(dataList)
#     # for i in range(len(dataList)):
#     #     print("dataList["+ str(i) +"]:"+str(dataList[i]))
#     #     s = '王瑲賢'
#     #     pos = s.find(dataList[i])
#     #     print(pos)
#     #     # if dataList[i] in s:   # 使用in運算子檢查
#     #     #     print('字串中有\'王\'')
#     #     # else:
#     #     #     print('字串中沒有\'王\'')
        

# if __name__ == "__main__":

#     main()
import os
import re
# import linebot.Date as d
def delBlank(str):
    return re.sub(r"\s+", "", str)

import pytesseract
from PIL import Image
import re
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
    img = Image.open(r"C:\\Users\\udev77\Desktop\\11_0.jpg")
    #img.show()
    # print(pytesseract.image_to_string(img, lang="chi_tra"))
    data = pytesseract.image_to_string(img, lang="chi_tra")
    dataList = re.split(r'\n ',data) # split the string
    print(dataList)
    # print(len(dataList))
    for i in range(len(dataList)-1):
        # print(str(i))
        if dataList[i] != "\n" and i>0:
            # if dataList[i] in "\n\n":
            # print(str(dataList[i]))#line.split(',')[1]str(i) + str("==>") + 
            # print(str(dataList[i]).split('\n\n')[0])
            print(str(dataList[i]).strip('\n'))
            # print(str(dataList[i]).split('\n\n')[2])
    # resultList = str([int(i.strip()) for i in dataList if i != '']) # remove the '' str and convert str to int.
    # print(resultList)
    

if __name__ == "__main__":
    # main()
    os.system("C:/linebot/PicToStrTest.py Z:\\13816417264421.jpg")

    # data = '04 月 目標'#'04 月 目標'
    # #ss=s.strip()
    # #print(ss)
    # import re
    # # demo = " Demo  Example  "
    # #print(s.strip())
    # #print(re.sub(r"^\s+|\s+$", "", s))
    # #print(re.sub(r"\s+", "", s))
    # # print(delBlank(s))
    # c=d.Date()
    # s=str(c.getMonth() + delBlank(data))
    # # print(c.getDay())
    # print("s: "+s)
    # print("data: "+data)
    # data=delBlank(data)
    # print("data: "+data)
    # # if data in s:   # 使用in運算子檢查
    # #     print('字串中有\'月目標\'')
    # # else:
    # #     print('字串中沒有\'月目標\'')

    # pos = data.find('月目標')
    # print(pos)
    