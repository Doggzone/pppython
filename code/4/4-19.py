def power(b,n):
    prod = 1
    while n > 0:
        if n % 2 == 0:
            b = b * b
            n = n // 2
        else:
            n = n - 1
            prod = b * prod
    return prod