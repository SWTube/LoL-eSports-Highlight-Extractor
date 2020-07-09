"""
This file will analyse the summoner spells availability.
"""
import cv2 as cv
import numpy as np
import warnings
import time
from matplotlib import pyplot as plt

"""
All spells are assumed to be 20x20 pixels

# Left-Side
No1 Summoner D Spells Coordinates [158, 5] -> [177, 24]
No1 Summoner F Spells Coordinates [181, 5] -> [200, 24]

No2 Summoner D Spells Coordinates [261, 5] -> [280, 24]
No2 Summoner F Spells Coordinates [284, 5] -> [303, 24]

No3 Summoner D Spells Coordinates [364, 5] -> [383, 24]
No3 Summoner F Spells Coordinates [387, 5] -> [406, 24]

No4 Summoner D Spells Coordinates [466, 5] -> [485, 24]
No4 Summoner F Spells Coordinates [489, 5] -> [508, 24]

No5 Summoner D Spells Coordinates [570, 5] -> [589, 24]
No5 Summoner F Spells Coordinates [593, 5] -> [612, 24]

# Right-Side
No1 Summoner D Spells Coordinates [158, 1894] -> [177, 1913]
No1 Summoner F Spells Coordinates [181, 1894] -> [200, 1913]

No2 Summoner D Spells Coordinates [261, 1894] -> [280, 1913]
No2 Summoner F Spells Coordinates [284, 1894] -> [303, 1913]

No3 Summoner D Spells Coordinates [364, 1894] -> [383, 1913]
No3 Summoner F Spells Coordinates [387, 1894] -> [406, 1913]

No4 Summoner D Spells Coordinates [466, 1894] -> [485, 1913]
No4 Summoner F Spells Coordinates [489, 1894] -> [508, 1913]

No5 Summoner D Spells Coordinates [570, 1894] -> [589, 1913]
No5 Summoner F Spells Coordinates [593, 1894] -> [612, 1913]
"""


def video_to_list(path: str) -> list:
    """
    Converts a video file to frames and returns a list of them.

    Args:
        path: String value of path to video file.

    Returns:
        If correct path is given, this function will convert the video file to a list of frames.
        If given path is wrong, returns an empty list.

    Raises:
        N/A
    """
    frame_list = []
    vid = cv.VideoCapture(path)

    while vid.isOpened():
        ret, frame = vid.read()

        if not ret:
            break
        frame_list.append(frame)

    vid.release()
    # vid.destroyAllWindows()

    return frame_list


def main():
    frames = []
    spell_image_data = []
    spell_file = ["Barrier.png", "Challenging_Smite.png", "Chilling_Smite.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png",
                  "Hexflash.png", "Ignite.png", "Smite.png", "Teleport.png"]

    video_path = "../resources/FULL_LCKSpring2020_GRFvsDWG_W8D1_G2.mp4"
    spell_path = "../resources/summoner_spells/"
    ## Initialise
    # Load spell images
    for i in range(len(spell_file)):
        spell_image = cv.imread(spell_path + spell_file[i])
        spell_image_data.append(spell_image)
        # OpenCV uses BGR as its default color order for images, so convert to RGB
        spell_image_data[i] = cv.cvtColor(spell_image_data[i], cv.COLOR_BGR2RGB)
    # Resize all spell images to 20x20
    for i in range(len(spell_image_data)):
        spell_image_data[i] = cv.resize(spell_image_data[i], (20, 20))
    # Converts video to list of frames and saves them in *frames* list variable.
    # frames = video_to_list(video_path)


if __name__ == '__main__':
    main()
