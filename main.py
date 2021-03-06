import os
import cv2

from filtres import blur, black_white as bw, dilate, ze_team
import logger as log


def filter(input, output, filter):
    """
    Access "input" directory, read each files, modify each files, save files in other directory ("input")
    and manage exceptions
    :param input: as directory of the start
    :param output: as directory of the end where are images save
    :param filter: this are filters (as string)
    """
    with os.scandir(input) as entries:
        if os.path.exists(input):
            for entry in entries:
                if not entry.name.endswith(('.png', '.jpg')):
                    print(f"The file is not in good format : {entry.name.split('.')[1]} !")
                    continue
                image = cv2.imread(f"{input}/{entry.name}")
                log.write_log(f"Opening : {entry.name}")
                # cv2.imshow('Original image', image)
                tab = filter.split("|")
                for k in tab:
                    if k.startswith("blur"):
                        if ":" in k:
                            value_filter = k.split(':')[1]
                        else:
                            log.write_log("No value has been entered for the blur filter -> default value 1")
                            value_filter = 1
                        if int(value_filter) % 2 == 0 or int(value_filter) <= 0:
                            print(f'The blur filter is even or negative \n')
                            continue
                        image = blur.blur(image, blur_number=int(value_filter))
                        log.write_log("Applying a blur filter ...")
                    elif k.startswith("bw"):
                        image = bw.black_white(image)
                        log.write_log("Applying a black and white filter ...")
                    elif k.startswith("dilate"):
                        if ":" in k:
                            value_filter = k.split(':')[1]
                        else:
                            log.write_log("No value has been entered for the dilate filter -> default value 1")
                            value_filter = 1
                        image = dilate.dilate(image, iterations=int(value_filter))
                        log.write_log("Applying a dilate filter ...")
                    elif k.startswith("ze_team"):
                        image = ze_team.ze_team(image)
                        log.write_log("Applying a ze team filter ...")
                    else:
                        print("No filters match")
                resultat = cv2.imwrite(f'{output}/{entry.name}', image)
                log.write_log(f"Save result image in {output}/{entry.name} : {resultat} !")
        else:
            print(f"The file doesn't exist  \n")
