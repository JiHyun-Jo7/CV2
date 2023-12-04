# https://github.com/JiHyun-Jo7/CV2/blob/main/README.md#22-contour

import cv2

def contour():
    img = cv2.imread('03.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Image binarization
    ret, thimg = cv2.threshold(imgray, 127, 255, 0)
    
    # Find outline
    contours, _ = cv2.findContours(thimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw outline
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

    cv2.imshow('binary', thimg)
    cv2.imshow('outline', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()
