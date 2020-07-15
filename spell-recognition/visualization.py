import lol_spell_recognition as lsr
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from types import FunctionType


def save_graph(compare_function: FunctionType, original_spell_image: np.ndarray, video_frames: list) -> None:
    """
    
    """
    assert callable(compare_function)

    ## Variable Construction
    x_axis = []
    y_axis = []
    in_game_spell = np.array([])

    # Make List of x,y_axis
    for video_frame in video_frames:
        in_game_spell = lsr.extract_spell_images(video_frame, 13)
        y_axis.append(compare_function(in_game_spell, original_spell_image))

    x_axis = list(range(len(video_frames)))

    # Make Graph
    plt.plot(x_axis, y_axis)
    plt.xlabel("Video Time")
    plt.ylabel("Similarity")
    plt.savefig("../result/comparison_result.png", format="png")


def main():
    ## Variable Construction
    frame_count = 0
    frames = []
    in_game_spell = np.array([])
    smite_image = np.array([])
    smite_path = "../resources/summoner_spells/Smite.png"
    video_path = "../resources/smite_test.mp4"

    ## Variable Initialization
    # Read testing file
    frames, frame_count = lsr.video_to_list(video_path)

    # Read smite image
    smite_image = cv.imread(smite_path)
    smite_image = cv.resize(smite_image, (20, 20))
    smite_image = cv.cvtColor(smite_image, cv.COLOR_BGR2RGB)

    ## Begin frame analysis
    save_graph(lsr.compare_images_1, smite_image, frames)


if __name__ == '__main__':
    main()
