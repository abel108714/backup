# import pytesseract
from PIL import Image
import re
import Date as d
import pytesseract
# from PIL import Image
import re
import sys
import os
from FileDataAccess import *
# from PIL import ImageFile
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

def delBlank(str):
    return re.sub(r"\s+", "", str)

def delSymbol(str,symbol):
    return re.sub(r"\s+", symbol, str)

def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False

def isChinese(str):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(str)
    if match:
        return True
    else:
        return False

def isDigit(str):
    regex = r"\d+"
    matches = re.finditer(regex, str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        if len(str) == match.end():
            return True
        else:
            return False

def checkSubstring(dataList, start, end, SubString):
    i=start
    ss=""
    while i <= end:#len(dataList[i])-1
        print(i)
        print(dataList[i])
        temp=dataList[i].strip().replace(',','')
        ss=str(ss)+str(temp)
        print(ss)
        if ss==SubString and i==2:
            return True
        
            
        i=i+1
        # print(ss)
        # print(isDigit(ss))
        # print(ss.isdigit())
    return False


# def main():
#     pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
#     img = Image.open(r"C:\\Users\\udev77\\Desktop\\11_0.jpg")
#     #img.show()
#     # print(pytesseract.image_to_string(img, lang="chi_tra"))
#     data = pytesseract.image_to_string(img, lang="chi_tra+eng")
#     print(data)
#     dataList = re.split(r'\n ',data) # split the string
#     print(dataList)
#     # print(len(dataList))
#     for i in range(len(dataList)-1):
#         # print(str(i))
#         if dataList[i] != "\n" and i>0:
#             # if dataList[i] in "\n\n":
#             # print(str(dataList[i]))#line.split(',')[1]str(i) + str("==>") + 
#             # print(str(dataList[i]).split('\n\n')[0])
#             print(str(dataList[i]).strip('\n'))
#             # print(str(dataList[i]).split('\n\n')[2])
#     # resultList = str([int(i.strip()) for i in dataList if i != '']) # remove the '' str and convert str to int.
#     # print(resultList)

def main(argv):
    args = sys.argv[1:]
    # print(args[0])
    # print("PP")
    # print(args[1])
    # print(args[2])
    # args = sys.argv[1:]
    # print(args[1])
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

    
    #img = Image.open(r"C:\\Users\\udev77\Desktop\\11_0.jpg")
    #argv
    img = Image.open(args[0])
    # print(img)
    
    # img.show()
    Image.LOAD_TRUNCATED_IMAGES = True
    # r,g,b=im.split()
    # om=Image.merge('RGB',(b,g,r))
    # om.save('mydog.jpg')
    # print("PP3")
    # print(pytesseract.image_to_string(img, lang="chi_tra+eng"))
    data = pytesseract.image_to_string(img, lang="chi_tra+eng")
    # print(data)

    dataList=[]
    dataList = re.split(r' ',data) # split the string1617172996588.jpg
    #resultList = [int(i.strip()) for i in dataList if i != ''] # remove the '' str and convert str to int.
    #print(resultList)
    # print(dataList)

    # print(checkSubstring(dataList,1,2,"月目標"))
    
    i=0
    j=0
    while i < len(dataList)-1:#len(dataList[i])-1
        # print(dataList[i])
        ss=dataList[i].strip().replace(',','')
        newDataAccess=FileDataAccess(0,'2','-','S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\網通部下個月業積目標.txt')

                    #print(ws.cell(row=cell.row, column=2).value) #change column number for any cell value you want
        # wb.sheets[0].range('D' + str(i+1)).value  = Data[0]
        # wb.sheets[0].range('E' + str(i+1)).value  = Data[1]
        # wb.sheets[0].range('F' + str(i+1)).value  = Data[2]
        # wb.sheets[0].range('G' + str(i+1)).value  = Data[3]
        # wb.sheets[0].range('H' + str(i+1)).value  = Data[4]
        # wb.sheets[0].range('J' + str(i+1)).value  = Data[6]
        if ss != "" and i !=0:

            # print(ss)
            # print(isDigit(ss))
            if isDigit(ss):
                newDataAccess.setData(str(j),[ss])
                j=j+1

        i=i+1
    print("已更新個人業績目標")
    # wb = Workbook()
    # ws = wb.active
    # # 定義你所要連接的檔案名稱
    # path="S:\\網通部\網通部資料暫存區\★網通部績效小幫手專用★\業績目標.xlsx"
    # wb = xw.Book(path)
    #找第二列
    # # for row in ws.iter_rows("4月目標"):
    # #     print("value1")
    # for cell in row:
    #     if cell.value == "4月目標":
    #         print("value2")


if __name__ == "__main__":
    print("Pic")
    print(sys.argv[0])
    print("Pic")
    main(sys.argv)
