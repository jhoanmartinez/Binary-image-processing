import cv2

#original image
image = cv2.imread("image.PNG")

#opening es erode after dilate
kernel_size = (9, 9)
kernel_core = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)

erode_img = cv2.erode(image, kernel_core, iterations=1)
dilate_img = cv2.erode(erode_img, kernel_core, iterations=1)

"""morph operations"""
imageMorphClosed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_core)

#display
cv2.imshow("image", image)
cv2.imshow("erode", erode_img)
cv2.imshow("dilate", dilate_img)
cv2.imshow("morph", imageMorphClosed)
cv2.waitKey(0)
cv2.destroyAllWindows()
