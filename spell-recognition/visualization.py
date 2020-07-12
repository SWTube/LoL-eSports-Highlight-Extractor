import lol_spell_recognition as lsr
import cv2 as cv
import numpy as np


def main():
    ## Variable Construction
    frames = []
    in_game_spell = np.array([])
    smite_image = np.array([])
    similarity = []
    smite_path = "../resources/summoner_spells/Smite.png"
    video_path = "../resources/smite_test.mp4"
    ## Variable Initialization
    # Read testing file
    frames = lsr.video_to_list(video_path)
    # Read smite image
    smite_image = cv.imread(smite_path)
    smite_image = cv.resize(smite_image, (20, 20))
    smite_image = cv.cvtColor(smite_image, cv.COLOR_BGR2RGB)
    ## Begin frame analysis
    for frame in frames:
        # Extract spell images from the frame.
        in_game_spell = lsr.extract_spell_images(frame, 13)
        similarity.append(lsr.compare_images_1(in_game_spell, smite_image))
    print(similarity)


if __name__ == '__main__':
    main()