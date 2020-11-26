import cv2


def ze_team(image):
    """
    This function filter colors image in ze team.
    :param image: image to modificate
    :return: filter
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 300)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    ze_team = cv2.putText(image, 'Fab et Lena', org, font, fontScale, color, thickness, cv2.LINE_AA)
    return ze_team
