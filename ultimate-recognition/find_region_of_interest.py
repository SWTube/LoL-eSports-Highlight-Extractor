import cv2 as cv
import numpy as np
"""
Name : luckydipper
team : Visual Recognition
created : 2020.7.8 
purpose : Find ultimate region.
"""

def convert_window_freestyle(name: str) -> None:
    """change window freestyle. ex) cv.imshow window -> mutable
    param: window's name.

    return : None

    raise : change window style
    """
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    return None


def extract_coordinate(gray_frame_list:np.ndarray)->np.ndarray:
    """
    in gray_frame_list,which import from video_to_list.py
    extract each single_gray_frame and replace only coordinate of ultimate skill frame data.

    ex) one frame is one data, among this, extract only ultimate coordinate
    pa = [[[1,2,3],
         [1,2,3]],

         [[2,3,4],
         [2,3,4]]]


    param:
        gray_frame_list: consisted of a lot of single_gray_frame list.

    return:
        coordinate of ultimate : new ndarray list, resize each gray_frame_list to ultimate coordinate

    raise: None
    """

def each_frame_to_score(gray_frame_list)->np.ndarray:
    """
    match each frame to each score ,one to one.
    param:
        gray_frame_list :
    return:
    raise
    """


def test():
    capture = cv.VideoCapture("ultimate_except.mp4")  # read the video file
    while True:
        check = capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(
            cv.CAP_PROP_FRAME_COUNT)  # current frame == all frame
        if check:
            capture.open("ultimate_use.mp4")
        ret, frame = capture.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        for k in range(5):
            cv.namedWindow(f'left{k + 1}', cv.WINDOW_NORMAL)
            cv.namedWindow(f'right{k + 1}', cv.WINDOW_NORMAL)

        cv.imshow("left1", frame[155:175, 65:80])
        cv.imshow("left2", frame[260:275, 65:80])
        cv.imshow("left3", frame[365:375, 65:80])
        cv.imshow("left4", frame[465:480, 65:80])
        cv.imshow("left5", frame[570:585, 65:80])

        cv.imshow("right1", frame[155:175, 1840:1855])
        cv.imshow("right2", frame[260:275, 1840:1855])
        cv.imshow("right3", frame[365:375, 1840:1855])
        cv.imshow("right4", frame[465:480, 1840:1855])
        cv.imshow("right5", frame[570:585, 1840:1855])
        key = cv.waitKey(1)  # analyze 33ms frame
        if key == 27:  # Esc key to stop
            break
    cv.destroyAllWindows()

def main():
    test()

if __name__ == '__main__':
    main()