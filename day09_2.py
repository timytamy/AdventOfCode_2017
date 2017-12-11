#!/usr/bin/env python3

from __future__ import print_function

examples = {"{}": 0,
            "{{{}}}": 0,
            "{{},{}}": 0,
            "{{{},{},{{}}}}": 0,
            "{<a>,<a>,<a>,<a>}": 4,
            "{{<ab>},{<ab>},{<ab>},{<ab>}}": 8,
            "{{<!!>},{<!!>},{<!!>},{<!!>}}": 0,
            "{{<a!>},{<a!>},{<a!>},{<ab>}}": 5}


def main():
    for eg in examples:
        if solve(eg) == examples[eg]:
            print("Test", eg, "passed")
        else:
            print("Test", eg, "failed")

    f = open("day09_input.txt", "r")
    puzzle = f.readline().replace("\n", "")

    ans = solve(puzzle)
    print("Answer =", ans)


def solve(stream):
    pos, score = group(1, stream, 1)
    return score


def group(pos, stream, depth):
    score = 0
    while True:
        if stream[pos] == "}":
            return pos, score
        elif stream[pos] == "<":
            pos, childScore = garbage(pos+1, stream)
            score += childScore
        elif stream[pos] == "{":
            pos, childScore = group(pos+1, stream, depth+1)
            score += childScore

        pos += 1


def garbage(pos, stream):
    chars = 0
    while stream[pos] != ">":
        if stream[pos] == "!":
            pos += 2
        else:
            pos += 1
            chars += 1

    return pos, chars


if __name__ == '__main__':
    main()
