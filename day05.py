#!/usr/bin/env python3

from __future__ import print_function

example = [0, 3, 0, 1, -3]
example_ans = 5


def main():
    if solve(example) == example_ans:
        print("Test", example, "passed")
    else:
        print("Test", example, "failed")

    f = open("day05_input.txt", "r")
    array = []
    for line in f:
        array.append(int(line))

    ans = solve(array)
    print("Answer =", ans)


def solve(offsets):
    i = 0
    jumps = 0
    while 0 <= i and i < len(offsets):
        offsets[i] += 1
        i += offsets[i] - 1
        jumps += 1

    return jumps


if __name__ == '__main__':
    main()
