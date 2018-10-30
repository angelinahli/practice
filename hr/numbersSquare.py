#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'numbersSquare' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
def numbersSquare(n, s):
    arr = [[None for col in range(n)] for row in range(n)]
    arr[0][0] = str(s)
    num = s + 1
    for wall in range(1, n):
        # fixed columns
        for newRow in range(wall + 1):
            arr[newRow][wall] = str(num)
            num += 1
        # fixed row
        for newCol in range(wall - 1, -1, -1):
            arr[wall][newCol] = str(num)
            num += 1
    for row in arr:
        print(" ".join(row))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    numbersSquare(n, s)
