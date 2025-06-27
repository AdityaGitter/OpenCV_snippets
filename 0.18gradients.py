import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets/cat2.jpg")
cv.imshow("Scene",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian',lap)

#Sobel
sobelx =cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("combined_sobel", combined_sobel)

cany = cv.Canny(gray, 150, 175)
cv.imshow("cany", cany)

cv.waitKey(0)

cv.waitKey(0)