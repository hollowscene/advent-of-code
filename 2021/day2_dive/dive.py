# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Day 2: Dive!

@author: Andrew Ting
@last-modified: 2022/07/10
"""


# %%

def dive(instructions: list) -> list:
    """Calculate the horizontal position and depth after planned course.

    Parameters
    ----------
    instructions : list
        List of instructions for the submarine to follow.

    Returns
    -------
    horizontal_position, depth : tuple
        The horizontal position and depth of the submarine after following the
        planned course.

    """
    horizontal_position = 0
    depth = 0

    for ins in instructions:
        direction, units = ins.split(" ")
        move = int(units)
        if direction == "forward":
            horizontal_position += move
        elif direction == "down":
            depth += move
        elif direction == "up":
            depth -= move

    return (horizontal_position, depth)


# %%

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        course_instructions = f.read()

        # Slice out final entry as it is an empty line
        list_ci = course_instructions.split("\n")[:-1]

        # Part 1
        part1_output = dive(list_ci)
        print(f"Part 1 solution: {part1_output[0] * part1_output[1]}")

        # Part 2
        # part2_output = dive(list_ci)
        # print(f"Part 2 solution: {part2_output}")
