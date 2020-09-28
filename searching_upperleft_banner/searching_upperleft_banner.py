"""
# File Name: searching_left_banner
#      Team: standardization
# Programmer: wpdudH
# Start Date: 07/15/20
#Last Update: September 28, 2020
#    Purpose: Raw video consists of in-game videos and replay videos.
#             So we need to distinguish between in-game videos and replay videos.
#             This program carries out that work.
"""

import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt

def check_algorithm(frame_resize: np.ndarray, compare_image: np.ndarray) -> bool:
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

    # frame_resize = cv.cvtColor(frame_resize, cv.COLOR_BGR2GRAY)

    keypoint_1, descriptor_1 = sift.detectAndCompute(frame_resize, None)
    keypoint_2, descriptor_2 = sift.detectAndCompute(compare_image, None)

    bf = cv.BFMatcher()
    matches = bf.knnMatch(descriptor_1, descriptor_2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    # plt_image = cv.drawMatchesKnn(frame_resize, keypoint_1, compare_image, keypoint_2, good, None, flags=2)
    # plt.imshow(plt_image)
    # plt.show()

    if len(good) > 30:
        return False
    else:
        return True

'''
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
'''

def frame_resize(frame: np.ndarray, image: int) -> np.ndarray:
    """
        Resize frame to be compared
        Args:
            frame: Frame of video
            image: Determinist of frame resize value
                   If image value is 0, frame will be resized to the same size as the replay banner
                   If image value is 1, frame will be resized to the same size as the highlight banner
                   If image value is 2, frame will be resized to the same size as the pro view banner
        Returns:
            frame_resize: Resized frame
        Raises:
            N/A
    """
    height, width = frame.shape

    if image == 0:
        start_height = round(45 / 1080 * height)
        start_width = 0
        end_width = round(254 / 1920 * width)
        end_height = round(122 / 1080 * height)
        # replay_banner start point : (0,45)
        # replay_banner end point : (254,122)
    elif image == 1:
        start_height = round(45 / 1080 * height)
        start_width = 0
        end_width = round(339 / 1920 * width)
        end_height = round(122 / 1080 * height)
        # highlight_banner start point : (0,45)
        # highlight_banner end point : (339,122)
    else:
        start_height = round(45 / 1080 * height)
        start_width = round(1592 / 1920 * width)
        end_width = 1920
        end_height = round(122 / 1080 * height)
        # pro_view_banner start point : (1592,45)
        # pro_view_banner end point : (1920,122)

    frame_resize = frame[start_height:end_height, start_width:end_width]
    # resizing frame to reduce the computation

    return frame_resize

'''
def store_video(video_name:str, video_path:str, compare_images: list ) -> None:
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
    # compare_result = []
    video_capture = cv.VideoCapture(video_path)

    total_frames = video_capture.get(cv.CAP_PROP_FRAME_COUNT)
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


        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % int(fps) == 0:
            if check_algorithm(frame_resize(frame, 0), compare_images[0]) == 1 or check_algorithm(frame_resize(frame, 2), compare_images[2]) == 1:
                # compare frame with replay_banner and pro view banner
                # compare_result.append('1')
                check = False
                print("replay")
            else:
                if video_capture.get(cv.CAP_PROP_POS_FRAMES) > total_frames - (240 * fps):
                    if check_algorithm(frame_resize(frame, 1), compare_images[1]) == 1 or check_algorithm(frame_resize(frame, 2), compare_images[2]) == 1:
                        # compare frame with highlight_banner and pro view banner
                        break
                # compare_result.append('0')
                check = True
                print("ingame")

        if check == True:
            output_video.write(frame)
            # cv.imshow("output", frame)

            # if cv.waitKey(1) > 0: break

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) == video_capture.get(cv.CAP_PROP_FRAME_COUNT):
            break

    video_capture.release()
    cv.destroyAllWindows()

    # checklist_writer(compare_result)
    '''

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
    return cv.imread(path, cv.IMREAD_GRAYSCALE)

"""
def main() -> None:
    replay_banner_path = "C:/Users/82102/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/replay_banner.png"
    replay_banner = resource(replay_banner_path)
    highlight_banner_path = "C:/Users/82102/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/highlight.png"
    highlight_banner = resource(highlight_banner_path)
    pro_view_banner_path = "C:/Users/82102/PycharmProjects/LoL-eSports-Highlight-Extractor/resources/pro view.png"
    pro_view_banner = resource(pro_view_banner_path)


    compare_images = []
    compare_images.append(replay_banner)
    compare_images.append(highlight_banner)
    compare_images.append(pro_view_banner)

    video_path = "./resources/standardization/sample_video"
    video_list = os.listdir(video_path)

    for video_file in video_list:
        new_video_path = video_path + "/" + video_file
        store_video(video_file[0:len(video_file) - 4], new_video_path, compare_images)

if __name__ == '__main__':
    main()
    """