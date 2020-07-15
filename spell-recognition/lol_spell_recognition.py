"""
#   File Name: lol_spell_recognition.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
               kkim99
#  Start Date: 06/05/20
# Last Update: July 10, 2020
#     Purpose: This file specifically tries to recognize the cooltime of summoner spells
               and uses this data to calculate highlight score of the game.
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import metrics

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


def video_to_list(path: str) -> list:
    """
    Converts a video file to frames and returns a list of them.

    Args:
        path: String value of path to video file.

    Returns:
        If correct path is given, this function will convert the video file to a list of frames.
        If given path is wrong, returns an empty list.

    Raises:
        None
    """
    assert isinstance(path, str)

    frame_list = []
    vid = cv.VideoCapture(path)

    while vid.isOpened():
        ret, frame = vid.read()

        if not ret:
            break

        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frame_list.append(frame)

    vid.release()
    # vid.destroyAllWindows()

    return frame_list


def mean_squared_error(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Calculates the 'Mean Squared Error' between the two images,
    which is the sum of the squared difference between the two images;
    CAUTION! the two images must have the same dimension.

    Args:
        imgA: Image to compare.
        imgB: Original image

    Returns:
        MSE. Lower the error, the more "similar" the two images are.

    Raises:
        None
    """
    assert isinstance(imgA, np.ndarray)
    assert isinstance(imgB, np.ndarray)

    error = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
    error /= float(imgA.shape[0] * imgA.shape[1])

    return error


# LAC
def compare_images_1(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Calculates the similarity of the two images.

    Args:
        imgA: Image to compare.
        imgB: Original image

    Returns:
        "Similarity" percentage of the two images.

    Raises:
        None
    """
    assert isinstance(imgA, np.ndarray)
    assert isinstance(imgB, np.ndarray)

    # compute the mean squared error
    mse_value = mean_squared_error(imgA, imgB)

    # compute the structural similarity
    ssim_value = metrics.structural_similarity(imgA, imgB, multichannel=True)

    # setup the figure
    fig = plt.figure("Image Comparison")
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (mse_value, ssim_value))

    # show first image
    axis_img_a = fig.add_subplot(1, 2, 1)
    plt.imshow(imgA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    axis_img_b = fig.add_subplot(1, 2, 2)
    plt.imshow(imgB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()

    return ssim_value


# LJH
def compare_images_2(imgA: np.ndarray, imgB: np.ndarray) -> float:
    """
    Compare two images through histogram

    Args:
        imgA: image in video
        imgB: original image

    Returns:
        Similarity between two images

    Raises:
        None
    """
    assert isinstance(imgA, np.ndarray)
    assert isinstance(imgB, np.ndarray)

    # Convert to hsv
    hsv_a = cv.cvtColor(imgA, cv.COLOR_BGR2HSV)
    hsv_b = cv.cvtColor(imgB, cv.COLOR_BGR2HSV)

    # Calculate and Normalize histogram
    hist_a = cv.calcHist([hsv_a], [0], None, [256], [0, 256])
    cv.normalize(hist_a, hist_a, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    hist_b = cv.calcHist([hsv_b], [0], None, [256], [0, 256])
    cv.normalize(hist_b, hist_b, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # Compare hist_a, hist_b
    a_b_comparison = cv.compareHist(hist_a, hist_b, 0)

    return a_b_comparison


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

    if (loc != 0) and (loc > 0) and loc <= 20:
        loc -= 1
        for y in range(position[loc][0], position[loc][2] + 1):
            in_game_spell.append([])
            for x in range(position[loc][1], position[loc][3] + 1):
                in_game_spell[y - position[loc][0]].append(frame[y][x])
        in_game_spell = np.array(in_game_spell, dtype="uint8")

        return in_game_spell
    elif loc == 0:
        for i in range(20):
            in_game_spell.append([])
            for y in range(position[i][0], position[i][2] + 1):
                in_game_spell[i].append([])
                for x in range(position[i][1], position[i][3] + 1):
                    in_game_spell[i][y - position[i][0]].append(frame[y][x])
                    # in_game_spell[i] = np.append(in_game_spell, frame[y][x], axis=0)
            in_game_spell[i] = np.array(in_game_spell[i], dtype="uint8")

        return in_game_spell
    else:
        assert False


def main():
    frames = []
    spell_image_data = []
    in_game_spell = []
    spell_file = ["Barrier.png", "Challenging_Smite.png", "Chilling_Smite.png", "Clarity.png", "Cleanse.png",
                  "Exhaust.png", "Flash.png", "Ghost.png", "Heal.png",
                  "Hexflash.png", "Ignite.png", "Smite.png", "Teleport.png"]

    video_path = "../resources/test.mp4"
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
    frames = video_to_list(video_path)

    ## Begin frame analysis
    # for frame in frames:
    #     # Extract spell images from the frame.
    #     in_game_spell = extract_spell_images(frame)

    # -- test -- #

    # idx = 2, 12
    # images in those indexes are on cooldown.

    in_game_spell = extract_spell_images(frames[0])

    compare_images_1(in_game_spell[2], spell_image_data[1])
    compare_images_1(in_game_spell[12], spell_image_data[1])

    print(compare_images_2(in_game_spell[2], spell_image_data[1]))
    print(compare_images_2(in_game_spell[12], spell_image_data[1]))


if __name__ == '__main__':
    main()
