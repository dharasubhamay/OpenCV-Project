import numpy as np
import cv2

img1 = np.zeros((250,500), np.uint8)
img2 = cv2.rectangle(img1, (0,0), (250, 250), (255,255,255), -1)
cv2.imshow('image1 console', img2)

bitNot = cv2.bitwise_not(img2)
cv2.imshow('bit Not console', bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()