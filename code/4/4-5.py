def sigma(n):
    total = 0
    while n > 0:
        n, total = n-1, n+total
    return total