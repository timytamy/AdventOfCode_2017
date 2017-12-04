#!/usr/bin/env python3

from __future__ import print_function

examples = {"aa bb cc dd ee": True,
            "aa bb cc dd aa": False,
            "aa bb cc dd aaa": True,
            }


def main():
    for test in examples:
        ans = isValid(test)
        if ans == examples[test]:
            print("Test", test, "passed")
        else:
            print("Test", test, "failed")

    f = open("day04_input.txt", "r")
    ans = 0
    for line in f:
        if isValid(line):
            ans += 1

    print("Answer = ", ans)


def isValid(passphrase):
    phrase = {}
    for word in passphrase.split():
        if word in phrase:
            return(False)
        phrase[word] = True  # Store word to compare

    return(True)


if __name__ == '__main__':
    main()
