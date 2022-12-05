# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 5: Supply Stacks

@author: Andrew Ting
@last-modified: 2022/12/05
"""

import re

from aoc_utils import load


# %%

def _parse_crates_at_height(crates: str, n_stacks: int) -> list:
    """Parse input line for crates at a given height."""
    # Note: Hardcoded to assume its 3 spaces, then a space and so on
    parsed_crates = []

    # Offset accounts for the space in between each crate
    offset = 0
    for i in range(n_stacks):
        crate = crates[3*i+offset+1]
        parsed_crates.append(crate)
        offset += 1

    return parsed_crates


def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    input_list = load.read_input_to_list(input_path)
    solution = None

    if part == 1:
        # Seperate input
        crate_input = []
        procedure_input = []

        instructions_switch = 0
        for line in input_list:
            if line == "":
                instructions_switch = 1
                continue

            if instructions_switch:
                procedure_input.append(line)
            else:
                crate_input.append(line)

        # Parse crate stack
        crate_indices = crate_input[-1][1:-1].split("   ")
        n_stacks = int(crate_indices[-1])

        crate_stack = []
        for _ in range(n_stacks):
            crate_stack.append([])
        
        # Consider the bottommost crate as height of 0
        # Each list corresponds to a stack from 1 to 9
        # Each item in the list is a crate from bottom to top
        for height in range(len(crate_input) - 1):
            crates_at_height = _parse_crates_at_height(crate_input[-height-2], n_stacks)
            for i in range(len(crates_at_height)):
                crate_stack[i].append(crates_at_height[i])

        # Remove empty crates from top of stacks
        for stack in crate_stack:
            while stack[-1] == " ":
                stack.pop()

        # print(crate_stack)

        # Execute reassignment procedure
        for move in procedure_input:
            number_of_moves, from_stack, to_stack = re.findall(r"\d+", move)

            number_of_moves = int(number_of_moves)
            from_stack = int(from_stack) - 1
            to_stack = int(to_stack) - 1

            for _ in range(number_of_moves):
                moved_crate = crate_stack[from_stack].pop()
                crate_stack[to_stack].append(moved_crate)

        # print(crate_stack)

        solution = ""
        for stack in crate_stack:
            solution += stack[-1]

    elif part == 2:
        # Seperate input
        crate_input = []
        procedure_input = []

        instructions_switch = 0
        for line in input_list:
            if line == "":
                instructions_switch = 1
                continue

            if instructions_switch:
                procedure_input.append(line)
            else:
                crate_input.append(line)

        # Parse crate stack
        crate_indices = crate_input[-1][1:-1].split("   ")
        n_stacks = int(crate_indices[-1])

        crate_stack = []
        for _ in range(n_stacks):
            crate_stack.append([])
        
        # Consider the bottommost crate as height of 0
        # Each list corresponds to a stack from 1 to 9
        # Each item in the list is a crate from bottom to top
        for height in range(len(crate_input) - 1):
            crates_at_height = _parse_crates_at_height(crate_input[-height-2], n_stacks)
            for i in range(len(crates_at_height)):
                crate_stack[i].append(crates_at_height[i])

        # Remove empty crates from top of stacks
        for stack in crate_stack:
            while stack[-1] == " ":
                stack.pop()

        # print(crate_stack)

        # Execute new reassignment procedure
        run_count = 0
        for move in procedure_input:
            number_of_moves, from_stack, to_stack = re.findall(r"\d+", move)

            number_of_moves = int(number_of_moves)
            from_stack = int(from_stack) - 1
            to_stack = int(to_stack) - 1

            crate_stack[to_stack] = crate_stack[to_stack] + crate_stack[from_stack][-number_of_moves:]
            crate_stack[from_stack] = crate_stack[from_stack][:-number_of_moves]

        # print(crate_stack)

        solution = ""
        for stack in crate_stack:
            solution += stack[-1]

    else:
        raise ValueError

    return solution


# %%

if __name__ == "__main__":
    input_path = "advent_of_code\\2022\\day5_supply_stacks\\input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
