def read():
    result = None
    try: 
        result = input().rstrip("\n")
    except EOFError:
        result = None
    finally:
        return result

def is_prime(num):
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

def get_least_n(b):
    n_val = 0
    p_val = 2
    while True:
        if is_prime(p_val):
            n_val += 1
            numer = ((p_val - 1)**n_val) + ((p_val + 1)**n_val)
            denom = p_val**2
            if numer % denom > b:
                return n_val
        p_val += 1

def run():
    num_cases = int(read())
    for _ in range(num_cases):
        b = int(read())
        print(get_least_n(b))

print(get_least_n(2*(10**9)))