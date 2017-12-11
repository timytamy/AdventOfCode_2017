#!/usr/bin/env python3

from __future__ import print_function
from day07 import findRoot

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

example_ans = 60

weights = {}  # Dict of all local weights
treeDict = {}  # Dict of all relationships


def main():
    if solve(example) == example_ans:
        print("Test", example, "passed")
    else:
        print("Test", example, "failed")

    f = open("day07_input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(line.replace("\n", " "))

    ans = solve(puzzle)
    print("Answer =", ans)


def solve(tree):
    root = findRoot(tree)  # Root found in part 1

    for record in tree:
        records = record.replace(", ", " ").strip(" ").split(" ")

        # Set up dicts
        weights[records[0]] = int(records[1].strip("()"))
        if "->" in record:
            treeDict[records[0]] = records[3:]

    return int(findWeight(root))

# Normally returns a int, when a str is retturned we have found our value!
# Order of recursion/stack means first unbalanced set is the one we need to fix
def findWeight(trunk):
    # Leaf weight
    if trunk not in treeDict:
        return weights[trunk]

    branchWeights = []  # List of weights of the child nodes
    for child in treeDict[trunk]:
        branchWeights.append(findWeight(child))

        # Recursive call found the answer, pass it back up
        if type(branchWeights[-1]) is not int:
            return float(branchWeights[-1])

    # If level is not balanced
    if len(set(branchWeights)) != 1:
        # Find index of the unbalanced child
        diffInd = branchWeights.index(min(branchWeights, key=branchWeights.count))
        # Difference between unbalanced and balanced children
        diff = branchWeights[diffInd]-branchWeights[(diffInd+1) % len(branchWeights)]

        # Return fixed weight as a string
        return str(weights[treeDict[trunk][diffInd]] - diff)

    # Return the total weight of this level and children
    return weights[trunk] + sum(branchWeights)


if __name__ == '__main__':
    main()
