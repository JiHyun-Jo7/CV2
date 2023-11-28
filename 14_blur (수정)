import cv2
import numpy as np

def bluring():
  img = cv2.imread('01.jpg')
  
  # 픽셀을 중심으로 5x5 영역을 만들고 이 영역의 모든 픽셀 값을 더한 후 이 값을 25로 나눈 값
  imgblu = np.ones((5, 5), np.float32)/25
  blur = cv2.filter2D(img, -1, imgblu)
  
  cv2.imshow('original', img)
  cv2.imshow('blur', blur)
  
  cv2.waitKey()
  cv2.destroyAllWindows()
bluring()
