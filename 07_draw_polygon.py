import cv2
import numpy as np

img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 50), (150, 160), (0, 255, 255), 4)
# cv2.line(img, (start), (end), Color, thickness)

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
# cv2.rectangle(img, (x, y, ∆x, ∆y), Color, thickness)
cv2.rectangle(img, (50, 200), (150, 300), (0, 155, 0), -1)
# cv2.rectangle(img, (start), (end), (color), -1 : fill)
다각형 그리기
cv2.circle(img, (300,100), 30, (255, 0, 0), -1)
# cv2.circle(img, (center), radius, (color), -1)
cv2.circle(img, (300,100), 60, (170, 70, 200), 3)

point = np.array([[250, 200], [300, 200], [350, 300], [250, 300], [220, 250]])
cv2.polylines(img, [point], True, (220, 200, 0), 4)
# point : vertex cv2.polylines(img, [point], True,  Color, thickness)

text = 'Hello World!'
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 3)
# cv2.putText(img, text, location, cv2.FONT_HERSHEY_SIMPLEX, Size, Color, thickness)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
