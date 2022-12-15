import numpy as np
import cv2
import matplotlib.pyplot as plt

row = 256
col = 256
img = np.zeros((row,col))
img[100:105, :] = 0.5
img[:, 100:105] = 1
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show


import cv2
import numpy as np

height = 512
width = 512
img = np.random.randint(255, size = (height, width, 1), dtype = np.uint8)

cv2.imshow('Binary',img)



import numpy as np
C = np.array([[1, 1, 2],[3, 5, 3],[5, 6, 9]])
C[:,2]



C = np.array([[1, 1, 2],[3, 5, 3],[5, 6, 9]])
s = sum(C[ : ])
print(s)
a = sum(C)
print(a)