# File Name: searching_left_banner
#      Team: standardization
# Programmer: wpdudH
# Start Date: 07/15/20
#Last Update: July 27, 2020
#    Purpose: Raw video consists of in-game videos and replay videos.
#             So we need to distinguish between in-game videos and replay videos.
#             This program carries out that work.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


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

def checklist_writer(compare_result:list) -> list:
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

def provider(video_path: str) -> np.ndarray:
    """
        Extracting video's capture for comparison
        Args:
            video_path: Path of video to extract
        Returns:
            frame_list: list consisting of video's frames
        Raises:
            N/A
    """
    frame_list = []
    video_capture = cv.VideoCapture(video_path)

    fps = video_capture.get(cv.CAP_PROP_FPS)
    width = video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)

    start_height = round(45 / 1080 * height)
    end_width = round(254 / 1920 * width)
    end_height = round(122 / 1080 * height)
    # upper_left_banner start point : (0,45)
    # upper_left_banner end point : (254,122)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("Error")
            break

        frame_resize = frame[start_height:end_height, 0:end_width]
        # resizing frame to reduce the computation

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % fps == 0:
            frame_list.append(frame_resize)
        # Save resized frame to frame_list every second

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) == video_capture.get(cv.CAP_PROP_FRAME_COUNT):
            break
        # Finish loop

    video_capture.release()
    cv.destroyAllWindows()

    return frame_list

def get_result(frame_list: list, compare_image: np.ndarray) -> list:
    """
        Making a list consisting of results of check_algorithm
        Args:
            frame_list: list consisting of video's frames
            compare_image: Image file for comparison
        Returns:
            compare_list: list consisting of results of check_algorithm
        Raises:
            N/A
    """
    compare_result = []

    for i in range(len(frame_list)):
        compare_result.append(check_algorithm(frame_list[i], compare_image))
    # Save results of check_algorithm in compare_result

    return compare_result

def store_video(video_name:str, video_path:str, compare_result:list) -> None:
    """
        Storing in-game video
        Args:
             video_path:Video's path to be stored
             compare_result: Results of check_algorithm
             video_name: File name of video
        Returns:
            None
        Raises:
            N/A
    """
    video_capture = cv.VideoCapture(video_path)

    fps = video_capture.get(cv.CAP_PROP_FPS)
    width = video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output_video = cv.VideoWriter(video_name+".mp4", fourcc, fps, (int(width), int(height)))

    play_time = 0
    # To determine whether this frame is replay or not
    check = False
    # If check is True, start storing frame
    # If check is False, stop storing frame

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("There is no frame.Check the video file")
            break

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % fps == 0: # Check frame every second
            if compare_result[play_time] == 1:
                check = False
                play_time = play_time + 1
            else:
                check = True
                play_time = play_time + 1

        if check == True:
            output_video.write(frame)

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) == video_capture.get(cv.CAP_PROP_FRAME_COUNT):
            break

    video_capture.release()
    cv.destroyAllWindows()

def main() -> None:
    replay_banner = cv.imread("C:/Users/82102/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/replay_banner.png", cv.IMREAD_GRAYSCALE)
    video_path = "C:/Users/82102/Downloads/video/FULL_LCKSpring2020_APKvsAF_W7D2_G1.mp4"

    frame_list = provider(video_path)
    compare_list = get_result(frame_list, replay_banner)

    checklist_writer(compare_list)
    store_video("FULL_LCKSpring2020_APKvsAF_W7D2_G1", video_path, compare_list)


if __name__ == '__main__':
    main()