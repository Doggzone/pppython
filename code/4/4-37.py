def fac(n):
    if n > 1:
        return fac(n-1) * n
    else:
        return 1