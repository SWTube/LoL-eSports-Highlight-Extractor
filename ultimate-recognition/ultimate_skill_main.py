import find_region_of_interest as froi
import give_highlight as gh
import cv2 as cv
import matplotlib.pyplot as plt
import math
import time
import point_visualize as pv


interval_frame = 60 # 60FPS 기준, 만약 다른 FPS가 나올시에 바꿀 것임.
initial_frame = 14400 # after 4 minute
path = "raw3_cuted.mp4"
# threshold 하고, standard 를 전역변수로 설정하면 다른 모듈에서 쓸 때 import 해야하나? 아니면 그냥 지역변수로 설정하는 것이 좋을까?
cap = cv.VideoCapture(path)
total_frame = cap.get(cv.CAP_PROP_FRAME_COUNT)
analize_frame = (total_frame - initial_frame) / interval_frame
threshold = math.sqrt(1/analize_frame)
cap = cv.VideoCapture(path)


skill_simularity_metrix = gh.in_game_similarity(initial_frame, interval_frame)

left1 = skill_simularity_metrix[:, 0]
left2 = skill_simularity_metrix[:, 1]
left3 = skill_simularity_metrix[:, 2]
left4 = skill_simularity_metrix[:, 3]
left5 = skill_simularity_metrix[:, 4]
right1 = skill_simularity_metrix[:, 5]
right2 = skill_simularity_metrix[:, 6]
right3 = skill_simularity_metrix[:, 7]
right4 = skill_simularity_metrix[:, 8]
right5 = skill_simularity_metrix[:, 9]


normal_left1 = gh.normalize(left1)
normal_left2 = gh.normalize(left2)
normal_left3 = gh.normalize(left3)
normal_left4 = gh.normalize(left4)
normal_left5 = gh.normalize(left5)
normal_right1 = gh.normalize(right1)
normal_right2 = gh.normalize(right2)
normal_right3 = gh.normalize(right3)
normal_right4 = gh.normalize(right4)
normal_right5 = gh.normalize(right5)


pv.visualize(normal_left1, "left1")
pv.visualize(normal_left2, "left2")
pv.visualize(normal_left3, "left3")
pv.visualize(normal_left4, "left4")
pv.visualize(normal_left5, "left5")
pv.visualize(normal_right1, "right1")
pv.visualize(normal_right2, "right2")
pv.visualize(normal_right3, "right3")
pv.visualize(normal_right4, "right4")
pv.visualize(normal_right5, "right5")

left1_frame = gh.ultimate_use_frame(normal_left1, threshold)
left2_frame = gh.ultimate_use_frame(normal_left2, threshold)
left3_frame = gh.ultimate_use_frame(normal_left3, threshold)
left4_frame = gh.ultimate_use_frame(normal_left4, threshold)
left5_frame = gh.ultimate_use_frame(normal_left5, threshold)
right1_frame = gh.ultimate_use_frame(normal_right1, threshold)
right2_frame = gh.ultimate_use_frame(normal_right2, threshold)
right3_frame = gh.ultimate_use_frame(normal_right3, threshold)
right4_frame = gh.ultimate_use_frame(normal_right4, threshold)
right5_frame = gh.ultimate_use_frame(normal_right5, threshold)


print(left1_frame)
print(left2_frame)
print(left3_frame)
print(left4_frame)
print(left5_frame)

print(right1_frame)
print(right2_frame)
print(right3_frame)
print(right4_frame)
print(right5_frame)
