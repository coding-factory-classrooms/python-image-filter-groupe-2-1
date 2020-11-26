import cv2


def black_white(image):
    """
    This function filter colors image in black and white.
    :param image: image to modificate
    :return: filter
    """
    black_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return black_white






