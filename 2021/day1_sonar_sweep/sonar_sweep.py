# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Day 1 Sonar Sweep

@author: Andrew Ting
@last-modified: 12/12/21
"""


# %%

import pandas as pd
import numpy as np


# %%

def sonar_sweep(measurements:list) -> int:
    """Return number of consecutively increasing numbers.

    Parameters
    ----------
    measurements : list
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    # create a new list for the difference between consecutive measurements
    # then just take the length of this new list
    return measurements
    

# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        depth_measurements = f.read()
        # Slice out final entry as it is an empty line
        list_dm = depth_measurements.split("\n")[:-1]
        print(sonar_sweep(list_dm))
        