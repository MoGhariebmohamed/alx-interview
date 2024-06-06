#!/usr/bin/python3
"""
lockboxes module
"""


def canUnlockAll(boxes):
    """
    this method to find true boxes
    """

    openBoxes = set([0])
    notOpen = set(boxes[0]).difference(set([0]))
    while len(notOpen) > 0:
        nowBox = notOpen.pop()
        if not nowBox or nowBox >= len(boxes):
            continue
        if nowBox not in openBoxes:
            notOpen = notOpen.union(boxes[nowBox])
            openBoxes.add(nowBox)
    return len(boxes) == len(openBoxes)
        
