# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Day 3: Binary Diagnostic

@author: Andrew Ting
@last-modified: 2022/07/10
"""


# %%

def binary_diagnostic(report: list) -> list:
    """Return most common and least common bits in each position.

    Parameters
    ----------
    report : list
        List of binary numbers as strings.

    Returns
    -------
    gamma_rate, epsilon_rate : str, str
        The gamma rate is a binary number representing the most common bits in
        each position. The epsilon is the same but for the least common bits.

    """
    gamma_rate = ""
    epsilon_rate = ""

    n = len(report[0])

    for i in range(n):
        bit_tracker = [0, 0]
        for num in report:
            bit_tracker[int(num[i])] += 1

        if bit_tracker[0] >= bit_tracker[1]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return (gamma_rate, epsilon_rate)


def binary_life_support_diagnostic(report: list) -> list:
    """Return most common and least common bits in each position.

    Parameters
    ----------
    report : list
        List of binary numbers as strings.

    Returns
    -------
    oxygen_generator_rating, co2_scrubbing_rating : str, str
        x

    """




    return (oxygen_generator_rating, co2_scrubbing_rating)


# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        diagnostic_report = f.read()

        # Slice out final entry as it is an empty line
        list_dr = diagnostic_report.split("\n")[:-1]

        # Part 1
        part1_output = binary_diagnostic(list_dr)
        power_consumption = int(part1_output[0], 2) * int(part1_output[1], 2)
        print(f"Part 1 solution: {power_consumption}")

        # Part 2
        # part2_output = binary_diagnostic(list_ci)
        # print(f"Part 2 solution: {part2_output}")
