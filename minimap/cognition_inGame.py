"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: August 10, 2020
#     Purpose: Determine the game is (Playing) or (not Playing) and cut Full Video when in_game
"""

import cv2 as cv
import numpy as np
import time


def cut_video(capture, temp):
    # fps, codec, output
    fps = int(capture.get(cv.CAP_PROP_FPS))
    total_frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output = cv.VideoWriter("D:/results/output.mp4", fourcc, fps, (1920, 1080), 1)
    is_ingame = False

    frame_number = 0
    capture.set(cv.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = capture.read()

    # Playing Video, writing output
    while success and frame_number <= total_frame_count:
        frame_number += fps
        capture.set(cv.CAP_PROP_POS_FRAMES, frame_number)
        success, frame = capture.read()

        current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
        percentage = int(round(current_frame / total_frame_count, 2) * 100)
        exe_time_seconds = int((total_frame_count - current_frame) / fps)
        minute = int(exe_time_seconds / 60)
        second = exe_time_seconds % 60

        if current_frame % fps == 0:
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            width_end, height_end = gray_frame.shape  # 1080, 1920
            width_start = round(266 / 1080 * width_end)  # 266
            height_start = round(289 / 1920 * height_end)  # 289

            frame_resize = gray_frame[width_start: width_end, height_start: height_end]

            # template matching
            res = cv.matchTemplate(frame_resize, temp, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.4)

            if loc[::-1][0].size != 0:  # playing
                is_ingame = True
                print("[writing] {}/{} - {}%, rest {} min {} s.".format(current_frame, total_frame_count, percentage,
                                                                        minute, second))
            else:
                is_ingame = False
                print("[not writing] {}/{} - {}%, rest {} min {} s.".format(current_frame, total_frame_count, percentage,
                                                                          minute, second))

        if is_ingame:
            output.write(frame)
        else:
            continue

    capture.release()
    output.release()
    cv.destroyAllWindows()


def main():
    start_time = time.time()

    # Full Videos
    cap = cv.VideoCapture("../resources/APKvsSB.mp4")

    # Template Image (minimap)
    template = cv.imread("../resources/minimap_templ.png", cv.IMREAD_GRAYSCALE)

    cut_video(cap, template)

    print('time:', time.time() - start_time)


if __name__ == '__main__':
    main()