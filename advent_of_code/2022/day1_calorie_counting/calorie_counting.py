# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 1: Calorie Counting

@author: Andrew Ting
@last-modified: 2022/12/01
"""

from aoc_utils import load


# %%

def calorie_counting(calories_list: list) -> int:
    """Return the elf carrying the most calories."""
    calories_log = [0]

    pointer = 0
    for item in calories_list:
        if item == "":
            calories_log.append(0)
            pointer += 1
        else:
            calories_log[pointer] += int(item)

    sorted_calories = sorted(calories_log, reverse=True)

    return sorted_calories


# %%

if __name__ == "__main__":
    input_path = "advent_of_code\\2022\\day1_calorie_counting\\input.txt"
    calories_list = load.read_input_to_list(input_path)

    sorted_calories = calorie_counting(calories_list)

    print(f"Part 1 solution: {sorted_calories[0]}")

    print(f"Part 2 solution: {sum(sorted_calories[:3])}")
