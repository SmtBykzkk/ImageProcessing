import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('dejkoveci.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
plt.imshow(hsvImage)
plt.show




rgbImage = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2RGB)
plt.imshow(rgbImage)
plt.show