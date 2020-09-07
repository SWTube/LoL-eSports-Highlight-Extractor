"""
#   File Name: decision_highlight.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 08/08/20
# Last Update: August 10, 2020
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


def find_max_cooltime_value(champion_cooltime_dictionary : dict) -> int:
    """
        Find ultimate skill's maximum cool time
        Args:
            champion_cooltime_dictionary : dictionary to find max value
        Returns:
            ultimate skill's maximum cool time
        Raises:
            None
    """
    # champion_cooltime_dictionary = load_ultimate_cooltime_dictionary()
    max_value = max(champion_cooltime_dictionary.values())

    return max_value


def decision_highlight_score(champion_name : list, is_ultimate_used : list) -> float:
    """
        Decision_highlight score using ultimate skill's cool time
        If ultimate skill is used, sum highlight score
        Args:
            champion_name : this is str type list, use to find ultimate skill's cool time
            is_ultimate_used : this is bool type list, to know ultimate is used, 1 dim list
        Returns:
            champion ultimate skill's cool time dictionary
        Raises:
            None
    """
    champion_cooltime_dictionary = load_ultimate_cooltime_dictionary()

    highlight_score = 0

    for champion_count in range(len(champion_name)):
        for decision_count in range(len(is_ultimate_used)):
            if is_ultimate_used[decision_count]:
                highlight_score += champion_cooltime_dictionary[champion_name[champion_count]]

    return highlight_score


def get_highlight_list(champion_name : list, is_ultimate_used : list) -> list:
    """
        Get highlight score by detect ultimate
        Args:
            champion_name : this is str type list, use to find ultimate skill's cool time
            is_ultimate_used : this is bool type list, to know ultimate is used, 2 dim list
        Returns:
            highlight score in each second
        Raises:
            None
    """
    # Add here!
    highlight_list = []

    for sec in is_ultimate_used:
        highlight_list.append(decision_highlight_score(champion_name, sec))

    return highlight_list


def main() -> None:
    print("decision_highlight.py")


if __name__ == "__main__":
    main()