#!/usr/bin/env python3

from __future__ import print_function

examples = {1: 0,
            12: 3,
            23: 2,
            1024: 31,
            }

puzzle = 347991


def main():
    for test in examples:
        ans = solve(test)
        if ans == examples[test]:
            print("Test", test, "passed")
        else:
            print("Test", test, "failed")

    ans = solve(puzzle)
    print("Answer = ", ans)


def solve(address):
    # Find the depth
    levelSum = 1
    for i in range(address):
        levelSum += i*8
        if address <= levelSum:
            break
    levelSum -= i*8

    # Find the distance from the centre of the edge
    if address <= levelSum+i*2:
        dist = abs(levelSum+i - address)
    elif address <= levelSum+i*4:
        dist = abs(levelSum+i*3 - address)
    elif address <= levelSum+i*6:
        dist = abs(levelSum+i*5 - address)
    elif address <= levelSum+i*8:
        dist = abs(levelSum+i*7 - address)
    else:
        print("Something went wrong!")
        exit()

    # Total distance is the depth + distance from center of edge
    return(i+dist)


if __name__ == '__main__':
    main()
