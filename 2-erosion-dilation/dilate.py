import cv2
import numpy as np

#erosion borra pixeles blancos 
#dilation agrega pixeles blancos

img = cv2.imread("dilation.PNG")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshhold the image
src = gray_img
thresh = 150
maxval = 255
type_thresh = cv2.THRESH_BINARY
original, thresh = cv2.threshold(src, thresh, maxval, type_thresh)

#dilation
kernel_size_1 = (7, 7) #big kernel 1 iteration
kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size_1)
dilation_1 = cv2.dilate(thresh, kernel_1)

kernel_size_2 = (3, 3)
kernel_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size_2)
dilation_2 = cv2.dilate(thresh, kernel_2, iterations=9)

cv2.imshow("original", img)
cv2.imshow("gray", gray_img)
cv2.imshow("thresh", thresh)
cv2.imshow("dilation 1", dilation_1)
cv2.imshow("dilation 2", dilation_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
