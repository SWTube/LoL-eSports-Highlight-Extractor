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

import csv
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from types import FunctionType


def evaluate_comparison_function(compare_function: FunctionType, original_spell_image: np.ndarray, video_frames: list) -> None:
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
        in_game_spell = np.array(in_game_spell[0], dtype="uint8")
        y_axis.append(compare_function(in_game_spell, original_spell_image))

    x_axis = list(range(len(video_frames)))

    # Make Graph
    plt.plot(x_axis, y_axis)
    plt.title("SSIM comparison")
    plt.xlabel("Second in Game")
    plt.ylabel("Result Data")
    plt.savefig("../result/comparison_result.png", format="png")


def visualize_result() -> None:
    """
    Visualizes 2D list of analysis result data and saves them in 'similarity' folder.
    "../result/similarity/"

    Raises:
        None
    """
    ## Variable Construction
    x_data = []
    y_data = []

    extension = ".csv"

    filename = ["left_summoner_1_D_spell", "left_summoner_1_F_spell", "left_summoner_2_D_spell",
                "left_summoner_2_F_spell", "left_summoner_3_D_spell", "left_summoner_3_F_spell",
                "left_summoner_4_D_spell", "left_summoner_4_F_spell", "left_summoner_5_D_spell",
                "left_summoner_5_F_spell", "right_summoner_1_D_spell", "right_summoner_1_F_spell",
                "right_summoner_2_D_spell", "right_summoner_2_F_spell", "right_summoner_3_D_spell",
                "right_summoner_3_F_spell", "right_summoner_4_D_spell", "right_summoner_4_F_spell",
                "right_summoner_5_D_spell", "right_summoner_5_F_spell"]

    # Read csv files
    for name in filename:
        path = "../result/similarity/" + name + extension

        with open(path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = csv_reader.__next__()
            data = [float(datum) for datum in data]
            y_data.append(data)

    del path
    del data

    x_data = list(range(len(y_data[0])))

    # Iterate through result_data
    fig, axs = plt.subplots(nrows=2, ncols=10, figsize=(100, 20))

    for idx in range(10):
        axs[0, idx].plot(x_data, y_data[idx])
        # axs[0, idx].set_title(filename[idx])
    for idx in range(10, 20):
        axs[1, idx - 10].plot(x_data, y_data[idx], "tab:green")
        axs[1, idx - 10].set_title(filename[idx])

    for ax in axs.flat:
        ax.set(xlabel="", ylabel="Result Data")

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.savefig("../result/Game_analysis.png", format="png")


def main():
    """## Variable Construction
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
    evaluate_comparison_function(lsr.compare_images_1, smite_image, frames)"""

    visualize_result()

    return None


if __name__ == '__main__':
    main()
