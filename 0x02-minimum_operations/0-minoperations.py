#!/usr/bin/python3
""" Minimum minoperations"""


def minOperations(n):
    """
    In a text file, there is a single character H. Your text editor can execute
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
