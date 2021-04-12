import numpy as np
import cv2

def click_event(event, x, y, flags, prams):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x,y), 3, (255,0,0), -1)
        color_console = np.zeros((512,512,3), np.uint8)
        color_console[:] = [blue, green, red]
        cv2.imshow('colored console', color_console)

img = cv2.imread('lena.jpg')
cv2.imshow('image console', img)

cv2.setMouseCallback('image console', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()