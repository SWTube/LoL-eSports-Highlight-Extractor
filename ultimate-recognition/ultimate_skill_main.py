import find_region_of_interest as froi
import give_highlight as gh
import cv2 as cv
import matplotlib.pyplot as plt
import math
import time


interval_frame = 60 # 60FPS 기준, 만약 다른 FPS가 나올시에 바꿀 것임.
initial_frame = 14400 # after 3 minute
path = "raw3_cuted.mp4"
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


nomal_left1 = gh.nomalize(left1)
nomal_left2 = gh.nomalize(left2)
nomal_left3 = gh.nomalize(left3)
nomal_left4 = gh.nomalize(left4)
nomal_left5 = gh.nomalize(left5)
nomal_right1 = gh.nomalize(right1)
nomal_right2 = gh.nomalize(right2)
nomal_right3 = gh.nomalize(right3)
nomal_right4 = gh.nomalize(right4)
nomal_right5 = gh.nomalize(right5)


left1_frame = gh.ultimate_use_frame(nomal_left1, threshold)
left2_frame = gh.ultimate_use_frame(nomal_left2, threshold)
left3_frame = gh.ultimate_use_frame(nomal_left3, threshold)
left4_frame = gh.ultimate_use_frame(nomal_left4, threshold)
left5_frame = gh.ultimate_use_frame(nomal_left5, threshold)
right1_frame = gh.ultimate_use_frame(nomal_right1, threshold)
right2_frame = gh.ultimate_use_frame(nomal_right2, threshold)
right3_frame = gh.ultimate_use_frame(nomal_right3, threshold)
right4_frame = gh.ultimate_use_frame(nomal_right4, threshold)
right5_frame = gh.ultimate_use_frame(nomal_right5, threshold)

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
