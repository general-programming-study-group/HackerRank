#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    return str(s).count('a') * (n // len(s)) + str(s[:n % len(s)]).count('a')

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
