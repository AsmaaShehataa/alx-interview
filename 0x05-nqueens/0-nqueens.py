#!/usr/bin/python3
"""N queens puzzle"""


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def nQueen(num):
    """Solves the N queens puzzle"""
    if num == 0:
        return [[]]
    queens_solution = nQueen(num - 1)
    return [solution + [(n, i + 1)]
            for i in range(N)
            for n in range(1, N + 1)
            for solution in queens_solution
            if isSafe((n, i + 1), solution)]


def queen_attack(square, queen):
    """Check if the square is under attack by a queen"""
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def isSafe(sq, Qs):
    """Check if a square is safe from attack by all queens"""
    for q in Qs:
        if queen_attack(sq, q):
            return False
    return True


for answer in reversed(isSafe(N)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
