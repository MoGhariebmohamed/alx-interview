#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N non-attacking queen
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2 or len(sys.argv) == None:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

countn = int(sys.argv[1])


def queen_pos(countn, x=0, a=[], b=[], c=[]):
    """
    to get the possible positions
    """
    if x < countn:
        for any in range(countn):
            if any not in a and x + any not in b and x - any not in c:
                yield from queen_pos(countn, x + 1, a +
                                     [any], b + [x + any], c + [x - any])

            else:
                yield a


def solution(countn):
    """
    to solve the location of n
    """
    x = []
    y = 0
    for any in queen_pos(countn, 0):
        for empty in any:
            x.append([y, empty])
            y += 1
        print(x)
        x = []
        y = 0


solution(countn)
