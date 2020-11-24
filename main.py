import numpy
import cv2

image = cv2.imread('input/meme.png')
cv2.imshow('Original image', image)

black_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', black_white)

blur = cv2.GaussianBlur(image, (15, 15), 0)

#status_black_white = cv2.imwrite('output/meme.png', black_white)
status_blur = cv2.imwrite('output/meme.png', blur)
#print("Image written to file-system black and white : ", status_black_white)
print("Image written to file-system blur : ", status_blur)


