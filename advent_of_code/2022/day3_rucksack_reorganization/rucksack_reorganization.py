# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 3: Rucksack Reorganization

@author: Andrew Ting
@last-modified: 2022/12/03
"""

from aoc_utils import load


# %%

def _convert_to_priority(item: str) -> int:
    """Convert an item type to its priority."""
    assert len(item) == 1, "Item type should be 1 character"

    offset = 0
    if item == item.lower():
        offset = 96
    elif item == item.upper():
        offset = 38

    return ord(item) - offset


def _count_items(compartment: list) -> dict:
    """Return counts of each item type in a compartment."""
    count_dict = {}

    for item in compartment:
        if item in count_dict.keys():
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    return count_dict


def rucksack_reorganization(rucksack_list: list) -> int:
    """Return the sum of priorities of items that appear in both compartments."""
    total_priority = 0
    for rucksack in rucksack_list:
        n = len(rucksack)
        shared_item = None

        assert n % 2 == 0, "Length of rucksacks should always be even"

        midpoint = int(n / 2)

        first_compartment = rucksack[:midpoint]
        second_compartment = rucksack[midpoint:]

        first_summary = _count_items(first_compartment)
        second_summary = _count_items(second_compartment)

        first_items = first_summary.keys()
        second_items = second_summary.keys()

        for item in first_items:
            if item in second_items:
                assert shared_item == None, "Multiple shared items found"
                shared_item = item

        # print(shared_item)
        total_priority += _convert_to_priority(shared_item)

    return total_priority


def rucksack_group_reorganization(rucksack_list: list) -> int:
    """Return the sum of priorities of items in both compartments."""
    total_priority = 0

    n_groups = len(rucksack_list)
    assert n_groups % 3 == 0, "Length of rucksacks should be divisible by 3"

    for start_pointer in range(0, n_groups, 3):
        shared_item = None

        first_group = rucksack_list[start_pointer]
        second_group = rucksack_list[start_pointer + 1]
        third_group = rucksack_list[start_pointer + 2]

        first_summary = _count_items(first_group)
        second_summary = _count_items(second_group)
        third_summary = _count_items(third_group)

        first_items = first_summary.keys()
        second_items = second_summary.keys()
        third_items = third_summary.keys()

        for item in first_items:
            if item in second_items:
                if item in third_items:
                    assert shared_item == None, "Multiple shared items found"
                    shared_item = item

        # print(shared_item)
        total_priority += _convert_to_priority(shared_item)

    return total_priority


# %%

if __name__ == "__main__":
    input_path = "advent_of_code\\2022\\day3_rucksack_reorganization\\input.txt"
    rucksack_list = load.read_input_to_list(input_path)

    total_priority = rucksack_reorganization(rucksack_list)

    print(f"Part 1 solution: {total_priority}")

    total_group_priority = rucksack_group_reorganization(rucksack_list)

    print(f"Part 2 solution: {total_group_priority}")
