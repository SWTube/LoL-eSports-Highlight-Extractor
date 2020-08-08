"""
#   File Name: decision_highlight.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 08/08/20
# Last Update: August 08, 2020
#     Purpose: to decision highlight score
"""


def load_ultimate_cooltime_dictionary() -> dict:
    """
        Load ultimate skill's cool time
        Args:

        Returns:
            champion ultimate skill's cool time dictionary
        Raises:
            None
    """
    champion_cooltime_dictionary = {}
    with open("../resources/champion_ultimate_cooltime.txt") as champion_ultimate_cooltime:
        for line in champion_ultimate_cooltime:
            (key, value) = line.split()
            champion_cooltime_dictionary[key] = int(value)

    return champion_cooltime_dictionary


def find_max_cooltime_value() -> int:
    """
        Find ultimate skill's maximum cool time
        Args:

        Returns:
            ultimate skill's maximum cool time
        Raises:
            None
    """
    champion_cooltime_dictionary = load_ultimate_cooltime_dictionary()
    max_value = max(champion_cooltime_dictionary.values())

    return max_value


def decision_highlight_score(champion_name : list, ultimate_is_used : list) -> float:
    """
        Decision_highlight score using ultimate skill's cool time
        If ultimate skill is used, sum highlight score
        Args:
            champion_name : this is str type list, use to find ultimate skill's cool time
            ultimate_is_used : this is bool type list, to know ultimate is used
        Returns:
            champion ultimate skill's cool time dictionary
        Raises:
            None
    """
    champion_cooltime_dictionary = load_ultimate_cooltime_dictionary()

    highlight_score = 0

    if ultimate_is_used:
        highlight_score += champion_cooltime_dictionary[champion_name]

    return highlight_score



def main() -> None:
    print("decision_highlight.py")


if __name__ == "__main__":
    main()