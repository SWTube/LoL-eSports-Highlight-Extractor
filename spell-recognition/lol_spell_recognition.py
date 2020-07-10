"""
#   File Name: lol_spell_recognition.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
#  Start Date: 06/05/20
# Last Update: July 10, 2020
#     Purpose: This file specifically tries to recognize the cooltime of summoner spells
               and uses this data to calculate highlight score of the game.
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
        None
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


def mse(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Calculates the 'Mean Squared Error' between the two images,
    which is the sum of the squared difference between the two images;
    CAUTION! the two images must have the same dimension.

    Args:
        imgA: Image to compare.
        imgB: Original image

    Returns:
        MSE. Lower the error, the more "similar" the two images are.

    Raises:
        None
    """
    error = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
    error /= float(imgA.shape[0] * imgA.shape[1])

    return error


# LAC
def compare_images_1(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Calculates the similarity of the two images.

    Args:
        imgA: Image to compare.
        imgB: Original image

    Returns:
        "Similarity" percentage of the two images.

    Raises:
        None
    """
    return None


# LJH
def compare_images_2(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Compare two images through histogram

    Args:
        imgA: image in video
        imgB: original image

    Returns:
        Similarity between two images

    Raises:
        None
    """
    #Convert to hsv
    hsv_a = cv.cvtColor(imgA, cv.COLOR_BGR2HSV)
    hsv_b = cv.cvtColor(imgB, cv.COLOR_BGR2HSV)

    # Calculate and Normalize histogram
    hist_a = cv.calcHist([hsv_a], [0], None, [256], [0, 256])
    cv.normalize(hist_a, hist_a, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    hist_b = cv.calcHist([hsv_b], [0], None, [256], [0, 256])
    cv.normalize(hist_b, hist_b, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # Compare hist_a, hist_b
    a_b_comparison = cv.compareHist(hist_a, hist_b, 0)

    return a_b_comparison


def extract_spell_images(frame: np.ndarray) -> list:
    """
    Extracts summoners' spell images from the in-game image given as a parameter.

    Args:
        frame: A single frame from the game video.

    Returns:
        list of summoners' spell images.

    Raises:
        None
    """
    in_game_spell = [[[], [], [], [], []], [[], [], [], [], []]]

    for y in range(158, 178):
        for x in range(5, 25):


    return None


def main():
    frames = []
    spell_image_data = []
    in_game_spell = []
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


    ####
    print(compare_images_2(spell_image_data[0], spell_image_data[0]))

if __name__ == '__main__':
    main()
