def sigma(n):
    sum = 0
    while n > 0:
        n, sum = n-1, n+sum
    return sum