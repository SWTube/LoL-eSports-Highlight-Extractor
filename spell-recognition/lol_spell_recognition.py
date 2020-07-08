"""
This file will analyse the summoner spells availability.
"""
import cv2 as cv
import numpy as np

"""
All spells are assumed to be 20x20 pixels

# Left-Side
No1 Summoner D Spells Coordinates [158, 5] -> [177, 24]
No1 Summoner F Spells Coordinates [181, 5] -> [200, 24]

No2 Summoner D Spells Coordinates [261, 5] -> [280, 24]
No2 Summoner F Spells Coordinates [284, 5] -> [303, 24]

No3 Summoner D Spells Coordinates [364, 5] -> [383, 24]
No3 Summoner F Spells Coordinates [387, 5] -> [406, 24]

No4 Summoner D Spells Coordinates [466, 5] -> [485, 24]
No4 Summoner F Spells Coordinates [489, 5] -> [508, 24]

No5 Summoner D Spells Coordinates [570, 5] -> [589, 24]
No5 Summoner F Spells Coordinates [593, 5] -> [612, 24]

# Right-Side
No1 Summoner D Spells Coordinates [158, 1894] -> [177, 1913]
No1 Summoner F Spells Coordinates [181, 1894] -> [200, 1913]

No2 Summoner D Spells Coordinates [261, 1894] -> [280, 1913]
No2 Summoner F Spells Coordinates [284, 1894] -> [303, 1913]

No3 Summoner D Spells Coordinates [364, 1894] -> [383, 1913]
No3 Summoner F Spells Coordinates [387, 1894] -> [406, 1913]

No4 Summoner D Spells Coordinates [466, 1894] -> [485, 1913]
No4 Summoner F Spells Coordinates [489, 1894] -> [508, 1913]

No5 Summoner D Spells Coordinates [570, 1894] -> [589, 1913]
No5 Summoner F Spells Coordinates [593, 1894] -> [612, 1913]
"""


def resize_image(img: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Resizes the image to a size given in the parameters.

    Args:
        img: Numpy array data of an image to be resized.
        width: Target width value of the converted data.
        height: Target height value of the converted data.

    Returns:
        If correct path is given, returns the numpy ndarray of the resized image.
        If given path is wrong, returns an empty numpy ndarray.

    Raises:
        AssertionError: An error occured from reading parameters. Incorrect type of data given as parameters.
    """
    # Check if data types of arguments are correct.
    assert isinstance(img, np.ndarray)
    assert isinstance(width, int)
    assert isinstance(height, int)

    


def video_to_list(path: str) -> list:
    """
    Converts a video file to frames and returns a list of them.

    Args:
        path: String value of path to video file.

    Returns:
        If correct path is given, this function will convert the video file to a list of frames.
        If given path is wrong, returns an empty list.

    Raises:
        N/A
    """
    frame_list = []
    vid = cv2.VideoCapture('')

    while(vid.isOpened()):
        ret, frame = vid.read()

        if ret == False:
            break
        frame_list.append(frame)

    vid.release()
    # vid.destroyAllWindows()

    return frame_list


def main():
    frames = []



if __name__ == '__main__':
    main()
