# counting socks

from collections import Counter

def read():
    result = None
    try: 
        result = input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def get_num(arr):
    vals = Counter(arr)
    total = 0
    for v, n in vals.most_common():
        total += math.floor(n / 2)
    return total

def run():
    n = int(read())
    arr = read().split(" ")
    print(get_num(arr))

# counting valleys

def countingValleys(n, s):
    numValleys = 0
    pos = 0
    dx = {"D": -1, "U": 1}
    for mv in s:
        newPos = pos + dx.get(mv)
        if pos >= 0 and newPos < 0:
            numValleys += 1
        pos = newPos
    return numValleys

# Jumping on the clouds

def jumpingOnClouds(c):
    numJumps = 0
    currInd = 0
    # if we haven't hit the end yet
    while currInd < len(c) - 1:
        if currInd <= len(c) - 3 and c[currInd + 2] == 0:
            currInd += 2
        else:
            currInd += 1
        numJumps += 1
    return numJumps

# repeated string

# aaaba, 15
from collections import Counter
from math import floor

def getA(string):
    return Counter(string)["a"]

def repeatedString(s, n):
    if len(s) < n:
        s = s[:n]
    numA = getA(s)
    numIterations = math.floor(n / len(s))
    numLeftover = getA(s[:n % len(s)])
    return (numA * numIterations) + numLeftover
