from typing import TypeVar

from matplotlib import pyplot as plt

import cv2 as cv
import numpy as np
import random

def draw_bounding_box(image: np.ndarray, contours: list, contours_poly: list, bound_rect: list, max_bound_rect_index: int) -> np.ndarray:
    """
    :param image:
    :param contours:
    :param contours_poly:
    :param bound_rect:
    :param max_bound_rect_index:
    :return: image with bounding box drawn on it
    """
    assert (isinstance(image, np.ndarray))
    assert (type(contours) == list)
    assert (type(contours_poly) == list)
    assert (type(bound_rect) == list)
    assert (type(max_bound_rect_index) == int)

    drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    # if (0 <= max_bound_rect_index < len(bound_rect)):
    #     color = (128, 128, 0)
    #     cv.drawContours(drawing, contours_poly, max_bound_rect_index, color)
    #     cv.rectangle(image, (int(bound_rect[max_bound_rect_index][0]), int(bound_rect[max_bound_rect_index][1])), \
    #                  (int(bound_rect[max_bound_rect_index][0] + bound_rect[max_bound_rect_index][2]), int(bound_rect[max_bound_rect_index][1] + bound_rect[max_bound_rect_index][3])), color, 2)

    for i in range(len(contours)):
        if (i is not max_bound_rect_index):
            color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        else:
            color = (255, 255, 255)
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(image, (int(bound_rect[i][0]), int(bound_rect[i][1])), \
                     (int(bound_rect[i][0] + bound_rect[i][2]), int(bound_rect[i][1] + bound_rect[i][3])), color, 2)

    return image

def draw_results(list_of_images: list, name_of_images: list, length: int, width: int) -> None:
    """
    :param list_of_images:
    :param name_of_images:
    :param length:
    :param width:
    plots all the images in list_of_images
    """
    assert (type(list_of_images) == list)
    assert (type(name_of_images) == list)
    assert (str(length).isnumeric())
    assert (str(width).isnumeric())
    for i in range(len(list_of_images)):
        plt.subplot(length, width, i + 1), plt.imshow(list_of_images[i], cmap='gray')
        plt.title(name_of_images[i]), plt.xticks([]), plt.yticks([])

    plt.show()

def get_bounding_box(image: np.ndarray) -> TypeVar(list, list, list, int):
    """
    :param image:
    :return: list0, list1, list2
    list0 is the contours,
    list1 is the contours poly,
    list2 is the bounding rectangle
    """
    assert (isinstance(image, np.ndarray))

    im2, contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_poly = [None] * len(contours)
    bound_rect = [None] * len(contours)
    max_bounding_rect = 0
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        bound_rect[i] = cv.boundingRect(contours_poly[i])
        if (get_size(bound_rect[i]) > get_size(bound_rect[max_bounding_rect])):
            max_bounding_rect = i

    return contours, contours_poly, bound_rect, max_bounding_rect;

def get_size(rectangle: tuple) -> int:
    assert (type(rectangle) == tuple)
    assert (len(rectangle) == 4)

    return abs(rectangle[0] - rectangle[2]) * abs(rectangle[1] - rectangle[3])

def sobel_detect_uint8(image: np.ndarray) -> np.ndarray:
    """
    :param image:
    :return: image with sobel detection done, and type converted to uint8
    """
    assert (isinstance(image, np.ndarray))

    sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)
    sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=5)
    # set type from float64 to uint8
    sobel = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sobel = (sobel * 255 / sobel.max()).astype(np.uint8)

    return sobel

def main() -> None:
    """
    loads an image and draws a bounding box on it
    """
    images = []
    names = []

    # init
    cv.setUseOptimized(True)
    # start_time = cv.getTickCount()

    cap = cv.VideoCapture("../resources/match_screenshots/2020_summer_drx_dyn.mp4")
    fourcc = cv.VideoWriter_fourcc(*'XIVD')
    out = cv.VideoWriter("output.avi", fourcc, 20.0, (1918, 1080))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Skipped frame")
            break

        frame = bounding_boxer(frame)
        out.write(frame)
        cv.imshow("image", frame)
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()
    # Display Performance Cost
    # end_time = cv.getTickCount()
    # print("Performance:", (end_time - start_time) * 1000 / cv.getTickFrequency(), "ms")

    # Display Results
    # draw_results(images, names, 3, 3)

def bounding_boxer(image: np.ndarray) -> np.ndarray:
    # crop image
    image = image[100:200, 640:1280]

    # images.append(image)
    # names.append("Original Image")

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # remove noise
    blurred_image = cv.bilateralFilter(gray_image, 9, 75, 75)

    # sobel edge detection
    sobel = sobel_detect_uint8(blurred_image)
    # images.append(sobel)
    # names.append("Sobel Edge Detection")

    # binarization
    sobel = cv.GaussianBlur(sobel, (5, 5), 0)
    ret, sobel_binarized = cv.threshold(sobel, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Erosion and Dilation
    # Create structure element for extracting horizontal lines through morphology operations
    horizontal_structure = cv.getStructuringElement(cv.MORPH_RECT, (100, 1))
    # Apply morphology operations
    kernel = np.ones((5, 5), np.uint8)
    horizontal_sobel = cv.morphologyEx(cv.dilate(sobel_binarized, kernel, iterations=4), cv.MORPH_OPEN,
                                       horizontal_structure)
    # images.append(horizontal_sobel)
    # names.append("Horizontal Dilation")

    # bounding box
    contours_sobel, contours_poly_sobel, bound_rect_sobel, max_bound_rect_index_sobel = get_bounding_box(horizontal_sobel)
    image_sobel = draw_bounding_box(image, contours_sobel, contours_poly_sobel, bound_rect_sobel, max_bound_rect_index_sobel)
    # images.append(image_sobel)
    # names.append("Bounding Box")

    return image_sobel

if __name__ == "__main__":
    main()