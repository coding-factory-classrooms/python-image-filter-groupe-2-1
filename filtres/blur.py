from pathlib import Path
import cv2


def blur():
    blur_number = 13
    img = Path('input/meme.png')
    try:
        image = cv2.imread(img.name)
        cv2.imshow('Original image', image)
        blur = cv2.GaussianBlur(image, (blur_number, blur_number), 0)
        status_blur = cv2.imwrite('output/meme.png', blur)
        print("Image written to file-system blur : ", status_blur)
    except cv2.error:
        if blur_number % 2 == 0 or blur_number <= 0:
            print(f'Le blur est pair ou négatif \n')
        elif not img.exists():
            print(f"Ce fichier n'existe pas  \n")
        elif not img.name.endswith(('.png', '.jpg')):
            print(f"Blur -> Le fichier n'est pas en bon format : {img.name.split('.')[1]} !")
