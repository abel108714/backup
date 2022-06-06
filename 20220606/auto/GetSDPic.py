
import sys
import pyscreenshot as ImageGrab
from io import BytesIO




# def main(argv):
# 	args = sys.argv[1:]
# 	print(argv[0])
# 	print(argv[1])
# 	print(argv[2])

# 	img_buffer = BytesIO()
# 	img = ImageGrab.grab(bbox=(28,200,1219,704))  # X1, Y1, X2, Y2

# 	img.save(argv[1]+argv[2]+"銷貨明細_"+argv[3]+".jpg")

# if __name__ == "__main__":
# 	main(sys.argv)



img_buffer = BytesIO()
img = ImageGrab.grab(bbox=(28,200,1219,704))  # X1, Y1, X2, Y2
img.save("SDPic.jpg")