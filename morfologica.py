import cv2
import numpy as np
img = cv2.imread('numberWithNoise.png',0)
kernel = np.ones((5,5),np.uint8)
#Erosión del elemento blanco (dilatación del negro)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imwrite("dilation.jpg",erosion)
#Dilatación del blanco (erosión del negro)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imwrite("erosionada.jpg",dilation)
#Apertura
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite("opening.jpg",opening)
#Gradiente
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("gradient.jpg",gradient)
