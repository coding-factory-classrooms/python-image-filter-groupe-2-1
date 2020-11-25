from pathlib import Path
import cv2
import numpy as np


def dilatation():
    img = Path('input/mouais.jpeg')
    try:
        image = cv2.imread(img.name)
        cv2.imshow('Original image', image)
        kernel = np.ones((5, 5), np.uint8)
        dilatation = cv2.dilate(image, kernel, iterations=1)
        status_dilatation = cv2.imwrite('output/mouais.jpeg', dilatation)
        print("Image written to file-system blur : ", status_dilatation)
    except cv2.error:
        if not img.exists():
            print(f"Ce fichier n'existe pas  \n")
        elif not img.name.endswith(('.png', '.jpg')):
            print(f"Dilatation -> Le fichier n'est pas en bon format : {img.name.split('.')[1]} !")
