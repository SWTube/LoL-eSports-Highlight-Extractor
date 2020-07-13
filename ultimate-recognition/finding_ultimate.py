"""
#   File Name: finding_ultimate.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 07/08/20
# Last Update: July 13, 2020
#     Purpose: to find ultimate skill's coordinate
"""

import cv2 as cv
import numpy as np

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
    img = cv.imread("test.jpeg")

    img = cv.circle(img, (circle_x, circle_y), 12, (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main() -> None:

    draw_circle_on_ultimate(1847, 165)


if __name__ == "__main__":
    main()