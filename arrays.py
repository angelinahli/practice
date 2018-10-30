# hourglasses

def getHourglassSum(arr, sr, sc):
    changes = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
    return sum(map(lambda tup: arr[sr + tup[0]][sc + tup[1]], changes))

def hourglassSum(arr):
    topSum = getHourglassSum(arr, 0, 0)
    for sr in range(0, len(arr) - 2):
        for sc in range(0, len(arr[0]) - 2):
            if sr == 0 and sc == 0:
                continue
            topSum = max(topSum, getHourglassSum(arr, sr, sc))
    return topSum

# rotate left

def rotLeft(a, d):
    d = d % len(a)
    return a[d:] + a[:d]

# new year chaos
