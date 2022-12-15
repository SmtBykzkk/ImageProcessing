import numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("ornek.jpg")
kernel1 = np.ones((3, 3))
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
res = np.hstack((image,img))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()



image = cv2.imread("ornek.jpg")
kernel1 = np.ones((5,5),np.float64)/30
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
res = np.hstack((image,img))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()




path = r"ornek.jpg"
img = cv2.imread(path)
im1 = cv2.blur(img,(5,5))
im2 = cv2.boxFilter(img, -1,(2,2), normalize = True)
res = np.hstack((im1,im2))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()




image = cv2.imread("resim1.png")
median = cv2.medianBlur(image,5)
compare = np.concatenate((image,median), axis=1)
plt.imshow(compare)
plt.show()




image = cv2.imread("resim2.png")
out = cv2.medianBlur(image, 5)
res = np.hstack((image,out))
plt.imshow(res)
plt.show()




import sys
import cv2 as cv
import numpy as np
ddepth = cv.CV_16S
kernel_size = 3
image = cv2.imread("ay.jpeg")
src = cv.GaussianBlur (image, (3, 3), 0)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
abs_dst = cv.convertScaleAbs(dst)
plt.imshow(image)
plt.show()
plt.imshow(abs_dst)
plt.show()