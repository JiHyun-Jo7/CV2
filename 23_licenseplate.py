# https://github.com/JiHyun-Jo7/CV2/blob/main/README.md#23-license-plate-

import cv2
import numpy as np
from PIL import Image
import pytesseract

# Read Image
img = cv2.imread('car04.jpg')

# Image to Gray
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray', imgray)

# Gaussian Blur
dst = cv2.GaussianBlur(imgray, (0, 0), 1)
cv2.imshow('Gaussian', dst)

# Image binarization
ret, thimg = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('binarization', thimg)

# Find outline
contours, _ = cv2.findContours(thimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# Initialize 
selected_contours = []

# Select Area
for contour in contours:
    area = cv2.contourArea(contour)
  # range of area can be adjusted depending on the img
    if area > 2800 and area < 5600:
        selected_contours.append(contour)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

if selected_contours:
    x, y, w, h = cv2.boundingRect(np.concatenate(selected_contours))
    plate_roi = img[y:y + h, x:x + w]
    plate_text = pytesseract.image_to_string(plate_roi, config='--psm 8', lang='kor')  

    print("Number:", plate_text)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
