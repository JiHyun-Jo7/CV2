import cv2
import numpy as np

img = cv2.imread('01.jpg', cv2.IMREAD_GRAYSCALE)

# if pixel > 127, pixel is 255 and pixel < 127, pixel is 0
# pixel < threshold_value, pixel is value and pixel < 127, pixel is 0
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# pixel > 127, pixel is 0 and pixel < 127, pixel is 255
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# if pixel > 127, pixel is 127 and pixel < 127, pixel is pixel
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# if pixel > 127, pixel is pixel and pixel < 127, pixel is 0
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# if pixel > 127, pixel is 0 and pixel < 127, pixel is pixel
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Original', img)
cv2.imshow('Binary', th1)
cv2.imshow('Binary_INV', th2)
cv2.imshow('TRUNC', th3)
cv2.imshow('TOZERO', th4)
cv2.imshow('TOZERO_INV', th5)

cv2.waitKey()
cv2.destroyAllWindows
