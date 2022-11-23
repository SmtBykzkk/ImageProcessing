#Gamma Donusumu
import cv2
import numpy as np
from matplotlib import pyplot as plt

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('babayagajr.jpg')
gammaImg = gammaCorrection(img, 2.2)

res = np.hstack((img,gammaImg))
plt.imshow(res)
plt.show()