import cv2 as cv
import numpy as np

img = cv.imread('assets/cat2.jpg')

cv.imshow('Cat', img)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

blank = np.zeros(resized.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray,125 , 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,255,0), thickness=1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)