# File Name: searching_left_banner
#      Team: standardization
# Programmer: wpdudH
# Start Date: 07/15/20
#Last Update: August 9, 2020
#    Purpose: Raw video consists of in-game videos and replay videos.
#             So we need to distinguish between in-game videos and replay videos.
#             This program carries out that work.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

def check_algorithm(frame_resize: np.ndarray, compare_image: np.ndarray) -> int:
    """
        Comparing video's capture to replay banner image to use sift algorithm
        Args:
            frame_resize: Resized frame for compare
            compare_image: Image file for comparison
        Returns:
            If list name of good has more than 30 values, return 1 (It means this frame is replay)
            If not, returns 0 (It means this frame is in-game)
        Raises:
            N/A
    """
    sift = cv.xfeatures2d.SIFT_create()

    frame_resize = cv.cvtColor(frame_resize, cv.COLOR_BGR2GRAY)

    keypoint_1, descriptor_1 = sift.detectAndCompute(frame_resize, None)
    keypoint_2, descriptor_2 = sift.detectAndCompute(compare_image, None)

    bf = cv.BFMatcher()
    matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    plt_image = cv.drawMatchesKnn(frame_resize, keypoint_1, compare_image, keypoint_2, good, None, flags=2)
    plt.imshow(plt_image)
    plt.show()

    if len(good) > 30:
        return 1
    else:
        return 0

def checklist_writer(compare_result:list) -> None:
    """
        Write check file consisting of results comparing video's capture to replay banner image
        Args:
            compare_result: list of result of compare
        Returns:
            None
        Raises:
            N/A
    """
    classified = []
    for i in range(len(compare_result)):
        classified.append("[{}, {}]".format(i * 30, compare_result[i]))
    # Store the video's play time and result of check_algorithm in the list named classified

    with open("checker.txt", 'w') as file:
        for i in range(len(classified)):
            text = classified[i]
            file.writelines(text+'\n')
    # Write csv file consisting of values of list named classified

def frame_resize(frame: np.ndarray) -> np.ndarray:
    """
        Resize frame to be compared
        Args:
            frame: Frame of video
        Returns:
            frame_resize: Resized frame
        Raises:
            N/A
    """
    height, width, channel = frame.shape

    start_height = round(45 / 1080 * height)
    end_width = round(254 / 1920 * width)
    end_height = round(122 / 1080 * height)
    # upper_left_banner start point : (0,45)
    # upper_left_banner end point : (254,122)

    frame_resize = frame[start_height:end_height, 0:end_width]
    # resizing frame to reduce the computation

    return frame_resize

def store_video(video_name:str, video_path:str, compare_image: np.ndarray ) -> None:
    """
        Storing in-game video
        Args:
             video_path:Video's path to be stored
             compare_image: Image comparing with frame
             video_name: File name of video
        Returns:
            None
        Raises:
            N/A
    """
    compare_result = []
    video_capture = cv.VideoCapture(video_path)

    fps = video_capture.get(cv.CAP_PROP_FPS)
    width = video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output_video = cv.VideoWriter(video_name+".mp4", fourcc, fps, (int(width), int(height)))

    check = False
    # If check is True, start storing frame
    # If check is False, stop storing frame

    print("here")

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("There is no frame.Check the video file")
            break

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % int(fps) == 0: # Check frame every second
            if check_algorithm(frame_resize(frame), compare_image) == 1:
                compare_result.append('1')
                check = False
                print("replay")
            else:
                compare_result.append('0')
                check = True
                print("ingame")

        if check == True:
            output_video.write(frame)
            cv.imshow("output", frame)

            if cv.waitKey(1) > 0: break

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) == video_capture.get(cv.CAP_PROP_FRAME_COUNT):
            break

    video_capture.release()
    cv.destroyAllWindows()

    checklist_writer(compare_result)

def resource(path:str) -> np.ndarray:
    """
        Changing the type of picture file with path

        Args:
            path: File's local path

        Returns:
            black-and-white image

        Raises:
            N/A
    """
    return cv.imread(path,cv.IMREAD_GRAYSCALE)


def main() -> None:
    image_path = "C:/Users/82102/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/replay_banner.png"
    replay_banner = resource(image_path)

    video_path = "./resources/standardization/sample_video"
    video_list = os.listdir(video_path)

    for video_file in video_list:
        new_video_path = video_path + "/" + video_file
        store_video(video_file[0:len(video_file) - 4], new_video_path, replay_banner)


if __name__ == '__main__':
    main()