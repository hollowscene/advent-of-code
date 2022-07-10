# -*- coding: utf-8 -*-
"""
Advent of Code 2021 - Day 2: Dive!

@author: Andrew Ting
@last-modified: 2022/07/10
"""


# %%

def dive(instructions: list) -> list:
    """Calculate the horizontal position and depth using instructions.

    Possible course instructions:
    'forward X': increases the horizontal position by X units.
    'down X'   : increases the depth by X units.
    'up X'     : decreases the depth by X units.

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


def updated_dive(instructions: list) -> list:
    """Calculate the horizontal position and depth using updated instructions.

    Possible course instructions:
    'forward X': increases the horizontal position by X units and increases the
                 depth by aim multiplied by X units.
    'down X'   : increases the aim by X units.
    'up X'     : decreases the aim by X units.

    Parameters
    ----------
    instructions : list
        List of instructions for the submarine to follow.

    Returns
    -------
    horizontal_position, depth : tuple
        The horizontal position and depth of the submarine after following the
        updated planned course.

    """
    horizontal_position = 0
    depth = 0
    aim = 0

    for ins in instructions:
        direction, units = ins.split(" ")
        move = int(units)
        if direction == "forward":
            horizontal_position += move
            depth += aim * move
        elif direction == "down":
            aim += move
        elif direction == "up":
            aim -= move

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
        part2_output = updated_dive(list_ci)
        print(f"Part 2 solution: {part2_output[0] * part2_output[1]}")
