import cv2 as cv
import numpy as np


def resize(frame, scale=0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimension = (height, width)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img1 = cv.imread('opencv/mushroooms.jpeg', cv.IMREAD_GRAYSCALE)
img = resize(img1, scale=1.2)
cv.imshow('mushrroms', img)

# laplacian
lap = cv.Laplacian(img, cv.CV_64F)  # type: ignore
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)  # type: ignore

# sobel
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobely, sobelx)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined', sobel_combined)

cv.waitKey(0)
cv.destroyAllWindows()
