import cv2
import matplotlib.pyplot as plt

#read image
image = cv2.imread("image.PNG")

#turn in a single channel
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#binarize the image
src_thresh = gray
threshold = 127
max_val = 255
bin_type = cv2.THRESH_BINARY
arr, threshed = cv2.threshold(src_thresh, threshold, max_val, bin_type)

#find contours
src_cont = threshed
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(src_cont, mode, method)
print("number of elements are {}". format(len(contours)))

#paint contours
src_draw = image
points = contours
contour_id = -1 #begative paitn all, positive just that one
color = (0, 255, 0)
thickness = 3
draw_contours = cv2.drawContours(src_draw, points, contour_id, color, thickness)


cv2.imshow("draw_contours", draw_contours)
cv2.imshow("src_draw", src_draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
