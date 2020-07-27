"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
# Last Update: July 26, 2020
#     Purpose: To determine the game is (Playing) or (not Playing) through "Template Matching" of minimap and actual game video.
"""

import cv2 as cv
import numpy as np


def main():
    # variable assignment

    # HighLights
    # cap = cv.VideoCapture("D:\Image\HightLighs_LCKSpring2020_T1vsGenG.mp4")

    # Full Videos
    cap = cv.VideoCapture("D:\Image\KTvsDragon_last_edited.mp4")

    # Template Image (minimap)
    template = cv.imread("D:\Image\minimap_templ.png", cv.IMREAD_GRAYSCALE)
    width, height = template.shape[::-1]  # width and height of minimap
    print(width, height)

    # fps, codec, output
    fps = cap.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output = cv.VideoWriter("D:\Image\output\output" + ".mp4", fourcc, fps, (1920, 1080), 1)

    # Playing Video, writing output
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # template matching
        res = cv.matchTemplate(gray_frame, template, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.4)

        if loc[::-1][0].size == 0:  # isn't playing
            print('Not Playing')
        else:  # playing
            print('Playing')
            output.write(frame)

        cv.imshow('Frame', frame)

        key = cv.waitKey(1)

        if key == 27:  # If User puts 'ESC' button, video is closed.
            break

    cap.release()
    output.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
