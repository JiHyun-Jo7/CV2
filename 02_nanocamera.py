# https://github.com/JiHyun-Jo7/CV2/tree/main#02-nano-camera-
import cv2
import nanocamera as nano

if __name__ == '__main__':
    # camera = nano.Camera(flip=2, width=640, height = 480, fps=30)
    camera = nano.Camera(camera_type=1, device_id=1, width=640, height=480, fps=30)
    # print("CSI Camera ready?:", camera.isReady())
    print("USB Camera ready?:", camera.isReady())

while camera.isReady():
    try:
        frame = camera.read()
        cv2.imshow("Video Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    except KeyboardInterrupt:
        break
camera.release()
del camera
