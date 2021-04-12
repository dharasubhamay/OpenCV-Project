import cv2
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
cv2.imshow('image console', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()