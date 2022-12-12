# -*- coding: utf-8 -*-
"""
Advent of Code 2022 - Day 8: Treetop Tree House

@author: Andrew Ting
@last-modified: 2022/12/12
"""

from aoc_utils import load


# %%

def main(input_path: str, part: int) -> int:
    """Solve today's Advent of Code problems."""
    assert part in [1, 2], "Part must be 1 or 2"

    input_list = load.read_input_to_list(input_path)
    solution = None

    tree_grid = input_list

    n_rows = len(tree_grid)
    n_columns = len(tree_grid[0])

    # see_from_left = []
    # see_from_right = []
    # see_from_above = []
    # see_from_below = []

    # for row in range(n_rows):
    #     tree_count = 0
    #     max_observed_height = -1
    #     for column in range(n_columns):
    #         tree_height = int(tree_grid[row][column])
    #         if tree_height > max_observed_height:
    #             max_observed_height = tree_height
    #             tree_count += 1
    #         else:
    #             break
    #     see_from_left.append(tree_count)

    #     tree_count = 0
    #     max_observed_height = -1
    #     for column in range(n_columns):
    #         tree_height = int(tree_grid[row][-column - 1])
    #         if tree_height > max_observed_height:
    #             max_observed_height = tree_height
    #             tree_count += 1
    #         else:
    #             break
    #     see_from_right.append(tree_count)

    # for column in range(n_columns):
    #     tree_count = 0
    #     max_observed_height = -1
    #     for row in range(n_rows):
    #         tree_height = int(tree_grid[row][column])
    #         if tree_height > max_observed_height:
    #             max_observed_height = tree_height
    #             tree_count += 1
    #         else:
    #             break
    #     see_from_above.append(tree_count)

    #     tree_count = 0
    #     max_observed_height = -1
    #     for row in range(n_rows):
    #         tree_height = int(tree_grid[-row - 1][column])
    #         if tree_height > max_observed_height:
    #             max_observed_height = tree_height
    #             tree_count += 1
    #         else:
    #             break
    #     see_from_below.append(tree_count)

    # print(see_from_left)
    # print(see_from_right)

    # print(see_from_above)
    # print(see_from_below)

    # visible_trees = 0
    # for row in range(n_rows):
    #     for column in range(n_columns):
    #         if row == 17 and column == 46:
    #             print((see_from_left[row]))
    #             print((see_from_right[row]))
    #             print((see_from_above[column]))
    #             print((see_from_below[column]))

    #         visible_horizontally = see_from_left[row] >= (column + 1) or see_from_right[row] >= n_columns - column
    #         visible_vertically = see_from_above[column] >= (row + 1) or see_from_below[column] >= n_rows - row
    #         if visible_horizontally or visible_vertically:
    #             print(row, column)
    #             visible_trees += 1

    # solution = visible_trees

    # Above does not work as it does not consider cases where there are trees
    # of equal length with a tree behind it of larger length (in which case the
    # middle of the smaller trees is not visible)

    # Brute force solution
    if part == 1:
        visible_trees = 0
        for row in range(n_rows):
            for column in range(n_columns):
                # Trees on the edge will always be viewable from at least one direction
                if row == 0 or column == 0 or row == n_rows or column == n_columns:
                    visible_trees += 1
                    continue

                tree_height = tree_grid[row][column]

                left_visible = True
                right_visible = True
                top_visible = True
                bottom_visible = True

                for column_i in range(0, column):
                    if tree_grid[row][column_i] >= tree_height:
                        left_visible = False
                        break

                for column_j in range(column + 1, n_columns):
                    if tree_grid[row][column_j] >= tree_height:
                        right_visible = False
                        break

                for row_i in range(0, row):
                    if tree_grid[row_i][column] >= tree_height:
                        top_visible = False
                        break

                for row_j in range(row + 1, n_rows):
                    if tree_grid[row_j][column] >= tree_height:
                        bottom_visible = False
                        break

                if any([left_visible, right_visible, top_visible, bottom_visible]):
                    visible_trees += 1

        solution = visible_trees

    elif part == 2:
        max_scenic_score = 0
        for row in range(n_rows):
            for column in range(n_columns):
                # At least one direction will have a viewing distance of 0
                if row == 0 or column == 0 or row == n_rows or column == n_columns:
                    scenic_score = 0
                    continue

                tree_height = tree_grid[row][column]

                left_distance = 0
                right_distance = 0
                top_distance = 0
                bottom_distance = 0

                for column_i in range(1, column + 1):
                    if tree_grid[row][column - column_i] >= tree_height:
                        left_distance += 1
                        break
                    left_distance += 1

                for column_j in range(column + 1, n_columns):
                    if tree_grid[row][column_j] >= tree_height:
                        right_distance += 1
                        break
                    right_distance += 1

                for row_i in range(1, row + 1):
                    if tree_grid[row - row_i][column] >= tree_height:
                        top_distance += 1
                        break
                    top_distance += 1

                for row_j in range(row + 1, n_rows):
                    if tree_grid[row_j][column] >= tree_height:
                        bottom_distance += 1
                        break
                    bottom_distance += 1

                scenic_score = left_distance * right_distance * top_distance * bottom_distance
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

        solution = max_scenic_score

    return solution


# %%

if __name__ == "__main__":
    input_path = "input.txt"

    part1_solution = main(input_path, 1)
    print(f"Part 1 solution: {part1_solution}")

    part2_solution = main(input_path, 2)
    print(f"Part 2 solution: {part2_solution}")
