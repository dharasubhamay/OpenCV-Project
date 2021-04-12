import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('chessboard.png',1)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cut_img = img[0:465, 0:900]
cv2.imshow('cut image',cut_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('cutting_img.png',cut_img)
