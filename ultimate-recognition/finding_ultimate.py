"""
#   File Name: finding_ultimate.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 07/08/20
# Last Update: August 10, 2020
#     Purpose: to find ultimate skill
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
Ultimate Skill's center(x, y) coordinate
radius : 12

# left-side player
# player 1 [x, y] -> [71, 165]
# player 2 [x, y] -> [71, 268]
# player 3 [x, y] -> [71, 371]
# player 4 [x, y] -> [71, 473]
# player 5 [x, y] -> [71, 577]

# right-side player
# player 1 [x, y] -> [1847, 165]
# player 2 [x, y] -> [1847, 268]
# player 3 [x, y] -> [1847, 371]
# player 4 [x, y] -> [1847, 473]
# player 5 [x, y] -> [1847, 577]

Champions icon's coordinate
len : 40

# left-side player
# player 1 [x, y] -> [31, 160]
# player 2 [x, y] -> [31, 263]
# player 3 [x, y] -> [31, 366]
# player 4 [x, y] -> [31, 468]
# player 5 [x, y] -> [31, 572]

# right-side player
# player 1 [x, y] -> [1847, 160]
# player 2 [x, y] -> [1847, 263]
# player 3 [x, y] -> [1847, 366]
# player 4 [x, y] -> [1847, 468]
# player 5 [x, y] -> [1847, 572]
"""


def video_to_list(path: str) -> (list, int):
    """
    Converts a video file to frames and returns a list of them.
    Args:
        path: String value of path to video file.
    Returns:
        If correct path is given, this function will return a list of frames and the number of frames.
        If given path is wrong, returns an empty list.
    Raises:
        None
    """
    assert isinstance(path, str)

    frame_list = []
    frame_count = 0
    frame_rate = 0
    vid = cv.VideoCapture(path)

    # Gets total frame count and the FPS of the video
    frame_count = int(vid.get(cv.CAP_PROP_FRAME_COUNT))
    frame_rate = vid.get(cv.CAP_PROP_FPS)

    # This rules out Drop-frame videos
    # 29.97 fps -> 30 fps
    if not frame_rate.is_integer():
        frame_rate = int(frame_rate + 1)
    elif frame_rate.is_integer():
        frame_rate = int(frame_rate)
    else:
        print("frame_rate is invalid.")
        assert False

    print("video_to_list()")
    for frame_no in range(frame_count):
        ret, frame = vid.read()

        if not ret:
            break

        # Reads every (FPS) frames to increase analysis speed
        if frame_no % frame_rate == 0:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame_list.append(frame)

    vid.release()

    return frame_list, frame_count


def get_image_from_video(image_path : str) -> None:
    """
    make video to one image, just make it, not return
    Args:
        image_path : this is mp4's path
    Returns:
        nothing return
    Raises:
        None
    """
    # get jpeg file use video to image
    video = cv.VideoCapture(image_path)
    success, image = video.read()

    iter = 0

    while(True):
        success, image = video.read()
        iter+=1

        if (iter == 500):
            break
    cv.imwrite("test4.jpeg", image)


def draw_circle_on_ultimate(circle_x : int, circle_y : int) -> None:
    """
    Draw circle on ultimate skill to get ultimate skill's coordinate

    Args:
        circle_x: x-coordinate of the center of the circle
        circle_y: y-coordinate of the center of the circle

    Returns:
        Just draw circle on ultimate skill

    Raises:
        None
    """
    # test function(to detect icon)
    img = cv.imread("test.jpeg")

    img = cv.circle(img, (circle_x, circle_y), 12, (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_rectangle_on_champion(rectangle_x : int, rectangle_y : int) -> None:
    """
    Draw rectangle on champion to get champions icon's coordinate

    Args:
        rectangle_x: x-coordinate of the center of the circle
        rectangle_y: y-coordinate of the center of the circle

    Returns:
        Draw rectangle on champions icon

    Raises:
        None
    """
    # test function(to detect icon)
    img = cv.imread("test.jpeg")

    img = cv.rectangle(img, (rectangle_x, rectangle_y), (rectangle_x + 40, rectangle_y + 40), (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def compare_champion_icon_with_champion_icon_data(champion_image_path : str, test_image_path : str,
                                                  champion_icon_file_list : list) -> list:
    """
        Compare two images(champion icon & champion icon data) using 'SIFT' similarity
        match_list mean how similar images they are

        Args:
            champion_image_path : champion image path
            test_image_path : test image path

        Returns:
            best matched list

        Raises:
            None
    """
    champions_icon_coordinate = [
        [160, 31],
        [263, 31],
        [366, 31],
        [468, 31],
        [572, 31],
        [160, 1847],
        [263, 1847],
        [366, 1847],
        [468, 1847],
        [572, 1847],
    ]
    best_matched_index = []

    # append list best matched champion icon
    for y_coordinate, x_coordinate in champions_icon_coordinate:
        matched_list = []

        for index in range(len(champion_icon_file_list)):

            img1 = cv.imread(champion_image_path + champion_icon_file_list[index])
            img2 = cv.imread(test_image_path)
            src = img2[y_coordinate:y_coordinate+40, x_coordinate:x_coordinate+40]

            # use sift algorithm
            sift = cv.xfeatures2d.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(src, None)
            bf = cv.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)

            match_list = []

            # choose matched over 0.5 * distance
            for m, n in matches:
                if m.distance < 0.5 * n.distance:
                    match_list.append([m])
            matched_list.append(len(match_list))
            print('{} done'.format(index))

        best_matched_index.append(matched_list.index(max(matched_list)))

    return best_matched_index
    # img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
    # plt.imshow(img3), plt.show()


def get_champion_name() -> None:
    champion_icon_data = []
    champion_name = []

    in_game_champion_icon = []
    in_game_ultimate_skills = []

    champion_icon_files = []

    champion_image_path = "../resources/champions_image/"
    test_video = "test4.mp4"
    get_image_from_video(test_video)
    test_image = "test4.jpeg"

    # Load champion's name list & append name to list
    champion_list = open("../resources/champion_list.txt", 'r')
    lines = champion_list.readlines()
    for line in lines:
        champion_icon_files.append(line[:-1])
    champion_list.close()

    # Load champion icon images
    for index in range(len(champion_icon_files)):
        champion_icon = cv.imread(champion_image_path + champion_icon_files[index])
        champion_icon_data.append(champion_icon)

        champion_icon_data[index] = cv.cvtColor(champion_icon_data[index], cv.COLOR_BGR2RGB)

    # Resize champion icon images(40 x 40)
    for index in range(len(champion_icon_data)):
        champion_icon_data[index] = cv.resize(champion_icon_data[index], (40, 40))

    # Get best match index list
    in_game_champion_icon = compare_champion_icon_with_champion_icon_data(champion_image_path,
                                                                   test_image, champion_icon_files)

    # Get champion name using champion index
    for champion_index in in_game_champion_icon:
        champion_name.append(champion_icon_files[champion_index][:-4])
    for index in range(len(champion_name)):
        print(champion_name[index])

    return champion_name


def main():
    print("finding_ultimate.py")


if __name__ == "__main__":
    main()