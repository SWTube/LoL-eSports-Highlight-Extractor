"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: August 03, 2020
#     Purpose: Determine the game is (Playing) or (not Playing) and cut Full Video when in_game
"""

import cv2 as cv
import numpy as np
import time


def cut_video(capture, temp):
    # fps, codec, output
    fps = capture.get(cv.CAP_PROP_FPS)
    new_fps = round(fps)
    fps_frame = 60
    total_frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    is_ingame = False

    # Playing Video, writing output
    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
        percentage = int(round(current_frame / total_frame_count, 2) * 100)

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width_end, height_end = gray_frame.shape # 1080, 1920
        width_start = round(266 / 1080 * width_end) # 266
        height_start = round(289 / 1920 * height_end) # 289

        frame_resize = gray_frame[width_start: width_end, height_start: height_end]

        if current_frame % fps_frame == 0:
            print("{}/{} - {}%".format(current_frame, total_frame_count, percentage))

            # template matching
            res = cv.matchTemplate(frame_resize, temp, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.4)

            if loc[::-1][0].size != 0:  # playing
                is_ingame = True
            else:
                is_ingame = False

        if is_ingame:
            output = cv.VideoWriter("../results/output_4" + ".mp4", fourcc, fps, (1920, 1080), 1)
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