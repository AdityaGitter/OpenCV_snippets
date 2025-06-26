import cv2 as cv

img = cv.imread('Photos/cat2.jpg')

cv.imshow('Cat',img)

cv.waitKey(0)
