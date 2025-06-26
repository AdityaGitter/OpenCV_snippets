import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

blank[200:300, 200:300] = 0,0,255
cv.imshow("Red", blank)

img = cv.imread("assets/cat2.jpg")

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0))
cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(255,0,0),thickness=-1)
cv.imshow("Circle", blank) 

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,255), thickness=100)
cv.imshow("Line", blank)

cv.putText(blank,"Hello,my name is Aditya",(0,255),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,0),2)
cv.imshow("Text", blank)

cv.waitKey(0)