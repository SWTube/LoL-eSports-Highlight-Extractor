"""
#   File Name: point_visualize.py
#        Team: visual recognition 2
#  Programmer: luckydipper
#  Start Date: 08/08/20
# Last Update: October 26, 2020
#     Purpose: to visualize for test
"""

import numpy as np
import matplotlib.pyplot as plt

def visualize(vector_1D: np.ndarray, name: str) -> None:
    """
    visualize 1D np.ndarray vector
    :param
        vector_1D: 1D array vector
    :raise
        show graph of 1D vector.
    :return
        None
    """
    plt.plot(vector_1D)
    plt.title(name)
    plt.show()
    return None


def main():
    print("This module just draw graph")
    return None

if __name__ == '__main__':
    main()