import cv2

img = cv2.imread('lena.jpg', 1) #color image = 1, grayscale image = 0, image with alpha channel = -1

cv2.imshow('image console', img)
k = cv2.waitKey(0)

if k ==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy_img.png', img)
    cv2.destroyAllWindows()