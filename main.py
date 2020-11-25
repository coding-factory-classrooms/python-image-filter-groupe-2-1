import os
import cv2
from filtres import blur, black_white as bw, dilatation


def filter(args):
    with os.scandir('img/') as entries:
        if os.path.exists('img'):
            for entry in entries:
                if not entry.name.endswith(('.png', '.jpg')):
                    print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]} !")
                    continue
                print(entry.name)
                image = cv2.imread(f"img/{entry.name}")
                #cv2.imshow('Original image', image)
                tab = args.split("|")
                for k in tab:
                    if k.startswith("blur"):
                        value_filter = k.split(':')[1]
                        image = blur.blur(image, blur_number=int(value_filter))
                    elif k.startswith("bw"):
                        image = bw.black_white(image)
                    elif k.startswith("dilatation"):
                        value_filter = k.split(':')[1]
                        image = dilatation.dilatation(image, iterations=int(value_filter))
                status = cv2.imwrite(f'output/{entry.name}', image)
                print("Image written to file-system : ", status)
        else:
            print(f"Le dossier n'existe pas  \n")




