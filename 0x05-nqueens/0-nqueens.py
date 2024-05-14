#!/usr/bin/python3
"""
N queens
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    NQ = int(sys.argv[1])
except ValueError:
    print('N must ba a number')
    exit(1)

if NQ < 4:
    print('N must ba at least 4')
    exit(1)


def solve_nqueens(n):
    ''' QUEENS PUZZLE descriptive '''
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(NQ)
            for solution in inner_solution
            if isSafequeen((n, i + 1), solution)]


def attack_queen(square, queen):
    '''QUEEN Puzzle aelf descriptive'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def isSafequeen(sqr, queens):
    '''self descriptive Nqueens Puzzzle'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    Chess_result = []
    for p in [list(p) for p in answer]:
        Chess_result.append([i - 1 for i in p])
    print(Chess_result)
