import cv2


def black_white(image):
    black_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return black_white






