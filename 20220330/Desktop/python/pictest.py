import pytesseract
from PIL import Image
import re

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\udev77\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
    img = Image.open(r"C:\\Users\\udev77\Desktop\\1.JPG")
    #img.show()
    #print(pytesseract.image_to_string(img, lang="chi_tra+eng"))
    print(pytesseract)
    data = pytesseract.image_to_string(img, lang="chi_tra+eng", config ='-psm 8')
    dataList = re.split(r' |\n',data) # split the string
    resultList = [i.strip() for i in dataList if i != ''] # remove the '' str and convert str to int.
    print(resultList)



if __name__ == "__main__":
    main()