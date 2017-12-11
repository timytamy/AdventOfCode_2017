#!/usr/bin/env python3

from __future__ import print_function

example = ['pbga (66)',
           'xhth (57)',
           'ebii (61)',
           'havc (66)',
           'ktlj (57)',
           'fwft (72) -> ktlj, cntj, xhth',
           'qoyq (66)',
           'padx (45) -> pbga, havc, qoyq',
           'tknk (41) -> ugml, padx, fwft',
           'jptl (61)',
           'ugml (68) -> gyxo, ebii, jptl',
           'gyxo (61)',
           'cntj (57)']

example_ans = "tknk"


def main():
    if findRoot(example) == example_ans:
        print("Test", example, "passed")
    else:
        print("Test", example, "failed")

    f = open("day07_input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(line.replace("\n", " "))

    ans = findRoot(puzzle)
    print("Answer =", ans)


def findRoot(tree):
    flat = []
    for record in tree:
        record = record.replace(", ", " ").split(" ")
        for entry in record:
            if "(" not in entry:  # Skip weights
                flat.append(entry)

    # Root is only mentioned once, so find item that is only mentioned once
    for item in flat:
        flat.remove(item)
        if item in flat:
            flat.append(item)
        else:
            return(item)


if __name__ == '__main__':
    main()
