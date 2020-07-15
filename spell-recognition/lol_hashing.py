import imagehash
import cv2 as cv
import os
import numpy as np
from PIL import Image

import lol_spell_recognition as lsr


def calc_hash_dist(image_one: np.ndarray, image_two: Image) -> int:
    """
    To compare two images to see how similar they are, you can hash the images and compare the hashes.
    Here, we use the imagehash module to calculate the hash values of the images and calculate

    Args:
        image_one: image to be compared
        image_two: original image

    Returns:
        Integer value of the distance between two image hash values.
        Lower the value, higher the similarity between the two images.

    Raises:
        None
    """
    assert isinstance(image_one, np.ndarray)
    assert isinstance(image_two, Image)

    return 0


def main():
    frames = []
    original_spell = None
    in_game_spell = None
    similarity = 0

    video_path = "../resources/smite_test.mp4"
    spell_path = "../resources/summoner_spells/Smite.png"

    # Variable Initialization
    frames = lsr.video_to_list(video_path)
    original_spell = Image.open(spell_path)

    original_spell_hash = imagehash.whash(original_spell)

    ## Begin Analysis
    for frame in frames:
        in_game_spell = lsr.extract_spell_images(frame, 13)

        # Imagehash module is only compatible with Image objects from PIL module.
        cv.imwrite("in_game_spell.png", in_game_spell)

        # Re-read the image using PIL module.
        in_game_spell = Image.open("in_game_spell.png")

        in_game_spell_hash = imagehash.whash(in_game_spell)

        similarity = in_game_spell_hash - original_spell_hash
        print(similarity)

    # Delete the image from the current directory to keep project folder clean
    os.remove("../spell-recognition/in_game_spell.png")

    return None


if __name__ == '__main__':
    main()
