import cv2 as cv

img = cv.imread("assets/cat2.jpg")

def scaleframe(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimesnions = (width, height)
    return cv.resize(frame, dimesnions, interpolation=cv.INTER_AREA)

resized_image = scaleframe(img, 0.5)

cv.imshow("Resized Cat", resized_image)
cv.imshow("Cat", img)

cv.waitKey(0)