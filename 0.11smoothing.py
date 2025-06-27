import cv2 as cv
import numpy as np

img = cv.imread("assets/images/mountain.jpeg")

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow("Original", img)

average = cv.blur(img, (3,3))
cv.imshow("Averaged blur", average)

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gauss", gauss)

median = cv.medianBlur(img, 3)
cv.imshow("Median blur", median)

bilateral = cv.bilateralFilter(img, 10, 35, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)