import cv2


def blur():
    image = cv2.imread('input/meme.png')
    cv2.imshow('Original image', image)
    blur = cv2.GaussianBlur(image, (15, 15), 0)
    status_blur = cv2.imwrite('output/meme.png', blur)
    print("Image written to file-system blur : ", status_blur)
