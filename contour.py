import cv2 as cv
import numpy as np

def resize(frame , scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    
    dimension = (height, width)
    
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

img= cv.imread('opencv/cuitie pie.jpg')
cv.imshow("cutie pie", img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gary cutie pie", gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('jav cutie pie', blur)

canny= cv.Canny(blur, 125, 175)
cv.imshow("canny and jav cutie pie", canny)

contour, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
print(len(contour))

ret, thres = cv.threshold(gray, 125, 275 , cv.THRESH_BINARY)
cv.imshow("thresh", thres)

cv.drawContours(blank, contour, -1, (250,0,100), 1)
cv.imshow('contour', blank)

cv.waitKey(0)   
cv.destroyAllWindows()