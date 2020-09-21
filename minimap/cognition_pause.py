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
import matplotlib as plot
import numpy as np
'''
def match_template(video_capture: np.ndarray, pause_image: np.ndarray) -> None:
    """
        Compare captured video and template image (minimap image) with sift_algorithm
        , and then write video frame that is in_game

        Args:
            video_capture: captured video using VideoCapture in __main__
            template: a template image (minimap image) to compare with video_capture
            video_file: name of video file in string type
            video_path: path of output_video (output_video will be stored this path)

        Returns:
            None

        Raises:
            N/A
    """
    is_writing = False

    # width = int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH))
    # height = int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    # fourcc = cv.VideoWriter_fourcc(*"mp4v")
    # fps = video_capture.get(cv.CAP_PROP_FPS)
    # output = cv.VideoWriter((video_path + '/' + file_name + '_output' + '.mp4'), fourcc, fps, (width, height), 1)

    # sift_ans = False
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width_end, height_end = frame_gray.shape

        width_start = round(780 / 1080 * width_end)
        height_start = round(1620 / 1920 * height_end)

        frame_resize = frame_gray[width_start: width_end, height_start: height_end]

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % int(fps) == 0:
            sift_ans = sift_algorithm(frame_resize, pause_image)
            if sift_ans:
                is_writing = True
            else:
                is_writing = False

        if is_writing:
            return False
        else:
            return True

    video_capture.release()
    cv.destroyAllWindows()
'''
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

    if len(success_match) > 15:
        return False
    else:
        return True