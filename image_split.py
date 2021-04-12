import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

ball = img[280:340, 330:390] #ball = img[y1:y2, x1:x2], where (y2-y1) = (x2-x1)
cut = img[273:333, 100:160]
cut1 = cut[:]
img[273:333, 100:160] = ball

#void_space = img[284:344, 15:75]
#img[280:340, 330:390] = void_space

cv2.imshow('image', img)
cv2.imshow('image i ', cut1)
cv2.waitKey(0)
cv2.destroyAllWindows()