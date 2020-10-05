"""
#   File Name: give_highlight.py
#        Team: visual recognition 2
#  Programmer: luckydipper
#  Start Date: 08/08/20
# Last Update: September 21, 2020
#     Purpose: to decide whether frame's skill is used or not
"""

import numpy as np
import find_region_of_interest as froi
import cv2 as cv
import time


def analyze_difference(standard_skill_image: np.ndarray, compare_skill_image: np.ndarray) -> int:
    """
    Image compare algorithm,
    analize tho image's brightness difference. 2D array gray image data should have same shape!
    :param
        standard_skill_image: Use global variable, 2D array
        compare_skill_image: compare image data
    :var
        difference: brightness difference
    :return
        difference: brightness difference
    """
    difference = int(np.sum(compare_skill_image)) - int(np.sum(standard_skill_image))
    return difference


def make_difference_list(path, initial_frame, compare_list: list) -> list:
    """
    input champion skill image data list.
    compare difference between unused skill image list.
    difference list contain difference, which ultimate skill used before and after
    :param
        compare_list: list, which contain 2D gray image array data
        ex) [2D array data, 2D array data, ...]
    :return
        1D array, which contain difference value
        ex) [difference rate, difference rate, ...]
    """
    start_frame = froi.call_frame(path, initial_frame)
    standard_skill_list = froi.cut_image(start_frame)
    difference_list = []
    for champion_index in range(10):
        difference = analyze_difference(standard_skill_list[champion_index], compare_list[champion_index])
        difference_list.append(difference)
    difference_list = np.array(difference_list)
    return difference_list


def in_game_similarity(path: str, initial: int, interval: int) -> np.ndarray:
    """
    after initial frame, call in game skill frame which we analyze.
    make 2D array matrix, which contain difference list.

    :param
        initial: start frame. ignore before initial frame.
        interval: analyze interval

    :var
        analyze_data: to append ndarray data, format first index.

    :return
        2D array matrix. interval of each frame is interval.
        row: indicate index of champion's skill
        col: indicate index of frame's number
        [[dif_left1, dif_left2, ... dif_right5], <- frame 1, after initial frame
         [dif_left1, dif_left2, ... dif_right5], <- frame 2
                           ....
         [dif_left1, dif_left2, ... dif_right5]] <- last frame

    :raise: print used time, and complete rate
    """
    start = time.time()
    analyze_data = np.empty(10)
    frame_number = 0
    cap = cv.VideoCapture(path)
    while cap.get(cv.CAP_PROP_FRAME_COUNT)-interval > initial+frame_number*interval:
        print((initial+frame_number*interval)/(cap.get(cv.CAP_PROP_FRAME_COUNT)-interval)*100, "% completed.")
        frame_number += 1
        compare_frame = froi.call_frame(path, initial+frame_number*interval)
        compare_skill_list = froi.cut_image(compare_frame)
        frame_similarity = make_difference_list(path, initial, compare_skill_list)
        analyze_data = np.vstack([analyze_data, frame_similarity])
    print("time :", time.time() - start)
    return analyze_data


def normalize(vector: np.ndarray) -> np.ndarray:
    """
    normalize 1D array data
    :param
        vector: 1D array
    :return
        normalized vector
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def ultimate_use_frame(skill_data_vector: np.ndarray, threshold: int):
    """
    Skill use frame find algorithm.

    !CATION! : THIS FUNCTION'S RETURN VALUE IS AFTER INITIAL FRAME, SECOND, NOT FRAME 4분 후 몇 초에 궁극기가 써질까?

    :param
        skill_data_vector: one champion's skill difference data. 1D array.
        threshold: global variable, It depend on the length of video.
    :var
        skill_use_second: after initial frame(4 minute), interval is 1 second. so, it means 4 minute after second list
    :return
        the skill use second after 4 minute,
    """
    skill_use_second=[]
    for frame_index in range(len(skill_data_vector)-1):
        if skill_data_vector[frame_index] < threshold:
            continue
        else:
            if -threshold < skill_data_vector[frame_index+1] < threshold:
                skill_use_second.append(frame_index)
            else:
                continue
    return skill_use_second


def error_check(paths:str, initial_frame:int, suspect_list:list):
    """
    last check error
    :param paths:
    :param initial_frame:
    :param suspect_list:
    :return:
    """
    standard_frame = froi.call_frame(paths, initial_frame)
    cut_standard_frame = standard_frame[40:63, 880:900]
    threshold = 1000
    result_list = []
    for each_frame in suspect_list:
        compare = froi.call_frame(paths, each_frame)
        cut_compare = compare[40:63, 880:900]
        difference = analyze_difference(cut_standard_frame, cut_compare)
        if abs(difference) > threshold:
            pass
        else:
            result_list.append(each_frame)
    return result_list


if __name__ == '__main__':
    path = "raw3_cuted.mp4"
    start_frame = 14400
    standard_skill_list_test = froi.cut_image_test(start_frame)
    compare_frame = froi.call_frame(path, 40000)
    compare_skill_list = froi.cut_image_test(compare_frame)
    print(make_difference_list(compare_skill_list))