import cv2
import numpy as np
from copy import deepcopy


def greyscaleify(img):
    rows, columns = img.shape[0], img.shape[1]
    for row in range(rows):
        for column in range(columns):
            img[row, column] = [np.mean(img[row, column])] * 3
    return img

def sepiaify(img):
    rows, columns = img.shape[0], img.shape[1]
    for row in range(rows):
        for column in range(columns):
            original_blue, original_green, original_red = img[row, column]
            sepia_red = int(.393 * original_red + .769 * original_green + .189 * original_blue)
            sepia_green = int(.349 * original_red + .686 * original_green + .168 * original_blue)
            sepia_blue = int(.272 * original_red + .534 * original_green + .131 * original_blue)
            img[row, column] = [sepia_blue, sepia_green, sepia_red]
    return img

def flipify(img):
    rows, columns = img.shape[0], img.shape[1]
    for row in range(rows):
        for column in range(columns):
            b, g, r = img[row, column]
            img[row, column] = [r, g, b]
    return img

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    width = int(capture.get(3))
    height = int(capture.get(4))
    output = np.zeros(frame.shape, np.uint8)
    subimage = cv2.resize(frame, (0, 0), fx=0.5, fy= 0.5)
    subimage2 = greyscaleify(deepcopy(subimage))
    subimage3 = sepiaify(deepcopy(subimage))
    subimage4 = flipify(deepcopy(subimage))
    output[:height//2, :width//2] = subimage
    output[:height//2, width//2:] = cv2.rotate(subimage2, cv2.ROTATE_180)
    output[height//2:, :width//2] = cv2.rotate(subimage3, cv2.ROTATE_180)
    output[height//2:, width//2:] = subimage4
    cv2.imshow("Boooo", output)
    if  cv2.waitKey(1) == ord("q"):
        break

capture.close()
capture.release()
cv2.destroyAllWindows()
