import cv2

rtsp_url = 'rtsp://210.99.70.120:1935/live/cctv040.stream'

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error")
    exit()
while True:
    ret, img = cap.read()
    if ret:
        cv2.imshow("video output", img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print("Error", Frame)
        break
cap.release()
cv2.destroyAllWindow()
