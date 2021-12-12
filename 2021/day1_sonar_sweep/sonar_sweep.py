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
    
    tmp = measurements[0]
    # Iterate through every measurement and compare to previous
    for m in measurements:
        if m > tmp:
            n_increases += 1
        tmp = m
    
    return n_increases


def rolling_sum(measurements:list,
                rolling_window:int = 3,
                ) -> list:
    """Convert measurements into a rolling sum list.
    
    Parameters
    ----------
    measurements : list
        DESCRIPTION.

    Returns
    -------
    list
        DESCRIPTION.

    """
    measurements_rs = []
    
    #
    for i in range(len(measurements) - rolling_window + 1):
        window = measurements[i:i+rolling_window]
        measurements_rs.append(sum(window))
        
    return measurements_rs


def str_to_int(lst:list) -> list:
    """Convert string items in list to int."""
    return [int(item) for item in lst]


# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        depth_measurements = f.read()
        # Slice out final entry as it is an empty line
        list_dm = depth_measurements.split("\n")[:-1]
        list_dm = str_to_int(list_dm)
        print(sonar_sweep(list_dm))
        print(sonar_sweep(rolling_sum(list_dm)))
        