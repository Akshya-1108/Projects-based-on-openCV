import cv2 as cv
import numpy as np

def resize(frame , scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    
    dimension = (height, width)
    
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

x = cv.imread('Threshold Binarising\koala.jpeg')
img = resize(x, scale=1.1)
cv.imshow("original", img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold , thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold, thresh_inv= cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv', thresh_inv)

# adaptive threshold
adap_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)  # type: ignore
cv.imshow('adaptive', adap_thresh)
adap_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)  # type: ignore
cv.imshow('adaptive_inv', adap_thresh_inv)

b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('red',red)
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.waitKey(0)
cv.destroyAllWindows()