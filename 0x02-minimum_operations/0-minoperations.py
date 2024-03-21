#!/usr/bin/python3
""" Module for 0x02-minimum_operations"""


def minOperations(n):
    """
    minOperations
    Determines the minimum number of operations required to obtain exactly n 'H' characters.
    """
    # To ensure all outputs are at least 2 characters: (min, Copy All => Paste)
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        # If n evenly divides by root
        if n % root == 0:
            # Total even divisions by root = total operations
            ops += root
            # Set n to the remainder
            n = n / root
            # Reduce root to find remaining smaller values that evenly divide n
            root -= 1
        # Increment root until it evenly divides n
        root += 1
    return ops

