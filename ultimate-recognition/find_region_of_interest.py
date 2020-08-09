import cv2 as cv
import numpy as np

path = "raw3.mp4"


def convert_window_freestyle(name: str) -> None:
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    return None


def call_frame(path: str,frame_number: int) -> np.ndarray:
    cap = cv.VideoCapture(path)
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if not ret:
        print("error")
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return frame


def call_frame_test(path,frame_number):
    cap = cv.VideoCapture(path)
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if not ret:
        print("error")
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    convert_window_freestyle("frame")
    cv.imshow('frame', frame)
    key = cv.waitKey(0)
    if key == 27:
        cap.release()
    cv.destroyAllWindows()
    return frame


def cut_image(image):
    left1 = image[155:175, 65:80]
    left2 = image[265:275, 65:80]
    left3 = image[365:375, 65:80]
    left4 = image[470:480, 65:80]
    left5 = image[570:590, 65:80]

    right1 = image[155:175, 1840:1855]
    right2 = image[260:280, 1840:1855]
    right3 = image[365:375, 1840:1855]
    right4 = image[465:485, 1840:1855]
    right5 = image[570:580, 1840:1855]
    result = [left1, left2, left3, left4, left5, right1, right2, right3, right4, right5]
    return result


def cut_image_test(image):
    left1 = image[155:175, 65:80]
    left2 = image[265:275, 65:80]
    left3 = image[365:375, 65:80]
    left4 = image[470:480, 65:80]
    left5 = image[570:590, 65:80]

    right1 = image[155:175, 1840:1855]
    right2 = image[260:280, 1840:1855]
    right3 = image[365:375, 1840:1855]
    right4 = image[465:485, 1840:1855]
    right5 = image[570:580, 1840:1855]
    result = [left1, left2, left3, left4, left5, right1, right2, right3, right4, right5]
    for index in range(len(result) - 1):
        convert_window_freestyle(f"image{index}")
        cv.imshow(f"image{index}", result[index])
    cv.waitKey()
    cv.destroyAllWindows()
    return result

if __name__ == '__main__':
    first_frame = call_frame_test(path,14000)
    cut_image_test(first_frame)
