#GriOlcek8-16-24
img = cv2.imread('vvv.jpeg')
img8 = img.astype('uint8')
img16 = img.astype('uint16')
img24 = img.astype('uint24')
res = np.hstack((img,img8,img16))
plt.imshow(res)
plt.show()