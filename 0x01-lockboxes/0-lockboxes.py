#!/usr/bin/python3
"""Function to determine if all the boxes can be opened"""

def canUnlockAll(boxes):
    """
    Determines whether all the boxes can be opened.
    
    Args:
        boxes (list): A list of lists representing lockboxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    keys = [0]
    for i in keys:
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False

