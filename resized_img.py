import cv2
import numpy as np
img = cv2.imread('cutting_img.png')
img = cv2.resize(img, (500,250))
cv2.imshow('image1 console', img)

img2 = np.zeros((250,500), np.uint8)
img2 = cv2.rectangle(img2, (200,0), (300,100), (255,255,255), -1)
cv2.imshow('image2 console',img2)

bitAnd = cv2.bitwise_and(img, img2)
cv2.imshow('BitWise And Console', bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()