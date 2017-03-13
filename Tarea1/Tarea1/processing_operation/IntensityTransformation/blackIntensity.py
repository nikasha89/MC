# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import cv2

image = cv2.imread('whiteIntensity.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
# build a lookup table mapping the pixel values [0, 255] to
# their adjusted gamma values
gamma = 2.0
#invGamma = 1.0 / gamma
table = np.array([((i / 255.0) ** gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

# apply gamma correction using the lookup table
img = cv2.LUT(image, table)
cv2.imwrite('blackIntensity.jpg',img)
cv2.imshow('Oscurecida', img)
cv2.waitKey(0)