import pytesseract
from PIL import Image
import re

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
    img = Image.open(r"C:\\Users\\udev77\Desktop\\1614301472530.jpg")
    #img.show()
    # print(pytesseract.image_to_string(img, lang="chi_tra"))
    data = pytesseract.image_to_string(img, lang="chi_tra")
    dataList = re.split(r' ',data) # split the string

    # resultList = [str(i.strip()) for i in dataList if i != ''] # remove the '' str and convert str to int.
    # print(resultList)
    print(data)
    print(dataList)
    for i in range(len(dataList)):
        print("dataList["+ str(i) +"]:"+str(dataList[i]))
        s = '王瑲賢'
        pos = s.find(dataList[i])
        print(pos)
        # if dataList[i] in s:   # 使用in運算子檢查
        #     print('字串中有\'王\'')
        # else:
        #     print('字串中沒有\'王\'')
        

if __name__ == "__main__":

    main()