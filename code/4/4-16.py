def power(b,n):
    prod = 1
    while n > 0:
        prod = b * prod
        n = n - 1
    return prod