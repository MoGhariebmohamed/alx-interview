#!/usr/bin/python3

"""
calculatee the  the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Return: the perimeter of the island described in grid
    """
    x = 0
    for any in range(len(grid)):
        for num in range(len(grid[any])):
            if (grid[any][num] == 1):
                if (any <= 0 or grid[any - 1][num] == 0):
                    x += 1
                if (any >= len(grid) - 1 or grid[any + 1][num] == 0):
                    x += 1
                if (num <= 0 or grid[any][num - 1] == 0):
                    x += 1
                if (num >= len(grid[any]) - 1 or grid[any][num + 1] == 0):
                    x += 1
    return x
