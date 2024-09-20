import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('balnk',blank)

blank[:] = 255,0,100
# # cv.imshow('balnk',blank)

# blank[200:300, 200:300] = 255,0,0
# cv.imshow('blank', blank)

# draw a rectangle
# cv.rectangle(blank, (0,0), (100,100), (255,0,100), thickness=1)
# cv.imshow('rectangle',blank)

# draw a line
cv.line(blank, (0,10), (100,10), (0,0,0), thickness=1)
# cv.imshow('line',blank)

# draw a circle
cv.circle(blank, (250,250), 100, (250.250,250), thickness=5)
# cv.imshow('circel', blank)

# write a text
cv.putText(blank, 'hello, I am retarded', (10,100), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)