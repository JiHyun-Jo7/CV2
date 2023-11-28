import cv2
import numpy as np
import matplotlib.pyplot as plt

def Canny():
    img = cv2.imread('01.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 150, 200)

    cv2.imshow('Original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey()
    cv2.destroyAllWindows()

Canny()
