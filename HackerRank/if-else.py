#!/bin/python3

# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print('Weird') if n%2!=0 or 5<n<21 else print('Not Weird')
