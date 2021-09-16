import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("pare.jpg", cv2.IMREAD_GRAYSCALE)

#binarize image thresh
arr, threshed = cv2.threshold(image, 190, 255, cv2.THRESH_BINARY)

#conected components
_, labels = cv2.connectedComponents(threshed)
connected = np.array(labels, dtype=np.uint8)

#tags
nComponents = labels.max()
print(nComponents)

cv2.imshow("image", image)
cv2.imshow("threshed", threshed)
cv2.imshow("conected", connected)
plt.imshow(labels)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()