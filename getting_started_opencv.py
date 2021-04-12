import cv2
img = cv2.imread('pic3.jpg', 1)
print(img)
cv2.imshow('image console', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('pic1_copy.png', img)

