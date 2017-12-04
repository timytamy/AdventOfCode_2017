#!/usr/bin/env python3

from __future__ import print_function

examples = {1: 2,
            4: 5,
            10: 11,
            24: 25,
            121: 122,
            303: 304
            }

puzzle = 347991

# All possible directions, first four are also directions that we move
dirns = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def main():
    for test in examples:
        ans = solve(test)
        if ans == examples[test]:
            print("Test", test, "passed")
        else:
            print("Test", test, "failed")

    ans = solve(puzzle)
    print("Answer =", ans)


def solve(address):
    x, y = 0, 0
    heading = 1
    array = {(0, 0): 1}
    for i in range(address*2):
        # Set x, y to new coordinate by moving "forward" one
        x, y = x+dirns[heading][0], y+dirns[heading][1]

        # Fill "cell"
        array[(x, y)] = 0
        for (vx, vy) in dirns:
            if (x+vx, y+vy) in array:
                array[(x, y)] += array[(x+vx, y+vy)]

        if array[(x, y)] > address:
            return(array[(x, y)])

        # Rotate if the cell to the left is empty
        dx, dy = dirns[(heading + 1) % 4]
        if (x+dx, y+dy) not in array:
            heading = (heading + 1) % 4


if __name__ == '__main__':
    main()
