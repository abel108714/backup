

import pyscreenshot as ImageGrab
from io import BytesIO

img_buffer = BytesIO()
img = ImageGrab.grab(bbox=(28,200,1219,704))  # X1, Y1, X2, Y2

img.save("xmessage.png")
