import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(1)

desired_width = 640
desired_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
	# rectangle, start point, end point, color, thickness
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        text = "{} ({})".format(barcode_data, barcode_type)
        cv2.putText(frame, text, (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        print("Barcode Data : {}, Type: {}".format(barcode_data, barcode_type))
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
