"""
This file will analyse the summoner spells availability.
"""
from lol_image import image_to_data


# All spells are assumed to be 20x20 pixels

## Left-Side
# No1 Summoner D Spells Coordniates [158, 5] -> [177, 24]
# No1 Summoner F Spells Coordniates [181, 5] -> [200, 24]

# No2 Summoner D Spells Coordniates [261, 5] -> [280, 24]
# No2 Summoner F Spells Coordniates [284, 5] -> [303, 24]

# No3 Summoner D Spells Coordniates [364, 5] -> [383, 24]
# No3 Summoner F Spells Coordniates [387, 5] -> [406, 24]

# No4 Summoner D Spells Coordniates [466, 5] -> [485, 24]
# No4 Summoner F Spells Coordniates [489, 5] -> [508, 24]

# No5 Summoner D Spells Coordniates [570, 5] -> [589, 24]
# No5 Summoner F Spells Coordniates [593, 5] -> [612, 24]

## Right-Side
# No1 Summoner D Spells Coordniates [158, 1894] -> [177, 1913]
# No1 Summoner F Spells Coordniates [181, 1894] -> [200, 1913]

# No2 Summoner D Spells Coordniates [261, 1894] -> [280, 1913]
# No2 Summoner F Spells Coordniates [284, 1894] -> [303, 1913]

# No3 Summoner D Spells Coordniates [364, 1894] -> [383, 1913]
# No3 Summoner F Spells Coordniates [387, 1894] -> [406, 1913]

# No4 Summoner D Spells Coordniates [466, 1894] -> [485, 1913]
# No4 Summoner F Spells Coordniates [489, 1894] -> [508, 1913]

# No5 Summoner D Spells Coordniates [570, 1894] -> [589, 1913]
# No5 Summoner F Spells Coordniates [593, 1894] -> [612, 1913]


def main():
    data = image_to_data('resources/preview.jpeg')
    print(data[165][10])


if __name__ == '__main__':
    main()