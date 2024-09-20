import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

# rectangle
rectangle = cv.rectangle(blank.copy(), (40,40), (360,360), 255, -1)
cv.imshow('recgtangle', rectangle)
# circle
circle= cv.circle(blank.copy(),(200,200) , 200, 255,-1) # type: ignore
cv.imshow('circle', circle)
# AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('AND', bitwise_and)

# or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('OR', bitwise_or)

# XOR
bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR', bitwise_XOR)

# NOT
bitwise_NOT = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_NOT)

cv.waitKey(0)
cv.destroyAllWindows()