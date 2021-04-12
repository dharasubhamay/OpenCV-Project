import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8) #For Black image use 3

cv2.imshow('image console', img)

cv2.waitKey(0)
cv2.destroyAllWindows()