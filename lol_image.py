"""
This file contains image-related functions.
"""
import PIL
import numpy as np
# Open image using Pillow
from PIL import Image


def image_to_data(path: str) -> np.ndarray:
    """Converts Image to numpy data

    Args:
        path: string parameter that contains the path to the image file.

    Returns:
        If correct path is given, returns the numpy ndarray of the image.
        If given path is wrong, returns an empty numpy ndarray.

    """
    # load the image
    image = Image.open(path)
    # convert image to numpy array
    data = np.asarray(image)
    return data


def main():
    # Print Pillow Version
    print('Pillow Version:', PIL.__version__)
    print(image_to_data('resources/preview.jpeg'))


if __name__ == '__main__':
    main()