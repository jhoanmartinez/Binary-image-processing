import cv2

img = cv2.imread("erosion.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#thresholding to binary
threshold = 140
maxval = 255
type_thr = cv2.THRESH_BINARY
arr, thr = cv2.threshold(gray, threshold, maxval, type_thr)

#erosion, erase white dots
kernel_size_1 = (15, 15)
kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE ,kernel_size_1)
erode_1 = cv2.erode(thr, kernel_1)

cv2.imshow("erosion original", img)
cv2.imshow("gray", gray)
cv2.imshow("threshold", thr)
cv2.imshow("erosion", erode_1)

cv2.waitKey(0)
cv2.destroyAllWindows()