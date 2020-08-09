import numpy as np
import find_region_of_interest as froi
import cv2 as cv

path = "raw3.mp4"
initial_frame = 20000
start_frame = froi.call_frame(path,initial_frame)
standard_skill_list = froi.cut_image(start_frame)


def analize_diffence(standard_skill_image,compare_skill_image):
    """
    15*20 skill image를 비교하는 함수, 2차원 ndarray
    :return:
    """
    difference = int(np.sum(compare_skill_image)) - int(np.sum(standard_skill_image))
    return difference


def make_diffence_list(compare_list):
    difference_list = []
    for champion_index in range(10):
        difference = analize_diffence(standard_skill_list[champion_index], compare_list[champion_index])
        difference_list.append(difference)
    difference_list = np.array(difference_list)
    return difference_list


def in_game_similarity(initial,interval)->np.ndarray: # 비동기적 처리 방식이 필요함.
    start = time.time()
    analize_data = np.empty(10)
    frame_number = 0
    while cap.get(cv.CAP_PROP_FRAME_COUNT)-interval > initial+frame_number*interval:
        print((initial+frame_number*interval)/(cap.get(cv.CAP_PROP_FRAME_COUNT)-interval)*100,"% 수행했습니다.")
        frame_number += 1
        compare_frame = froi.call_frame(path,initial+frame_number*interval)
        compare_skill_list = froi.cut_image(compare_frame)
        frame_similarity = gh.make_diffence_list(compare_skill_list)
        analize_data = np.vstack([analize_data,frame_similarity])
    print("time :", time.time() - start)
    return analize_data


def nomalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def ultimate_use_frame(skill_data_vector,threshold):
    skill_use_frame=[]
    for frame_index in range(len(skill_data_vector)-1):
        if skill_data_vector[frame_index]<threshold:
            continue
        else:
            if -threshold<skill_data_vector[frame_index+1]<threshold:
                skill_use_frame.append(frame_index)
    return skill_use_frame


if __name__ == '__main__':
    standard_skill_list_test = froi.cut_image_test(start_frame)
    compare_frame = froi.call_frame(path, 40000)
    compare_skill_list = froi.cut_image_test(compare_frame)
    print(make_diffence_list(compare_skill_list))
