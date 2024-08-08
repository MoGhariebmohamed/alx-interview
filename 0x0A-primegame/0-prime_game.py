#!/usr/bin/python3

"""
calculatee the  Prime Game
"""


def isWinner(x, nums):
    """
    x is the number of rounds 
    nums is an array of n
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        delMultiply(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
 

def delMultiply(y, x):
    """
    to delete the multiply
    """
    for i in range(2, len(y)):
        try:
            y[i * x] = 0
        except (ValueError, IndexError):
            break

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
