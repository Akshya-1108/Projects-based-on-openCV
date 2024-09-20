import cv2 as cv
import numpy as np

def resize(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale*1.5)
    
    dimension = (height, width)
    
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)



def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotpoint= None):
    (height, width)= img.shape[:2]
    
    if rotpoint is None:
        rotpoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint, angle,1.0)
    dimensions = (height, width)
    
    return cv.warpAffine(img, rotMat, dimensions)


img = resize(cv.imread('opencv/pexels-karolina-grabowska-4226881.jpg'),0.1)
cv.imshow('original', img)

# translated
Timg=translate(img,100, 100)
cv.imshow('translated', Timg)

# rotated
rotated = rotate(Timg, 90)
cv.imshow("rotated", rotated)

cv.waitKey(0)
