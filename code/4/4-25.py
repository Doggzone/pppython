def gcd(m,n):
    k = 1
    while not (m == 0 or n == 0):
        if even(m) and even(n):
            m, n, k = _______
        elif even(m) and odd(n):
            m = _______
        elif odd(m) and even(n):
            n = _______
        elif m <= n:
            n = _______
        else:
            m, n = _______
    if m == 0:
        return _______
    else: # n == 0
        return _______