from pathlib import Path
import cv2


def black_white():
    img = Path('input/meme2.png')
    try:
        image = cv2.imread(img.name)
        cv2.imshow('Original image', image)
        black_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray image', black_white)
        status_black_white = cv2.imwrite('output/meme2.png', black_white)
        print("Image written to file-system black and white : ", status_black_white)
    except cv2.error:
        if not img.exists():
            print(f"Ce fichier n'existe pas  \n")
        elif not img.name.endswith(('.png', '.jpg')):
            print(f"Black and White -> Le fichier n'est pas en bon format : {img.name.split('.')[1]} !")

