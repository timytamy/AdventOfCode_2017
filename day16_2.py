#!/usr/bin/env python3

from __future__ import print_function

example = "s1,x3/4,pe/b"
exampleAns = "cbade"


def main():
    if solve(example, list("abcde")) == exampleAns:
        print("Test passed")
    else:
        print("Test failed")

    f = open("day16_input.txt", "r")
    puzzle = f.readline().replace("\n", "")

    line = list("abcdefghijklmnop")
    ans = solve(puzzle, line)
    print("Answer =", ans)


def solve(dance, line):
    dance = dance.split(",")
    for i in range(1000000000):
        print(i)
        line = perform(dance, line)
    return "".join(line)


def perform(dance, line):
    for move in dance:
        if move[0] == "s":
            line = spin(line, int(move[1:]))
        elif move[0] == "x":
            move = move[1:].split("/")
            line = swapPos(line, int(move[0]), int(move[1]))
        elif move[0] == "p":
            move = move[1:].split("/")
            line = swapName(line, move[0], move[1])

    return line


def spin(line, size):
    size %= len(line)
    line = line[len(line)-size:] + line[:len(line)-size]
    return line


def swapPos(line, A, B):
    line[A], line[B] = line[B], line[A]
    return line


def swapName(line, A, B):
    indA, indB = line.index(A), line.index(B)
    line[indA], line[indB] = B, A
    return line


if __name__ == '__main__':
    main()
