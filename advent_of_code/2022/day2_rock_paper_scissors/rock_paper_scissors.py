# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 2: Rock Paper Scissors

@author: Andrew Ting
@last-modified: 2022/12/02
"""

from aoc_utils import load


# %%

def rock_paper_scissors(strategy_guide: list) -> int:
    """Return the score from following the strategy guide."""
    total_score = 0

    for match in strategy_guide:
        score = 0

        if match[2] == "X":
            score += 1
            if match[0] == "A":
                score += 3
            elif match[0] == "B":
                score += 0
            elif match[0] == "C":
                score += 6

        elif match[2] == "Y":
            score += 2
            if match[0] == "A":
                score += 6
            elif match[0] == "B":
                score += 3
            elif match[0] == "C":
                score += 0

        elif match[2] == "Z":
            score += 3
            if match[0] == "A":
                score += 0
            elif match[0] == "B":
                score += 6
            elif match[0] == "C":
                score += 3

        total_score += score

    return total_score


def rock_paper_scissors_decrypted(strategy_guide: list) -> int:
    """Return the score from decrypting the strategy guide."""
    total_score = 0

    for match in strategy_guide:
        score = 0
        
        if match[2] == "X":
            score += 0
            if match[0] == "A":
                score += 3
            elif match[0] == "B":
                score += 1
            elif match[0] == "C":
                score += 2

        elif match[2] == "Y":
            score += 3
            if match[0] == "A":
                score += 1
            elif match[0] == "B":
                score += 2
            elif match[0] == "C":
                score += 3

        elif match[2] == "Z":
            score += 6
            if match[0] == "A":
                score += 2
            elif match[0] == "B":
                score += 3
            elif match[0] == "C":
                score += 1

        total_score += score

    return total_score


# %%

if __name__ == "__main__":
    input_path = "advent_of_code\\2022\\day2_rock_paper_scissors\\input.txt"
    strategy_guide = load.read_input_to_list(input_path)

    total_score = rock_paper_scissors(strategy_guide)

    print(f"Part 1 solution: {total_score}")

    new_total_score = rock_paper_scissors_decrypted(strategy_guide)

    print(f"Part 2 solution: {new_total_score}")
