import cv2


def blur(image, blur_number):
    try:
        blur = cv2.GaussianBlur(image, (blur_number, blur_number), 0)
        return blur
    except cv2.error:
        if blur_number % 2 == 0 or blur_number <= 0:
            print(f'Le blur est pair ou négatif \n')
            return None



