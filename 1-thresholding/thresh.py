import cv2
import numpy as np

#para imagenes blancoynegro, pone un limite en el thresh
#si pasa ese limite el pixel se convierte al el valor max

#src
image_1 = cv2.imread("numbers.png")

#params threshold
src = image_1
thresh_limit = 120 #si esta por debajo de 120 se convierte a 255
maxval_to = 255
type_thres = cv2.THRESH_BINARY_INV

#output threshold
original, thres_image = cv2.threshold(src, thresh_limit, maxval_to, type_thres)

#showing output
cv2.imshow("trheshold", thres_image)
cv2.imshow("original", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
