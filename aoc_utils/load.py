# -*- coding: utf-8 -*-
"""
Common functions to load Advent Of Code inputs.

@author: Andrew Ting
@last-modified: 2022/12/06
"""

import inspect
import os
from pathlib import Path


# %%

def read_input_to_list(relative_file_path: str) -> list:
    """Load Advent of Code problem input and return contents as a list."""
    file_path = Path(inspect.currentframe().f_back.f_code.co_filename)

    full_file_path = os.path.join(file_path.parent, relative_file_path)

    with open(full_file_path, "r") as f:
        stream = f.read()

        # Convert to list split by new lines and slice out final item as it 
        # will always be an empty line
        inputs = stream.split("\n")[:-1]

    return inputs
