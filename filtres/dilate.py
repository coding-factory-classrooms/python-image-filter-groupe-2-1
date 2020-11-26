import cv2
import numpy as np


def dilate(image, iterations):
    kernel = np.ones((5, 5), np.uint8)
    dilatation = cv2.dilate(image, kernel, iterations=iterations)
    return dilatation

