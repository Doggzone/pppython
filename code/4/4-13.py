def power(b,n):
    if n > 0:
        return b * power(b,n-1)
    else:
        return 1