import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("assets/scene.jpeg")
cv.imshow("Scene",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY , 11, 3 )
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)