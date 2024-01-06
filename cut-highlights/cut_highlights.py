#   File Name: cut_highlights.py
#        Team: standardization
#  Programmer: ssw03270
#  Start Date: 07/08/20
# Last Update: August 2, 2020
#     Purpose: Almost highlight video has 3 game.
#              So we have to cut it to compare with our highlights.
#              This program help to do it.

# 1620, 780 (1920, 1080) : minimap start point in edit video, raw video size
# If you want to see visual working process, erase #(notes) under the code.

import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt


def matching(video_file: str, video_capture: np.ndarray, video_path: str, compare_image: np.ndarray) -> None:
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
    is_writing = False
    game_set = ["_GAME1", "_GAME2", "_GAME3", "_GAME4", "_GAME5"]
    game_num = -1

    width = int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    fps = video_capture.get(cv.CAP_PROP_FPS)

    sift_ans = False
    while True:
        if not sift_ans:
            is_writing = False

        else:
            if not is_writing:
                is_writing = True
                game_num += 1
                out = cv.VideoWriter(video_file + game_set[game_num] + ".mp4", fourcc, fps, (width, height), 1)

            out.write(frame_color)
            # cv.imshow("EditedFrame", frame_color)

        ret, frame_color = video_capture.read()
        if not ret:
            break
        frame_gray = cv.cvtColor(frame_color, cv.COLOR_BGR2GRAY)
        width_end, height_end = frame_gray.shape

        width_start = round(780 / 1080 * width_end)
        height_start = round(1620 / 1920 * height_end)

        frame_resize = frame_gray[width_start: width_end, height_start: height_end]

        # Showing video.
        # cv.imshow("VideoFrame", frame_gray)

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % fps == 0:
            print("start comparing..." + str(video_capture.get(cv.CAP_PROP_POS_FRAMES)))
            sift_ans = sift_algorithm(frame_resize, compare_image)
            checker.append([video_capture.get(cv.CAP_PROP_POS_FRAMES), sift_ans])

        # Stopping video.
        # if cv.waitKey(1) > 0:
        #     break

    # write_txt(checker)
    out.release()
    video_capture.release()
    cv.destroyAllWindows()


def sift_algorithm(frame_resize: np.ndarray, compare_image: np.ndarray) -> bool:
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

    if len(good) > 15:
        print("this frame is ingame.")
        return True
    else:
        print("this frame isn't ingame.")
        return False


def write_txt(checker: list) -> None:
    """
        Writing the value that the frame has.
        Now, it wasn't needed - 2020/08/02

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
    image_path = "../resources/standardization/sample_image"
    video_path = "../resources/standardization/sample_video"

    video_list = os.listdir(video_path)
    for video_file in video_list:
        new_video_path = video_path + "/" + video_file
        video_capture = make_resource(new_video_path, 0)

        minimap_file = image_path + "/minimap.png"
        minimap_image = make_resource(minimap_file, 1)

        matching(video_file[0:len(video_file) - 4], video_capture, video_path, minimap_image)


if __name__ == '__main__':
    main()
