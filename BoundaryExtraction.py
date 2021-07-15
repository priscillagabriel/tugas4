import cv2
import numpy as np

I = cv2.imread('Image3.jpg', 0)
ret, img = cv2.threshold(I, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3, 3), np.uint8)
r = cv2.erode(img, kernel, iterations=1)

e = img-r

cv2.imshow('img', img)
cv2.imshow('erode', r)
cv2.imshow('edge', e)
cv2.imwrite('edge.png', e)

cv2.waitKey(0)
cv2.destroyAllWindows()
