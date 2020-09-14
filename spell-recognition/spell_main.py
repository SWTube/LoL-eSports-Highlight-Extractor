"""
#   File Name: spell_main.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
               ssw03270
#  Start Date: 07/29/20
# Last Update: Sep 14, 2020
#     Purpose: Main file to run spell analysis.
"""
import lol_spell_recognition as lsr
import numpy as np
import visualization as vs

import cv2 as cv


def main():
    fixed_spell_list = []
    similarity_result = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    spell_image_data = []
    spell_names = []

    spell_file = ["Barrier.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png", "Ignite.png", "Teleport.png"]

    video_path = "../resources/AFvsAFK_G1_output.mp4"
    spell_path = "../resources/summoner_spells/"

    ## Initialize
    # Load spell images
    for idx in range(len(spell_file)):
        spell_image = cv.imread(spell_path + spell_file[idx])
        spell_image_data.append(spell_image)

        # OpenCV uses BGR as its default color order for images, so convert to RGB
        spell_image_data[idx] = cv.cvtColor(spell_image_data[idx], cv.COLOR_BGR2RGB)

    # Delete variable used inside for loop for efficient memory usage
    del spell_image

    # Resize all spell images to 20x20
    for idx in range(len(spell_image_data)):
        spell_image_data[idx] = cv.resize(spell_image_data[idx], (20, 20))

    # Convert video to list of frames and saves them in *frames* list variable.
    frames, frame_count, frame_rate = lsr.video_to_list(video_path)

    ## First frame analysis
    first_frame_spell = lsr.extract_spell_images(frames[0])
    loop_num = 0

    for in_game_spell_image in first_frame_spell:
        similarity_list = []
        spell_index = 0

        # Compare in-game spell images to original spells and calculates similarity value for each comparison.
        for original_spell_image in spell_image_data:
            similarity_list.append(lsr.compare_images(in_game_spell_image, original_spell_image))

        # Find the image with the highest similarity value.
        spell_index = similarity_list.index(max(similarity_list))
        # Check the image load correctly.
        print(lsr.check_spell_name(spell_file, spell_index, loop_num))
        # Append name of spell to find smite.
        spell_names.append(lsr.check_spell_name(spell_file, spell_index, loop_num))
        # Append this spell image in fixed_spell_list as np.ndarray data type.
        fixed_spell_list.append(spell_image_data[spell_index])

        loop_num += 1

    del similarity_list
    del spell_index

    ## Begin video analysis
    frame_num = 1

    print("-- Analysing Video --")
    for frame in frames:
        print(end='\r')
        print("Processing... {}%".format(round(frame_num * 100 / len(frames), 2)), end='')

        # Extract spell images from the frame.
        in_game_spells = lsr.extract_spell_images(frame)

        # Compare and add similarity values into list.
        for idx in range(len(in_game_spells)):
            similarity_result[idx].append(lsr.compare_images(in_game_spells[idx], fixed_spell_list[idx]))

        frame_num += 1

    del in_game_spells
    print()

    # Save these results in csv file
    lsr.save_result_as_csv(similarity_result, spell_names)

    vs.visualize_result()

    ## -- test -- ##
    print("-- test --")

    video_timer = lsr.save_highlight_score()
    frame_num = 1
    is_highlight = []
    is_highlight_able = np.zeros(100000)
    print("-- Checking Video --")

    for frame in frames:
        print(end='\r')
        print("Processing... {}%".format(round(frame_num * 100 / len(frames), 2)), end='')

        if video_timer[frame_num] >= 20:
            for i in range((frame_num - 5) * frame_rate, (frame_num + 5) * frame_rate):
                if is_highlight_able[i] == 0:
                    is_highlight.append(i)
                    is_highlight_able[i] = 1
        frame_num += 1

    video_capture = cv.VideoCapture(video_path)

    width = int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    fps = frame_rate

    out = cv.VideoWriter("testvideo_highlight.mp4", fourcc, fps, (width, height), 1)

    hightlight_num = 0
    frame_num = 1

    print("-- Writing Video --")
    while True:
        ret, frame_color = video_capture.read()
        if not ret:
            break
        if len(is_highlight) <= hightlight_num:
            break
        if is_highlight[hightlight_num] == int(video_capture.get(cv.CAP_PROP_POS_FRAMES)):
            out.write(frame_color)
            hightlight_num += 1
        frame_num += 1

    out.release()
    return None


if __name__ == '__main__':
    main()
