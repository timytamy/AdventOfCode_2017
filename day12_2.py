#!/usr/bin/env python3

from __future__ import print_function

example = ["0 <-> 2",
           "1 <-> 1",
           "2 <-> 0, 3, 4",
           "3 <-> 2, 4",
           "4 <-> 2, 3, 6",
           "5 <-> 6",
           "6 <-> 4, 5"]

exampleAns = 2

group = [[]]


def main():
    if solve(example) == exampleAns:
        print("Test passed")
    else:
        print("Test failed")

    f = open("day12_input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(line.replace("\n", ""))

    ans = solve(puzzle)
    print("Answer =", ans)


def solve(data):
    count = 0
    group.clear()
    for row in data:
        row = row.replace(",", "").split(" ")
        if int(row[0]) not in group:
            addPrograms(row[0], data)
            count += 1
    return count


def addPrograms(progIn, data):
    progIn = int(progIn)

    if progIn in group:
        return

    group.append(progIn)

    row = data[progIn].replace(",", "").split(" ")
    for program in row[2:]:
        addPrograms(program, data)


if __name__ == '__main__':
    main()
