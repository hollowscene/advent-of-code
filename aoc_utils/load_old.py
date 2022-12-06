# -*- coding: utf-8 -*-
"""
Common functions to load Advent Of Code inputs.

@author: Andrew Ting
@last-modified: 2022/12/05
"""

import inspect
import os
from pathlib import Path


# %%

def get_full_file_path(relative_path: str = None) -> os.path:
    """Convert a relative file path to an absolute file path."""
    # Use stack to find path of caller
    # https://stackoverflow.com/questions/55469447/get-caller-functions-absolute-path-to-its-file
    # Apparently this isn't best practice but I haven't been able to get any 
    # other solutions to work
    # See https://stackoverflow.com/questions/2654113/how-to-get-the-callers-method-name-in-the-called-method
    frame = inspect.stack()[1]
    p = frame[0].f_code.co_filename

    if relative_path is None:
        full_path_to_input = Path(p)
    else:
        full_path_to_input = os.path.join(Path(p).parent, relative_path)

    return full_path_to_input


def read_input_to_list(file_path: str) -> list:
    """Load Advent of Code problem input and return contents as a list."""
    with open(file_path, "r") as f:
        stream = f.read()

        # Convert to list split by new lines and slice out final item as it 
        # will always be an empty line
        inputs = stream.split("\n")[:-1]

    return inputs
