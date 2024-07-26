#!/usr/bin/python3

"""
making change program
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    remain = 0
    coins = sorted(coins)[::-1]
    for all in coins:
        while all <= total:
            total -= all
            remain += 1
        if total == 0:
            return remain
    return -1

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))