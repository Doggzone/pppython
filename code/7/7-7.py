def comb(n,r):
    if r != 0 and r != n:
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1