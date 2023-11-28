import cv2

img = cv2.imread('02.jpg')
# cv2.imwrite('gray02.jpg', img)

if img is None:
    print("Image load failed")
    exit()

cv2.namedWindow('image')
cv2.moveWindow('image', 900, 400)       # Specify the position where the window appears (0, 0 based on the upper left)
cv2.resizeWindow('image', 200, 500)
cv2.imshow('image', img)                # cv2.imshow('file name', option), default: color

cv2.waitKey(2000)                       # use with imshow()
while True:
    # if cv2.waitKey() == ord('q'):    # ord : Transform ASCII
    if cv2.waitKey() == 27: # 27(ESC), 13(ENTER), 9(TAB)
        break
        
cv2.destroyAllWindows()
