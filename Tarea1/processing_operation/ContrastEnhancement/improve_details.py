import cv2

img = cv2.imread('leoJimenez.jpeg')

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.waitKey(0)
cv2.imwrite('improveDetailsImg.jpg',img_output)
cv2.imshow('Histogram equalized', img_output)
cv2.waitKey(0)