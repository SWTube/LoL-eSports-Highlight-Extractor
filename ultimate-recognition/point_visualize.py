import numpy as np
import find_region_of_interest as froi
import give_highlight as gh
import matplotlib.pyplot as plt
import cv2 as cv
import time
import math

interval_frame = 60 # 1second
initial_frame = 14400 # 4minute
path = "raw3_cuted.mp4"


def visualize(vector_1D: np.ndarray, name: str) -> None:
    """
    visualize 1D np.ndarray vector
    :param
        vector_1D: 1D array vector
    :raise
        show graph of 1D vector.
    :return
        None
    """
    plt.plot(vector_1D)
    plt.title(name)
    plt.show()
    return None


def change_to_frame(suspect_list):
    frame_converted_list = []
    for suspect_time in suspect_list:
        frame_number = initial_frame + suspect_time * interval_frame
        frame_converted_list.append(frame_number)
    return frame_converted_list


def change_to_frame(initial_frame: int, interval_frame: int, suspect_minute: list) -> list:
    """
    :param after_4_minute:
    :return:
    """
    frame_list = []
    for second in suspect_minute:
        frame_number = initial_frame + second * interval_frame
        frame_list.append(frame_number)
    return frame_list


def frame_to_bool(total_frame, zipped_frame_list: np.ndarray) -> np.ndarray:
    champion_number = 10
    formats = np.full((total_frame, champion_number), False)
    champion_index = 0
    for suspect_list in zipped_frame_list:
        for frame_data in suspect_list:
            formats[frame_data, champion_index] = True
        champion_index += 1
    return formats


if __name__ == '__main__':
    print("test")