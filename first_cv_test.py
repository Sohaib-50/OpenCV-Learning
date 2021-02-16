import cv2
from filters import *

img = cv2.imread('C:\Google Drive\Coding projects\FirstOpencvTest\ill4.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
# print(img)
subimg = img[75:498, 412:540]
subimg = cv2.resize(subimg, (0, 0), fx=0.5, fy=0.5)
subimg = cv2.rotate(subimg, cv2.ROTATE_90_CLOCKWISE)
img[:64, :212] = flipify(subimg)
img[img.shape[0]-64:, img.shape[1]-212:] = greyscaleify(subimg)
img = sepiaify(img)
img = flipify(img)
cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 