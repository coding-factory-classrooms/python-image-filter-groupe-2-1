import cv2


def blur(image, blur_number):
    """
    This function filter colors image in blur.
    :param image: image to modificate
    :param blur_number: intensity of blur
    :return: filter
    """
    blur = cv2.GaussianBlur(image, (blur_number, blur_number), 0)
    return blur



