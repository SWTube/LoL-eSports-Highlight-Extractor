"""
Name : sw0000j
"""

# from matplotlib import pyplot as plt

import cv2 as cv
# import numpy as np

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
"""

def get_ultimate_coordinate(circle_x : int, circle_y : int) -> None:
    # get image appended ultimate detect circle
    img = cv.imread("test.jpeg")

    img = cv.circle(img, (circle_x, circle_y), 12, (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main() -> None:
    """
    loading and finding champion's ultimate
    """

    get_ultimate_coordinate(1847, 165)


if __name__ == "__main__":
    main()