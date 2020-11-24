import cv2


def black_white():
    image = cv2.imread('input/meme2.png')
    cv2.imshow('Original image', image)
    black_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', black_white)
    status_black_white = cv2.imwrite('output/meme2.png', black_white)
    print("Image written to file-system black and white : ", status_black_white)
