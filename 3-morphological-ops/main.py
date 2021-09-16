import cv2
import numpy as np
import matplotlib.pyplot as plt

"""erosion amd dilation from scratch"""

#create an empty image
im = np.zeros((10, 10), dtype='uint8')
print(im)

#add some white blobs
im[0,1] = 1
im[-1,0]= 1
im[-2,-1]=1
im[2,2] = 1
im[5:8,5:8] = 1
print(im)
plt.imshow(im)
plt.show()

#elipse estruccturing element
kernel_size_1 = (2, 2)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size_1)
print(kernel)
ksize = kernel.shape[0]
height, width = im.shape[:2]

#check dilation from openCV
dilate = cv2.dilate(im, kernel)
print(dilate)
plt.imshow(dilate)
plt.show()

#dilate, cuando el pixel del centro detecta un pixel blanco, colorea los pixeles vecinos con blanco(agrega)

#erode, cuando el pixel del centro detecta pixel pixel blanco, colorea los pixeles vecinos de negro(borra)
