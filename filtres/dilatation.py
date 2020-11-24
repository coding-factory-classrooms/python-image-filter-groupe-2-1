import cv2
import numpy as np

def dilatation():
    image = cv2.imread('input/meme3.png')
    cv2.imshow('Original image', image)
    kernel = np.ones((5, 5), np.uint8)
    dilatation = cv2.dilate(image, kernel, iterations = 1)
    status_dilatation = cv2.imwrite('output/meme3.png', dilatation)
    print("Image written to file-system blur : ", status_dilatation)