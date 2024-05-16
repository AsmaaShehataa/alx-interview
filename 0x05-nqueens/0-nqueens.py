#!/usr/bin/python3
"""
solves the N queens puzzle
"""
import sys


def valid_pos(solu, position):
    """
    Function that verifies if a queen can be placed at given
    position on the chess board with out conflicting with the
    already placed queens in the list.
    """
    for queen in solu:
        if queen[1] == position[1]:
            return False
        if (queen[0] + queen[1]) == (position[0] + position[1]):
            return False
        if (queen[0] - queen[1]) == (position[0] - position[1]):
            return False
    return True


def solve_queens(row, n, solu):
    """
    Function that finds the solution recursively, from the root down
    """
    if (row == n):
        print(solu)
    else:
        for col in range(n):
            position = [row, col]
            if valid_pos(solu, position):
                solu.append(position)
                solve_queens(row + 1, n, solu)
                solu.remove(position)


def main(n):
    """
    Main function
    """
    solution = []
    """ From root(0) down(n) """
    solve_queens(0, n, solution)


if __name__ == '__main__':
    """ Validate the arguments from OS """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        i = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    i = int(sys.argv[1])
    if i < 4:
        print('N must be at least 4')
        sys.exit(1)

    """ Calling the main function """
    main(i)