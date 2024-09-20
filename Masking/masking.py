import cv2 as cv
import numpy as np

def rotate(img, angle, rotpoint= None):
    (height, width)= img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint, angle,1.0)
    dimensions = (height, width)
    
    return cv.warpAffine(img, rotMat, dimensions)

img = cv.imread('Masking\View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu_(cropped).jpg')
cv.imshow('original', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

rect = cv.rectangle(blank.copy(),(img.shape[1]//2-250,img.shape[0]//2-150),(img.shape[1]//2+250,img.shape[0]//2+150), 255, -1)
rect2 = cv.rectangle(blank.copy(),(img.shape[1]//2-150,img.shape[0]//2-250),(img.shape[1]//2+150,img.shape[0]//2+250), 255, -1)
# cv.imshow("mask", rect)
mask2 = cv.bitwise_or(rect,rect2)
# cv.imshow("mask2", mask2)


mask = cv.circle(blank.copy(),(img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #type: ignore

masked1 = cv.bitwise_and(img, img, mask=mask2)
cv.imshow('masked1', masked1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

# masked3= 
cv.imshow('masked3', cv.bitwise_xor(img,masked1))

cv.waitKey(0)
cv.destroyAllWindows()