import numpy as np
import find_region_of_interest as froi
import cv2 as cv
import time
path = "raw3_cuted.mp4"
cap = cv.VideoCapture(path)

path = "raw3.mp4"
initial_frame = 14400
start_frame = froi.call_frame(path, initial_frame)
standard_skill_list = froi.cut_image(start_frame)


def analize_diffence(standard_skill_image: np.ndarray, compare_skill_image: np.ndarray) -> int: # 여기서는 standard 변수를 받았는데 아래 함수에서는 전역 변수로 사용함. 모두 전역 변수로 사용하게 해야하나? 아니면 근야 둘다 함수 얀에서 선언할까?
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


def make_difference_list(compare_list: list) -> list:
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
    difference_list = []
    for champion_index in range(10):
        difference = analize_diffence(standard_skill_list[champion_index], compare_list[champion_index])
        difference_list.append(difference)
    difference_list = np.array(difference_list)
    return difference_list


def in_game_similarity(initial: int, interval: int) -> np.ndarray:  # 각 챔피언마다 해서 비동기적으로 하면 더 빠를 듯. 비동기적으로 못하면 행렬로 한번에 계산하는 것이 더 빠를 듯. 너무 오래걸림. 그리고 더 분할 해야 할 듯
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
    while cap.get(cv.CAP_PROP_FRAME_COUNT)-interval > initial+frame_number*interval:
        print((initial+frame_number*interval)/(cap.get(cv.CAP_PROP_FRAME_COUNT)-interval)*100,"% completed.")
        frame_number += 1
        compare_frame = froi.call_frame(path, initial+frame_number*interval)
        compare_skill_list = froi.cut_image(compare_frame)
        frame_similarity = make_difference_list(compare_skill_list)
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


def second_to_frame(second):
    """ initial frame 에서 60의 interval을 주었으므로, second 기준으로 됨. 그러므로 frame 기준으로 바꿀 필요가 있음.

    :param second:
    :return:
    """
    return None


def make_bool():
    return None




def ultimate_use_frame(skill_data_vector: np.ndarray, threshold: int):# threshold를 안에다가 설정하면 함수를 부를 때마다 다시 계산하는거 아닌가?
    """
    Skill use frame find algorithm.
    4분 후 몇초에 궁극기가 써질까?
    :param
        skill_data_vector: one champion's skill difference data. 1D array.
        threshold: global variable, It depend on the length of video.
    :var
        skill_use_second: after initial frame(4 minute), interval is 1 second. so, it means 4 minute after second list
    :return
        the
    """
    skill_use_second=[]
    print("threshold : ", threshold)
    for frame_index in range(len(skill_data_vector)-1):
        if skill_data_vector[frame_index] < threshold:
            continue
        else:
            print(frame_index, sep="")
            if -threshold < skill_data_vector[frame_index+1] < threshold:
                skill_use_second.append(frame_index)
            else:
                continue
    return skill_use_second



if __name__ == '__main__':
    standard_skill_list_test = froi.cut_image_test(start_frame)
    compare_frame = froi.call_frame(path, 40000)
    compare_skill_list = froi.cut_image_test(compare_frame)
    print(make_difference_list(compare_skill_list))
