import os
import cv2
from filtres import blur, black_white as bw, dilatation


with os.scandir('img/') as entries:
    if os.path.exists('img'):
        for entry in entries:
            if not entry.name.endswith(('.png', '.jpg')):
                print(f"Blur -> Le fichier n'est pas en bon format : {entry.name.split('.')[1]} !")
                continue
            print(entry.name)
            image = cv2.imread(f"img/{entry.name}")
            #cv2.imshow('Original image', image)
            image = blur.blur(image)
            image = bw.black_white(image)
            image = dilatation.dilatation(image)
            status = cv2.imwrite(f'output/{entry.name}', image)
            print("Image written to file-system : ", status)
    else:
        print(f"Le dossier n'existe pas  \n")




