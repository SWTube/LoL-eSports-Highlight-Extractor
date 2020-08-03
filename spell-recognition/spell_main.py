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
import visualization as vs


def main():
    first_frame_spell = []
    fixed_spell_list = []
    frames = []
    highlight_score_result = []
    in_game_spells = []
    similarity_result = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    spell_image_data = []

    frame_count = 0

    spell_file = ["Barrier.png", "Challenging_Smite.png", "Chilling_Smite.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png",
                  "Hexflash.png", "Ignite.png", "Smite.png", "Teleport.png"]

    video_path = "../resources/test_video_one_minute.mp4.mp4"
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
    first_frame_spell = lsr.extract_spell_images(frames[0])

    for in_game_spell_image in first_frame_spell:
        similarity_list = []
        spell_index = 0

        # Compare in-game spell images to original spells and calculates similarity value for each comparison.
        for original_spell_image in spell_image_data:
            similarity_list.append(lsr.compare_images_1(in_game_spell_image, original_spell_image))

        # Find the image with the highest similarity value.
        spell_index = similarity_list.index(max(similarity_list))

        # Append this spell image in fixed_spell_list as np.ndarray data type.
        fixed_spell_list.append(spell_image_data[spell_index])

    ## Begin video analysis
    for frame in frames:
        # Extract spell images from the frame.
        in_game_spells = lsr.extract_spell_images(frame)

        # Compare and add similarity values into list.
        for idx in range(len(in_game_spells)):
            similarity_result[idx].append(lsr.compare_images_1(in_game_spells[idx], fixed_spell_list[idx]))

    ## -- test -- ##
    print("-- test --")

    return None


if __name__ == '__main__':
    main()
