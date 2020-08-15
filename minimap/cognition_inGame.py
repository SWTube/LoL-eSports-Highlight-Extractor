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


def cut_video(capture, temp, frame, frame_number) -> None:
    # fps, codec, output
    fps = int(capture.get(cv.CAP_PROP_FPS))
    total_frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output = cv.VideoWriter("D:/results/output_2.mp4", fourcc, 30, (1920, 1080), 1)
    is_ingame = False

    success = True

    while capture.isOpened():
        # Playing Video, writing output
        if success and frame_number <= total_frame_count:
            frame_number += fps
            capture.set(cv.CAP_PROP_POS_FRAMES, frame_number)
            success, frame = capture.read() # is it loaded well? (frame)

            current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
            percentage = int(round(current_frame / total_frame_count, 2) * 100)

            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # It have an Error
            width_end, height_end = gray_frame.shape  # 1080, 1920
            width_start = round(266 / 1080 * width_end)  # 266
            height_start = round(289 / 1920 * height_end)  # 289

            frame_resize = gray_frame[width_start: width_end, height_start: height_end]

            # template matching
            res = cv.matchTemplate(frame_resize, temp, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.4)

            if loc[::-1][0].size != 0:  # playing
                is_ingame = True
            else:
                is_ingame = False

            if is_ingame:
                print("[writing] {}/{} - {}%".format(current_frame, total_frame_count, percentage))
                output.write(frame)
            else:
                print("[not writing] {}/{} - {}%".format(current_frame, total_frame_count, percentage))
                continue


    capture.release()
    output.release()
    cv.destroyAllWindows()


def main() -> None:
    start_time = time.time()

    # Full Videos
    cap = cv.VideoCapture("../resources/SPvsAF.mp4")

    # Template Image (minimap)
    template = cv.imread("../resources/minimap_templ.png")
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

    frame_number = 0
    success, frame = cap.read()

    cut_video(cap, template, frame, frame_number)

    print('time:', time.time() - start_time)


if __name__ == '__main__':
    main()
