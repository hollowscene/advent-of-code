# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 10: Cathode-Ray Tube

@author: Andrew Ting
@last-modified: 2022/12/14
"""

import os

from aoc_utils import load


# %%

def _collate_part1_solution(cycle_counter: int, register_value: int) -> int:
    """Apply specific logic to solve part 1 solution."""
    signal_strength_solution = 0

    if cycle_counter in [20, 60, 100, 140, 180, 220]:
        signal_strength_solution += (cycle_counter * register_value)

    return signal_strength_solution


def _collate_part2_solution(cycle_counter: int, register_value: int) -> int:
    """Apply specific logic to solve part 1 solution."""
    pixel_value = "."

    horizontal_crt_position = cycle_counter % 40

    if abs(register_value - horizontal_crt_position) <= 1:
        pixel_value = "#"

    return pixel_value


def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    assert part in [1, 2], "Part must be 1 or 2"

    cpu_instructions = load.read_input_to_list(input_path)
    solution = None

    sum_of_signal_strengths = 0
    register_value = 1
    previous_value = 0
    cycle_counter = 0

    if part == 1:
        for instruction in cpu_instructions:
            # Add previous value in cycle
            register_value += previous_value

            # Process current instruction
            if instruction == "noop":
                previous_value = 0
            elif instruction.startswith("addx"):
                value_to_add = int(instruction.split(" ")[1])
                previous_value = value_to_add

                cycle_counter += 1
                sum_of_signal_strengths += _collate_part1_solution(cycle_counter, register_value)
            else:
                raise ValueError(f"Unexpected instruction {instruction}")

            cycle_counter += 1
            sum_of_signal_strengths += _collate_part1_solution(cycle_counter, register_value)

        solution = sum_of_signal_strengths

    elif part == 2:
        crt_output = ""
        for instruction in cpu_instructions:
            # Add previous value in cycle
            register_value += previous_value

            # Process current instruction
            if instruction == "noop":
                previous_value = 0
            elif instruction.startswith("addx"):
                value_to_add = int(instruction.split(" ")[1])
                previous_value = value_to_add

                crt_output += _collate_part2_solution(cycle_counter, register_value)
                cycle_counter += 1
            else:
                raise ValueError(f"Unexpected instruction {instruction}")

            crt_output += _collate_part2_solution(cycle_counter, register_value)
            cycle_counter += 1

        # print(crt_output)

        current_directory = os.path.dirname(__file__)
        output_path = os.path.join(current_directory, "output.txt")
        with open(output_path, mode="w") as f:
            n = len(crt_output)
            line_number = 0
            while True:
                start_of_line = 40 * line_number
                end_of_line = 40 * (line_number + 1)
                if end_of_line > n:
                    end_of_line = n
                    f.write(crt_output[start_of_line:end_of_line])
                    break
                f.write(crt_output[start_of_line:end_of_line])
                f.write("\n")
                line_number += 1

        solution = "Successfully finished writing to output.txt"

    return solution


# %%

if __name__ == "__main__":
    input_path = "input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
