#SaltPaperHistogram
import random
import cv2
 
def add_noise(img):
 
    row , col = img.shape

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

img = cv2.imread('xxx.jpg',cv2.IMREAD_GRAYSCALE)
 
cv2.imwrite('salt_and_pepper_test.jpg',add_noise(img))
noise=add_noise(img)
plt.imshow(noise)
plt.show()

histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show()