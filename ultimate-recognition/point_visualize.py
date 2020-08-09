import numpy as np
import find_region_of_interest as froi
import give_highlight as gh
import matplotlib.pyplot as plt
import cv2 as cv
import time
import math
path = "raw3_cuted.mp4"
interval_frame = 60
initial_frame = 14400


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


# def visualize(normal_vec):
#     plt.plot(normal_vec)
#     plt.show()
#     return None
#
# cap = cv.VideoCapture(path)
# analize_metrix = in_game_similarity(14400,60)
# norm_data = nomalize(analize_metrix[:,0])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,1])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,2])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,3])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,4])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,5])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,6])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,7])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,8])
# visualize(norm_data)
# norm_data = nomalize(analize_metrix[:,9])
# visualize(norm_data)
#
# #의심스러운 frame만 골라서 준다.
# img = froi.call_frame_test(path,20000+21*200)
# froi.cut_image_test(img)

def ultimate_use_frame(skill_data_vector,threshold):
    skill_use_frame=[]
    for frame_index in range(len(skill_data_vector)-1):
        if skill_data_vector[frame_index]<threshold:
            continue
        else:
            if -threshold<skill_data_vector[frame_index+1]<threshold:
                skill_use_frame.append(frame_index)
    return skill_use_frame


cap = cv.VideoCapture(path)
total_frame = cap.get(cv.CAP_PROP_FRAME_COUNT)
analize_frame = (total_frame - initial_frame)/interval_frame
threshold = math.sqrt(1/analize_frame)

analize_metrix = in_game_similarity(14400,60)
norm_data = nomalize(analize_metrix[:,0])

print(norm_data)

frame_list = ultimate_use_frame(norm_data,threshold)
print(frame_list)

def test(second):
    for k in range(20):
        froi.call_frame_test(path,initial_frame+(second-10+k)*interval_frame)
    return None


for frame in frame_list:
    test(frame)