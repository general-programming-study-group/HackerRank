#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

#def queensAttack(n, k, r_q, c_q, obstacles):
#    # Write your code here
#    if r_q < c_q:
#        _short = r_q
#        _long = c_q
#       e = [[1, c_q - r_q + 1], [r_q, 1], [r_q + (n - c_q), 1], [n, c_q], ]
#  else:
 #       _short = c_q
 #       _long = r_q
 #   
#
 #   for i in obstacles:
 #       # find on straight cross
 #       if i[0] == r_q:
 ##           
 #       elif i[1] == c_q:
 #           
 #       else:
 #           if i[0] > r_q and i[1] > c_q:
 #               if i[1] - (i[0] - r_q) == c_q:
 ##               
 #           elif i[0] > r_q and i[1] < c_q:
 #               if i[1] + (i[0] - r_q) == c_q:
 ####               
 ##           elif i[0] < r_q and i[1] > c_q:
 #               if i[1] + (r_q - i[0]) == c_q:
 ##               
 ##           elif i[0] < r_q and i[1] < c_q:
 #               if i[1] + (r_q - i[0]) == c_q:
 
def queensAttack(n, k, r_q, c_q, obstacles):
    if n==0:
        return 0
    vset=set([tuple(item) for item in obstacles])
    if (r_q,c_q) in vset:
        return 0
    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count=0
    for u,v in directions:
        cur=(r_q+u,c_q+v)
        while 1<=cur[0]<=n and 1<=cur[1]<=n and cur not in vset:
            cur=(cur[0]+u,cur[1]+v)
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
