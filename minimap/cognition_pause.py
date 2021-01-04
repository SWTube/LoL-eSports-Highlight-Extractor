"""
#   File Name: cognition_pause.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: September 28, 2020
#     Purpose: This file will be used module of cognition_inGame.py.
#              compare every frame and pause_image, and then cut the frame that has a pause_image.
"""

import cv2 as cv
# import matplotlib.pyplot as plot
import numpy as np


def sift_algorithm(frame_resize: np.ndarray, pause_image: np.ndarray) -> bool:
    """
        Compare video's frame and pause image, using sift_algorithm

        Args:
            frame_resize: each of video's frame that is resized to template image
            pause_image: a image (pause_image) to compare with video_capture

        Returns:
            [bool type]
            if frame_resize and pause_image match more than 15 points, return False (this frame isn't ingame.)
            if not, return True (this frame is ingame. -> match with template_image)

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