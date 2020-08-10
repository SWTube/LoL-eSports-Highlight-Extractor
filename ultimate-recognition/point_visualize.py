import numpy as np
import find_region_of_interest as froi
import give_highlight as gh
import matplotlib.pyplot as plt
import cv2 as cv
import time
import math

interval_frame = 60
initial_frame = 14400
path = "raw3_cuted.mp4"

def visualize(normal_vec):
    plt.plot(normal_vec)
    plt.show()
    return None


def test(second):
    for k in range(4):
        froi.call_frame_test(path, initial_frame+(second-2+k)*interval_frame)
    return None


### result
l1 = [244, 353, 500, 608, 611, 722, 725, 960, 962]
l2 = [244, 435, 669, 695, 723, 958]
l3 = [244, 490, 669, 695, 720, 957]
l4 = [425, 490, 669, 693, 695, 734, 965, 1015, 1135]
l5 =[439, 669, 695, 721, 993]

r1 = [273, 419, 495, 601, 962]
r2 = [434, 992, 1110]
r3 = [260, 310, 321, 342, 372, 396, 415, 426, 463, 490, 560, 579, 595, 620, 632, 644, 656, 672, 689, 700, 708, 734, 744, 808, 820, 834, 856, 872, 921, 982, 988, 999, 1006, 1016, 1118, 1136, 1142, 1172]
r4 = [235, 490, 499, 615, 725, 990]
r5 = [490, 723, 960]

for second in l1:
    test(second)