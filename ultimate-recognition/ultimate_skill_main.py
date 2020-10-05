import find_region_of_interest as froi
import give_highlight as gh
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import point_visualize as pv
import finding_ultimate as fu
import decision_highlight as dh


def get_is_ultimate_used() -> list:
    """
        AVI for 1920 x 1080 version

        Can get bool type list is ultimate skill used
        Args:

        Returns:
            bool type list, it shows is ultimate skill used
        Raises:
            None
    """
    # Configuration Variable
    path ="test5.mp4"
    initial_frame = 14400 # after 4 minute


    cap = cv.VideoCapture(path)
    interval_frame = int(cap.get(cv.CAP_PROP_FPS))+1
    total_frame = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    total_sec = int(total_frame / 60)
    analyze_frame = (total_frame - initial_frame) / interval_frame


    assert analyze_frame >= 0, "initial frame is larger than total frame"
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



    print(
        f"""
        --- ultimate used second ---
        -> after 4minute + this second
        left1 : {left1_frame}
        left2 : {left2_frame}
        left3 : {left3_frame}
        left4 : {left4_frame}
        left5 : {left5_frame}
        right1 : {right1_frame}
        right2 : {right2_frame}
        right3 : {right3_frame}
        right4 : {right4_frame}
        right5 : {right5_frame}
        """)


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

    result_frame_l1 = gh.error_check(path, initial_frame, suspect_frame_left1)
    result_frame_l2 = gh.error_check(path, initial_frame, suspect_frame_left2)
    result_frame_l3 = gh.error_check(path, initial_frame, suspect_frame_left3)
    result_frame_l4 = gh.error_check(path, initial_frame, suspect_frame_left4)
    result_frame_l5 = gh.error_check(path, initial_frame, suspect_frame_left5)
    result_frame_r1 = gh.error_check(path, initial_frame, suspect_frame_right1)
    result_frame_r2 = gh.error_check(path, initial_frame, suspect_frame_right2)
    result_frame_r3 = gh.error_check(path, initial_frame, suspect_frame_right3)
    result_frame_r4 = gh.error_check(path, initial_frame, suspect_frame_right4)
    result_frame_r5 = gh.error_check(path, initial_frame, suspect_frame_right5)

    print(
        f"""
        --- ultimate used frame ---
        left1 : {result_frame_l1}
        left2 : {result_frame_l2}
        left3 : {result_frame_l3}
        left4 : {result_frame_l4}
        left5 : {result_frame_l5}
        right1 : {result_frame_r1}
        right2 : {result_frame_r2}
        right3 : {result_frame_r3}
        right4 : {result_frame_r4}
        right5 : {result_frame_r5}
        """)

    frame_zip = [result_frame_l1, result_frame_l2, result_frame_l3, result_frame_l4, result_frame_l5,
                  result_frame_r1, result_frame_r2, result_frame_r3, result_frame_r4, result_frame_r5]


    bool_list = pv.frame2bool_per_sec(total_sec, frame_zip)

    return bool_list


def get_highlight_graph() -> None:
    """
        draw graph and return highlight score list
        Args:

        Returns:
            highlight score list
        Raises:
            None
    """
    # load champion name, bool type list(is ultimate used)
    champion_name = fu.get_champion_name()
    is_ultimate_used = get_is_ultimate_used()

    # make highlight list
    highlight_score_list = dh.get_highlight_list(champion_name, is_ultimate_used)

    # draw highlight graph
    graph_x = range(len(is_ultimate_used))
    graph_y = highlight_score_list

    plt.plot(graph_x, graph_y)
    plt.show()

    return highlight_score_list


def main():
    get_highlight_graph()


if __name__ == "__main__":
    main()