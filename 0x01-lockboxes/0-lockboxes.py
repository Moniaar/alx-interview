#!/usr/bin/python3
""" This module has the answer to the lockup interview question """


def canUnlockAll(boxes):
    """ This is the method that will check for your boxes
    if they can be opened or not"""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
