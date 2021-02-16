import cv2
import numpy as np
from copy import deepcopy

def flipify(img):
    rows, columns = img.shape[0], img.shape[1]
    for row in range(rows):
        for column in range(columns):
            b, g, r = img[row, column]
            avg = np.mean((b, g, r))
            img[row, column] = [(b - avg)%255, (g-avg)%255, (r-avg)%255]
    return img

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    # frame = flipify(frame)
    img = cv2.imread('C:\Google Drive\Coding projects\FirstOpencvTest\ill4.jpg', 1)
    img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
    subimg = img[75:498, 412:540]
    subimg = cv2.resize(subimg, (0, 0), fx=0.5, fy=0.5)
    frame[:212, :64] = subimg
    x, y = 212, 100
    # print(frame.shape)
    frame[x:x+212, y:y+64] = subimg
    cv2.imshow("Boooo", frame)
    if  cv2.waitKey(1) == ord("q"):
        break

capture.close()
capture.release()
cv2.destroyAllWindows()
