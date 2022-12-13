# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 9: Rope Bridge

@author: Andrew Ting
@last-modified: 2022/12/13
"""

import math

from aoc_utils import load


# %%

def move_logic(horizontal_distance: int, vertical_distance: int) -> tuple:
    """Return move to make based on difference."""
    horizontal_move = 0
    vertical_move = 0

    # tail is 1 space from head
    if abs(horizontal_distance) <= 1 and abs(vertical_distance) <= 1:
        return (0, 0)

    if horizontal_distance >= 1:
        horizontal_move = 1
    elif horizontal_distance <= -1:
        horizontal_move = -1

    if vertical_distance >= 1:
        vertical_move = 1
    elif vertical_distance <= -1:
        vertical_move = -1

    return horizontal_move, vertical_move


def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    assert part in [1, 2], "Part must be 1 or 2"

    input_list = load.read_input_to_list(input_path)
    solution = None

    move_list = input_list

    visited_positions = set()
    starting_coordinate = (0, 0)

    current_head = starting_coordinate
    current_tail = starting_coordinate

    step_count = 0

    if part == 2:
        # It's not going to be pretty but I think the easiest
        # solution here truly is to just do the same logic for
        # every knot in the rope.
        rope_positions = []
        for _ in range(10):
            rope_positions.append((0, 0))

    for move in move_list:
        move_instruction = move.split(" ")
        direction = move_instruction[0]
        distance = int(move_instruction[1])

        for step in range(int(distance)):
            # Move head
            if direction == "U":
                current_head = (current_head[0], current_head[1] + 1)
            elif direction == "D":
                current_head = (current_head[0], current_head[1] - 1)
            elif direction == "L":
                current_head = (current_head[0] - 1, current_head[1])
            elif direction == "R":
                current_head = (current_head[0] + 1, current_head[1])
            else:
                raise ValueError(f"Got unexpected direction {direction}")

            if part == 1:
                if step_count >= 1:
                    # Move tail
                    horizontal_difference = current_head[0] - current_tail[0]
                    vertical_difference = current_head[1] - current_tail[1]

                    horizontal_move, vertical_move = move_logic(horizontal_difference, vertical_difference)
                    current_tail = (
                        current_tail[0] + horizontal_move,
                        current_tail[1] + vertical_move,
                    )
            elif part == 2:
                rope_positions[0] = current_head

                # Move every position in the rope
                for i in range(min(step_count, 9)):
                    current_head = rope_positions[i]
                    current_tail = rope_positions[i + 1]
                    # print(rope_positions)

                    # Move tail
                    horizontal_difference = current_head[0] - current_tail[0]
                    vertical_difference = current_head[1] - current_tail[1]

                    horizontal_move, vertical_move = move_logic(horizontal_difference, vertical_difference)

                    current_tail = (
                        current_tail[0] + horizontal_move,
                        current_tail[1] + vertical_move,
                    )

                    rope_positions[i + 1] = current_tail

                current_head = rope_positions[0]
                current_tail = rope_positions[-1]

                # print(rope_positions)

            # print("H", current_head)
            # print("T", current_tail)

            # print(current_tail)
            visited_positions.add(current_tail)

            step_count += 1

    solution = len(visited_positions)

    return solution


# %%

if __name__ == "__main__":
    input_path = "input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
