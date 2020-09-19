"""
#   File Name: lol_spell_recognition.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
               ssw03270
#  Start Date: 06/05/20
# Last Update: Sep 19, 2020
#     Purpose: Functions that recognizes the cooltime of summoner spells
               and uses this data to calculate highlight score of the game.
"""
import csv
import cv2 as cv
import numpy as np
import os
from skimage import metrics

# Spell Highlight Scores
g_clarity_score = 0.1

g_smite_score = 5
g_challenging_smite_score = 5
g_chilling_smite_score = 5
g_hexflash_score = 5

g_ghost_score = 10
g_exhaust_score = 10
g_ignite_score = 10
g_heal_score = 10
g_barrier_score = 10
g_cleanse_score = 10

g_teleport_score = 15

g_flash_score = 20

video_total_frame = 0
video_frame_rate = 30

video_timer = np.zeros(10000)

def video_to_list(path: str) -> (list, int):
    """
    Converts a video file to frames and returns a list of them.

    Args:
        path: String value of path to video file.

    Returns:
        If correct path is given, this function will return a list of frames and the number of frames.
        If given path is wrong, returns an empty list.
        frame_rate
    Raises:
        None
    """
    assert isinstance(path, str)

    frame_list = []
    total_frame_count = 0
    frame_rate = 0
    vid = cv.VideoCapture(path)

    # Gets total frame count and the FPS of the video
    total_frame_count = int(vid.get(cv.CAP_PROP_FRAME_COUNT))
    frame_rate = vid.get(cv.CAP_PROP_FPS)

    # This rules out Drop-frame videos
    # ex) 29.97 fps -> 30 fps
    if not frame_rate.is_integer():
        frame_rate = int(frame_rate + 1)
    elif frame_rate.is_integer():
        frame_rate = int(frame_rate)
    else:
        print("frame_rate is invalid.")
        assert False

    print("-- Converting Video --")
    for frame_no in range(total_frame_count):
        print(end='\r')
        print("Processing... {}%".format(round(frame_no * 100 / total_frame_count, 2)), end='')

        ret, frame = vid.read()

        if not ret:
            break

        # Reads every (FPS) frames to increase analysis speed
        if frame_no % frame_rate == 0:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame_list.append(frame)
        else:
            continue

    print()
    vid.release()

    return frame_list, total_frame_count, frame_rate


def compare_images(image_one: np.ndarray, image_two: np.ndarray) -> float:
    """
    Calculates the similarity of the two images.

    Args:
        image_one: Image to compare.
        image_two: Original image

    Returns:
        "Similarity" percentage of the two images.

    Raises:
        None
    """
    assert isinstance(image_one, np.ndarray)
    assert isinstance(image_two, np.ndarray)

    # compute the structural similarity
    ssim_value = metrics.structural_similarity(image_one, image_two, multichannel=True)

    # convert ssim_value data type from np.float64 to float
    ssim_value = float(ssim_value)

    return ssim_value

def extract_spell_images(frame: np.ndarray, loc: int = 0) -> list:
    """
    Extracts summoners' spell images from the in-game image given as a parameter.

    Args:
        frame: A single frame from the game video.
        loc: An integer between 1~20 representing one specific location of the spell.
             If nothing is parsed, function returns all spells in the given frame.
             1 - Left Summoner 1 D, 2 - Left SUmmoner 1 F, ... , 20 - Right Summoner 5 - F

    Returns:
        list of summoners' spell image(s). This list will look like:
        [["Summoner 1 D"], ["Summoner 1 F"], ["Summoner 2 D"], ["Summoner 2 F"], ...]
            or
        ["Summoner 4 F"]

    Raises:
        None
    """
    assert isinstance(frame, np.ndarray)
    assert isinstance(loc, int)

    in_game_spell = []
    position = [
        [158, 5, 177, 24], [181, 5, 200, 24],
        [261, 5, 280, 24], [284, 5, 303, 24],
        [364, 5, 383, 24], [387, 5, 406, 24],
        [466, 5, 485, 24], [489, 5, 508, 24],
        [570, 5, 589, 24], [593, 5, 612, 24],
        [158, 1894, 177, 1913], [181, 1894, 200, 1913],
        [261, 1894, 280, 1913], [284, 1894, 303, 1913],
        [364, 1894, 383, 1913], [387, 1894, 406, 1913],
        [466, 1894, 485, 1913], [489, 1894, 508, 1913],
        [570, 1894, 589, 1913], [593, 1894, 612, 1913]
    ]

    # If the loc argument is parsed
    if (loc != 0) and (loc > 0) and loc <= 20:
        loc -= 1
        for y in range(position[loc][0], position[loc][2] + 1):
            in_game_spell.append([])
            for x in range(position[loc][1], position[loc][3] + 1):
                in_game_spell[y - position[loc][0]].append(frame[y][x])
        in_game_spell[0] = np.array(in_game_spell, dtype="uint8")

        return in_game_spell
    # If no loc argument is parsed
    elif loc == 0:
        for i in range(20):
            in_game_spell.append([])
            for y in range(position[i][0], position[i][2] + 1):
                in_game_spell[i].append([])
                for x in range(position[i][1], position[i][3] + 1):
                    in_game_spell[i][y - position[i][0]].append(frame[y][x])
            in_game_spell[i] = np.array(in_game_spell[i], dtype="uint8")

        return in_game_spell
    else:
        print("Invalid argument parsed into extract_spell_images() function.")
        assert False


def save_result_as_csv(similarity: list, spell_names: list) -> None:
    """
    Save similarity_list as csv file.

    Args:
        similarity: Result list containing all similarity values.
        spell_names : List of sumonner's spell in game.

    Raises:
        None
    """
    extension = ".csv"

    filename = ["left_summoner_1_D_spell", "left_summoner_1_F_spell", "left_summoner_2_D_spell",
                "left_summoner_2_F_spell", "left_summoner_3_D_spell", "left_summoner_3_F_spell",
                "left_summoner_4_D_spell", "left_summoner_4_F_spell", "left_summoner_5_D_spell",
                "left_summoner_5_F_spell", "right_summoner_1_D_spell", "right_summoner_1_F_spell",
                "right_summoner_2_D_spell", "right_summoner_2_F_spell", "right_summoner_3_D_spell",
                "right_summoner_3_F_spell", "right_summoner_4_D_spell", "right_summoner_4_F_spell",
                "right_summoner_5_D_spell", "right_summoner_5_F_spell"]

    left_side = np.zeros(3600)
    for idx in range(len(filename)):
        # Saving similarity
        path = "../result/similarity/" + filename[idx] + extension
        with open(path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(similarity[idx])

        # Checking when this spell used
        path = "../result/similarity_check/" + filename[idx] + extension
        with open(path, 'w', newline='') as file:
            check_row = []
            for idx2 in range(len(similarity[idx]) - 1):
                if((similarity[idx][idx2 + 1] - similarity[idx][idx2]) / similarity[idx][idx2] * 100) < -50:
                    similarity_error = True
                    # Checking similarity while 10s
                    if(idx2 + 10 < len(similarity[idx]) - 1):
                        for idx3 in range(idx2, idx2 + 10):
                            if ((similarity[idx][idx3 + 1] - similarity[idx][idx2]) / similarity[idx][idx2] * 100) > -50:
                                similarity_error = False
                    if similarity_error:
                        # If left side was hidden, erase it
                        if "left" in filename[idx]:
                            left_side[idx2] += 1
                            if left_side[idx2] == 10:
                                for i in range(int(idx2) - 5, int(idx2) + 5):
                                    video_timer[i] -= 200
                        check_row.append(idx2)

            # Write name of spell and used time
            csv_writer = csv.writer(file)
            csv_writer.writerow(spell_names[idx])
            csv_writer.writerow(check_row)

    return None

def check_spell_name(spell_name: list, spell_index: int, loop_num : int) -> list:
    """
    Check first frame analysis works well.

    Args:
        spell_name: List of summoner spell's name.
        spell_index: Index of spell_name list
        loop_num : var which indicates how many times function loop

    Raises:
        None

    Returns:
        list of summoner spell name
        summoner_spell
    """

    spell_location = ["left_summoner_1_D_spell", "left_summoner_1_F_spell", "left_summoner_2_D_spell",
                      "left_summoner_2_F_spell", "left_summoner_3_D_spell", "left_summoner_3_F_spell",
                      "left_summoner_4_D_spell", "left_summoner_4_F_spell", "left_summoner_5_D_spell",
                      "left_summoner_5_F_spell", "right_summoner_1_D_spell", "right_summoner_1_F_spell",
                      "right_summoner_2_D_spell", "right_summoner_2_F_spell", "right_summoner_3_D_spell",
                      "right_summoner_3_F_spell", "right_summoner_4_D_spell", "right_summoner_4_F_spell",
                      "right_summoner_5_D_spell", "right_summoner_5_F_spell"]

    summoner_spell = []

    summoner_spell.append(spell_location[loop_num] + ":" + spell_name[spell_index])
    return summoner_spell

def save_highlight_score() -> list:
    """
        Set highlight score using similarity_check csv file.

        Args:
            None

        Returns:
            video timer which take highlight score

    """
    path = "../result/similarity_check"
    filelist = os.listdir(path)

    for filename in filelist:
        with open(path + "/" + filename, 'r') as file:
            rdr = csv.reader(file)
            score = 0
            for idx in rdr:
                if score == 0:
                    score = set_highlight_score(idx[0])
                else:
                    for member in idx:
                        for i in range(int(member) - 5, int(member) + 5):
                            video_timer[i] += score

    return video_timer

def set_highlight_score(spell_name: str):
    """
    It doesn't save highlight score in array. Just check highlight score each spell.

    Args:
        spell_name: str of spell name
    Returns:
        spell_score : score, corresponding to the spell name
    """
    spell_file = ["Barrier.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png", "Ignite.png", "Teleport.png"]
    spell_score = [10, 0.1, 10, 10, 20, 10, 10, 10, 15]
    num = 0
    for i in range(len(spell_file)):
        if spell_file[i] in spell_name:
            num = i
            break
    return spell_score[num]

def main():
    print("----------------------------------------")
    print("lol_spell_recognition.py called as main.")
    print("----------------------------------------")

    return None


if __name__ == '__main__':
    main()
