import cv2 as cv

img = cv.imread('brain_glioma_0009.jpg')
cv.imshow('window', img)
img1 = cv.imread('brain_glioma_0009.jpg')
cv.imshow('window1', img1)
cv.waitKey(0) 
cv.destroyAllWindows()