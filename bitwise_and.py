import numpy as np
import cv2

img1 = np.zeros((250,500), np.uint8)
img2 = cv2.rectangle(img1, (0,0), (250, 250), (255,255,255), -1)

cv2.imshow('image1 console', img2)

img3 = np.zeros((250,500), np.uint8)
img4 = cv2.rectangle(img3, (200,0), (300,100), (255,255,255), -1)
cv2.imshow('image2 console', img4)

bitAnd = cv2.bitwise_and(img2, img4)
cv2.imshow('bit and console', bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()