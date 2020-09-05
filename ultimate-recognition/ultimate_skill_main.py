import find_region_of_interest as froi
import give_highlight as gh
import cv2 as cv
import matplotlib.pyplot as plt
import math
import time
import point_visualize as pv

# Configuration Variable
path ="test.mp4"
initial_frame = 14400 # after 4 minute


cap = cv.VideoCapture(path)
interval_frame = int(cap.get(cv.CAP_PROP_FPS))+1
total_frame = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
analyze_frame = (total_frame - initial_frame) / interval_frame
threshold = math.sqrt(1/analyze_frame)


skill_similarity_matrix = gh.in_game_similarity(path, initial_frame, interval_frame)


left1 = skill_similarity_matrix[:, 0]
left2 = skill_similarity_matrix[:, 1]
left3 = skill_similarity_matrix[:, 2]
left4 = skill_similarity_matrix[:, 3]
left5 = skill_similarity_matrix[:, 4]
right1 = skill_similarity_matrix[:, 5]
right2 = skill_similarity_matrix[:, 6]
right3 = skill_similarity_matrix[:, 7]
right4 = skill_similarity_matrix[:, 8]
right5 = skill_similarity_matrix[:, 9]


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


suspect_frame_left1 = pv.change_to_frame(initial_frame, interval_frame, left1_frame)
suspect_frame_left2 = pv.change_to_frame(initial_frame, interval_frame, left2_frame)
suspect_frame_left3 = pv.change_to_frame(initial_frame, interval_frame, left3_frame)
suspect_frame_left4 = pv.change_to_frame(initial_frame, interval_frame, left4_frame)
suspect_frame_left5 = pv.change_to_frame(initial_frame, interval_frame, left5_frame)
suspect_frame_right1 = pv.change_to_frame(initial_frame, interval_frame, right1_frame)
suspect_frame_right2 = pv.change_to_frame(initial_frame, interval_frame, right2_frame)
suspect_frame_right3 = pv.change_to_frame(initial_frame, interval_frame, right3_frame)
suspect_frame_right4 = pv.change_to_frame(initial_frame, interval_frame, right4_frame)
suspect_frame_right5 = pv.change_to_frame(initial_frame, interval_frame, right5_frame)

frame_zip = [suspect_frame_left1, suspect_frame_left2, suspect_frame_left3, suspect_frame_left4, suspect_frame_left5,
              suspect_frame_right1, suspect_frame_right2, suspect_frame_right3, suspect_frame_right4, suspect_frame_right5]

bool_list = pv.frame_to_bool(total_frame, frame_zip)

print(bool_list)
