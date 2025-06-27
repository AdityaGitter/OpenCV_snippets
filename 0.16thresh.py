import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets/scene.jpeg")
cv.imshow("Scene",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

thresold, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
cv.imshow("Simple thresold", thresh)

thresold_inverse, thresh_inverse = cv.threshold(gray, 50, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple thresold Inverse", thresh_inverse)

cv.waitKey(0)