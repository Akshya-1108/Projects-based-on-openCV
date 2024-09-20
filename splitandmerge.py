import cv2 as cv
import numpy as np

img = cv.imread('View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu_(cropped).jpg')
# cv.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r= cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape, b.shape, g.shape, r.shape)

merged_iumage = cv.merge([b,g,r])
cv.imshow('merged', merged_iumage)

cv.waitKey(0)
cv.destroyAllWindows()