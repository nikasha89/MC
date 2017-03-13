import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('leoJimenez.jpeg')
cv2.imshow('Original',img)
cv2.waitKey(0)

img2 = np.log2(1 + img.astype(np.float)).astype(np.uint8)

img2 = 36*img2
cv2.imwrite('whiteIntensity.jpg',img2)
cv2.imshow('Iluminada',img2)
cv2.waitKey(0)
fig = plt.gcf()
fig.canvas.set_window_title('LSP histogram')
plt.hist(img2.ravel(),256,[0,256]); plt.show()
img3 = img2
B = np.int(img3.max())
A = np.int(img3.min())
print ("Maximum intensity = ", B)
print ("minimum intensity = ", A)

cv2.destroyAllWindows()