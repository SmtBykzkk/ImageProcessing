#Erozyon ve Genişleme

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('resim1.png',0)

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations = 1)
img_dilation = cv2.dilate(img, kernel, iterations = 1)

res = np.vstack((img,img_erosion,img_dilation))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()



#Açma

img = cv2.imread('resim1.png',0)

kernel = np.ones((5,5), dtype = np.uint8)

whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise * 255
noise_img = whiteNoise + img

opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
res = np.vstack((img,noise_img,opening))
res = res.astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

plt.imshow(res)
plt.show()



#Kapama

img = cv2.imread('resim1.png',0)

kernel = np.ones((5,5), dtype = np.uint8)

blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = blackNoise * -255
noise_img = blackNoise + img
noise_img[noise_img <= -245] = 0

closing = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
res = np.vstack((img,noise_img,opening))
res = res.astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

plt.imshow(res)
plt.show()




