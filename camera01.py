import cv2
import datetime
from pyzbar import pyzbar

cap = cv2.VideoCapture(1)

# limit size
desired_width = 640
disired_hieght = 480
desired_fps = 30

cap.set(3, desired_width)
cap.set(4, disired_hieght)
cap.set(5, desired_fps)

# save
csv = open("barcode.csv", 'w')
found = set()

while True:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x+y, y+h), (0, 0, 255), 2) 

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if barcodeData not in found:
            csv.write("{}.{}\n".format(datetime.datetime.now(), barcodeData))
            csv.flush()
            found.add(barcodeData)

    cv2.imshow("Barcode Scanner", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
print("[INFO] Cleaning up ..")
csv.close()
cap.release()
cv2.destroyAllWindows()
