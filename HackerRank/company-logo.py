#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    counter = {}
    for char in s:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1

    newlist = []
    for key, value in counter.items():
        newlist.append((key, value))
        # print(newlist)

    sorted_list = sorted(newlist, key=lambda sublist: (-sublist[1], sublist[0]))

    for i in range(3):
        print(str(sorted_list[i][0]) + " " + str(sorted_list[i][1]))
