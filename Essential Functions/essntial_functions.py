import cv2 as cv
import numpy as np

def resize(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale*2)
    
    dimension = (height, width)
    
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)


img1 = cv.imread('opencv/pexels-karolina-grabowska-4226881.jpg')
img= resize(img1, scale=0.1)
cv.imshow('original', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# egde cascade
canny = cv.Canny(img, 125, 125)
cv.imshow("canny", canny)

# dilation
dilated = cv.dilate(canny, (3,3), iterations=3) # type: ignore
cv.imshow("dilate", dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=3) # type: ignore
cv.imshow('eroded', eroded)

cv.waitKey(0)
cv.destroyAllWindows()