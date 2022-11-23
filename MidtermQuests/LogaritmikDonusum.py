#Logaritmik Donusum
import cv2
import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide = 'ignore')

image = cv2.imread('smtbykzkk.jpg')

c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype = np.uint8)

res = np.hstack((image,log_image))
plt.imshow(res)
plt.show()