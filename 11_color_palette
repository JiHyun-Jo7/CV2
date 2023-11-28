import cv2
import numpy as np

def onChange(x):
    pass
def trackbar():
    img = np.zeros((200, 512,3), np.uint8)
    cv2.namedWindow('color_palette')    # create palette (size : 200x512)

    # create Trackbar(can change 0 to 255) in palette
    cv2.createTrackbar('B', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('G', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('R', 'color_palette', 0, 255, onChange)

    # create Switch(can change 0 and 1) in palette
    switch = '0 : Off\n 1 : On'
    cv2.createTrackbar(switch, 'color_palette', 0, 1, onChange)

    while True:
        cv2.imshow('color_palette',img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27: # ESC
            break
        
        # load Trackbar Data
        b = cv2.getTrackbarPos('B', 'color_palette')
        g = cv2.getTrackbarPos('G', 'color_palette')
        r = cv2.getTrackbarPos('R', 'color_palette')
        s = cv2.getTrackbarPos(switch, 'color_palette')

        # If trackbar is Black, can control 
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]
    cv2.destroyAllWindows()
trackbar()
