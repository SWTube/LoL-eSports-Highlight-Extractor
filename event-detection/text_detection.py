from typing import Union
import cv2 as cv
import easyocr
import numpy as np
import ocr_text
import random

"""
TODO: cv VideoCapture has fps feature/attribute... check it when you want to.... hahahahaha
"""

KILL_EVENTS = [
    "선취점!",
    "처치했습니다!",
    "더블 킬!",
    "트리플 킬!",
    "쿼드라 킬!",
    "헥사킬!",
    "학살 중입니다!",
    "미쳐 날뛰고 있습니다!",
    "도저히 막을 수 없습니다!",
    "전장의 지배자!",
    "전장의 화신!",
    "전설의 출현!",
    "제압되었습니다!",
    "마지막 적 처치!",
    "연속 킬 차단!"
]

OBJECT_EVENTS = [
    "빨강 팀이 드래곤을 처치했습니다!",
    "파랑 팀이 드래곤을 처치했습니다!",
    "빨강 팀이 협곡의 전령을 소환했습니다!",
    "파랑 팀이 협곡의 전령을 소환했습니다!",
    "빨강 팀이 내셔 남작을 처치했습니다!",
    "파랑 팀이 내셔 남작을 처치했습니다!",
    "빨강 팀이 내셔 남작을 빼앗았습니다!",
    "파랑 팀이 내셔 남작을 빼앗았습니다!"
]

TOWER_EVENTS = [
    "빨강 팀의 포탑이 파괴되었습니다!",
    "파랑 팀 포탑이 파괴되었습니다!",
    "빨강 팀 억제기를 파괴했습니다!",
    "파랑 팀 억제기를 파괴했습니다!",
]

GAME_EVENTS = [
    "소환사의 협곡에 오신 것을 환영합니다",
    "미니언 생성까지 30초 남았습니다",
    "미니언이 생성되었습니다"
]


def draw_bounding_box(image: np.ndarray, bound_rect: list) -> np.ndarray:
    """
    :param image:
    :param contours:
    :param contours_poly:
    :param bound_rect:
    :param max_bound_rect_index:
    :return: image with bounding box drawn on it
    """
    assert (isinstance(image, np.ndarray))
    assert (type(bound_rect) == list)

    for i in bound_rect:
        color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        cv.rectangle(image, (int(i[0][0]), int(i[0][1])), (int(i[2][0]), int(i[2][1])), color, 2)

    return image


def get_events_from_frame(reader: easyocr.Reader, frame: np.ndarray) -> list:
    result = reader.readtext(frame)

    ocr_results_per_frame = []

    # check if text is bigger than ~
    for element in result:
        event_type = None
        if element[0][-1][1] - element[0][0][1] >= 40:
            for event in OBJECT_EVENTS:
                if event_type is None and event in element[1]:
                    event_type = "OBJECT"
                    break
            for event in TOWER_EVENTS:
                if event_type is None and event in element[1]:
                    event_type = "TOWER"
                    break
            for event in KILL_EVENTS:
                if event_type is None and event in element[1]:
                    event_type = "KILL"
                    break
            for event in GAME_EVENTS:
                if event_type is None and event in element[1]:
                    event_type = "GAME"
                    break
            if event_type is not None:
                ocr_results_per_frame.append(ocr_text.Text(element, event_type))

    return ocr_results_per_frame


def get_events_from_video(reader: easyocr.Reader, cap: cv.VideoCapture, accuracy: int = 30)\
        -> Union[cv.VideoCapture, list]:
    count = 0
    timer = -1
    log = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Skipped frame")
            break

        # if frame_crop is not None:
        #     frame = frame[frame_crop[0][1]:frame_crop[2][1], :]
        frame = frame[int(frame.shape[0] / 4.954129 + 0.5):int(frame.shape[0] / 4.014870 + 0.5)
        , int(frame.shape[1] / 3.157895 + 0.5):int(frame.shape[1] / 1.452345 + 0.5)]

        if count > timer and count % accuracy == 0:
            ocr_results_per_frame = get_events_from_frame(reader, frame)

            # wait for certain amount of time
            if len(ocr_results_per_frame) > 0:
                timer = count + 180
                for element in ocr_results_per_frame:
                    log.append(str(count).rjust(6) + " | " + str(element))
                    print(log[-1])
                    log[-1] += '\n'

            frame = draw_bounding_box(frame, [ocr_result.bounding_box for ocr_result in ocr_results_per_frame])

        cv.imshow("image", frame)
        if cv.waitKey(1) == ord('q'):
            break
        count += 1

    return cap, log


def main(input_video_path: str, output_file_path: str) -> None:
    """
    loads an image and draws a bounding box on it
    """

    # init
    cv.setUseOptimized(True)

    file = open(output_file_path, 'w', encoding="utf-8");
    cap = cv.VideoCapture(input_video_path)
    reader = easyocr.Reader(["ko", "en"], gpu=True)

    cap, events_per_frame = get_events_from_video(reader, cap, 90)

    for event in events_per_frame:
        file.write(event)

    file.close()
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main("../resources/SANDBOX vs APK Prince Game 1 - LCK 2020 Spring Split W1D2 - SBG vs APK G1.mp4",
         "result_per_frame.txt")
