# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 6: Tuning Trouble

@author: Andrew Ting
@last-modified: 2022/12/06
"""

import re

from aoc_utils import load


# %%

def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    assert part in [1, 2], "Part must be 1 or 2"

    input_list = load.read_input_to_list(input_path)
    solution = None

    stream = input_list[0]
    n = len(stream)

    if part == 1:
        signal_length = 4
    elif part == 2:
        signal_length = 14

    for i in range(n - signal_length):
        rolling_signal = stream[i:i+signal_length]
        if len(set(rolling_signal)) == signal_length:
            solution = i + signal_length
            break

    return solution


# %%

if __name__ == "__main__":
    input_path = "input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
