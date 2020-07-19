"""
#   File Name: finding_ultimate.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 07/08/20
# Last Update: July 13, 2020
#     Purpose: to find ultimate skill's coordinate
"""

import cv2 as cv
import numpy as np

"""
Ultimate Skill's center(x, y) coordinate
radius : 12

# left-side player
# player 1 [x, y] -> [71, 165]
# player 2 [x, y] -> [71, 268]
# player 3 [x, y] -> [71, 371]
# player 4 [x, y] -> [71, 473]
# player 5 [x, y] -> [71, 577]

# right-side player
# player 1 [x, y] -> [1847, 165]
# player 2 [x, y] -> [1847, 268]
# player 3 [x, y] -> [1847, 371]
# player 4 [x, y] -> [1847, 473]
# player 5 [x, y] -> [1847, 577]

Champions icon's coordinate
len : 40

# left-side player
# player 1 [x, y] -> [31, 160]
# player 2 [x, y] -> [31, 263]
# player 3 [x, y] -> [31, 366]
# player 4 [x, y] -> [31, 468]
# player 5 [x, y] -> [31, 572]

# right-side player
# player 1 [x, y] -> [1847, 160]
# player 2 [x, y] -> [1847, 263]
# player 3 [x, y] -> [1847, 366]
# player 4 [x, y] -> [1847, 468]
# player 5 [x, y] -> [1847, 572]
"""

def draw_circle_on_ultimate(circle_x : int, circle_y : int) -> None:
    """
    Draw circle on ultimate skill to get ultimate skill's coordinate

    Args:
        circle_x: x-coordinate of the center of the circle
        circle_y: y-coordinate of the center of the circle

    Returns:
        Just draw circle on ultimate skill

    Raises:
        None
    """
    img = cv.imread("test.jpeg")

    img = cv.circle(img, (circle_x, circle_y), 12, (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def draw_rectangle_on_champion(rectangle_x : int, rectangle_y : int) -> None:
    """
    Draw rectangle on champion to get champions icon's coordinate

    Args:
        rectangle_x: x-coordinate of the center of the circle
        rectangle_y: y-coordinate of the center of the circle

    Returns:
        Draw rectangle on champions icon

    Raises:
        None
    """
    img = cv.imread("test.jpeg")

    img = cv.rectangle(img, (rectangle_x, rectangle_y), (rectangle_x + 40, rectangle_y + 40), (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main() -> None:
    #draw_circle_on_ultimate(1847, 165)
    #draw_rectangle_on_champion(1847, 160)

    champion_icon_data = []
    ultimate_skills_data = []

    in_game_champion_icon = []
    in_game_ultimate_skills = []

    champion_icon_files = ["Aatrox.png", "Ahri.png", "Akali.png", "Alistar.png", "Amumu.png", "Anivia.png",
                            "Annie.png", "Aphelios.png", "Ashe.png", "Aurelionsol.png", "Azir.png", "Bard.png",
                            "Blitzcrank.png", "Brand.png", "Braum.png", "Caitlyn.png", "Camille.png",
                            "Cassiopeia.png", "Chogath.png", "Corki.png", "Darius.png", "Diana.png", "Dr_mundo.png",
                            "Draven.png", "Ekko.png", "Elise.png", "Evelynn.png", "Ezreal.png", "Fiddlesticks.png",
                            "Fiora.png", "Fizz.png", "Galio.png", "Gangplank.png", "Garen.png", "Gnar.png",
                            "Gragas.png", "Graves.png", "Hecarim.png", "Heimerdinger.png", "Illaoi.png", "Irelia.png",
                            "Ivern.png", "Janna.png", "Jarvan.png", "Jax.png", "Jayce.png", "Jhin.png", "Jinx.png",
                            "Kaisa.png", "Kalista.png", "Karma.png", "Karthus.png", "Kassadin.png", "Katarina.png",
                            "Kayle.png", "Kayn.png", "Kennen.png", "Khazix.png", "Kindred.png", "Kled.png",
                            "Kogmaw.png", "Leblanc.png", "Leesin.png", "Leona.png", "Lillia.png", "Lissandra.png",
                            "Lucian.png", "Lulu.png", "Lux.png", "Malphite.png", "Malzahar.png", "Maokai.png",
                            "Masteryi.png", "Missfortune.png", "Mordekaiser.png", "Morgana.png", "Nami.png",
                            "Nasus.png", "Nautilus.png", "Neeko.png", "Nidalee.png", "Nocturne.png", "Nunu.png",
                            "Olaf.png", "Orianna.png", "Ornn.png", "Pantheon.png", "Poppy.png", "Pyke.png",
                            "Qiyana.png", "Quinn.png", "Rakan.png", "Rammus.png", "Reksai.png", "Renekton.png",
                            "Rengar.png", "Riven.png", "Rumble.png", "Ryze.png", "Sejuani.png", "Senna.png",
                            "Sett.png", "Shaco.png", "Shen.png", "Shyvana.png", "Singed.png", "Sion.png",
                            "Sivir.png", "Skarner.png", "Sona.png", "Soraka.png", "Swain.png", "Sylas.png",
                            "Syndra.png", "Tahmkench.png", "Taliyah.png", "Talon.png", "Taric.png", "Teemo.png",
                            "Thresh.png", "Tristana.png", "Trundle.png", "Tryndamere.png", "Twistedfate.png",
                            "Twitch.png", "Udyr.png", "Urgot.png", "Varus.png", "Vayne.png", "Veigar.png", "Velkoz.png",
                            "Vi.png", "Viktor.png", "Vladimir.png", "Volibear.png", "Warwick.png", "Wukong.png",
                            "Xayah.png", "Xerath.png", "Xinzhao.png", "Yasuo.png", "Yorick.png", "Yuumi.png", "Zac.png",
                            "Zed.png", "Ziggs.png", "Zilean.png", "Zoe.png", "Zyra.png"]

    champion_image_path = "../resources/champions_image/"

    # Load champion icon images
    for i in range(len(champion_icon_files)):
        champion_icon = cv.imread(champion_image_path + champion_icon_files[i])
        champion_icon_data.append(champion_icon)

        champion_icon_data[i] = cv.cvtColor(champion_icon_data[i], cv.COLOR_BGR2RGB)

    # Resize champion icon images(40 x 40)
    for i in range(len(champion_icon_data)):
        champion_icon_data[i] = cv.resize(champion_icon_data[i], (40, 40))






if __name__ == "__main__":
    main()