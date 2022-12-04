# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 4: Camp Cleanup

@author: Andrew Ting
@last-modified: 2022/12/04
"""

from aoc_utils import load


# %%

def _parse_assignment(assignment: str):
    """Parse assignment into sections."""
    pair_assignment = assignment.split(",")
    
    first_section = pair_assignment[0].split("-")
    second_section = pair_assignment[1].split("-")

    first_section[0] = int(first_section[0])
    first_section[1] = int(first_section[1])
    second_section[0] = int(second_section[0])
    second_section[1] = int(second_section[1])

    return first_section, second_section


def _check_contained_by(first_section: tuple, second_section: tuple) -> bool:
    """Determine whether first tuple is fully contained in the second tuple."""
    contained_by = False
    if (first_section[0] >= second_section[0]) and (first_section[1] <= second_section[1]):
        contained_by = True
    return contained_by


def _check_overlapping(first_section: tuple, second_section: tuple) -> bool:
    """Determine whether first tuple is overlapping with the second tuple."""
    overlapping = False
    if (first_section[0] >= second_section[0]) and (first_section[0] <= second_section[1]):
        overlapping = True
    return overlapping


def camp_cleanup_contain(assignment_list: list) -> int:
    """Return the number of assignment pairs with redundant assignments."""
    redundant_pairs = 0
    for assignment in assignment_list:
        first_section, second_section = _parse_assignment(assignment)

        if _check_contained_by(first_section, second_section):
            redundant_pairs += 1
        elif _check_contained_by(second_section, first_section):
            redundant_pairs += 1

    return redundant_pairs


def camp_cleanup_overlap(assignment_list: list) -> int:
    """Return the number of assignment pairs with overlapping assignments."""
    redundant_pairs = 0
    for assignment in assignment_list:
        first_section, second_section = _parse_assignment(assignment)

        if _check_overlapping(first_section, second_section):
            redundant_pairs += 1
        elif _check_overlapping(second_section, first_section):
            redundant_pairs += 1

    return redundant_pairs


# %%

if __name__ == "__main__":
    input_path = "advent_of_code\\2022\\day4_camp_cleanup\\input.txt"
    assignment_list = load.read_input_to_list(input_path)

    redundant_pairs_contain = camp_cleanup_contain(assignment_list)

    print(f"Part 1 solution: {redundant_pairs_contain}")

    redundant_pairs_overlap = camp_cleanup_overlap(assignment_list)

    print(f"Part 2 solution: {redundant_pairs_overlap}")
