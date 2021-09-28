#if only need to find blobs, ll turn to a gray image, them threshed and them find conneceted components
#   or find contours

#find particular kinds of blobs

#if we need to find especific blobs, especific caracteristics we can do simple blob detector

import cv2
import numpy as np

img = cv2.imread("image.PNG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detector instance
detector = cv2.SimpleBlobDetector_create()

#points
keypoints = detector.detect(gray)

#mark in for loop
# Mark blobs using image annotation concepts we have studied so far
for k in keypoints:
    #pt get the values from the objects?
    x = int(round(k.pt[0]))
    y = int(round(k.pt[1]))
    #x=int(round(x))
    #y=int(round(y))
    # Mark center in BLACK
    cv2.circle(gray, (x,y), 5, (0,0,0), -1)
    # Get radius of blob
    diameter = k.size
    radius = int(round(diameter/2))
    # Mark blob in RED
    for_img = cv2.circle(gray, (x,y), radius, (0,0,255), 2)

#mark blobs using image anotation
im_with_keypoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print(keypoints[1].pt)

for point in keypoints:
    print(point.pt,"\n")

cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("drawed", im_with_keypoints)
cv2.imshow("for loop", for_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
