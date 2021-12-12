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
    """Returns number of increasing measurements.
    
    Iterates through measurements and increments n_increases whenever 
    measurements[i] is larger than measurements[i-1].

    Parameters
    ----------
    measurements : list
        A list of depth measurements as strings.

    Returns
    -------
    n_increases : int
        The number of times a depth measurement increases from the previous.

    """
    n_increases = 0
    
    tmp = int(measurements[0])
    # Iterate through every measurement and compare to previous
    for m in measurements:
        m = int(m)
        if m > tmp:
            n_increases += 1
            tmp = m
    
    return n_increases
    

# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        depth_measurements = f.read()
        # Slice out final entry as it is an empty line
        list_dm = depth_measurements.split("\n")[:-1]
        print(sonar_sweep(list_dm))
        