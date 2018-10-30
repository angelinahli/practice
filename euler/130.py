import time
import math
import sys
from fractions import gcd

K = []
CAND_PRIMES = []

def read():
    result = None
    try: 
        result = input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def is_prime_bf(num):
    if num < 2:
        return False
    elif num % 2 == 0:
        return num == 2
    k = 3
    while k*k <= num:
        if num % k == 0:
            return False
        k += 2
    return True

def is_prime(num):
    if num < 2:
        return False
    ind = 0
    pn = CAND_PRIMES[ind]
    while pn*pn <= num:
        if num % pn == 0:
            return False
        ind += 1
        pn = CAND_PRIMES[ind]
    return True

def a(num):
    k_index = 0
    while True:
        if len(K) - 1 < k_index:
            K.append(int("1" * (k_index + 1)))
        r = K[k_index]
        if r % num == 0:
            return k_index + 1
        k_index += 1
    return None

def get_nums(l, r):
    nums = []
    lst = [91, 259, 451, 481, 703, 1729, 2821, 2981, 3367, 4141, 
           4187, 5461, 6533, 6541, 6601, 7471, 7777, 8149, 8401, 
           8911, 10001, 11111, 12403, 13981, 14701, 14911, 15211, 
           15841, 19201, 21931, 22321, 24013, 24661, 27613, 29341,
           34133, 34441, 35113, 38503, 41041]
    for num in lst:
        if l < num and r >= num:
            nums.append(num)
            l = num + 1
        elif r < num or l > num:
            break

    for num in range(l, r + 1):
        if not gcd(num, 10) == 1:
            continue
        if is_prime(num):
            continue
        if (num - 1) % a(num) != 0:
            continue
        nums.append(num)
    return nums

def run():
    while True:
        line = read()
        if line == None:
            break
        l, r = map(int, line.split())
        CAND_PRIMES = filter(is_prime_bf, range(int(math.floor(math.sqrt(r)))))
        nums = get_nums(l, r)
        for num in nums:
            print(num)

if __name__ == "__main__":
    start = 42000
    incr = 2000
    CAND_PRIMES = filter(is_prime_bf, range(int(math.floor(math.sqrt(start + incr * 5)))))
    for num in range(start, start + incr * 4 + 1, incr):
        print num, num + incr 
        start = time.time()
        print(get_nums(num, num + incr))
        print(time.time() - start)
