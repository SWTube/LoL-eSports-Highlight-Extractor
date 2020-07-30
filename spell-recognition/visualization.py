"""
#   File Name: visualization.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
#  Start Date: 07/27/20
# Last Update: July 29, 2020
#     Purpose: Imports image comparison functions from lol_spell_recognition.py file and evaulautes them.
               Evaluation results are saved in 'result' directory.
"""
import lol_spell_recognition as lsr

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from types import FunctionType


def save_graph(compare_function: FunctionType, original_spell_image: np.ndarray, video_frames: list) -> None:
    """
    Make graph with compare_function's return value and save as PNG file

    Args:
        compare_function: Function of image comparison
        original_spell_image: Original image of spell
        video_frames : List of video

    Returns:
        None

    Raises:
        None
    """

    assert callable(compare_function)
    assert isinstance(original_spell_image, np.ndarray)
    assert isinstance(video_frames, list)

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
    plt.xlabel("Second in Game")
    plt.ylabel("Result Data")
    plt.savefig("../result/comparison_result.png", format="png")


def visualize_result(result_data: list) -> None:
    """
    Visualizes 2D list of analysis result data and
    saves them in 'result' folder.

    Args:
        result_data: 2D list of values returned from

    Returns:
        None

    Raises:
        None
    """
    assert isinstance(result_data, list)

    ## Variable Construction
    x_data = list(range(len(result_data[0])))
    y_data = result_data

    file_name = ["Left Summoner 1 D spell", "Left Summoner 1 F spell",
                 "Left Summoner 2 D spell", "Left Summoner 2 F spell",
                 "Left Summoner 3 D spell", "Left Summoner 3 F spell",
                 "Left Summoner 4 D spell", "Left Summoner 4 F spell",
                 "Left Summoner 5 D spell", "Left Summoner 5 F spell",
                 "Right Summoner 1 D spell", "Right Summoner 1 F spell",
                 "Right Summoner 2 D spell", "Right Summoner 2 F spell",
                 "Right Summoner 3 D spell", "Right Summoner 3 F spell",
                 "Right Summoner 4 D spell", "Right Summoner 4 F spell",
                 "Right Summoner 5 D spell", "Right Summoner 5 F spell"]

    # Iterate through result_data
    fig, axs = plt.subplots(10, 2)

    for i in range(10):
        axs[0, i].plot(x_data, y_data[i])
        axs[0, i].set_title(file_name[i])
    for i in range(11, 21):
        axs[1, i].plot(x_data, -y_data[i], "tab:green")
        axs[1, i].set_title(file_name[i])

    for ax in axs.flat:
        ax.set(xlabel="Second in Game", ylabel="Result Data")

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.savefig("../result/Game_analysis.png", format="png")


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
    save_graph(lsr.mean_squared_error, smite_image, frames)


if __name__ == '__main__':
    main()
