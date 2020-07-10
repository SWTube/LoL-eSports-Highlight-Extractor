#   File Name: cut_highlights.py
#        Team: standardization
#  Programmer: ssw03270
#  Start Date: 07/08/20
# Last Update: July 10, 2020
#     Purpose: Almost highlight video has 3 game.
#              So we have to cut it to compare with our highlights.
#              This program help to do it.


# 1620, 780 (1920, 1080) : minimap start point in edit video, raw video size
# If you want to see visual working process, erase #(notes) under the code.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def matching(video_capture: np.ndarray, video_path: str, compare_image: np.ndarray) -> None:
    """
        For comparing video's capture and image

        Args:
            video_capture: One frame of video for compare
            video_path: Video's path that user input
            compare_image: Image file for compare

        Returns:
            N/A

        Raises:
            N/A
    """
    checker = []
    while True:
        ret, frame = video_capture.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        width_end, height_end = frame.shape

        width_start = round(780 / 1080 * width_end)
        height_start = round(1620 / 1920 * height_end)

        frame_resize = frame[width_start: width_end, height_start: height_end]

        # Showing video.
        # cv.imshow("VideoFrame", frame)

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % 30 == 0:
            print("start comparing..." + str(video_capture.get(cv.CAP_PROP_POS_FRAMES)))
            checker.append([video_capture.get(cv.CAP_PROP_POS_FRAMES), sift_algorithm(frame_resize, compare_image)])

        # Stopping video.
        # if cv.waitKey(1) > 0:
        #     break

    write_txt(checker)
    video_capture.release()
    cv.destroyAllWindows()

def sift_algorithm(frame_resize: np.ndarray, compare_image: np.ndarray) -> int:
    """
        Using sift algorithm to compare video's capture and image

        Args:
            frame_resize: Resized frame for compare
            compare_image: Image file for compare

        Returns:
            If list name of good has 30 or more values, returns 1. (It means this frame is ingame)
            If not, returns 0. (It means this frame isn't ingame)

        Raises:
            N/A
    """
    sift = cv.xfeatures2d.SIFT_create()

    keypoint_1, descriptor_1 = sift.detectAndCompute(frame_resize, None)
    keypoint_2, descriptor_2 = sift.detectAndCompute(compare_image, None)

    bf = cv.BFMatcher()
    matches = bf.knnMatch(descriptor_1, descriptor_2, 2)

    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    # Showing plt.
    # plt_image = cv.drawMatchesKnn(frame_resize, keypoint_1, compare_image, keypoint_2, good, None, flags=2)
    # plt.imshow(plt_image)
    # plt.show()


    if len(good) > 30:
        print("this frame is ingame.")
        return 1
    else:
        print("this frame isn't ingame.")
        return 0

def write_txt(checker: list) -> None:
    """
        Writing the value that the frame has.

        Args:
            checker: This list has current frame number and that's status.

        Returns:
            N/A

        Raises:
            N/A
    """
    print("start writeing...")
    f = open("checker.txt", "w")
    for data in checker:
        f.writelines(str(data) + "\n")
    f.close()

def make_resource(path: str, type: int) -> np.ndarray:
    """
        Making a resource with path, according to type.

        Args:
            path: File's local path.
            type: File's type, 0 is video file, 1 is image file.

        Returns:
            If type is 0, returns video capture.
            If type is 1, returns image which convert gray.

        Raises:
            N/A
    """
    if type == 0:
        return cv.VideoCapture(path)
    elif type == 1:
        return cv.imread(path, cv.COLOR_BGR2GRAY)

def main() -> None:
    video_path = "C:/Users/ttd85/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/standardization/sample_video/FULL_LCKSpring2020_GRFvsHLE_W9D1_G1.mp4"
    video_capture = make_resource(video_path, 0)

    compare_path = "C:/Users/ttd85/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/standardization/sample_image/minimap.png"
    compare_image = make_resource(compare_path, 1)

    matching(video_capture, video_path, compare_image)

if __name__ == '__main__':
    main()







