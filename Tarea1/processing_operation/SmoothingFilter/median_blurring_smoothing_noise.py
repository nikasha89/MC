import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('casa.jpg')
'''kernel = np.ones((5,5),np.float32)/25'''
median = cv2.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
cv2.imwrite('median_blur_smooth_noise.jpg',median)
plt.subplot(122),plt.imshow(median),plt.title('Median Blur')
plt.xticks([]), plt.yticks([])
plt.show()