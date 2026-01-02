import cv2 as cv

img = cv.imread('brain_glioma_0009.jpg')
cv.imshow('window', img)

cv.imwrite('brain_glioma_0009_copy.jpg', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('brain_glioma_0009_gray.jpg', gray)

cv.waitKey(0)
cv.destroyAllWindows()