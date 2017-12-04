#!/usr/bin/env python3

from __future__ import print_function

examples = {"abcde fghij": True,
            "abcde xyz ecdab": False,
            "a ab abc abd abf abj": True,
            "iiii oiii ooii oooi oooo": True,
            "oiii ioii iioi iiio": False
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
        word = "".join(sorted(word))  # Anagrams are the same when sorted
        if word in phrase:
            return(False)
        phrase[word] = True  # Store sorted anagram to compare

    return(True)


if __name__ == '__main__':
    main()
