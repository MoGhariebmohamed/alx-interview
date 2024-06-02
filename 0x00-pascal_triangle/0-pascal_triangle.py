#!/usr/bin/python3
"""
let's create the Pascal's triangle
"""

def pascal_triangle(n):
    """
    create the triangle
    """
    result = [[1]]
    for x in range(n - 1):
        resultTemp = [0] + result[-1] + [0]
        newRow = []
        for y in range(len(result[-1]) + 1):
            newRow.append(resultTemp[y] + resultTemp[y + 1])
        result.append(newRow)
    return result