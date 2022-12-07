# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 7: No Space Left On Device

@author: Andrew Ting
@last-modified: 2022/12/07
"""

from __future__ import annotations

from aoc_utils import load


# %%

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name


class Folder:
    def __init__(self, name: str, children: list = None, parent: Folder = None):
        if children is None:
            children = []

        self.name = name
        self.children = children
        self.parent = parent

    def __repr__(self):
        return self.name + "/"

    def add_child(self, file_: Folder):
        self.children.append(file_)

    def get_size(self) -> int:
        total_size = 0
        for child in self.children:
            if isinstance(child, Folder):
                total_size += child.get_size()
            else:
                total_size += child.size
        return total_size

    def change_directory(self, folder_name: str) -> Folder:
        if folder_name == "..":
            return self.parent

        for file_ in self.children:
            if file_.name == folder_name:
                return file_

        raise Exception(f"Couldn't find file called {folder_name}")


# %%

def _construct_part1_solution(CurrentFolder: Folder, max_size: int = 100000) -> int:
    """Recursive auxiliary function to find all folders with at most some size."""
    sum_of_sizes = 0

    for Child in CurrentFolder.children:
        if isinstance(Child, Folder):
            folder_size = Child.get_size()
            if folder_size <= max_size:
                # print(Child.name, folder_size)
                sum_of_sizes += folder_size

            sum_of_sizes += _construct_part1_solution(Child, max_size)

    return sum_of_sizes


def _construct_part2_solution(CurrentFolder: Folder, deletion_size: int) -> list:
    """Docstring"""
    viable_folders_to_delete = []

    for Child in CurrentFolder.children:
        if isinstance(Child, Folder):
            folder_size = Child.get_size()
            if folder_size >= deletion_size:
                viable_folders_to_delete.append(Child)

            viable_folders_to_delete += _construct_part2_solution(Child, deletion_size)

    return viable_folders_to_delete


def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    assert part in [1, 2], "Part must be 1 or 2"

    input_list = load.read_input_to_list(input_path)
    solution = None

    RootFolder = Folder("/", parent="HOME")
    HomeFolder = Folder("HOME", [RootFolder])
    CurrentFolder = HomeFolder

    start_reading_toggle = 0
    for command_line in input_list:
        # print(command_line)
        # print(CurrentFolder.name, CurrentFolder.children)
        if command_line.startswith("$ cd "):
            argument = command_line[5:]
            CurrentFolder = CurrentFolder.change_directory(argument)
            start_reading_toggle = 0
        elif command_line == "$ ls":
            start_reading_toggle = 1
        elif command_line.startswith("dir "):
            argument = command_line[4:]
            CurrentFolder.add_child(Folder(argument, parent=CurrentFolder))
        else:
            # file found
            file_size, file_name = command_line.split(" ")
            CurrentFolder.add_child(File(file_name, size=int(file_size)))

    if part == 1:
        solution = _construct_part1_solution(HomeFolder)

    elif part == 2:
        total_space = 70000000
        required_space = 30000000

        directory_size = HomeFolder.get_size()
        unused_space = total_space - directory_size

        deletion_size = required_space - unused_space

        viable_folders = _construct_part2_solution(HomeFolder, deletion_size)

        # Choose the viable folder with the smallest size
        BestFolder = RootFolder
        for ViableFolder in viable_folders:
            if ViableFolder.get_size() < BestFolder.get_size():
                BestFolder = ViableFolder

        solution = BestFolder.get_size()

    return solution


# %%

if __name__ == "__main__":
    input_path = "input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
