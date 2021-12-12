# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Day 1 Sonar Sweep

@author: Andrew Ting
@last-modified: 12/12/21
"""


# %%

def sonar_sweep(measurements:list) -> int:
    """Returns number of increasing consecutive measurements.
    
    Iterates through measurements and increments n_increases whenever 
    measurements[i] is larger than measurements[i-1].

    Parameters
    ----------
    measurements : list
        A list of integer depth measurements.

    Returns
    -------
    n_increases : int
        The number of times a depth measurement increases from the previous.

    """
    n_increases = 0
    
    # Iterate through every measurement and compare to previous
    tmp = measurements[0]
    for m in measurements:
        if m > tmp:
            n_increases += 1
        tmp = m
    
    return n_increases


def rolling_sum(measurements:list,
                rw_size:int = 3,
                ) -> list:
    """Convert measurements into a rolling sum list.
    
    Generates a new rolling sum list consisting of the sum of 
    measurements[i:i+n] where n is the rolling_window size.
    
    Parameters
    ----------
    measurements : list
        A list of integer depth measurements.
    rw_size : int
        Rolling window size.

    Returns
    -------
    measurements_rs : list
        A modified rolling sum list.

    """
    measurements_rs = []
    
    # Iterate through measurements to generate rolling sums
    for i in range(len(measurements) - rw_size + 1):
        window = measurements[i:i+rw_size]
        measurements_rs.append(sum(window))
        
    return measurements_rs


def str_to_int(lst:list) -> list:
    """Convert data type of all list items to integer."""
    return [int(item) for item in lst]


# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        depth_measurements = f.read()
        
        # Slice out final entry as it is an empty line
        list_dm = depth_measurements.split("\n")[:-1]
        list_dm = str_to_int(list_dm)
        
        # Part 1
        part1_output = sonar_sweep(list_dm)
        print(f"Part 1 solution: {part1_output}")
        
        # Part 2
        part2_output = sonar_sweep(rolling_sum(list_dm))
        print(f"Part 2 solution: {part2_output}")
        