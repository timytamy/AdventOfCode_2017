#!/usr/bin/env python3

from __future__ import print_function

example = [0, 2, 7, 0]
example_ans = 5

puzzle = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]


def main():
    if solve(example) == example_ans:
        print("Test", example, "passed")
    else:
        print("Test", example, "failed")

    ans = solve(puzzle)
    print("Answer =", ans)


def solve(memory):
    i = 0
    seenStates = []
    while str(memory) not in seenStates:
        seenStates.append(str(memory))

        maxBank = memory.index(max(memory))
        extraBanks = memory[maxBank]
        memory[maxBank] = 0
        for i in range(extraBanks):
            memory[(maxBank + 1 + i) % len(memory)] += 1

    return len(seenStates)


if __name__ == '__main__':
    main()
