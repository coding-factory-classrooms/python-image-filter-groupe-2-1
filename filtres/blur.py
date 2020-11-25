import cv2


def blur(image, blur_number):
    blur = cv2.GaussianBlur(image, (blur_number, blur_number), 0)
    return blur



