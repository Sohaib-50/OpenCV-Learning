import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    width = int(capture.get(3))
    height = int(capture.get(4))
    output = np.zeros(frame.shape, np.uint8)
    subimage = cv2.resize(frame, (0, 0), fx=0.5, fy= 0.5)
    output[:height//2, :width//2] = subimage
    output[height//2:, width//2:] = cv2.rotate(subimage, cv2.ROTATE_180)
    cv2.imshow("Boooo", output)
    if  cv2.waitKey(1) == ord("q"):
        break

capture.close()
capture.release()
cv2.destroyAllWindows()