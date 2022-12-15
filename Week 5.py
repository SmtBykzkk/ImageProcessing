import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def gaussian_noise(image): 
    row,col,ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean,sigma,(row,col,ch)) 
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

img = cv.imread("ornek.jpeg")
img = img/255
noise_img = gaussian_noise(img) 
res = np.hstack((img,noise_img))
plt.imshow(res)
plt.show()



import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import random
 
def saltPepper(img):
    row, col, channels = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 0

    return img

img = cv.imread("ornek2.jpg")
img2 = saltPepper(img)
res = np.hstack((img,img2))
plt.imshow(res)
plt.show()




img = cv.imread("kopke.jpg")
cv.imwrite('kopke_sp.jpg',
            saltPepper(img))
img2 = cv.imread("kopke_sp.jpg")
res = np.hstack((img,img2))
plt.imshow(res)
plt.show()