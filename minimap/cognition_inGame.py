"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: August 02, 2020
#     Purpose: Determine the game is (Playing) or (not Playing) and cut Full_Video not in_game
"""

import cv2 as cv
import numpy as np
import time


def cut_video(capture, temp):
    # fps, codec, output
    fps = capture.get(cv.CAP_PROP_FPS)
    total_frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output = cv.VideoWriter("../results/output" + ".mp4", fourcc, fps, (1920, 1080), 1)

    # Playing Video, writing output
    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
        print("{}/{} - {}%".format(current_frame, total_frame_count, round(current_frame/total_frame_count, 2)))

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if capture.get(cv.CAP_PROP_POS_FRAMES) % fps == 0:
            # template matching
            res = cv.matchTemplate(gray_frame, temp, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.4)

            if loc[::-1][0].size != 0:  # playing
                # print('writing')
                output.write(frame)
            else:
                # print('not writing')
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