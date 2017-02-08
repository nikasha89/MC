import numpy as np
import os
import cv2

'''
Parameters
----------
    One of the following strings, selecting the type of noise to add:

    'gauss'     Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.'''

noise_typ = 's&p'
imgPath = 'trex.jpg'
image = cv2.imread(imgPath)
if noise_typ == "s&p":
    row, col, ch = image.shape
    s_vs_p = 0.8
    amount = 0.06
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    noisyImgPath = "noisyImg/saltandPepperNoisy.jpg"
    cv2.imwrite(noisyImgPath, out)
elif noise_typ == "speckle":
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)
    noisy = image + image * gauss
    noisyImgPath = "noisyImg/speckleNoisy.jpg"
    cv2.imwrite(noisyImgPath, noisy)
