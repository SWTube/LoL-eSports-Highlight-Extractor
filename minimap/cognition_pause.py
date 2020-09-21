"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: August 02, 2020
#     Purpose: Determine the game is (Playing) or (not Playing) and cut Full_Video not in_game
# Last Update: September 21, 2020
#     Purpose: Full video of LCK will be given in this program.
#              And compare frame and minimap image (template) per frame, using sift_algorithm.
#              (if it success for compare, that frame is ingame, if not, that frame is not ingame.)
#              Finally, this program will return edited video, except for frame that is not ingame.
"""

import cv2 as cv
# import matplotlib.pyplot as plot
import numpy as np


def sift_algorithm(frame_resize: np.ndarray, pause_image: np.ndarray) -> bool:
    """
        Compare video's frame and template image, using sift_algorithm

        Args:
            frame_resize: each of video's frame that is resized to template image
            template: a template image (minimap image) to compare with video_capture

        Returns:
            [bool type]
            if frame_resize and template match more than 15 points, return True (this frame is ingame.)
            if not, return False (this frame is not ingame.)

        Raises:
            N/A
    """
    sift = cv.xfeatures2d.SIFT_create()

    keypoint_1, descriptor_1 = sift.detectAndCompute(frame_resize, None)
    keypoint_2, descriptor_2 = sift.detectAndCompute(pause_image, None)

    bf_matcher = cv.BFMatcher()
    match = bf_matcher.knnMatch(descriptor_1, descriptor_2, 2)

    success_match = []
    for m, n in match:
        if m.distance < n.distance * 0.75:
            success_match.append([m])

    # plot_image = cv.drawMatchesKnn(frame_resize, keypoint_1, pause_image, keypoint_2, success_match, None, flags=2)
    # plot.imshow(plot_image)
    # plot.show()

    if len(success_match) > 15:
        return False
    else:
        return True