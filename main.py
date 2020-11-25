import os
from pathlib import Path

import cv2
from filtres import blur, black_white as bw, dilatation
import logger as log


def filter(args):
    with os.scandir('img/') as entries:
        if os.path.exists('img'):
            for entry in entries:
                if not entry.name.endswith(('.png', '.jpg')):
                    print(f"Le fichier n'est pas en bon format : {entry.name.split('.')[1]} !")
                    continue
                image = cv2.imread(f"img/{entry.name}")
                log.write_log(f"Opening : {entry.name}")
                #cv2.imshow('Original image', image)
                tab = args.split("|")
                for k in tab:
                    if k.startswith("blur"):
                        value_filter = k.split(':')[1]
                        if int(value_filter) % 2 == 0 or int(value_filter) <= 0:
                            print(f'Le blur est pair ou négatif \n')
                            continue
                        image = blur.blur(image, blur_number=int(value_filter))
                        log.write_log("Applying a blur filter ...")
                    elif k.startswith("bw"):
                        image = bw.black_white(image)
                        log.write_log("Applying a black and white filter ...")
                    elif k.startswith("dilatation"):
                        value_filter = k.split(':')[1]
                        image = dilatation.dilatation(image, iterations=int(value_filter))
                        log.write_log("Applying a dilatation filter ...")
                resultat = cv2.imwrite(f'output/{entry.name}', image)
                log.write_log(f"Save result image in output/{entry.name} : {resultat} !")
        else:
            print(f"Le dossier n'existe pas  \n")




