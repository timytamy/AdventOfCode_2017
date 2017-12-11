#!/usr/bin/env python3

from __future__ import print_function

from collections import defaultdict

example = ["b inc 5 if a > 1",
           "a inc 1 if b < 5",
           "c dec -10 if a >= 1",
           "c inc -20 if c == 10"]
example_ans = 1


def main():
    if solve(example) == example_ans:
        print("Test", example, "passed")
    else:
        print("Test", example, "failed")

    f = open("day08_input.txt", "r")
    array = []
    for line in f:
        array.append(line.replace("\n", " "))

    ans = solve(array)
    print("Answer =", ans)


def solve(program):
    regs = defaultdict(int)

    for line in program:
        line = line.replace("inc", "+").replace("dec", "-").split(" ")

        if eval(str(regs[line[4]]) + line[5] + line[6]):
            regs[line[0]] += eval(line[1] + line[2])

    return max(regs.values())


if __name__ == '__main__':
    main()
