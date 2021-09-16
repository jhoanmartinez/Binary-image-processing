import cv2

image = cv2.imread("white.PNG")

#kernel
kernel_size = (17, 17)
kernel_core = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)

#dilation
dilate_img = cv2.dilate(image, kernel_core, iterations=1)

#erosion
erode_img = cv2.erode(image, kernel_core)

"""morph operations"""
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
            (2*10+1, 2*10+1),
            (10, 10))

imageMorphClosed = cv2.morphologyEx(image,
                                    cv2.MORPH_CLOSE, element)

cv2.imshow("image", image)
cv2.imshow("dilate", dilate_img)
cv2.imshow("erode", erode_img)
cv2.imshow("morph", imageMorphClosed)
cv2.waitKey(0)
cv2.destroyAllWindows()