import cv2 as cv
import numpy as np

img1 = cv.imread('View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu_(cropped).jpg')
if img1 is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Resize the image
    img = cv.resize(img1, (1000, 500), interpolation=cv.INTER_AREA)
    cv.imshow("original", img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

cv.waitKey(0)
cv.destroyAllWindows()