def sigma(n):
    if n > 0:
        return sigma(n-1) + n
    else:
        return 0