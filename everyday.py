#!/usr/bin/env python3

from __future__ import print_function

import datetime as dt
import os

STARS = "*"*60


def main():
    today = dt.datetime.today()
    if today.year == 2017 and today.month == 12:
        day = today.day
    else:
        day = 25

    for i in range(1, day+1):
            print("\n{}\nDay {:02d}\n{}".format(STARS, i, STARS))
            os.system("python3 day{:02d}.py".format(i))
            print("\n{}\nDay {:02d}, Part 2\n{}".format(STARS, i, STARS))
            os.system("python3 day{:02d}_2.py".format(i))


if __name__ == '__main__':
    main()
