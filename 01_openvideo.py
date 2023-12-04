# https://github.com/JiHyun-Jo7/CV2/tree/main#01-open-video
import cv2

cap = cv2.VideoCapture('cat.mp4')

if cap.isOpened() == False:
    print("Error opening")
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    else:
        break
cap.release()
cv2.destroyAllWindows()
