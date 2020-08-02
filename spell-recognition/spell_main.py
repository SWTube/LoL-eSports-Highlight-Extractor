"""
#   File Name: spell_main.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
#  Start Date: 07/29/20
# Last Update: July 29, 2020
#     Purpose: Main file to run spell analysis.
"""
import cv2 as cv
import lol_spell_recognition as lsr
import pyprind
import sys


def main():
    frames = []
    spell_image_data = []
    in_game_spell = []
    first_frame_spell = []
    fixed_spell_list = []
    frame_count = 0
    spell_file = ["Barrier.png", "Challenging_Smite.png", "Chilling_Smite.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png",
                  "Hexflash.png", "Ignite.png", "Smite.png", "Teleport.png"]

    video_path = "../resources/APK Prince vs SANDBOX Game 1 - LCK 2020 Spring Split W6D5 - APK vs SBG G1.mp4"
    spell_path = "../resources/summoner_spells/"

    ## Initialize
    # Load spell images
    for i in range(len(spell_file)):
        spell_image = cv.imread(spell_path + spell_file[i])
        spell_image_data.append(spell_image)

        # OpenCV uses BGR as its default color order for images, so convert to RGB
        spell_image_data[i] = cv.cvtColor(spell_image_data[i], cv.COLOR_BGR2RGB)

    # Resize all spell images to 20x20
    for i in range(len(spell_image_data)):
        spell_image_data[i] = cv.resize(spell_image_data[i], (20, 20))

    # Convert video to list of frames and saves them in *frames* list variable.
    frames, frame_count = lsr.video_to_list(video_path)

    ## First frame analysis
    # Fix spells - frames[0] -> list[20]
    first_frame_spell = lsr.extract_spell_images(frames[0])

    bar = pyprind.ProgBar(len(first_frame_spell), stream=sys.stdout)
    for in_game_spell_image in first_frame_spell:
        similarity_list = []
        spell_index = 0
        for original_spell_image in spell_image_data:
            similarity_list.append(lsr.compare_images_1(original_spell_image, in_game_spell_image))
            spell_index = similarity_list.index(max(similarity_list))
            fixed_spell_list.append(spell_image_data[spell_index])
        bar.update()

    ## Begin frame analysis
    # for frame in frames:
    #     # Extract spell images from the frame.
    #     in_game_spell = lsr.extract_spell_images(frame)

    # -- test -- #
    print("-- test --")

    # idx = 2, 12
    # images in those indexes are on cooldown.

    # in_game_spell = extract_spell_images(frames[0])
    #
    # compare_images_1(in_game_spell[2], spell_image_data[1])
    # compare_images_1(in_game_spell[12], spell_image_data[1])
    #
    # print(compare_images_2(in_game_spell[2], spell_image_data[1]))
    # print(compare_images_2(in_game_spell[12], spell_image_data[1]))

    return None


if __name__ == '__main__':
    main()
