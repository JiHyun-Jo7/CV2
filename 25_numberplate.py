# function values can be adjusted depending on the img

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
dst = cv2.GaussianBlur(imgray, (0, 0), 1.5)
cv2.imshow('Gaussian', dst)

# Convert image to black and white and Outline extraction
edge = cv2.Canny(dst, 150, 180)
cv2.imshow('edge', edge)

# Find Outline
contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initailize
selected_contours = []

# Select Area
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 2800 and area < 5000:
        selected_contours.append(contour)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

if selected_contours:
    x, y, w, h = cv2.boundingRect(np.concatenate(selected_contours))
    plate_roi = img[y:y + h, x:x + w]

    plate_text = pytesseract.image_to_string(plate_roi, lang='kor')
    print("license plate:", plate_text)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
