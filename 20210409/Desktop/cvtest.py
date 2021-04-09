import cv2 as cv

img = cv.imread("1617932464850.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 降噪
ret, thresh = cv.threshold(gray_img, 127, 255, 0)
# 尋找輪廓
contours, hierarchy = cv.findContours(gray_img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cnt = contours[0]
# 獲取影像矩
M = cv.moments(cnt)
print(M)

# 質心
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])

print(f'質心為：[{cx}, {cy}]')