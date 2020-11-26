import cv2
import numpy as np


def dilate(image, iterations):
    """
    This function filter colors image in dilate.
    :param image: image to modificate
    :param iterations: intensity of dilate
    :return: filter
    """
    kernel = np.ones((5, 5), np.uint8)
    dilatation = cv2.dilate(image, kernel, iterations=iterations)
    return dilatation

