# -*- coding: utf-8 -*-
"""
Common functions to load Advent Of Code inputs.

@author: Andrew Ting
@last-modified: 2022/12/01
"""

import os


# %%

def read_input_to_list(relative_path: str) -> list:
    """Load Advent of Code problem input and return contents as a list."""
    cwd = os.getcwd()
    if relative_path[:2] != "\\":
        relative_path = "\\" + relative_path
    full_path_to_input = cwd + relative_path

    with open(full_path_to_input, "r") as f:
        stream = f.read()

        # Convert to list split by new lines and slice out final item as it 
        # will always be an empty line
        inputs = stream.split("\n")[:-1]

    return inputs
