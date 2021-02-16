import numpy as np
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